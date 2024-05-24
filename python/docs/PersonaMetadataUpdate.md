# PersonaMetadataUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.persona_metadata_update import PersonaMetadataUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaMetadataUpdate from a JSON string
persona_metadata_update_instance = PersonaMetadataUpdate.from_json(json)
# print the JSON string representation of the object
print(PersonaMetadataUpdate.to_json())

# convert the object into a dict
persona_metadata_update_dict = persona_metadata_update_instance.to_dict()
# create an instance of PersonaMetadataUpdate from a dict
persona_metadata_update_from_dict = PersonaMetadataUpdate.from_dict(persona_metadata_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


