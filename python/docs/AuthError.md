# AuthError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from tpdk.models.auth_error import AuthError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthError from a JSON string
auth_error_instance = AuthError.from_json(json)
# print the JSON string representation of the object
print(AuthError.to_json())

# convert the object into a dict
auth_error_dict = auth_error_instance.to_dict()
# create an instance of AuthError from a dict
auth_error_from_dict = AuthError.from_dict(auth_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


