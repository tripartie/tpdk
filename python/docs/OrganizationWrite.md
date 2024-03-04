# OrganizationWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**vat_number** | **str** |  | 
**commercial_registry_number** | **str** |  | 
**website_url** | **str** |  | [optional] 
**billing_address** | [**OrganizationWriteBillingAddress**](OrganizationWriteBillingAddress.md) |  | [optional] 

## Example

```python
from tpdk.models.organization_write import OrganizationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWrite from a JSON string
organization_write_instance = OrganizationWrite.from_json(json)
# print the JSON string representation of the object
print OrganizationWrite.to_json()

# convert the object into a dict
organization_write_dict = organization_write_instance.to_dict()
# create an instance of OrganizationWrite from a dict
organization_write_form_dict = organization_write.from_dict(organization_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


