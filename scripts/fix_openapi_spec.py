#!/usr/bin/env python3
"""
Patch the Torizon OpenAPI spec before it is fed to openapi-generator.

The spec has several free-form/nullable fields written as:

    someField:
      anyOf:
      - {}
      - type: 'null'

openapi-generator's python codegen mishandles the empty schema (`{}`)
inside an `anyOf` block: it emits a reference to a model called `AnyOf`
without ever generating that class, so any response containing the field
crashes with `NameError: name 'AnyOf' is not defined` at deserialization
time.

Since `{}` alone already means "any value, including null", we collapse
the whole `anyOf` block down to `field: {}`, which is semantically
equivalent and avoids the broken codegen path entirely. Safe to run
multiple times (no-op once the pattern is gone).
"""

import re
import sys
from pathlib import Path

ANYOF_NULL_PATTERN = re.compile(r"( *)anyOf:\n\1- \{\}\n\1- type: 'null'\n")
EMPTY_BLOCK_PATTERN = re.compile(r"^( *)(\w+):\n\1\{\}\n", re.MULTILINE)


def fix_spec(text: str) -> tuple[str, int]:
    text, n = ANYOF_NULL_PATTERN.subn(
        lambda m: f"{m.group(1)[:-2]}{{}}\n", text
    )
    text, _ = EMPTY_BLOCK_PATTERN.subn(
        lambda m: f"{m.group(1)}{m.group(2)}: {{}}\n", text
    )
    return text, n


def main() -> int:
    if len(sys.argv) > 1:
        spec_path = Path(sys.argv[1])
    else:
        spec_path = Path(__file__).resolve().parent.parent / "torizon-2.0-openapi.yaml"

    text = spec_path.read_text()
    fixed_text, n = fix_spec(text)

    if n:
        spec_path.write_text(fixed_text)
        print(f"fix-openapi-spec: collapsed {n} anyOf[{{}}, null] block(s) in {spec_path}")
    else:
        print(f"fix-openapi-spec: nothing to fix in {spec_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
