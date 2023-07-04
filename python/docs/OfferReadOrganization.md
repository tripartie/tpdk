# OfferReadOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**icon** | [**EvidenceReadMedia**](EvidenceReadMedia.md) |  | [optional] 
**logo** | [**EvidenceReadMedia**](EvidenceReadMedia.md) |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**error_color** | **str** |  | [optional] 
**info_color** | **str** |  | [optional] 
**success_color** | **str** |  | [optional] 
**warning_color** | **str** |  | [optional] 
**direct_notification_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 
**rate_commission_safe_checkout** | **float** |  | 

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


