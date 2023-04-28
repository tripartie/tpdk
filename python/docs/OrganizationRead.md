# OrganizationRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**domain_verified** | **bool** |  | 

## Example

```python
from tpdk.models.organization_read import OrganizationRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRead from a JSON string
organization_read_instance = OrganizationRead.from_json(json)
# print the JSON string representation of the object
print OrganizationRead.to_json()

# convert the object into a dict
organization_read_dict = organization_read_instance.to_dict()
# create an instance of OrganizationRead from a dict
organization_read_form_dict = organization_read.from_dict(organization_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

