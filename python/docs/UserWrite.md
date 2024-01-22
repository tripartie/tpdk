# UserWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**public_name** | **str** |  | 
**role_in_company** | **str** |  | 
**birthday** | **datetime** |  | [optional] 
**email** | **str** |  | 
**plain_password** | **str** |  | 
**intl_phone_number** | **str** |  | [optional] 
**origin_country** | **str** | The originating country | 
**preferred_language** | **str** |  | 
**consent_mail_notification** | **bool** |  | [optional] 
**consent_mail_ads** | **bool** |  | [optional] 
**organization** | [**OrganizationWrite**](OrganizationWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.user_write import UserWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserWrite from a JSON string
user_write_instance = UserWrite.from_json(json)
# print the JSON string representation of the object
print UserWrite.to_json()

# convert the object into a dict
user_write_dict = user_write_instance.to_dict()
# create an instance of UserWrite from a dict
user_write_form_dict = user_write.from_dict(user_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


