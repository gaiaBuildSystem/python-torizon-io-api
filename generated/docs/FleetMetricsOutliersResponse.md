# FleetMetricsOutliersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[OutlierValues]**](OutlierValues.md) |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.fleet_metrics_outliers_response import FleetMetricsOutliersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FleetMetricsOutliersResponse from a JSON string
fleet_metrics_outliers_response_instance = FleetMetricsOutliersResponse.from_json(json)
# print the JSON string representation of the object
print(FleetMetricsOutliersResponse.to_json())

# convert the object into a dict
fleet_metrics_outliers_response_dict = fleet_metrics_outliers_response_instance.to_dict()
# create an instance of FleetMetricsOutliersResponse from a dict
fleet_metrics_outliers_response_from_dict = FleetMetricsOutliersResponse.from_dict(fleet_metrics_outliers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


