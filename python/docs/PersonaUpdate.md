# PersonaUpdate



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
**address** | [**PersonaAddressUpdate**](PersonaAddressUpdate.md) |  | [optional] 
**external_purchase_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**external_sell_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**metadata** | [**List[PersonaMetadataUpdate]**](PersonaMetadataUpdate.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | [optional] 

## Example

```python
from tpdk.models.persona_update import PersonaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PersonaUpdate from a JSON string
persona_update_instance = PersonaUpdate.from_json(json)
# print the JSON string representation of the object
print(PersonaUpdate.to_json())

# convert the object into a dict
persona_update_dict = persona_update_instance.to_dict()
# create an instance of PersonaUpdate from a dict
persona_update_from_dict = PersonaUpdate.from_dict(persona_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


