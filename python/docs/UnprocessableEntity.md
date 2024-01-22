# UnprocessableEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**violations** | [**List[UnprocessableEntityViolationsInner]**](UnprocessableEntityViolationsInner.md) |  | [optional] 

## Example

```python
from tpdk.models.unprocessable_entity import UnprocessableEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessableEntity from a JSON string
unprocessable_entity_instance = UnprocessableEntity.from_json(json)
# print the JSON string representation of the object
print UnprocessableEntity.to_json()

# convert the object into a dict
unprocessable_entity_dict = unprocessable_entity_instance.to_dict()
# create an instance of UnprocessableEntity from a dict
unprocessable_entity_form_dict = unprocessable_entity.from_dict(unprocessable_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


