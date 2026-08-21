# OutlierValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** |  | 
**aggregation** | [**OutlierAggregationMethod**](OutlierAggregationMethod.md) |  | 
**outliers** | [**List[Outlier]**](Outlier.md) |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.outlier_values import OutlierValues

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierValues from a JSON string
outlier_values_instance = OutlierValues.from_json(json)
# print the JSON string representation of the object
print(OutlierValues.to_json())

# convert the object into a dict
outlier_values_dict = outlier_values_instance.to_dict()
# create an instance of OutlierValues from a dict
outlier_values_from_dict = OutlierValues.from_dict(outlier_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


