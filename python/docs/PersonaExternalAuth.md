# PersonaExternalAuth



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
from tpdk.models.persona_external_auth import PersonaExternalAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaExternalAuth from a JSON string
persona_external_auth_instance = PersonaExternalAuth.from_json(json)
# print the JSON string representation of the object
print(PersonaExternalAuth.to_json())

# convert the object into a dict
persona_external_auth_dict = persona_external_auth_instance.to_dict()
# create an instance of PersonaExternalAuth from a dict
persona_external_auth_from_dict = PersonaExternalAuth.from_dict(persona_external_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


