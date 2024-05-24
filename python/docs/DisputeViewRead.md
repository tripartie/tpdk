# DisputeViewRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_count** | **int** |  | [default to 1]
**created_at** | **datetime** |  | [optional] [readonly] 
**named_source** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute_view_read import DisputeViewRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeViewRead from a JSON string
dispute_view_read_instance = DisputeViewRead.from_json(json)
# print the JSON string representation of the object
print(DisputeViewRead.to_json())

# convert the object into a dict
dispute_view_read_dict = dispute_view_read_instance.to_dict()
# create an instance of DisputeViewRead from a dict
dispute_view_read_from_dict = DisputeViewRead.from_dict(dispute_view_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


