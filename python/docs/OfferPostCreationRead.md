# OfferPostCreationRead

An Offer object represent a public listening

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.offer_post_creation_read import OfferPostCreationRead

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPostCreationRead from a JSON string
offer_post_creation_read_instance = OfferPostCreationRead.from_json(json)
# print the JSON string representation of the object
print OfferPostCreationRead.to_json()

# convert the object into a dict
offer_post_creation_read_dict = offer_post_creation_read_instance.to_dict()
# create an instance of OfferPostCreationRead from a dict
offer_post_creation_read_form_dict = offer_post_creation_read.from_dict(offer_post_creation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


