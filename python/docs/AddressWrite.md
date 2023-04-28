# AddressWrite



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
from tpdk.models.address_write import AddressWrite

# TODO update the JSON string below
json = "{}"
# create an instance of AddressWrite from a JSON string
address_write_instance = AddressWrite.from_json(json)
# print the JSON string representation of the object
print AddressWrite.to_json()

# convert the object into a dict
address_write_dict = address_write_instance.to_dict()
# create an instance of AddressWrite from a dict
address_write_form_dict = address_write.from_dict(address_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


