# OrganizationDisputeRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**icon** | [**MediaDisputeRead**](MediaDisputeRead.md) |  | [optional] 
**logo** | [**MediaDisputeRead**](MediaDisputeRead.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**error_color** | **str** |  | [optional] 
**info_color** | **str** |  | [optional] 
**success_color** | **str** |  | [optional] 
**warning_color** | **str** |  | [optional] 
**direct_notification_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**counter_proposal_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | 

## Example

```python
from tpdk.models.organization_dispute_read import OrganizationDisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDisputeRead from a JSON string
organization_dispute_read_instance = OrganizationDisputeRead.from_json(json)
# print the JSON string representation of the object
print OrganizationDisputeRead.to_json()

# convert the object into a dict
organization_dispute_read_dict = organization_dispute_read_instance.to_dict()
# create an instance of OrganizationDisputeRead from a dict
organization_dispute_read_form_dict = organization_dispute_read.from_dict(organization_dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


