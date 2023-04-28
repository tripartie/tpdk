# PersonaToken



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**persona** | **str** |  | 
**object_id** | **str** | Optional limitation on a specific object. | [optional] 
**token** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**expire_at** | **datetime** |  | 

## Example

```python
from tpdk.models.persona_token import PersonaToken

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaToken from a JSON string
persona_token_instance = PersonaToken.from_json(json)
# print the JSON string representation of the object
print PersonaToken.to_json()

# convert the object into a dict
persona_token_dict = persona_token_instance.to_dict()
# create an instance of PersonaToken from a dict
persona_token_form_dict = persona_token.from_dict(persona_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


