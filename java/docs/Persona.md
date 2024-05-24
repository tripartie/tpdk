

# Persona



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**captcha** | **String** |  |  [optional] |
|**organization** | **String** |  |  [optional] |
|**targetUrl** | **String** | The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona. |  [optional] |
|**authUrl** | **URI** | Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them. |  [optional] |
|**expireAt** | **OffsetDateTime** | This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour. |  [optional] |
|**password** | **String** | The hashed password |  [optional] |
|**plainPassword** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**dateOfBirth** | **LocalDate** |  |  [optional] |
|**language** | **String** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. |  [optional] |
|**email** | **String** |  |  [optional] |
|**mobilePhoneNumber** | **String** |  |  [optional] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**riskLevel** | [**RiskLevelEnum**](#RiskLevelEnum) | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. |  [optional] |
|**riskScore** | **Integer** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. |  [optional] |
|**externalPurchaseCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**externalSellCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**metadata** | [**List&lt;Metadata&gt;**](Metadata.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. |  [optional] |
|**offers** | **List&lt;String&gt;** |  |  |
|**purchases** | **List&lt;String&gt;** |  |  |
|**views** | [**List&lt;View&gt;**](View.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**offerCount** | **Integer** | Issued Offers count owned by a given Persona |  [optional] [readonly] |
|**purchaseCount** | **Integer** |  |  [optional] [readonly] |
|**roles** | **List&lt;String&gt;** |  |  [optional] |
|**userIdentifier** | **String** | Either email or the mobile phone number |  [optional] [readonly] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| OTHER | &quot;OTHER&quot; |
| RATHER_NOT_SAY | &quot;RATHER_NOT_SAY&quot; |



## Enum: RiskLevelEnum

| Name | Value |
|---- | -----|
| WEAK | &quot;WEAK&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| NULL | &quot;null&quot; |



