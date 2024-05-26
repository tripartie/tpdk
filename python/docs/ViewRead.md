# ViewRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_count** | **int** |  | [default to 1]
**created_at** | **datetime** |  | [optional] [readonly] 
**named_source** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.view_read import ViewRead

# TODO update the JSON string below
json = "{}"
# create an instance of ViewRead from a JSON string
view_read_instance = ViewRead.from_json(json)
# print the JSON string representation of the object
print(ViewRead.to_json())

# convert the object into a dict
view_read_dict = view_read_instance.to_dict()
# create an instance of ViewRead from a dict
view_read_from_dict = ViewRead.from_dict(view_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


