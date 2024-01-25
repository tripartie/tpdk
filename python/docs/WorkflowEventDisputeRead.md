# WorkflowEventDisputeRead



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
from tpdk.models.workflow_event_dispute_read import WorkflowEventDisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEventDisputeRead from a JSON string
workflow_event_dispute_read_instance = WorkflowEventDisputeRead.from_json(json)
# print the JSON string representation of the object
print WorkflowEventDisputeRead.to_json()

# convert the object into a dict
workflow_event_dispute_read_dict = workflow_event_dispute_read_instance.to_dict()
# create an instance of WorkflowEventDisputeRead from a dict
workflow_event_dispute_read_form_dict = workflow_event_dispute_read.from_dict(workflow_event_dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


