# ParcelDisputeRead



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
from tpdk.models.parcel_dispute_read import ParcelDisputeRead

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelDisputeRead from a JSON string
parcel_dispute_read_instance = ParcelDisputeRead.from_json(json)
# print the JSON string representation of the object
print(ParcelDisputeRead.to_json())

# convert the object into a dict
parcel_dispute_read_dict = parcel_dispute_read_instance.to_dict()
# create an instance of ParcelDisputeRead from a dict
parcel_dispute_read_from_dict = ParcelDisputeRead.from_dict(parcel_dispute_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


