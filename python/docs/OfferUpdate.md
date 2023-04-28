# OfferUpdate



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**enforce_persona_auth** | **bool** | Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration. | 
**override_rate_commission_safe_checkout** | **float** | Override YOUR platform fees for that particular Offer. | 
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [default to 1]
**weight_in_gram** | **int** |  | [optional] 
**shipping_allowed** | **bool** | That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined. | 
**hand_delivery_allowed** | **bool** | Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product. | [default to True]
**shipping_carriers** | **List[str]** | If you wish to enable automated shipping label generation through a specific provider, specify it there. | 
**ean_code** | **str** |  | [optional] 
**metadata** | [**List[MetadataUpdate]**](MetadataUpdate.md) |  | 

## Example

```python
from tpdk.models.offer_update import OfferUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OfferUpdate from a JSON string
offer_update_instance = OfferUpdate.from_json(json)
# print the JSON string representation of the object
print OfferUpdate.to_json()

# convert the object into a dict
offer_update_dict = offer_update_instance.to_dict()
# create an instance of OfferUpdate from a dict
offer_update_form_dict = offer_update.from_dict(offer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


