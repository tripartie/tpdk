# DisputeUpdate

Access directly our resolution center without having used the safe-checkout feature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_count** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional] 
**issue_type** | **str** |  | [optional] 
**issue_in_description_type** | **str** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional] 
**issue_mentioned_in_offer** | **bool** |  | [optional] 
**issue_details** | **str** |  | [optional] 
**complainant_stake** | **str** |  | [optional] 
**chosen_solution** | **str** |  | [optional] 
**chosen_partial_refund_amount** | **int** |  | [optional] 
**counter_solution** | **str** |  | [optional] 
**counter_partial_refund_amount** | **int** |  | [optional] 
**seller_notes** | **str** |  | [optional] 
**seller_rejection_reason** | **str** |  | [optional] 
**complainant_approval** | **bool** |  | [optional] 
**seller_approval** | **bool** |  | [optional] 
**platform_reasoning** | **str** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. | [optional] 

## Example

```python
from tpdk.models.dispute_update import DisputeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeUpdate from a JSON string
dispute_update_instance = DisputeUpdate.from_json(json)
# print the JSON string representation of the object
print DisputeUpdate.to_json()

# convert the object into a dict
dispute_update_dict = dispute_update_instance.to_dict()
# create an instance of DisputeUpdate from a dict
dispute_update_form_dict = dispute_update.from_dict(dispute_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


