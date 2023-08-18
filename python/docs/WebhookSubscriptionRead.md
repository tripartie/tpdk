# WebhookSubscriptionRead



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**webhook_secret** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.webhook_subscription_read import WebhookSubscriptionRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionRead from a JSON string
webhook_subscription_read_instance = WebhookSubscriptionRead.from_json(json)
# print the JSON string representation of the object
print WebhookSubscriptionRead.to_json()

# convert the object into a dict
webhook_subscription_read_dict = webhook_subscription_read_instance.to_dict()
# create an instance of WebhookSubscriptionRead from a dict
webhook_subscription_read_form_dict = webhook_subscription_read.from_dict(webhook_subscription_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


