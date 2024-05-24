# DisputeTransactionIndependentWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**DisputeOfferIndependentWrite**](DisputeOfferIndependentWrite.md) |  | 
**buyer** | [**DisputePersonaIndependentWrite**](DisputePersonaIndependentWrite.md) |  | 
**fees** | **float** |  | [optional] 
**refundable_fees** | **bool** |  | [optional] 
**metadata** | [**List[DisputeMetadataIndependentWrite]**](DisputeMetadataIndependentWrite.md) |  | [optional] 
**parcels** | [**List[DisputeParcelIndependentWrite]**](DisputeParcelIndependentWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.dispute_transaction_independent_write import DisputeTransactionIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeTransactionIndependentWrite from a JSON string
dispute_transaction_independent_write_instance = DisputeTransactionIndependentWrite.from_json(json)
# print the JSON string representation of the object
print(DisputeTransactionIndependentWrite.to_json())

# convert the object into a dict
dispute_transaction_independent_write_dict = dispute_transaction_independent_write_instance.to_dict()
# create an instance of DisputeTransactionIndependentWrite from a dict
dispute_transaction_independent_write_from_dict = DisputeTransactionIndependentWrite.from_dict(dispute_transaction_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


