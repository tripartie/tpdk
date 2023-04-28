# AddressIndependentWrite



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

## Example

```python
from tpdk.models.address_independent_write import AddressIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of AddressIndependentWrite from a JSON string
address_independent_write_instance = AddressIndependentWrite.from_json(json)
# print the JSON string representation of the object
print AddressIndependentWrite.to_json()

# convert the object into a dict
address_independent_write_dict = address_independent_write_instance.to_dict()
# create an instance of AddressIndependentWrite from a dict
address_independent_write_form_dict = address_independent_write.from_dict(address_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


