# NotificationRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**seen** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.notification_read import NotificationRead

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRead from a JSON string
notification_read_instance = NotificationRead.from_json(json)
# print the JSON string representation of the object
print NotificationRead.to_json()

# convert the object into a dict
notification_read_dict = notification_read_instance.to_dict()
# create an instance of NotificationRead from a dict
notification_read_form_dict = notification_read.from_dict(notification_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


