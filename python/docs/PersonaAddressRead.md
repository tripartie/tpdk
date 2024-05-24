# PersonaAddressRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from tpdk.models.persona_address_read import PersonaAddressRead

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaAddressRead from a JSON string
persona_address_read_instance = PersonaAddressRead.from_json(json)
# print the JSON string representation of the object
print(PersonaAddressRead.to_json())

# convert the object into a dict
persona_address_read_dict = persona_address_read_instance.to_dict()
# create an instance of PersonaAddressRead from a dict
persona_address_read_from_dict = PersonaAddressRead.from_dict(persona_address_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


