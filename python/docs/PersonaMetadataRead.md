# PersonaMetadataRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.persona_metadata_read import PersonaMetadataRead

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaMetadataRead from a JSON string
persona_metadata_read_instance = PersonaMetadataRead.from_json(json)
# print the JSON string representation of the object
print(PersonaMetadataRead.to_json())

# convert the object into a dict
persona_metadata_read_dict = persona_metadata_read_instance.to_dict()
# create an instance of PersonaMetadataRead from a dict
persona_metadata_read_from_dict = PersonaMetadataRead.from_dict(persona_metadata_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


