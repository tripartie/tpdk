# OrganizationAddressUpdate



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
from tpdk.models.organization_address_update import OrganizationAddressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAddressUpdate from a JSON string
organization_address_update_instance = OrganizationAddressUpdate.from_json(json)
# print the JSON string representation of the object
print(OrganizationAddressUpdate.to_json())

# convert the object into a dict
organization_address_update_dict = organization_address_update_instance.to_dict()
# create an instance of OrganizationAddressUpdate from a dict
organization_address_update_from_dict = OrganizationAddressUpdate.from_dict(organization_address_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


