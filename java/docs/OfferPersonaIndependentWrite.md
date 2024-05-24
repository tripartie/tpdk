

# OfferPersonaIndependentWrite



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
|**address** | [**OfferAddressIndependentWrite**](OfferAddressIndependentWrite.md) |  |  [optional] |
|**metadata** | [**List&lt;OfferMetadataIndependentWrite&gt;**](OfferMetadataIndependentWrite.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| OTHER | &quot;OTHER&quot; |
| RATHER_NOT_SAY | &quot;RATHER_NOT_SAY&quot; |



