# User



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**captcha** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**role_in_company** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**invited_role** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | 
**password** | **str** | The hashed password | [optional] 
**plain_password** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 
**totp_secret** | **str** |  | [optional] 
**totp_uri** | **str** |  | [optional] 
**totp_enabled** | **bool** |  | [optional] 
**totp_challenge** | **str** |  | [optional] 
**intl_phone_number** | **str** |  | [optional] 
**origin_country** | **str** | The originating country | [optional] 
**preferred_language** | **str** |  | [optional] 
**last_successful_log_in** | **datetime** |  | [optional] 
**email_verification_code** | **str** |  | [optional] 
**email_verification_input** | **str** |  | [optional] 
**phone_verification_code** | **str** |  | [optional] 
**phone_verification_input** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**notifications** | **List[str]** |  | [optional] 
**medias** | **List[str]** |  | [optional] 
**views** | [**List[View]**](View.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**consent_mail_notification** | **bool** |  | 
**consent_mail_ads** | **bool** |  | 
**keys** | **List[str]** |  | 
**organization** | **str** |  | [optional] 
**impersonated_organization** | **str** |  | [optional] 
**username** | **str** | A visual identifier that represents this user. | [optional] [readonly] 
**salt** | **str** |  | [optional] [readonly] 
**user_identifier** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


