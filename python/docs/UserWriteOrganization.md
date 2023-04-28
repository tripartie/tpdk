# UserWriteOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**commercial_registry_number** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**billing_address** | [**OrganizationWriteBillingAddress**](OrganizationWriteBillingAddress.md) |  | [optional] 

## Example

```python
from tpdk.models.user_write_organization import UserWriteOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of UserWriteOrganization from a JSON string
user_write_organization_instance = UserWriteOrganization.from_json(json)
# print the JSON string representation of the object
print UserWriteOrganization.to_json()

# convert the object into a dict
user_write_organization_dict = user_write_organization_instance.to_dict()
# create an instance of UserWriteOrganization from a dict
user_write_organization_form_dict = user_write_organization.from_dict(user_write_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


