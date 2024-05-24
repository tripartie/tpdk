# DisputePersonaCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.dispute_persona_collection_read import DisputePersonaCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputePersonaCollectionRead from a JSON string
dispute_persona_collection_read_instance = DisputePersonaCollectionRead.from_json(json)
# print the JSON string representation of the object
print(DisputePersonaCollectionRead.to_json())

# convert the object into a dict
dispute_persona_collection_read_dict = dispute_persona_collection_read_instance.to_dict()
# create an instance of DisputePersonaCollectionRead from a dict
dispute_persona_collection_read_from_dict = DisputePersonaCollectionRead.from_dict(dispute_persona_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


