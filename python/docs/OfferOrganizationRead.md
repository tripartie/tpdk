# OfferOrganizationRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**custom_base_url** | **str** |  | [optional] 
**icon** | [**OfferMediaRead**](OfferMediaRead.md) |  | [optional] 
**logo** | [**OfferMediaRead**](OfferMediaRead.md) |  | [optional] 
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
from tpdk.models.offer_organization_read import OfferOrganizationRead

# TODO update the JSON string below
json = "{}"
# create an instance of OfferOrganizationRead from a JSON string
offer_organization_read_instance = OfferOrganizationRead.from_json(json)
# print the JSON string representation of the object
print(OfferOrganizationRead.to_json())

# convert the object into a dict
offer_organization_read_dict = offer_organization_read_instance.to_dict()
# create an instance of OfferOrganizationRead from a dict
offer_organization_read_from_dict = OfferOrganizationRead.from_dict(offer_organization_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


