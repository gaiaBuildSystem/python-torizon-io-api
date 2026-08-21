# PaginationResultUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[UpdateResponse]**](UpdateResponse.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from phobos_torizon_io_api.models.pagination_result_update_response import PaginationResultUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultUpdateResponse from a JSON string
pagination_result_update_response_instance = PaginationResultUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(PaginationResultUpdateResponse.to_json())

# convert the object into a dict
pagination_result_update_response_dict = pagination_result_update_response_instance.to_dict()
# create an instance of PaginationResultUpdateResponse from a dict
pagination_result_update_response_from_dict = PaginationResultUpdateResponse.from_dict(pagination_result_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


