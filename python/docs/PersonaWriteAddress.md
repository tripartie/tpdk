# PersonaWriteAddress

Always the Shipping address. Thus enabling automated package returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**zip_code** | **object** |  | [optional] 
**city_name** | **object** |  | [optional] 
**first_line** | **object** |  | [optional] 
**second_line** | **object** |  | [optional] 
**building_name** | **object** |  | [optional] 
**building_floor** | **object** |  | [optional] 
**gate_or_portal_or_inbox_code** | **object** |  | [optional] 

## Example

```python
from tpdk.models.persona_write_address import PersonaWriteAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaWriteAddress from a JSON string
persona_write_address_instance = PersonaWriteAddress.from_json(json)
# print the JSON string representation of the object
print PersonaWriteAddress.to_json()

# convert the object into a dict
persona_write_address_dict = persona_write_address_instance.to_dict()
# create an instance of PersonaWriteAddress from a dict
persona_write_address_form_dict = persona_write_address.from_dict(persona_write_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


