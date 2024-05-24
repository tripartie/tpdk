# DisputeTransactionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**offer** | [**DisputeOfferRead**](DisputeOfferRead.md) |  | 
**buyer** | [**DisputePersonaRead**](DisputePersonaRead.md) |  | 
**fees** | **float** |  | [optional] 
**refundable_fees** | **bool** |  | [optional] 
**metadata** | [**List[DisputeMetadataRead]**](DisputeMetadataRead.md) |  | [optional] 
**parcels** | [**List[DisputeParcelRead]**](DisputeParcelRead.md) |  | [optional] 

## Example

```python
from tpdk.models.dispute_transaction_read import DisputeTransactionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeTransactionRead from a JSON string
dispute_transaction_read_instance = DisputeTransactionRead.from_json(json)
# print the JSON string representation of the object
print(DisputeTransactionRead.to_json())

# convert the object into a dict
dispute_transaction_read_dict = dispute_transaction_read_instance.to_dict()
# create an instance of DisputeTransactionRead from a dict
dispute_transaction_read_from_dict = DisputeTransactionRead.from_dict(dispute_transaction_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


