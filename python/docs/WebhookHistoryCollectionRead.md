# WebhookHistoryCollectionRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**object_id** | **str** |  | [optional] 
**event** | **str** |  | 
**response_code** | **int** |  | [optional] 
**occurred_at** | **datetime** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**attempted_at** | **datetime** |  | [optional] [readonly] 
**retry_count** | **int** |  | 
**in_progress** | **bool** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.webhook_history_collection_read import WebhookHistoryCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookHistoryCollectionRead from a JSON string
webhook_history_collection_read_instance = WebhookHistoryCollectionRead.from_json(json)
# print the JSON string representation of the object
print(WebhookHistoryCollectionRead.to_json())

# convert the object into a dict
webhook_history_collection_read_dict = webhook_history_collection_read_instance.to_dict()
# create an instance of WebhookHistoryCollectionRead from a dict
webhook_history_collection_read_from_dict = WebhookHistoryCollectionRead.from_dict(webhook_history_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


