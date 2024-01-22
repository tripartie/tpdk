# OfferCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**seller** | [**PersonaCollectionRead**](PersonaCollectionRead.md) | If the seller is actually YOUR organization, set it to NULL. | 
**title** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']

## Example

```python
from tpdk.models.offer_collection_read import OfferCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of OfferCollectionRead from a JSON string
offer_collection_read_instance = OfferCollectionRead.from_json(json)
# print the JSON string representation of the object
print OfferCollectionRead.to_json()

# convert the object into a dict
offer_collection_read_dict = offer_collection_read_instance.to_dict()
# create an instance of OfferCollectionRead from a dict
offer_collection_read_form_dict = offer_collection_read.from_dict(offer_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


