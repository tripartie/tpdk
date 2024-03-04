# PersonaAddress

Always the Shipping address. Thus enabling automated package returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] [readonly] 
**company_name** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 
**zip_code** | **object** |  | [optional] 
**city_name** | **object** |  | [optional] 
**first_line** | **object** |  | [optional] 
**second_line** | **object** |  | [optional] 
**building_name** | **object** |  | [optional] 
**building_floor** | **object** |  | [optional] 
**gate_or_portal_or_inbox_code** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] [readonly] 
**updated_at** | **object** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.persona_address import PersonaAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaAddress from a JSON string
persona_address_instance = PersonaAddress.from_json(json)
# print the JSON string representation of the object
print PersonaAddress.to_json()

# convert the object into a dict
persona_address_dict = persona_address_instance.to_dict()
# create an instance of PersonaAddress from a dict
persona_address_form_dict = persona_address.from_dict(persona_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


