# UserCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**role_in_company** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**roles** | **List[str]** |  | 
**totp_enabled** | **bool** |  | [optional] 
**intl_phone_number** | **str** |  | [optional] 
**last_successful_log_in** | **datetime** |  | [optional] 
**avatar** | [**UserMediaCollectionRead**](UserMediaCollectionRead.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | [**UserOrganizationCollectionRead**](UserOrganizationCollectionRead.md) |  | [optional] 
**iri** | **str** |  | [optional] [readonly] 
**second_auth_factor** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.user_collection_read import UserCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionRead from a JSON string
user_collection_read_instance = UserCollectionRead.from_json(json)
# print the JSON string representation of the object
print(UserCollectionRead.to_json())

# convert the object into a dict
user_collection_read_dict = user_collection_read_instance.to_dict()
# create an instance of UserCollectionRead from a dict
user_collection_read_from_dict = UserCollectionRead.from_dict(user_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


