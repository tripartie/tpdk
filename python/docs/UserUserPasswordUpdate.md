# UserUserPasswordUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plain_password** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from tpdk.models.user_user_password_update import UserUserPasswordUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserPasswordUpdate from a JSON string
user_user_password_update_instance = UserUserPasswordUpdate.from_json(json)
# print the JSON string representation of the object
print UserUserPasswordUpdate.to_json()

# convert the object into a dict
user_user_password_update_dict = user_user_password_update_instance.to_dict()
# create an instance of UserUserPasswordUpdate from a dict
user_user_password_update_form_dict = user_user_password_update.from_dict(user_user_password_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


