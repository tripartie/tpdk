# UserAuthenticatedRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**role_in_company** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**roles** | **List[str]** |  | 
**totp_enabled** | **bool** |  | [optional] 
**intl_phone_number** | **str** |  | [optional] 
**origin_country** | **str** | The originating country | [optional] 
**preferred_language** | **str** |  | [optional] 
**last_successful_log_in** | **datetime** |  | [optional] 
**avatar** | [**OrganizationAuthenticatedReadIcon**](OrganizationAuthenticatedReadIcon.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**consent_mail_notification** | **bool** |  | 
**consent_mail_ads** | **bool** |  | 
**lockdown** | **bool** |  | 
**organization** | [**UserAuthenticatedReadOrganization**](UserAuthenticatedReadOrganization.md) |  | [optional] 
**iri** | **str** |  | [optional] [readonly] 
**impersonating_organization** | **bool** |  | [optional] [readonly] 
**var_2fa** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.user_authenticated_read import UserAuthenticatedRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuthenticatedRead from a JSON string
user_authenticated_read_instance = UserAuthenticatedRead.from_json(json)
# print the JSON string representation of the object
print UserAuthenticatedRead.to_json()

# convert the object into a dict
user_authenticated_read_dict = user_authenticated_read_instance.to_dict()
# create an instance of UserAuthenticatedRead from a dict
user_authenticated_read_form_dict = user_authenticated_read.from_dict(user_authenticated_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


