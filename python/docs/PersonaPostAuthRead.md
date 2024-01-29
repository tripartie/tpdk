# PersonaPostAuthRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them. | [optional] 
**expire_at** | **datetime** | This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour. | [optional] 

## Example

```python
from tpdk.models.persona_post_auth_read import PersonaPostAuthRead

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaPostAuthRead from a JSON string
persona_post_auth_read_instance = PersonaPostAuthRead.from_json(json)
# print the JSON string representation of the object
print PersonaPostAuthRead.to_json()

# convert the object into a dict
persona_post_auth_read_dict = persona_post_auth_read_instance.to_dict()
# create an instance of PersonaPostAuthRead from a dict
persona_post_auth_read_form_dict = persona_post_auth_read.from_dict(persona_post_auth_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


