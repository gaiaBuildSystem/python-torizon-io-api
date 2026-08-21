# PublicKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**Dict[str, KeyData]**](KeyData.md) |  | 

## Example

```python
from phobos_torizon_io_api.models.public_keys import PublicKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeys from a JSON string
public_keys_instance = PublicKeys.from_json(json)
# print the JSON string representation of the object
print(PublicKeys.to_json())

# convert the object into a dict
public_keys_dict = public_keys_instance.to_dict()
# create an instance of PublicKeys from a dict
public_keys_from_dict = PublicKeys.from_dict(public_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


