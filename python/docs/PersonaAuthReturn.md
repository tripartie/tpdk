# PersonaAuthReturn



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them. | [optional] 
**expire_at** | **datetime** | This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour. | [optional] 

## Example

```python
from tpdk.models.persona_auth_return import PersonaAuthReturn

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaAuthReturn from a JSON string
persona_auth_return_instance = PersonaAuthReturn.from_json(json)
# print the JSON string representation of the object
print(PersonaAuthReturn.to_json())

# convert the object into a dict
persona_auth_return_dict = persona_auth_return_instance.to_dict()
# create an instance of PersonaAuthReturn from a dict
persona_auth_return_from_dict = PersonaAuthReturn.from_dict(persona_auth_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


