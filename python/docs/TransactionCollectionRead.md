# TransactionCollectionRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**offer** | [**OfferCollectionRead**](OfferCollectionRead.md) |  | [optional] 

## Example

```python
from tpdk.models.transaction_collection_read import TransactionCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCollectionRead from a JSON string
transaction_collection_read_instance = TransactionCollectionRead.from_json(json)
# print the JSON string representation of the object
print TransactionCollectionRead.to_json()

# convert the object into a dict
transaction_collection_read_dict = transaction_collection_read_instance.to_dict()
# create an instance of TransactionCollectionRead from a dict
transaction_collection_read_form_dict = transaction_collection_read.from_dict(transaction_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


