# WebhookObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**transaction** | [**TransactionRead**](TransactionRead.md) |  | [optional] 
**status** | **str** |  | [default to 'CREATED']
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**item_count** | **int** |  | [optional] [default to 1]
**issue_type** | **str** |  | [optional] 
**issue_in_description_type** | **str** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional] 
**issue_mentioned_in_offer** | **bool** |  | [optional] 
**issue_details** | **str** |  | [optional] 
**complainant_truthfulness_score** | **int** |  | [default to 100]
**seller_truthfulness_score** | **int** |  | [default to 100]
**complainant_stake** | **str** |  | [optional] 
**inferred_stake** | **str** |  | [optional] 
**recommended_solution** | **str** |  | [optional] 
**recommended_partial_refund_amount** | **int** |  | [optional] 
**chosen_solution** | **str** |  | [optional] 
**chosen_partial_refund_amount** | **int** |  | [optional] 
**counter_solution** | **str** |  | [optional] 
**counter_partial_refund_amount** | **int** |  | [optional] 
**seller_notes** | **str** |  | [optional] 
**seller_rejection_reason** | **str** |  | [optional] 
**complainant_approval** | **bool** |  | [optional] 
**seller_approval** | **bool** |  | [optional] 
**platform_solution** | **str** |  | [optional] 
**platform_partial_refund_amount** | **int** |  | [optional] 
**platform_approval** | **bool** |  | [optional] 
**platform_actor_type** | **str** |  | [optional] 
**platform_reasoning** | **str** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. | [optional] 
**arbitration_by** | **str** |  | [optional] 
**parcels** | [**List[ParcelRead]**](ParcelRead.md) |  | 
**views** | [**List[ViewRead]**](ViewRead.md) |  | 
**metadata** | [**List[MetadataRead]**](MetadataRead.md) |  | 
**events** | [**List[WorkflowEventRead]**](WorkflowEventRead.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**view_count** | **int** |  | [optional] [readonly] 
**status_expiration** | **datetime** | Yield if eligible the date-time at which the dispute state expire. | [optional] [readonly] 
**awaited_party** | **str** | Determine who is awaited (actor) for the next transition | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 
**message_count** | **int** |  | [optional] [readonly] 
**closed_in_favor_of** | **str** | Determine who won the case, if not specified, then it is ongoing. | [optional] [readonly] 
**disbursed_by_buyer** | **float** | Total amount disbursed by the buyer to acquire the item. | [optional] [readonly] 
**max_refundable_for_buyer** | **float** | How much the buyer can actually receive back in case of a full refund. | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**organization** | [**OrganizationRead**](OrganizationRead.md) |  | [optional] 
**seller** | [**PersonaRead**](PersonaRead.md) | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**condition** | **str** |  | [optional] [default to 'USED']
**medias** | [**List[MediaRead]**](MediaRead.md) |  | 

## Example

```python
from tpdk.models.webhook_object import WebhookObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookObject from a JSON string
webhook_object_instance = WebhookObject.from_json(json)
# print the JSON string representation of the object
print(WebhookObject.to_json())

# convert the object into a dict
webhook_object_dict = webhook_object_instance.to_dict()
# create an instance of WebhookObject from a dict
webhook_object_from_dict = WebhookObject.from_dict(webhook_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


