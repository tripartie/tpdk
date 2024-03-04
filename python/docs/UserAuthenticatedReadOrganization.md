# UserAuthenticatedReadOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] [readonly] 
**name** | **object** |  | [optional] 
**domain_verified** | **object** |  | 
**icon** | [**OrganizationAuthenticatedReadIcon**](OrganizationAuthenticatedReadIcon.md) |  | [optional] 
**logo** | [**OrganizationAuthenticatedReadIcon**](OrganizationAuthenticatedReadIcon.md) |  | [optional] 
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
from tpdk.models.user_authenticated_read_organization import UserAuthenticatedReadOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuthenticatedReadOrganization from a JSON string
user_authenticated_read_organization_instance = UserAuthenticatedReadOrganization.from_json(json)
# print the JSON string representation of the object
print UserAuthenticatedReadOrganization.to_json()

# convert the object into a dict
user_authenticated_read_organization_dict = user_authenticated_read_organization_instance.to_dict()
# create an instance of UserAuthenticatedReadOrganization from a dict
user_authenticated_read_organization_form_dict = user_authenticated_read_organization.from_dict(user_authenticated_read_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


