# DisputeOfferIndependentWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**seller** | [**DisputePersonaIndependentWrite**](DisputePersonaIndependentWrite.md) | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**weight_in_gram** | **int** |  | [optional] 
**ean_code** | **str** |  | [optional] 
**metadata** | [**List[DisputeMetadataIndependentWrite]**](DisputeMetadataIndependentWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.dispute_offer_independent_write import DisputeOfferIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeOfferIndependentWrite from a JSON string
dispute_offer_independent_write_instance = DisputeOfferIndependentWrite.from_json(json)
# print the JSON string representation of the object
print(DisputeOfferIndependentWrite.to_json())

# convert the object into a dict
dispute_offer_independent_write_dict = dispute_offer_independent_write_instance.to_dict()
# create an instance of DisputeOfferIndependentWrite from a dict
dispute_offer_independent_write_from_dict = DisputeOfferIndependentWrite.from_dict(dispute_offer_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


