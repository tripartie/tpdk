# OrganizationUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**vat_number** | **str** |  | [optional] 
**commercial_registry_number** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**billing_address** | [**OrganizationAddressUpdate**](OrganizationAddressUpdate.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**direct_notification_toggle** | **bool** |  | [optional] [default to True]
**anonymity_level** | **str** |  | [optional] [default to 'PARTIAL_FIRST_NAME']
**internal_messaging_toggle** | **bool** |  | [optional] [default to True]
**persona_auth_portal_toggle** | **bool** |  | [optional] 
**automated_return_toggle** | **bool** |  | [optional] [default to True]
**counter_proposal_toggle** | **bool** |  | [optional] [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.organization_update import OrganizationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdate from a JSON string
organization_update_instance = OrganizationUpdate.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdate.to_json())

# convert the object into a dict
organization_update_dict = organization_update_instance.to_dict()
# create an instance of OrganizationUpdate from a dict
organization_update_from_dict = OrganizationUpdate.from_dict(organization_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


