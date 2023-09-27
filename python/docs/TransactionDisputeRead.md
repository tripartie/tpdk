# TransactionDisputeRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**offer** | [**OfferDisputeRead**](OfferDisputeRead.md) |  | 
**buyer** | **str** |  | 
**fees** | **float** |  | [optional] 
**metadata** | [**List[MetadataDisputeRead]**](MetadataDisputeRead.md) |  | [optional] 
**parcels** | [**List[ParcelDisputeRead]**](ParcelDisputeRead.md) |  | [optional] 

## Example

```python
from tpdk.models.transaction_dispute_read import TransactionDisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDisputeRead from a JSON string
transaction_dispute_read_instance = TransactionDisputeRead.from_json(json)
# print the JSON string representation of the object
print TransactionDisputeRead.to_json()

# convert the object into a dict
transaction_dispute_read_dict = transaction_dispute_read_instance.to_dict()
# create an instance of TransactionDisputeRead from a dict
transaction_dispute_read_form_dict = transaction_dispute_read.from_dict(transaction_dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


