

# UserUserRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**publicName** | **String** |  |  [optional] |
|**roleInCompany** | **String** |  |  [optional] |
|**birthday** | **OffsetDateTime** |  |  [optional] |
|**email** | **String** |  |  |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) |  |  [optional] |
|**totpEnabled** | **Boolean** |  |  [optional] |
|**intlPhoneNumber** | **String** |  |  [optional] |
|**originCountry** | **String** | The originating country |  [optional] |
|**preferredLanguage** | **String** |  |  [optional] |
|**lastSuccessfulLogIn** | **OffsetDateTime** |  |  [optional] |
|**avatar** | [**MediaUserRead**](MediaUserRead.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**consentMailNotification** | **Boolean** |  |  [optional] |
|**consentMailAds** | **Boolean** |  |  [optional] |
|**lockdown** | **Boolean** |  |  [optional] |
|**organization** | [**OrganizationUserRead**](OrganizationUserRead.md) |  |  [optional] |
|**iri** | **String** |  |  [optional] [readonly] |
|**impersonatingOrganization** | **Boolean** |  |  [optional] [readonly] |
|**_2fa** | **Boolean** |  |  [optional] [readonly] |



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



