# DisputeWorkflowEventRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**occurred_at** | **datetime** |  | [optional] [readonly] 
**initiator** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute_workflow_event_read import DisputeWorkflowEventRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeWorkflowEventRead from a JSON string
dispute_workflow_event_read_instance = DisputeWorkflowEventRead.from_json(json)
# print the JSON string representation of the object
print(DisputeWorkflowEventRead.to_json())

# convert the object into a dict
dispute_workflow_event_read_dict = dispute_workflow_event_read_instance.to_dict()
# create an instance of DisputeWorkflowEventRead from a dict
dispute_workflow_event_read_from_dict = DisputeWorkflowEventRead.from_dict(dispute_workflow_event_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


