# Parcel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**carrier** | **str** |  | 
**identifier** | **str** |  | 
**price** | **float** |  | [optional] 
**refundable** | **bool** |  | [optional] 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] 
**dispute** | **str** |  | [optional] 
**transaction** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.parcel import Parcel

# TODO update the JSON string below
json = "{}"
# create an instance of Parcel from a JSON string
parcel_instance = Parcel.from_json(json)
# print the JSON string representation of the object
print Parcel.to_json()

# convert the object into a dict
parcel_dict = parcel_instance.to_dict()
# create an instance of Parcel from a dict
parcel_form_dict = parcel.from_dict(parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


