# TransactionOfferCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**seller** | **str** | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**medias** | **List[str]** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.transaction_offer_collection_read import TransactionOfferCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionOfferCollectionRead from a JSON string
transaction_offer_collection_read_instance = TransactionOfferCollectionRead.from_json(json)
# print the JSON string representation of the object
print(TransactionOfferCollectionRead.to_json())

# convert the object into a dict
transaction_offer_collection_read_dict = transaction_offer_collection_read_instance.to_dict()
# create an instance of TransactionOfferCollectionRead from a dict
transaction_offer_collection_read_from_dict = TransactionOfferCollectionRead.from_dict(transaction_offer_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


