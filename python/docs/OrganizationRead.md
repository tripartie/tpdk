# OrganizationRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**icon** | [**MediaRead**](MediaRead.md) |  | [optional] 
**logo** | [**MediaRead**](MediaRead.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**direct_notification_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**counter_proposal_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.organization_read import OrganizationRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRead from a JSON string
organization_read_instance = OrganizationRead.from_json(json)
# print the JSON string representation of the object
print(OrganizationRead.to_json())

# convert the object into a dict
organization_read_dict = organization_read_instance.to_dict()
# create an instance of OrganizationRead from a dict
organization_read_from_dict = OrganizationRead.from_dict(organization_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


