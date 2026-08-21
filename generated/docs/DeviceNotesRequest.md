# DeviceNotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** |  | 

## Example

```python
from phobos_torizon_io_api.models.device_notes_request import DeviceNotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNotesRequest from a JSON string
device_notes_request_instance = DeviceNotesRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceNotesRequest.to_json())

# convert the object into a dict
device_notes_request_dict = device_notes_request_instance.to_dict()
# create an instance of DeviceNotesRequest from a dict
device_notes_request_from_dict = DeviceNotesRequest.from_dict(device_notes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


