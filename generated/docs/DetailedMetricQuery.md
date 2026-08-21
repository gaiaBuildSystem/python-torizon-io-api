# DetailedMetricQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** |  | 
**var_from** | **int** |  | 
**to** | **int** |  | 
**datapoint_count** | **int** |  | [optional] 
**total_buckets** | **int** |  | [optional] 

## Example

```python
from phobos_torizon_io_api.models.detailed_metric_query import DetailedMetricQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedMetricQuery from a JSON string
detailed_metric_query_instance = DetailedMetricQuery.from_json(json)
# print the JSON string representation of the object
print(DetailedMetricQuery.to_json())

# convert the object into a dict
detailed_metric_query_dict = detailed_metric_query_instance.to_dict()
# create an instance of DetailedMetricQuery from a dict
detailed_metric_query_from_dict = DetailedMetricQuery.from_dict(detailed_metric_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


