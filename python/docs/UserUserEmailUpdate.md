# UserUserEmailUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**plain_password** | **str** |  | 

## Example

```python
from tpdk.models.user_user_email_update import UserUserEmailUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserEmailUpdate from a JSON string
user_user_email_update_instance = UserUserEmailUpdate.from_json(json)
# print the JSON string representation of the object
print(UserUserEmailUpdate.to_json())

# convert the object into a dict
user_user_email_update_dict = user_user_email_update_instance.to_dict()
# create an instance of UserUserEmailUpdate from a dict
user_user_email_update_from_dict = UserUserEmailUpdate.from_dict(user_user_email_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


