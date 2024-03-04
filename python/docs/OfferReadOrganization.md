# OfferReadOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**website_url** | **object** |  | [optional] 
**custom_base_url** | **object** |  | [optional] 
**icon** | [**EvidenceReadMedia**](EvidenceReadMedia.md) |  | [optional] 
**logo** | [**EvidenceReadMedia**](EvidenceReadMedia.md) |  | [optional] 
**primary_color** | **object** |  | [optional] 
**secondary_color** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 
**error_color** | **object** |  | [optional] 
**info_color** | **object** |  | [optional] 
**success_color** | **object** |  | [optional] 
**warning_color** | **object** |  | [optional] 
**direct_notification_toggle** | **object** |  | 
**persona_auth_portal_toggle** | **object** |  | 
**counter_proposal_toggle** | **object** |  | 
**flat_rate_enabled** | **object** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **object** |  | 

## Example

```python
from tpdk.models.offer_read_organization import OfferReadOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of OfferReadOrganization from a JSON string
offer_read_organization_instance = OfferReadOrganization.from_json(json)
# print the JSON string representation of the object
print OfferReadOrganization.to_json()

# convert the object into a dict
offer_read_organization_dict = offer_read_organization_instance.to_dict()
# create an instance of OfferReadOrganization from a dict
offer_read_organization_form_dict = offer_read_organization.from_dict(offer_read_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


