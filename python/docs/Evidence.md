# Evidence



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**dispute** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**status** | **str** |  | [default to 'SUBMITTED']
**media** | **str** |  | [optional] 
**additional_information** | **str** | Description of what the evidence actually is. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**publisher** | **str** | Shortcut to whomever sent the evidence | [optional] [readonly] 

## Example

```python
from tpdk.models.evidence import Evidence

# TODO update the JSON string below
json = "{}"
# create an instance of Evidence from a JSON string
evidence_instance = Evidence.from_json(json)
# print the JSON string representation of the object
print Evidence.to_json()

# convert the object into a dict
evidence_dict = evidence_instance.to_dict()
# create an instance of Evidence from a dict
evidence_form_dict = evidence.from_dict(evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


