# OrganizationUpdate



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**commercial_registry_number** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**billing_address** | [**OrganizationUpdateBillingAddress**](OrganizationUpdateBillingAddress.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**error_color** | **str** |  | [optional] 
**info_color** | **str** |  | [optional] 
**success_color** | **str** |  | [optional] 
**warning_color** | **str** |  | [optional] 
**end_user_notification_toggle** | **bool** |  | 
**anonymity_level** | **str** |  | [default to 'PARTIAL_FIRST_NAME']
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | 

## Example

```python
from tpdk.models.organization_update import OrganizationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdate from a JSON string
organization_update_instance = OrganizationUpdate.from_json(json)
# print the JSON string representation of the object
print OrganizationUpdate.to_json()

# convert the object into a dict
organization_update_dict = organization_update_instance.to_dict()
# create an instance of OrganizationUpdate from a dict
organization_update_form_dict = organization_update.from_dict(organization_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


