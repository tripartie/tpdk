# DisputeWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 

## Example

```python
from tpdk.models.dispute_write import DisputeWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeWrite from a JSON string
dispute_write_instance = DisputeWrite.from_json(json)
# print the JSON string representation of the object
print DisputeWrite.to_json()

# convert the object into a dict
dispute_write_dict = dispute_write_instance.to_dict()
# create an instance of DisputeWrite from a dict
dispute_write_form_dict = dispute_write.from_dict(dispute_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


