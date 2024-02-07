

# PersonaRegister



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captcha** | **String** |  |  [optional] |
|**plainPassword** | **String** |  |  [optional] |
|**firstName** | **String** |  |  |
|**lastName** | **String** |  |  |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  |
|**dateOfBirth** | **LocalDate** |  |  [optional] |
|**language** | **String** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. |  [optional] |
|**email** | **String** |  |  [optional] |
|**mobilePhoneNumber** | **String** |  |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| OTHER | &quot;OTHER&quot; |
| RATHER_NOT_SAY | &quot;RATHER_NOT_SAY&quot; |



