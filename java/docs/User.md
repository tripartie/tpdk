

# User



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**captcha** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**publicName** | **String** |  |  [optional] |
|**roleInCompany** | **String** |  |  [optional] |
|**birthday** | **OffsetDateTime** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**invitedRole** | [**List&lt;InvitedRoleEnum&gt;**](#List&lt;InvitedRoleEnum&gt;) |  |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) |  |  |
|**password** | **String** | The hashed password |  [optional] |
|**plainPassword** | **String** |  |  [optional] |
|**newPassword** | **String** |  |  [optional] |
|**totpSecret** | **String** |  |  [optional] |
|**totpUri** | **String** |  |  [optional] |
|**totpEnabled** | **Boolean** |  |  [optional] |
|**totpChallenge** | **String** |  |  [optional] |
|**intlPhoneNumber** | **String** |  |  [optional] |
|**originCountry** | **String** | The originating country |  [optional] |
|**preferredLanguage** | **String** |  |  [optional] |
|**lastSuccessfulLogIn** | **OffsetDateTime** |  |  [optional] |
|**emailVerificationCode** | **String** |  |  [optional] |
|**emailVerificationInput** | **String** |  |  [optional] |
|**phoneVerificationCode** | **String** |  |  [optional] |
|**phoneVerificationInput** | **String** |  |  [optional] |
|**avatar** | **String** |  |  [optional] |
|**notifications** | **List&lt;String&gt;** |  |  [optional] |
|**medias** | **List&lt;String&gt;** |  |  [optional] |
|**views** | [**List&lt;View&gt;**](View.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**consentMailNotification** | **Boolean** |  |  |
|**consentMailAds** | **Boolean** |  |  |
|**lockdown** | **Boolean** |  |  |
|**keys** | **List&lt;String&gt;** |  |  |
|**organization** | **String** |  |  [optional] |
|**impersonatedOrganization** | **String** |  |  [optional] |
|**iri** | **String** |  |  [optional] [readonly] |
|**username** | **String** | A visual identifier that represents this user. |  [optional] [readonly] |
|**salt** | **String** |  |  [optional] [readonly] |
|**userIdentifier** | **String** |  |  [optional] [readonly] |
|**impersonatingOrganization** | **Boolean** |  |  [optional] [readonly] |
|**_2fa** | **Boolean** |  |  [optional] [readonly] |



## Enum: List&lt;InvitedRoleEnum&gt;

| Name | Value |
|---- | -----|
| ADMIN | &quot;ROLE_ADMIN&quot; |
| CONSULTANT | &quot;ROLE_CONSULTANT&quot; |
| ACCOUNTING_MANAGER | &quot;ROLE_ACCOUNTING_MANAGER&quot; |
| BILLING_MANAGER | &quot;ROLE_BILLING_MANAGER&quot; |
| CUSTOMER_SERVICE | &quot;ROLE_CUSTOMER_SERVICE&quot; |
| CUSTOMER_SERVICE2 | &quot;ROLE_CUSTOMER_SERVICE&quot; |
| PLATFORM_ADMIN | &quot;ROLE_PLATFORM_ADMIN&quot; |
| PLATFORM_SUPPORT | &quot;ROLE_PLATFORM_SUPPORT&quot; |
| ORGANIZATION_OWNER | &quot;ROLE_ORGANIZATION_OWNER&quot; |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| ORGANIZATION_OWNER | &quot;ROLE_ORGANIZATION_OWNER&quot; |
| ADMIN | &quot;ROLE_ADMIN&quot; |
| CONSULTANT | &quot;ROLE_CONSULTANT&quot; |
| ACCOUNTING_MANAGER | &quot;ROLE_ACCOUNTING_MANAGER&quot; |
| BILLING_MANAGER | &quot;ROLE_BILLING_MANAGER&quot; |
| CUSTOMER_SERVICE | &quot;ROLE_CUSTOMER_SERVICE&quot; |
| PLATFORM_SUPPORT | &quot;ROLE_PLATFORM_SUPPORT&quot; |
| PLATFORM_ADMIN | &quot;ROLE_PLATFORM_ADMIN&quot; |
| USER | &quot;ROLE_USER&quot; |



