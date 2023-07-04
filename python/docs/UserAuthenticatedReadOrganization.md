# UserAuthenticatedReadOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**domain_verified** | **bool** |  | 
**icon** | [**OrganizationAuthenticatedReadIcon**](OrganizationAuthenticatedReadIcon.md) |  | [optional] 
**logo** | [**OrganizationAuthenticatedReadIcon**](OrganizationAuthenticatedReadIcon.md) |  | [optional] 
**safe_checkout_toggle** | **bool** |  | 
**resolution_center_toggle** | **bool** |  | [default to True]
**internal_messaging_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**automated_return_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | 

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


