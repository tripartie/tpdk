# DisputeIndependentWrite

Access directly our resolution center without having used the safe-checkout feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**TransactionIndependentWrite**](TransactionIndependentWrite.md) |  | 
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**metadata** | [**List[MetadataIndependentWrite]**](MetadataIndependentWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.dispute_independent_write import DisputeIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeIndependentWrite from a JSON string
dispute_independent_write_instance = DisputeIndependentWrite.from_json(json)
# print the JSON string representation of the object
print DisputeIndependentWrite.to_json()

# convert the object into a dict
dispute_independent_write_dict = dispute_independent_write_instance.to_dict()
# create an instance of DisputeIndependentWrite from a dict
dispute_independent_write_form_dict = dispute_independent_write.from_dict(dispute_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


