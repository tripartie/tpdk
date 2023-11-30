# View



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**ip_address** | **str** |  | 
**offer** | **str** |  | [optional] 
**dispute** | **str** |  | [optional] 
**persona** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**hit_count** | **int** |  | [default to 1]
**created_at** | **datetime** |  | [optional] [readonly] 
**named_source** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print View.to_json()

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_form_dict = view.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


