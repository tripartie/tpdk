# UserCollectionReadOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] [readonly] 
**name** | **object** |  | [optional] 
**vat_number** | **object** |  | [optional] 
**commercial_registry_number** | **object** |  | [optional] 
**website_url** | **object** |  | [optional] 
**icon** | [**OrganizationCollectionReadIcon**](OrganizationCollectionReadIcon.md) |  | [optional] 
**logo** | [**OrganizationCollectionReadIcon**](OrganizationCollectionReadIcon.md) |  | [optional] 
**direct_notification_toggle** | **object** |  | 
**safe_checkout_toggle** | **object** |  | 
**resolution_center_toggle** | **object** |  | 
**internal_messaging_toggle** | **object** |  | 
**persona_auth_portal_toggle** | **object** |  | 
**automated_return_toggle** | **object** |  | 
**counter_proposal_toggle** | **object** |  | 
**flat_rate_enabled** | **object** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **object** |  | 

## Example

```python
from tpdk.models.user_collection_read_organization import UserCollectionReadOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionReadOrganization from a JSON string
user_collection_read_organization_instance = UserCollectionReadOrganization.from_json(json)
# print the JSON string representation of the object
print UserCollectionReadOrganization.to_json()

# convert the object into a dict
user_collection_read_organization_dict = user_collection_read_organization_instance.to_dict()
# create an instance of UserCollectionReadOrganization from a dict
user_collection_read_organization_form_dict = user_collection_read_organization.from_dict(user_collection_read_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


