# LastSshSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_at** | **datetime** |  | 
**ip_address** | **str** |  | 

## Example

```python
from phobos_torizon_io_api.models.last_ssh_session import LastSshSession

# TODO update the JSON string below
json = "{}"
# create an instance of LastSshSession from a JSON string
last_ssh_session_instance = LastSshSession.from_json(json)
# print the JSON string representation of the object
print(LastSshSession.to_json())

# convert the object into a dict
last_ssh_session_dict = last_ssh_session_instance.to_dict()
# create an instance of LastSshSession from a dict
last_ssh_session_from_dict = LastSshSession.from_dict(last_ssh_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


