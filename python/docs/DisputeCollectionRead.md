# DisputeCollectionRead

Access directly our resolution center without having used the safe-checkout feature.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**transaction** | [**TransactionCollectionRead**](TransactionCollectionRead.md) |  | [optional] 
**status** | **str** |  | [default to 'CREATED']
**item_count** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional] 
**issue_type** | **str** |  | 
**issue_in_description_type** | **str** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional] 
**complainant_stake** | **str** |  | 
**inferred_stake** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 
**message_count** | **int** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute_collection_read import DisputeCollectionRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeCollectionRead from a JSON string
dispute_collection_read_instance = DisputeCollectionRead.from_json(json)
# print the JSON string representation of the object
print DisputeCollectionRead.to_json()

# convert the object into a dict
dispute_collection_read_dict = dispute_collection_read_instance.to_dict()
# create an instance of DisputeCollectionRead from a dict
dispute_collection_read_form_dict = dispute_collection_read.from_dict(dispute_collection_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


