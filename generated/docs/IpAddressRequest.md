# IpAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | 

## Example

```python
from phobos_torizon_io_api.models.ip_address_request import IpAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressRequest from a JSON string
ip_address_request_instance = IpAddressRequest.from_json(json)
# print the JSON string representation of the object
print(IpAddressRequest.to_json())

# convert the object into a dict
ip_address_request_dict = ip_address_request_instance.to_dict()
# create an instance of IpAddressRequest from a dict
ip_address_request_from_dict = IpAddressRequest.from_dict(ip_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


