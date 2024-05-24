# ViewDisputeRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_count** | **int** |  | [default to 1]
**created_at** | **datetime** |  | [optional] [readonly] 
**named_source** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.view_dispute_read import ViewDisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDisputeRead from a JSON string
view_dispute_read_instance = ViewDisputeRead.from_json(json)
# print the JSON string representation of the object
print(ViewDisputeRead.to_json())

# convert the object into a dict
view_dispute_read_dict = view_dispute_read_instance.to_dict()
# create an instance of ViewDisputeRead from a dict
view_dispute_read_from_dict = ViewDisputeRead.from_dict(view_dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


