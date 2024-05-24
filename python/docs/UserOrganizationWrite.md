# UserOrganizationWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**vat_number** | **str** |  | [optional] 
**commercial_registry_number** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**billing_address** | [**UserAddressWrite**](UserAddressWrite.md) |  | [optional] 

## Example

```python
from tpdk.models.user_organization_write import UserOrganizationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationWrite from a JSON string
user_organization_write_instance = UserOrganizationWrite.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationWrite.to_json())

# convert the object into a dict
user_organization_write_dict = user_organization_write_instance.to_dict()
# create an instance of UserOrganizationWrite from a dict
user_organization_write_from_dict = UserOrganizationWrite.from_dict(user_organization_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


