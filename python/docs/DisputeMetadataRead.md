# DisputeMetadataRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.dispute_metadata_read import DisputeMetadataRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeMetadataRead from a JSON string
dispute_metadata_read_instance = DisputeMetadataRead.from_json(json)
# print the JSON string representation of the object
print(DisputeMetadataRead.to_json())

# convert the object into a dict
dispute_metadata_read_dict = dispute_metadata_read_instance.to_dict()
# create an instance of DisputeMetadataRead from a dict
dispute_metadata_read_from_dict = DisputeMetadataRead.from_dict(dispute_metadata_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


