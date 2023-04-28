# OrganizationSupportRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.organization_support_read import OrganizationSupportRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSupportRead from a JSON string
organization_support_read_instance = OrganizationSupportRead.from_json(json)
# print the JSON string representation of the object
print OrganizationSupportRead.to_json()

# convert the object into a dict
organization_support_read_dict = organization_support_read_instance.to_dict()
# create an instance of OrganizationSupportRead from a dict
organization_support_read_form_dict = organization_support_read.from_dict(organization_support_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


