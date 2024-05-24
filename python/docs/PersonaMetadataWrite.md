# PersonaMetadataWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.persona_metadata_write import PersonaMetadataWrite

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaMetadataWrite from a JSON string
persona_metadata_write_instance = PersonaMetadataWrite.from_json(json)
# print the JSON string representation of the object
print(PersonaMetadataWrite.to_json())

# convert the object into a dict
persona_metadata_write_dict = persona_metadata_write_instance.to_dict()
# create an instance of PersonaMetadataWrite from a dict
persona_metadata_write_from_dict = PersonaMetadataWrite.from_dict(persona_metadata_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


