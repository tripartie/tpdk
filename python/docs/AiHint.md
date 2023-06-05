# AiHint



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**dispute** | **str** |  | [optional] 
**evidence** | **str** |  | [optional] 
**score_of_trust** | **int** |  | 
**label** | **str** |  | 
**dismissed** | **bool** |  | 
**to_be_disclosed** | **bool** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.ai_hint import AiHint

# TODO update the JSON string below
json = "{}"
# create an instance of AiHint from a JSON string
ai_hint_instance = AiHint.from_json(json)
# print the JSON string representation of the object
print AiHint.to_json()

# convert the object into a dict
ai_hint_dict = ai_hint_instance.to_dict()
# create an instance of AiHint from a dict
ai_hint_form_dict = ai_hint.from_dict(ai_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


