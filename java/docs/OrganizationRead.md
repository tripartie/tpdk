

# OrganizationRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**vatNumber** | **String** |  |  [optional] |
|**commercialRegistryNumber** | **String** |  |  [optional] |
|**websiteUrl** | **String** |  |  [optional] |
|**customBaseUrl** | **String** |  |  [optional] |
|**domainVerified** | **Boolean** |  |  |
|**icon** | [**OrganizationMediaRead**](OrganizationMediaRead.md) |  |  [optional] |
|**logo** | [**OrganizationMediaRead**](OrganizationMediaRead.md) |  |  [optional] |
|**primaryColor** | **String** |  |  [optional] |
|**secondaryColor** | **String** |  |  [optional] |
|**accentColor** | **String** |  |  [optional] |
|**errorColor** | **String** |  |  [optional] |
|**infoColor** | **String** |  |  [optional] |
|**successColor** | **String** |  |  [optional] |
|**warningColor** | **String** |  |  [optional] |
|**directNotificationToggle** | **Boolean** |  |  |
|**anonymityLevel** | [**AnonymityLevelEnum**](#AnonymityLevelEnum) |  |  |
|**safeCheckoutToggle** | **Boolean** |  |  |
|**resolutionCenterToggle** | **Boolean** |  |  |
|**internalMessagingToggle** | **Boolean** |  |  |
|**personaAuthPortalToggle** | **Boolean** |  |  |
|**automatedReturnToggle** | **Boolean** |  |  |
|**counterProposalToggle** | **Boolean** |  |  |
|**flatRateEnabled** | **Boolean** |  |  [optional] [readonly] |
|**rateCommissionSafeCheckout** | **BigDecimal** |  |  |



## Enum: AnonymityLevelEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;COMPLETE&quot; |
| PARTIAL_FIRST_NAME | &quot;PARTIAL_FIRST_NAME&quot; |
| TRANSPARENT | &quot;TRANSPARENT&quot; |



