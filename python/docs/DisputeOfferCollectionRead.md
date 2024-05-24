# DisputeOfferCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**seller** | [**DisputePersonaCollectionRead**](DisputePersonaCollectionRead.md) | If the seller is actually YOUR organization, set it to NULL. | 
**title** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']

## Example

```python
from tpdk.models.dispute_offer_collection_read import DisputeOfferCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeOfferCollectionRead from a JSON string
dispute_offer_collection_read_instance = DisputeOfferCollectionRead.from_json(json)
# print the JSON string representation of the object
print(DisputeOfferCollectionRead.to_json())

# convert the object into a dict
dispute_offer_collection_read_dict = dispute_offer_collection_read_instance.to_dict()
# create an instance of DisputeOfferCollectionRead from a dict
dispute_offer_collection_read_from_dict = DisputeOfferCollectionRead.from_dict(dispute_offer_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


