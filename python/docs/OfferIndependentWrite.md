# OfferIndependentWrite

An Offer object represent a public listening

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**seller** | [**PersonaIndependentWrite**](PersonaIndependentWrite.md) |  | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**weight_in_gram** | **int** |  | [optional] 
**ean_code** | **str** |  | [optional] 
**metadata** | [**List[MetadataIndependentWrite]**](MetadataIndependentWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.offer_independent_write import OfferIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of OfferIndependentWrite from a JSON string
offer_independent_write_instance = OfferIndependentWrite.from_json(json)
# print the JSON string representation of the object
print OfferIndependentWrite.to_json()

# convert the object into a dict
offer_independent_write_dict = offer_independent_write_instance.to_dict()
# create an instance of OfferIndependentWrite from a dict
offer_independent_write_form_dict = offer_independent_write.from_dict(offer_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


