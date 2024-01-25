# WorkflowEventRead



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
from tpdk.models.workflow_event_read import WorkflowEventRead

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEventRead from a JSON string
workflow_event_read_instance = WorkflowEventRead.from_json(json)
# print the JSON string representation of the object
print WorkflowEventRead.to_json()

# convert the object into a dict
workflow_event_read_dict = workflow_event_read_instance.to_dict()
# create an instance of WorkflowEventRead from a dict
workflow_event_read_form_dict = workflow_event_read.from_dict(workflow_event_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


