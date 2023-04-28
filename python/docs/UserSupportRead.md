# UserSupportRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**role_in_company** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**intl_phone_number** | **str** |  | [optional] 
**last_successful_log_in** | **datetime** |  | [optional] 
**avatar** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | [**UserSupportReadOrganization**](UserSupportReadOrganization.md) |  | [optional] 

## Example

```python
from tpdk.models.user_support_read import UserSupportRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserSupportRead from a JSON string
user_support_read_instance = UserSupportRead.from_json(json)
# print the JSON string representation of the object
print UserSupportRead.to_json()

# convert the object into a dict
user_support_read_dict = user_support_read_instance.to_dict()
# create an instance of UserSupportRead from a dict
user_support_read_form_dict = user_support_read.from_dict(user_support_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


