# UpdateReportedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_code** | **str** |  | 
**success** | **bool** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.update_reported_result import UpdateReportedResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReportedResult from a JSON string
update_reported_result_instance = UpdateReportedResult.from_json(json)
# print the JSON string representation of the object
print(UpdateReportedResult.to_json())

# convert the object into a dict
update_reported_result_dict = update_reported_result_instance.to_dict()
# create an instance of UpdateReportedResult from a dict
update_reported_result_from_dict = UpdateReportedResult.from_dict(update_reported_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


