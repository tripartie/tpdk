# InvalidQueryError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from tpdk.models.invalid_query_error import InvalidQueryError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidQueryError from a JSON string
invalid_query_error_instance = InvalidQueryError.from_json(json)
# print the JSON string representation of the object
print InvalidQueryError.to_json()

# convert the object into a dict
invalid_query_error_dict = invalid_query_error_instance.to_dict()
# create an instance of InvalidQueryError from a dict
invalid_query_error_form_dict = invalid_query_error.from_dict(invalid_query_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


