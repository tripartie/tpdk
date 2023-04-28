# OfferIndependentWriteSeller

If the seller is actually YOUR organization, set it to NULL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**address** | [**PersonaIndependentWriteAddress**](PersonaIndependentWriteAddress.md) |  | [optional] 
**external_purchase_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**external_sell_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**metadata** | [**List[MetadataIndependentWrite]**](MetadataIndependentWrite.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | 

## Example

```python
from tpdk.models.offer_independent_write_seller import OfferIndependentWriteSeller

# TODO update the JSON string below
json = "{}"
# create an instance of OfferIndependentWriteSeller from a JSON string
offer_independent_write_seller_instance = OfferIndependentWriteSeller.from_json(json)
# print the JSON string representation of the object
print OfferIndependentWriteSeller.to_json()

# convert the object into a dict
offer_independent_write_seller_dict = offer_independent_write_seller_instance.to_dict()
# create an instance of OfferIndependentWriteSeller from a dict
offer_independent_write_seller_form_dict = offer_independent_write_seller.from_dict(offer_independent_write_seller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


