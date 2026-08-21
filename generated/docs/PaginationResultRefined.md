# PaginationResultRefined


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from phobos_torizon_io_api.models.pagination_result_refined import PaginationResultRefined

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultRefined from a JSON string
pagination_result_refined_instance = PaginationResultRefined.from_json(json)
# print the JSON string representation of the object
print(PaginationResultRefined.to_json())

# convert the object into a dict
pagination_result_refined_dict = pagination_result_refined_instance.to_dict()
# create an instance of PaginationResultRefined from a dict
pagination_result_refined_from_dict = PaginationResultRefined.from_dict(pagination_result_refined_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


