# UserEmailValidationWrite



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | 
**plain_password** | **str** |  | [optional] 
**email_verification_input** | **str** |  | 

## Example

```python
from tpdk.models.user_email_validation_write import UserEmailValidationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserEmailValidationWrite from a JSON string
user_email_validation_write_instance = UserEmailValidationWrite.from_json(json)
# print the JSON string representation of the object
print UserEmailValidationWrite.to_json()

# convert the object into a dict
user_email_validation_write_dict = user_email_validation_write_instance.to_dict()
# create an instance of UserEmailValidationWrite from a dict
user_email_validation_write_form_dict = user_email_validation_write.from_dict(user_email_validation_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


