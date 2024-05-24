# DisputeTransactionCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**offer** | [**DisputeOfferCollectionRead**](DisputeOfferCollectionRead.md) |  | 
**buyer** | [**DisputePersonaCollectionRead**](DisputePersonaCollectionRead.md) |  | 

## Example

```python
from tpdk.models.dispute_transaction_collection_read import DisputeTransactionCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeTransactionCollectionRead from a JSON string
dispute_transaction_collection_read_instance = DisputeTransactionCollectionRead.from_json(json)
# print the JSON string representation of the object
print(DisputeTransactionCollectionRead.to_json())

# convert the object into a dict
dispute_transaction_collection_read_dict = dispute_transaction_collection_read_instance.to_dict()
# create an instance of DisputeTransactionCollectionRead from a dict
dispute_transaction_collection_read_from_dict = DisputeTransactionCollectionRead.from_dict(dispute_transaction_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


