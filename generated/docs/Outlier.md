# Outlier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **UUID** |  | 
**value** | **float** |  | [optional] 
**observed_at** | **datetime** |  | 

## Example

```python
from phobos_torizon_io_api.models.outlier import Outlier

# TODO update the JSON string below
json = "{}"
# create an instance of Outlier from a JSON string
outlier_instance = Outlier.from_json(json)
# print the JSON string representation of the object
print(Outlier.to_json())

# convert the object into a dict
outlier_dict = outlier_instance.to_dict()
# create an instance of Outlier from a dict
outlier_from_dict = Outlier.from_dict(outlier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


