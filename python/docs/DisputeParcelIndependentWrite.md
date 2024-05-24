# DisputeParcelIndependentWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**refundable** | **bool** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from tpdk.models.dispute_parcel_independent_write import DisputeParcelIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeParcelIndependentWrite from a JSON string
dispute_parcel_independent_write_instance = DisputeParcelIndependentWrite.from_json(json)
# print the JSON string representation of the object
print(DisputeParcelIndependentWrite.to_json())

# convert the object into a dict
dispute_parcel_independent_write_dict = dispute_parcel_independent_write_instance.to_dict()
# create an instance of DisputeParcelIndependentWrite from a dict
dispute_parcel_independent_write_from_dict = DisputeParcelIndependentWrite.from_dict(dispute_parcel_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


