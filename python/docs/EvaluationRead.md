# EvaluationRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **int** |  | 
**comment** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.evaluation_read import EvaluationRead

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationRead from a JSON string
evaluation_read_instance = EvaluationRead.from_json(json)
# print the JSON string representation of the object
print EvaluationRead.to_json()

# convert the object into a dict
evaluation_read_dict = evaluation_read_instance.to_dict()
# create an instance of EvaluationRead from a dict
evaluation_read_form_dict = evaluation_read.from_dict(evaluation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


