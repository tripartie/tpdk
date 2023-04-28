# UserSupportReadOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.user_support_read_organization import UserSupportReadOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of UserSupportReadOrganization from a JSON string
user_support_read_organization_instance = UserSupportReadOrganization.from_json(json)
# print the JSON string representation of the object
print UserSupportReadOrganization.to_json()

# convert the object into a dict
user_support_read_organization_dict = user_support_read_organization_instance.to_dict()
# create an instance of UserSupportReadOrganization from a dict
user_support_read_organization_form_dict = user_support_read_organization.from_dict(user_support_read_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


