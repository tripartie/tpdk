# MetadataWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.metadata_write import MetadataWrite

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataWrite from a JSON string
metadata_write_instance = MetadataWrite.from_json(json)
# print the JSON string representation of the object
print(MetadataWrite.to_json())

# convert the object into a dict
metadata_write_dict = metadata_write_instance.to_dict()
# create an instance of MetadataWrite from a dict
metadata_write_from_dict = MetadataWrite.from_dict(metadata_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


