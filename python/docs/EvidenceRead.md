# EvidenceRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**status** | **str** |  | [default to 'SUBMITTED']
**media** | [**EvidenceReadMedia**](EvidenceReadMedia.md) |  | [optional] 
**additional_information** | **str** | Description of what the evidence actually is. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**publisher** | **str** | Shortcut to whomever sent the evidence | [optional] [readonly] 

## Example

```python
from tpdk.models.evidence_read import EvidenceRead

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceRead from a JSON string
evidence_read_instance = EvidenceRead.from_json(json)
# print the JSON string representation of the object
print EvidenceRead.to_json()

# convert the object into a dict
evidence_read_dict = evidence_read_instance.to_dict()
# create an instance of EvidenceRead from a dict
evidence_read_form_dict = evidence_read.from_dict(evidence_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


