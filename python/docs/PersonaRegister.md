# PersonaRegister



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | [optional] 
**plain_password** | **str** |  | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**gender** | **str** |  | [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 

## Example

```python
from tpdk.models.persona_register import PersonaRegister

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaRegister from a JSON string
persona_register_instance = PersonaRegister.from_json(json)
# print the JSON string representation of the object
print(PersonaRegister.to_json())

# convert the object into a dict
persona_register_dict = persona_register_instance.to_dict()
# create an instance of PersonaRegister from a dict
persona_register_from_dict = PersonaRegister.from_dict(persona_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


