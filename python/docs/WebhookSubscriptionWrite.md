# WebhookSubscriptionWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**callback_url** | **str** |  | 

## Example

```python
from tpdk.models.webhook_subscription_write import WebhookSubscriptionWrite

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionWrite from a JSON string
webhook_subscription_write_instance = WebhookSubscriptionWrite.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionWrite.to_json())

# convert the object into a dict
webhook_subscription_write_dict = webhook_subscription_write_instance.to_dict()
# create an instance of WebhookSubscriptionWrite from a dict
webhook_subscription_write_from_dict = WebhookSubscriptionWrite.from_dict(webhook_subscription_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


