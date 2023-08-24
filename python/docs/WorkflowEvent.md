# WorkflowEvent



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**label** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**persona** | **str** |  | [optional] 
**dispute** | **str** |  | [optional] 
**occurred_at** | **datetime** |  | [optional] [readonly] 
**initiator** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.workflow_event import WorkflowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEvent from a JSON string
workflow_event_instance = WorkflowEvent.from_json(json)
# print the JSON string representation of the object
print WorkflowEvent.to_json()

# convert the object into a dict
workflow_event_dict = workflow_event_instance.to_dict()
# create an instance of WorkflowEvent from a dict
workflow_event_form_dict = workflow_event.from_dict(workflow_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


