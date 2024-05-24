# UserOrganizationCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.user_organization_collection_read import UserOrganizationCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationCollectionRead from a JSON string
user_organization_collection_read_instance = UserOrganizationCollectionRead.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationCollectionRead.to_json())

# convert the object into a dict
user_organization_collection_read_dict = user_organization_collection_read_instance.to_dict()
# create an instance of UserOrganizationCollectionRead from a dict
user_organization_collection_read_from_dict = UserOrganizationCollectionRead.from_dict(user_organization_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


