# MetadataRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.metadata_read import MetadataRead

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataRead from a JSON string
metadata_read_instance = MetadataRead.from_json(json)
# print the JSON string representation of the object
print MetadataRead.to_json()

# convert the object into a dict
metadata_read_dict = metadata_read_instance.to_dict()
# create an instance of MetadataRead from a dict
metadata_read_form_dict = metadata_read.from_dict(metadata_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


