# UserOrganizationRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**domain_verified** | **bool** |  | [optional] 
**icon** | [**UserMediaRead**](UserMediaRead.md) |  | [optional] 
**logo** | [**UserMediaRead**](UserMediaRead.md) |  | [optional] 
**safe_checkout_toggle** | **bool** |  | [optional] 
**resolution_center_toggle** | **bool** |  | [optional] [default to True]
**internal_messaging_toggle** | **bool** |  | [optional] [default to True]
**persona_auth_portal_toggle** | **bool** |  | [optional] 
**automated_return_toggle** | **bool** |  | [optional] [default to True]
**counter_proposal_toggle** | **bool** |  | [optional] [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | [optional] 

## Example

```python
from tpdk.models.user_organization_read import UserOrganizationRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationRead from a JSON string
user_organization_read_instance = UserOrganizationRead.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationRead.to_json())

# convert the object into a dict
user_organization_read_dict = user_organization_read_instance.to_dict()
# create an instance of UserOrganizationRead from a dict
user_organization_read_from_dict = UserOrganizationRead.from_dict(user_organization_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


