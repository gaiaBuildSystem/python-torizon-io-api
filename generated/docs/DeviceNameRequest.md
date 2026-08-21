# DeviceNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from phobos_torizon_io_api.models.device_name_request import DeviceNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNameRequest from a JSON string
device_name_request_instance = DeviceNameRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceNameRequest.to_json())

# convert the object into a dict
device_name_request_dict = device_name_request_instance.to_dict()
# create an instance of DeviceNameRequest from a dict
device_name_request_from_dict = DeviceNameRequest.from_dict(device_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


