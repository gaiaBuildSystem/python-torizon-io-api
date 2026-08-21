# DeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **UUID** |  | 
**last_api_connect** | **datetime** |  | [optional] 
**last_ssh_session_connect** | [**LastSshSession**](LastSshSession.md) |  | [optional] 
**last_version** | **str** |  | [optional] 
**last_user_connect** | [**UserInfo**](UserInfo.md) |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.device_info import DeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfo from a JSON string
device_info_instance = DeviceInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceInfo.to_json())

# convert the object into a dict
device_info_dict = device_info_instance.to_dict()
# create an instance of DeviceInfo from a dict
device_info_from_dict = DeviceInfo.from_dict(device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


