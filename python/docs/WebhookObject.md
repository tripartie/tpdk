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
**complainant_approval** | **bool** |  | [optional] 
**seller_approval** | **bool** |  | [optional] 
**platform_solution** | **str** |  | [optional] 
**platform_partial_refund_amount** | **int** |  | [optional] 
**platform_approval** | **bool** |  | [optional] 
**arbitration_by** | **str** |  | [optional] 
**parcels** | [**List[ParcelRead]**](ParcelRead.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 
**message_count** | **int** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**address** | [**PersonaReadAddress**](PersonaReadAddress.md) |  | [optional] 
**risk_level** | **str** | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. | [optional] 
**risk_score** | **int** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. | [optional] 
**external_purchase_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**external_sell_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**metadata** | [**List[MetadataRead]**](MetadataRead.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | [optional] 
**offer_count** | **int** | Issued Offers count owned by a given Persona | [optional] [readonly] 
**purchase_count** | **int** |  | [optional] [readonly] 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**organization** | [**OfferReadOrganization**](OfferReadOrganization.md) |  | [optional] 
**seller** | **str** | If the seller is actually YOUR organization, set it to NULL. | 
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
print WebhookObject.to_json()

# convert the object into a dict
webhook_object_dict = webhook_object_instance.to_dict()
# create an instance of WebhookObject from a dict
webhook_object_form_dict = webhook_object.from_dict(webhook_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


