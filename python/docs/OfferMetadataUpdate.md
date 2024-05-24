# OfferMetadataUpdate



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.offer_metadata_update import OfferMetadataUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMetadataUpdate from a JSON string
offer_metadata_update_instance = OfferMetadataUpdate.from_json(json)
# print the JSON string representation of the object
print(OfferMetadataUpdate.to_json())

# convert the object into a dict
offer_metadata_update_dict = offer_metadata_update_instance.to_dict()
# create an instance of OfferMetadataUpdate from a dict
offer_metadata_update_from_dict = OfferMetadataUpdate.from_dict(offer_metadata_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


