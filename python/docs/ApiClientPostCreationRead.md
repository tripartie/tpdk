# ApiClientPostCreationRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from tpdk.models.api_client_post_creation_read import ApiClientPostCreationRead

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientPostCreationRead from a JSON string
api_client_post_creation_read_instance = ApiClientPostCreationRead.from_json(json)
# print the JSON string representation of the object
print ApiClientPostCreationRead.to_json()

# convert the object into a dict
api_client_post_creation_read_dict = api_client_post_creation_read_instance.to_dict()
# create an instance of ApiClientPostCreationRead from a dict
api_client_post_creation_read_form_dict = api_client_post_creation_read.from_dict(api_client_post_creation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


