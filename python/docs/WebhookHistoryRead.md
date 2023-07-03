# WebhookHistoryRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**url** | **str** |  | 
**response_code** | **int** |  | 
**response_body** | **str** |  | 
**occurred_at** | **datetime** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**attempted_at** | **datetime** |  | [optional] [readonly] 
**retry_count** | **int** |  | 

## Example

```python
from tpdk.models.webhook_history_read import WebhookHistoryRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookHistoryRead from a JSON string
webhook_history_read_instance = WebhookHistoryRead.from_json(json)
# print the JSON string representation of the object
print WebhookHistoryRead.to_json()

# convert the object into a dict
webhook_history_read_dict = webhook_history_read_instance.to_dict()
# create an instance of WebhookHistoryRead from a dict
webhook_history_read_form_dict = webhook_history_read.from_dict(webhook_history_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


