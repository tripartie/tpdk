# WebhookObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **object** |  | 
**transaction** | [**TransactionRead**](TransactionRead.md) |  | [optional] 
**status** | **object** |  | 
**redirect_url** | **object** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**item_count** | **object** |  | [optional] 
**issue_type** | **object** |  | [optional] 
**issue_in_description_type** | **object** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional] 
**issue_mentioned_in_offer** | **object** |  | [optional] 
**issue_details** | **object** |  | [optional] 
**complainant_truthfulness_score** | **object** |  | 
**seller_truthfulness_score** | **object** |  | 
**complainant_stake** | **object** |  | [optional] 
**inferred_stake** | **object** |  | [optional] 
**recommended_solution** | **object** |  | [optional] 
**recommended_partial_refund_amount** | **object** |  | [optional] 
**chosen_solution** | **object** |  | [optional] 
**chosen_partial_refund_amount** | **object** |  | [optional] 
**counter_solution** | **object** |  | [optional] 
**counter_partial_refund_amount** | **object** |  | [optional] 
**seller_notes** | **object** |  | [optional] 
**seller_rejection_reason** | **object** |  | [optional] 
**complainant_approval** | **object** |  | [optional] 
**seller_approval** | **object** |  | [optional] 
**platform_solution** | **object** |  | [optional] 
**platform_partial_refund_amount** | **object** |  | [optional] 
**platform_approval** | **object** |  | [optional] 
**platform_actor_type** | **object** |  | [optional] 
**platform_reasoning** | **object** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. | [optional] 
**arbitration_by** | **object** |  | [optional] 
**parcels** | **object** |  | 
**metadata** | **object** |  | 
**events** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] [readonly] 
**updated_at** | **object** |  | [optional] [readonly] 
**status_expiration** | **object** | Yield if eligible the date-time at which the dispute state expire. | [optional] [readonly] 
**awaited_party** | **object** | Determine who is awaited (actor) for the next transition | [optional] [readonly] 
**iri** | **object** |  | [optional] [readonly] 
**message_count** | **object** |  | [optional] [readonly] 
**id** | **object** |  | [optional] [readonly] 
**first_name** | **object** |  | [optional] 
**last_name** | **object** |  | [optional] 
**gender** | **object** |  | [optional] 
**date_of_birth** | **object** |  | [optional] 
**language** | **object** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **object** |  | [optional] 
**mobile_phone_number** | **object** |  | [optional] 
**address** | [**AddressRead**](AddressRead.md) |  | [optional] 
**risk_level** | **object** | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. | [optional] 
**risk_score** | **object** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. | [optional] 
**external_purchase_count** | **object** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**external_sell_count** | **object** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**offer_count** | **object** | Issued Offers count owned by a given Persona | [optional] [readonly] 
**purchase_count** | **object** |  | [optional] [readonly] 
**public_url** | **object** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**organization** | [**OrganizationRead**](OrganizationRead.md) |  | [optional] 
**seller** | **object** | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **object** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | 
**title** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**unit_price** | **object** |  | [optional] 
**currency_code** | **object** |  | [optional] 
**condition** | **object** |  | [optional] 
**medias** | **object** |  | 

## Example

```python
from tpdk.models.webhook_object import WebhookObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookObject from a JSON string
webhook_object_instance = WebhookObject.from_json(json)
# print the JSON string representation of the object
print WebhookObject.to_json()

# convert the object into a dict
webhook_object_dict = webhook_object_instance.to_dict()
# create an instance of WebhookObject from a dict
webhook_object_form_dict = webhook_object.from_dict(webhook_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


