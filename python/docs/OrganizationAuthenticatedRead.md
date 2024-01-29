# OrganizationAuthenticatedRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**domain_verified** | **bool** |  | 
**icon** | [**MediaAuthenticatedRead**](MediaAuthenticatedRead.md) |  | [optional] 
**logo** | [**MediaAuthenticatedRead**](MediaAuthenticatedRead.md) |  | [optional] 
**safe_checkout_toggle** | **bool** |  | 
**resolution_center_toggle** | **bool** |  | [default to True]
**internal_messaging_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**automated_return_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | 

## Example

```python
from tpdk.models.organization_authenticated_read import OrganizationAuthenticatedRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAuthenticatedRead from a JSON string
organization_authenticated_read_instance = OrganizationAuthenticatedRead.from_json(json)
# print the JSON string representation of the object
print OrganizationAuthenticatedRead.to_json()

# convert the object into a dict
organization_authenticated_read_dict = organization_authenticated_read_instance.to_dict()
# create an instance of OrganizationAuthenticatedRead from a dict
organization_authenticated_read_form_dict = organization_authenticated_read.from_dict(organization_authenticated_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


