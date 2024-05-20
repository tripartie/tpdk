# MessageError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from tpdk.models.message_error import MessageError

# TODO update the JSON string below
json = "{}"
# create an instance of MessageError from a JSON string
message_error_instance = MessageError.from_json(json)
# print the JSON string representation of the object
print(MessageError.to_json())

# convert the object into a dict
message_error_dict = message_error_instance.to_dict()
# create an instance of MessageError from a dict
message_error_from_dict = MessageError.from_dict(message_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


