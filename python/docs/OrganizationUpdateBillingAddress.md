# OrganizationUpdateBillingAddress


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
from tpdk.models.organization_update_billing_address import OrganizationUpdateBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdateBillingAddress from a JSON string
organization_update_billing_address_instance = OrganizationUpdateBillingAddress.from_json(json)
# print the JSON string representation of the object
print OrganizationUpdateBillingAddress.to_json()

# convert the object into a dict
organization_update_billing_address_dict = organization_update_billing_address_instance.to_dict()
# create an instance of OrganizationUpdateBillingAddress from a dict
organization_update_billing_address_form_dict = organization_update_billing_address.from_dict(organization_update_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


