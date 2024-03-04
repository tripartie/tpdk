# OfferRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**organization** | [**OfferReadOrganization**](OfferReadOrganization.md) |  | [optional] 
**seller** | [**PersonaRead**](PersonaRead.md) | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**medias** | [**List[MediaRead]**](MediaRead.md) |  | 

## Example

```python
from tpdk.models.offer_read import OfferRead

# TODO update the JSON string below
json = "{}"
# create an instance of OfferRead from a JSON string
offer_read_instance = OfferRead.from_json(json)
# print the JSON string representation of the object
print OfferRead.to_json()

# convert the object into a dict
offer_read_dict = offer_read_instance.to_dict()
# create an instance of OfferRead from a dict
offer_read_form_dict = offer_read.from_dict(offer_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


