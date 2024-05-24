# OfferMetadataWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from tpdk.models.offer_metadata_write import OfferMetadataWrite

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMetadataWrite from a JSON string
offer_metadata_write_instance = OfferMetadataWrite.from_json(json)
# print the JSON string representation of the object
print(OfferMetadataWrite.to_json())

# convert the object into a dict
offer_metadata_write_dict = offer_metadata_write_instance.to_dict()
# create an instance of OfferMetadataWrite from a dict
offer_metadata_write_from_dict = OfferMetadataWrite.from_dict(offer_metadata_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


