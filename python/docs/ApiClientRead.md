# ApiClientRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**created_at** | **datetime** |  | 
**scopes** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.api_client_read import ApiClientRead

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientRead from a JSON string
api_client_read_instance = ApiClientRead.from_json(json)
# print the JSON string representation of the object
print ApiClientRead.to_json()

# convert the object into a dict
api_client_read_dict = api_client_read_instance.to_dict()
# create an instance of ApiClientRead from a dict
api_client_read_form_dict = api_client_read.from_dict(api_client_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


