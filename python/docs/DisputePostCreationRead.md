# DisputePostCreationRead

Access directly our resolution center without having used the safe-checkout feature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from tpdk.models.dispute_post_creation_read import DisputePostCreationRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputePostCreationRead from a JSON string
dispute_post_creation_read_instance = DisputePostCreationRead.from_json(json)
# print the JSON string representation of the object
print DisputePostCreationRead.to_json()

# convert the object into a dict
dispute_post_creation_read_dict = dispute_post_creation_read_instance.to_dict()
# create an instance of DisputePostCreationRead from a dict
dispute_post_creation_read_form_dict = dispute_post_creation_read.from_dict(dispute_post_creation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


