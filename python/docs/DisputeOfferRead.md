# DisputeOfferRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **str** |  | 
**public_url** | **str** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional] 
**organization** | [**DisputeOrganizationRead**](DisputeOrganizationRead.md) |  | [optional] 
**seller** | [**DisputePersonaRead**](DisputePersonaRead.md) | If the seller is actually YOUR organization, set it to NULL. | 
**nature** | **str** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'EUR']
**item_count** | **int** |  | [optional] [default to 1]
**condition** | **str** |  | [optional] [default to 'USED']
**medias** | [**List[DisputeMediaRead]**](DisputeMediaRead.md) |  | 

## Example

```python
from tpdk.models.dispute_offer_read import DisputeOfferRead

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeOfferRead from a JSON string
dispute_offer_read_instance = DisputeOfferRead.from_json(json)
# print the JSON string representation of the object
print(DisputeOfferRead.to_json())

# convert the object into a dict
dispute_offer_read_dict = dispute_offer_read_instance.to_dict()
# create an instance of DisputeOfferRead from a dict
dispute_offer_read_from_dict = DisputeOfferRead.from_dict(dispute_offer_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


