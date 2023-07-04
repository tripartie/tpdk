# DisputeRead

Access directly our resolution center without having used the safe-checkout feature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**transaction** | [**TransactionRead**](TransactionRead.md) |  | [optional] 
**status** | **str** |  | [default to 'CREATED']
**redirect_url** | **str** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional] 
**item_count** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional] 
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

## Example

```python
from tpdk.models.dispute_read import DisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeRead from a JSON string
dispute_read_instance = DisputeRead.from_json(json)
# print the JSON string representation of the object
print DisputeRead.to_json()

# convert the object into a dict
dispute_read_dict = dispute_read_instance.to_dict()
# create an instance of DisputeRead from a dict
dispute_read_form_dict = dispute_read.from_dict(dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


