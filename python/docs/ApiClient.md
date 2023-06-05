# ApiClient



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**owner** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**secret** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**redirect_uris** | **List[object]** |  | [optional] 
**grants** | **List[object]** |  | [optional] 
**scopes** | **List[object]** |  | [optional] 
**active** | **bool** |  | [optional] 
**allow_plain_text_pkce** | **bool** |  | [optional] 
**confidential** | **bool** |  | [optional] [readonly] 
**plain_text_pkce_allowed** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.api_client import ApiClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClient from a JSON string
api_client_instance = ApiClient.from_json(json)
# print the JSON string representation of the object
print ApiClient.to_json()

# convert the object into a dict
api_client_dict = api_client_instance.to_dict()
# create an instance of ApiClient from a dict
api_client_form_dict = api_client.from_dict(api_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


