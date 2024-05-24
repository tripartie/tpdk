# ApiClientWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_name** | **str** |  | [optional] 
**desired_scopes** | **List[str]** |  | [optional] 

## Example

```python
from tpdk.models.api_client_write import ApiClientWrite

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientWrite from a JSON string
api_client_write_instance = ApiClientWrite.from_json(json)
# print the JSON string representation of the object
print(ApiClientWrite.to_json())

# convert the object into a dict
api_client_write_dict = api_client_write_instance.to_dict()
# create an instance of ApiClientWrite from a dict
api_client_write_from_dict = ApiClientWrite.from_dict(api_client_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


