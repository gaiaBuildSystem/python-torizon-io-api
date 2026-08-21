# SshSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_pub_keys** | **List[str]** |  | [optional] 
**reverse_port** | **int** |  | 
**ra_server_url** | **str** |  | 
**ra_server_ssh_pub_key** | **str** |  | 
**reverse_server_url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from phobos_torizon_io_api.models.ssh_session import SshSession

# TODO update the JSON string below
json = "{}"
# create an instance of SshSession from a JSON string
ssh_session_instance = SshSession.from_json(json)
# print the JSON string representation of the object
print(SshSession.to_json())

# convert the object into a dict
ssh_session_dict = ssh_session_instance.to_dict()
# create an instance of SshSession from a dict
ssh_session_from_dict = SshSession.from_dict(ssh_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


