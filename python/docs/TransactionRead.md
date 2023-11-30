# TransactionRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**offer** | [**OfferRead**](OfferRead.md) |  | 
**buyer** | [**PersonaRead**](PersonaRead.md) |  | 
**fees** | **float** |  | [optional] 
**refundable_fees** | **bool** |  | [optional] 
**metadata** | [**List[MetadataRead]**](MetadataRead.md) |  | [optional] 
**parcels** | [**List[ParcelRead]**](ParcelRead.md) |  | [optional] 

## Example

```python
from tpdk.models.transaction_read import TransactionRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRead from a JSON string
transaction_read_instance = TransactionRead.from_json(json)
# print the JSON string representation of the object
print TransactionRead.to_json()

# convert the object into a dict
transaction_read_dict = transaction_read_instance.to_dict()
# create an instance of TransactionRead from a dict
transaction_read_form_dict = transaction_read.from_dict(transaction_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


