# PersonaAddress

Always the Shipping address. Thus enabling automated package returns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**company_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**first_line** | **str** |  | [optional] 
**second_line** | **str** |  | [optional] 
**building_name** | **str** |  | [optional] 
**building_floor** | **str** |  | [optional] 
**gate_or_portal_or_inbox_code** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

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


