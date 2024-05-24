# OfferCollectionRead

An Offer object represent a public listening

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**enforce_persona_auth** | **bool** | Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration. | [default to True]
**override_rate_commission_safe_checkout** | **float** | Override YOUR platform fees for that particular Offer. | [optional] 
**seller** | **str** | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**shipping_allowed** | **bool** | That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined. | 
**hand_delivery_allowed** | **bool** | Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product. | [default to True]
**shipping_carriers** | **List[str]** | If you wish to enable automated shipping label generation through a specific provider, specify it there. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.offer_collection_read import OfferCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of OfferCollectionRead from a JSON string
offer_collection_read_instance = OfferCollectionRead.from_json(json)
# print the JSON string representation of the object
print(OfferCollectionRead.to_json())

# convert the object into a dict
offer_collection_read_dict = offer_collection_read_instance.to_dict()
# create an instance of OfferCollectionRead from a dict
offer_collection_read_from_dict = OfferCollectionRead.from_dict(offer_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


