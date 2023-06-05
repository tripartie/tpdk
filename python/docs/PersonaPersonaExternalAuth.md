# PersonaPersonaExternalAuth



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | [optional] 
**target_url** | **str** | The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona. | [optional] 
**plain_password** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 

## Example

```python
from tpdk.models.persona_persona_external_auth import PersonaPersonaExternalAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaPersonaExternalAuth from a JSON string
persona_persona_external_auth_instance = PersonaPersonaExternalAuth.from_json(json)
# print the JSON string representation of the object
print PersonaPersonaExternalAuth.to_json()

# convert the object into a dict
persona_persona_external_auth_dict = persona_persona_external_auth_instance.to_dict()
# create an instance of PersonaPersonaExternalAuth from a dict
persona_persona_external_auth_form_dict = persona_persona_external_auth.from_dict(persona_persona_external_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


