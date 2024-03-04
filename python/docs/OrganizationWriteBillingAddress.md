# OrganizationWriteBillingAddress


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
from tpdk.models.organization_write_billing_address import OrganizationWriteBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWriteBillingAddress from a JSON string
organization_write_billing_address_instance = OrganizationWriteBillingAddress.from_json(json)
# print the JSON string representation of the object
print OrganizationWriteBillingAddress.to_json()

# convert the object into a dict
organization_write_billing_address_dict = organization_write_billing_address_instance.to_dict()
# create an instance of OrganizationWriteBillingAddress from a dict
organization_write_billing_address_form_dict = organization_write_billing_address.from_dict(organization_write_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


