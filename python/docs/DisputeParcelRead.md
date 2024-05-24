# DisputeParcelRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** |  | 
**identifier** | **str** |  | 
**price** | **float** |  | [optional] 
**refundable** | **bool** |  | [optional] 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.dispute_parcel_read import DisputeParcelRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeParcelRead from a JSON string
dispute_parcel_read_instance = DisputeParcelRead.from_json(json)
# print the JSON string representation of the object
print(DisputeParcelRead.to_json())

# convert the object into a dict
dispute_parcel_read_dict = dispute_parcel_read_instance.to_dict()
# create an instance of DisputeParcelRead from a dict
dispute_parcel_read_from_dict = DisputeParcelRead.from_dict(dispute_parcel_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


