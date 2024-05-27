# DisputeOrganizationRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**icon** | [**DisputeMediaRead**](DisputeMediaRead.md) |  | [optional] 
**logo** | [**DisputeMediaRead**](DisputeMediaRead.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**direct_notification_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**counter_proposal_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute_organization_read import DisputeOrganizationRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeOrganizationRead from a JSON string
dispute_organization_read_instance = DisputeOrganizationRead.from_json(json)
# print the JSON string representation of the object
print(DisputeOrganizationRead.to_json())

# convert the object into a dict
dispute_organization_read_dict = dispute_organization_read_instance.to_dict()
# create an instance of DisputeOrganizationRead from a dict
dispute_organization_read_from_dict = DisputeOrganizationRead.from_dict(dispute_organization_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


