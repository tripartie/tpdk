# UserTotpSetupRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp_uri** | **str** |  | [optional] 

## Example

```python
from tpdk.models.user_totp_setup_read import UserTotpSetupRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserTotpSetupRead from a JSON string
user_totp_setup_read_instance = UserTotpSetupRead.from_json(json)
# print the JSON string representation of the object
print(UserTotpSetupRead.to_json())

# convert the object into a dict
user_totp_setup_read_dict = user_totp_setup_read_instance.to_dict()
# create an instance of UserTotpSetupRead from a dict
user_totp_setup_read_from_dict = UserTotpSetupRead.from_dict(user_totp_setup_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


