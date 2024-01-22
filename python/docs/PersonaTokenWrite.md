# PersonaTokenWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | **str** | The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona. | 

## Example

```python
from tpdk.models.persona_token_write import PersonaTokenWrite

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaTokenWrite from a JSON string
persona_token_write_instance = PersonaTokenWrite.from_json(json)
# print the JSON string representation of the object
print PersonaTokenWrite.to_json()

# convert the object into a dict
persona_token_write_dict = persona_token_write_instance.to_dict()
# create an instance of PersonaTokenWrite from a dict
persona_token_write_form_dict = persona_token_write.from_dict(persona_token_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


