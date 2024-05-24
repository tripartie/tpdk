# AccessError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from tpdk.models.access_error import AccessError

# TODO update the JSON string below
json = "{}"
# create an instance of AccessError from a JSON string
access_error_instance = AccessError.from_json(json)
# print the JSON string representation of the object
print(AccessError.to_json())

# convert the object into a dict
access_error_dict = access_error_instance.to_dict()
# create an instance of AccessError from a dict
access_error_from_dict = AccessError.from_dict(access_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


