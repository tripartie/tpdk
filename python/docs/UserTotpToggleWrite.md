# UserTotpToggleWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp_enabled** | **bool** |  | 
**totp_challenge** | **str** |  | 

## Example

```python
from tpdk.models.user_totp_toggle_write import UserTotpToggleWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserTotpToggleWrite from a JSON string
user_totp_toggle_write_instance = UserTotpToggleWrite.from_json(json)
# print the JSON string representation of the object
print(UserTotpToggleWrite.to_json())

# convert the object into a dict
user_totp_toggle_write_dict = user_totp_toggle_write_instance.to_dict()
# create an instance of UserTotpToggleWrite from a dict
user_totp_toggle_write_from_dict = UserTotpToggleWrite.from_dict(user_totp_toggle_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


