# Persona



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**captcha** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**target_url** | **str** | The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona. | [optional] 
**auth_url** | **str** | Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them. | [optional] 
**expire_at** | **datetime** | This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour. | [optional] 
**password** | **str** | The hashed password | [optional] 
**plain_password** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] [default to 'RATHER_NOT_SAY']
**date_of_birth** | **date** |  | [optional] 
**language** | **str** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional] 
**email** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**address** | [**PersonaAddress**](PersonaAddress.md) |  | [optional] 
**risk_level** | **str** | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. | [optional] 
**risk_score** | **int** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. | [optional] 
**external_purchase_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**external_sell_count** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. | [optional] 
**offers** | **List[str]** |  | 
**purchases** | **object** |  | 
**views** | [**List[View]**](View.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**offer_count** | **int** | Issued Offers count owned by a given Persona | [optional] [readonly] 
**purchase_count** | **int** |  | [optional] [readonly] 
**roles** | **List[str]** |  | [optional] 
**user_identifier** | **str** | Either email or the mobile phone number | [optional] [readonly] 

## Example

```python
from tpdk.models.persona import Persona

# TODO update the JSON string below
json = "{}"
# create an instance of Persona from a JSON string
persona_instance = Persona.from_json(json)
# print the JSON string representation of the object
print Persona.to_json()

# convert the object into a dict
persona_dict = persona_instance.to_dict()
# create an instance of Persona from a dict
persona_form_dict = persona.from_dict(persona_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


