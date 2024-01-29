# UserJwtWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**totp_input** | **str** |  | [optional] 

## Example

```python
from tpdk.models.user_jwt_write import UserJwtWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserJwtWrite from a JSON string
user_jwt_write_instance = UserJwtWrite.from_json(json)
# print the JSON string representation of the object
print UserJwtWrite.to_json()

# convert the object into a dict
user_jwt_write_dict = user_jwt_write_instance.to_dict()
# create an instance of UserJwtWrite from a dict
user_jwt_write_form_dict = user_jwt_write.from_dict(user_jwt_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


