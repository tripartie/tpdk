# TransactionParcelRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** |  | 
**identifier** | **str** |  | 
**price** | **float** |  | [optional] 
**refundable** | **bool** |  | [optional] 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.transaction_parcel_read import TransactionParcelRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionParcelRead from a JSON string
transaction_parcel_read_instance = TransactionParcelRead.from_json(json)
# print the JSON string representation of the object
print(TransactionParcelRead.to_json())

# convert the object into a dict
transaction_parcel_read_dict = transaction_parcel_read_instance.to_dict()
# create an instance of TransactionParcelRead from a dict
transaction_parcel_read_from_dict = TransactionParcelRead.from_dict(transaction_parcel_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


