# DisputePersonaRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 

## Example

```python
from tpdk.models.dispute_persona_read import DisputePersonaRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputePersonaRead from a JSON string
dispute_persona_read_instance = DisputePersonaRead.from_json(json)
# print the JSON string representation of the object
print(DisputePersonaRead.to_json())

# convert the object into a dict
dispute_persona_read_dict = dispute_persona_read_instance.to_dict()
# create an instance of DisputePersonaRead from a dict
dispute_persona_read_from_dict = DisputePersonaRead.from_dict(dispute_persona_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


