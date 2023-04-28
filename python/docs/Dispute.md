# Dispute

Access directly our resolution center without having used the safe-checkout feature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**ulid** | **str** |  | 
**url** | **str** |  | [optional] 
**transaction** | **str** |  | [optional] 
**status** | **str** |  | [default to 'CREATED']
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**item_count** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional] 
**issue_type** | **str** |  | 
**issue_in_description_type** | **str** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional] 
**issue_details** | **str** |  | [optional] 
**complainant_truthfulness_score** | **int** |  | [default to 100]
**seller_truthfulness_score** | **int** |  | [default to 100]
**complainant_stake** | **str** |  | 
**inferred_stake** | **str** |  | [optional] 
**recommended_solution** | **str** |  | [optional] 
**recommended_partial_refund_amount** | **int** |  | [optional] 
**chosen_solution** | **str** |  | [optional] 
**chosen_partial_refund_amount** | **int** |  | [optional] 
**counter_solution** | **str** |  | [optional] 
**counter_partial_refund_amount** | **int** |  | [optional] 
**complainant_approval** | **bool** |  | [optional] 
**seller_approval** | **bool** |  | 
**platform_solution** | **str** |  | [optional] 
**platform_partial_refund_amount** | **int** |  | [optional] 
**platform_approval** | **bool** |  | [optional] 
**arbitration_by** | **str** |  | [optional] 
**parcels** | **List[str]** |  | 
**messages** | [**List[Message]**](Message.md) |  | 
**views** | [**List[View]**](View.md) |  | 
**metadata** | [**List[Metadata]**](Metadata.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 
**message_count** | **int** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute import Dispute

# TODO update the JSON string below
json = "{}"
# create an instance of Dispute from a JSON string
dispute_instance = Dispute.from_json(json)
# print the JSON string representation of the object
print Dispute.to_json()

# convert the object into a dict
dispute_dict = dispute_instance.to_dict()
# create an instance of Dispute from a dict
dispute_form_dict = dispute.from_dict(dispute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


