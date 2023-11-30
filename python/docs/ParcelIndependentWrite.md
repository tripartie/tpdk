# ParcelIndependentWrite



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **str** |  | 
**identifier** | **str** |  | 
**price** | **float** |  | [optional] 
**refundable** | **bool** |  | [optional] 
**currency** | **str** |  | [optional] [default to 'EUR']

## Example

```python
from tpdk.models.parcel_independent_write import ParcelIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelIndependentWrite from a JSON string
parcel_independent_write_instance = ParcelIndependentWrite.from_json(json)
# print the JSON string representation of the object
print ParcelIndependentWrite.to_json()

# convert the object into a dict
parcel_independent_write_dict = parcel_independent_write_instance.to_dict()
# create an instance of ParcelIndependentWrite from a dict
parcel_independent_write_form_dict = parcel_independent_write.from_dict(parcel_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


