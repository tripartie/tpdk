# TransactionIndependentWrite



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferIndependentWrite**](OfferIndependentWrite.md) |  | [optional] 
**buyer** | [**PersonaIndependentWrite**](PersonaIndependentWrite.md) |  | [optional] 
**fees** | **float** |  | [optional] 
**metadata** | [**List[MetadataIndependentWrite]**](MetadataIndependentWrite.md) |  | 
**parcels** | [**List[ParcelIndependentWrite]**](ParcelIndependentWrite.md) |  | 

## Example

```python
from tpdk.models.transaction_independent_write import TransactionIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIndependentWrite from a JSON string
transaction_independent_write_instance = TransactionIndependentWrite.from_json(json)
# print the JSON string representation of the object
print TransactionIndependentWrite.to_json()

# convert the object into a dict
transaction_independent_write_dict = transaction_independent_write_instance.to_dict()
# create an instance of TransactionIndependentWrite from a dict
transaction_independent_write_form_dict = transaction_independent_write.from_dict(transaction_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


