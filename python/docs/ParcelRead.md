# ParcelRead



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
from tpdk.models.parcel_read import ParcelRead

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelRead from a JSON string
parcel_read_instance = ParcelRead.from_json(json)
# print the JSON string representation of the object
print(ParcelRead.to_json())

# convert the object into a dict
parcel_read_dict = parcel_read_instance.to_dict()
# create an instance of ParcelRead from a dict
parcel_read_from_dict = ParcelRead.from_dict(parcel_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


