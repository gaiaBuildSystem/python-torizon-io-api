# FleetMetricsOutliersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** |  | 
**var_from** | **int** |  | 
**to** | **int** |  | 
**aggregation** | [**OutlierAggregationMethod**](OutlierAggregationMethod.md) |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.fleet_metrics_outliers_request import FleetMetricsOutliersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FleetMetricsOutliersRequest from a JSON string
fleet_metrics_outliers_request_instance = FleetMetricsOutliersRequest.from_json(json)
# print the JSON string representation of the object
print(FleetMetricsOutliersRequest.to_json())

# convert the object into a dict
fleet_metrics_outliers_request_dict = fleet_metrics_outliers_request_instance.to_dict()
# create an instance of FleetMetricsOutliersRequest from a dict
fleet_metrics_outliers_request_from_dict = FleetMetricsOutliersRequest.from_dict(fleet_metrics_outliers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


