# UnprocessableEntityViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_path** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from tpdk.models.unprocessable_entity_violations_inner import UnprocessableEntityViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessableEntityViolationsInner from a JSON string
unprocessable_entity_violations_inner_instance = UnprocessableEntityViolationsInner.from_json(json)
# print the JSON string representation of the object
print UnprocessableEntityViolationsInner.to_json()

# convert the object into a dict
unprocessable_entity_violations_inner_dict = unprocessable_entity_violations_inner_instance.to_dict()
# create an instance of UnprocessableEntityViolationsInner from a dict
unprocessable_entity_violations_inner_form_dict = unprocessable_entity_violations_inner.from_dict(unprocessable_entity_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


