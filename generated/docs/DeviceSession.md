# DeviceSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh** | [**SshSession**](SshSession.md) |  | 

## Example

```python
from phobos_torizon_io_api.models.device_session import DeviceSession

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSession from a JSON string
device_session_instance = DeviceSession.from_json(json)
# print the JSON string representation of the object
print(DeviceSession.to_json())

# convert the object into a dict
device_session_dict = device_session_instance.to_dict()
# create an instance of DeviceSession from a dict
device_session_from_dict = DeviceSession.from_dict(device_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


