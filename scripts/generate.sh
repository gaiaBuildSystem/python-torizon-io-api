#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$ROOT/scripts/fix_openapi_spec.py" "$ROOT/torizon-2.0-openapi.yaml"

docker run --rm \
  -v "$ROOT:/local" \
  --user 1000:1000 \
  openapitools/openapi-generator-cli:latest \
  generate \
  -i /local/torizon-2.0-openapi.yaml \
  -g python \
  -o /local/generated \
  --additional-properties packageName=phobos_torizon_io_api \
  --additional-properties packageVersion=0.0.7 \
  --additional-properties projectName=phobos-torizon-io-api

# openapi-generator overwrites generated/test-requirements.txt on every run;
# the canonical, hand-maintained copy lives at the project root.
cp "$ROOT/test-requirements.txt" "$ROOT/generated/test-requirements.txt"
