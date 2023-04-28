# PersonaWrite



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**address** | [**PersonaWriteAddress**](PersonaWriteAddress.md) |  | [optional] 
**metadata** | [**List[MetadataWrite]**](MetadataWrite.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | 

## Example

```python
from tpdk.models.persona_write import PersonaWrite

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaWrite from a JSON string
persona_write_instance = PersonaWrite.from_json(json)
# print the JSON string representation of the object
print PersonaWrite.to_json()

# convert the object into a dict
persona_write_dict = persona_write_instance.to_dict()
# create an instance of PersonaWrite from a dict
persona_write_form_dict = persona_write.from_dict(persona_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

