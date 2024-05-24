

# PersonaUpdate



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** |  |  |
|**lastName** | **String** |  |  |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  |
|**dateOfBirth** | **LocalDate** |  |  [optional] |
|**language** | **String** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. |  [optional] |
|**email** | **String** |  |  [optional] |
|**mobilePhoneNumber** | **String** |  |  [optional] |
|**address** | [**PersonaAddressUpdate**](PersonaAddressUpdate.md) |  |  [optional] |
|**externalPurchaseCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**externalSellCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**metadata** | [**List&lt;PersonaMetadataUpdate&gt;**](PersonaMetadataUpdate.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| OTHER | &quot;OTHER&quot; |
| RATHER_NOT_SAY | &quot;RATHER_NOT_SAY&quot; |



