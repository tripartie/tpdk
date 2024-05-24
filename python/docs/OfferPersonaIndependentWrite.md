# OfferPersonaIndependentWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**gender** | **str** |  | [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**address** | [**OfferAddressIndependentWrite**](OfferAddressIndependentWrite.md) |  | [optional] 
**metadata** | [**List[OfferMetadataIndependentWrite]**](OfferMetadataIndependentWrite.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | [optional] 

## Example

```python
from tpdk.models.offer_persona_independent_write import OfferPersonaIndependentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPersonaIndependentWrite from a JSON string
offer_persona_independent_write_instance = OfferPersonaIndependentWrite.from_json(json)
# print the JSON string representation of the object
print(OfferPersonaIndependentWrite.to_json())

# convert the object into a dict
offer_persona_independent_write_dict = offer_persona_independent_write_instance.to_dict()
# create an instance of OfferPersonaIndependentWrite from a dict
offer_persona_independent_write_from_dict = OfferPersonaIndependentWrite.from_dict(offer_persona_independent_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


