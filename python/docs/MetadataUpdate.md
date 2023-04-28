# MetadataUpdate



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.metadata_update import MetadataUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataUpdate from a JSON string
metadata_update_instance = MetadataUpdate.from_json(json)
# print the JSON string representation of the object
print MetadataUpdate.to_json()

# convert the object into a dict
metadata_update_dict = metadata_update_instance.to_dict()
# create an instance of MetadataUpdate from a dict
metadata_update_form_dict = metadata_update.from_dict(metadata_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


