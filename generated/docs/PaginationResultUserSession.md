# PaginationResultUserSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[UserSession]**](UserSession.md) |  | [optional] 
**total** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from phobos_torizon_io_api.models.pagination_result_user_session import PaginationResultUserSession

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultUserSession from a JSON string
pagination_result_user_session_instance = PaginationResultUserSession.from_json(json)
# print the JSON string representation of the object
print(PaginationResultUserSession.to_json())

# convert the object into a dict
pagination_result_user_session_dict = pagination_result_user_session_instance.to_dict()
# create an instance of PaginationResultUserSession from a dict
pagination_result_user_session_from_dict = PaginationResultUserSession.from_dict(pagination_result_user_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


