# OrganizationCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**commercial_registry_number** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**icon** | [**OrganizationMediaCollectionRead**](OrganizationMediaCollectionRead.md) |  | [optional] 
**logo** | [**OrganizationMediaCollectionRead**](OrganizationMediaCollectionRead.md) |  | [optional] 
**direct_notification_toggle** | **bool** |  | [default to True]
**internal_messaging_toggle** | **bool** |  | [default to True]
**persona_auth_portal_toggle** | **bool** |  | 
**automated_return_toggle** | **bool** |  | [default to True]
**counter_proposal_toggle** | **bool** |  | [default to True]
**flat_rate_enabled** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.organization_collection_read import OrganizationCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCollectionRead from a JSON string
organization_collection_read_instance = OrganizationCollectionRead.from_json(json)
# print the JSON string representation of the object
print(OrganizationCollectionRead.to_json())

# convert the object into a dict
organization_collection_read_dict = organization_collection_read_instance.to_dict()
# create an instance of OrganizationCollectionRead from a dict
organization_collection_read_from_dict = OrganizationCollectionRead.from_dict(organization_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


