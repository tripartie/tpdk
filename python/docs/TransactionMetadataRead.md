# TransactionMetadataRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.transaction_metadata_read import TransactionMetadataRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMetadataRead from a JSON string
transaction_metadata_read_instance = TransactionMetadataRead.from_json(json)
# print the JSON string representation of the object
print(TransactionMetadataRead.to_json())

# convert the object into a dict
transaction_metadata_read_dict = transaction_metadata_read_instance.to_dict()
# create an instance of TransactionMetadataRead from a dict
transaction_metadata_read_from_dict = TransactionMetadataRead.from_dict(transaction_metadata_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


