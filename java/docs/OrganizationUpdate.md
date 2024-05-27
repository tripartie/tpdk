

# OrganizationUpdate



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**vatNumber** | **String** |  |  [optional] |
|**commercialRegistryNumber** | **String** |  |  [optional] |
|**websiteUrl** | **URI** |  |  [optional] |
|**customBaseUrl** | **URI** |  |  [optional] |
|**billingAddress** | [**OrganizationAddressUpdate**](OrganizationAddressUpdate.md) |  |  [optional] |
|**primaryColor** | **String** |  |  [optional] |
|**directNotificationToggle** | **Boolean** |  |  [optional] |
|**anonymityLevel** | [**AnonymityLevelEnum**](#AnonymityLevelEnum) |  |  [optional] |
|**internalMessagingToggle** | **Boolean** |  |  [optional] |
|**personaAuthPortalToggle** | **Boolean** |  |  [optional] |
|**automatedReturnToggle** | **Boolean** |  |  [optional] |
|**counterProposalToggle** | **Boolean** |  |  [optional] |
|**flatRateEnabled** | **Boolean** |  |  [optional] [readonly] |



## Enum: AnonymityLevelEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;COMPLETE&quot; |
| PARTIAL_FIRST_NAME | &quot;PARTIAL_FIRST_NAME&quot; |
| TRANSPARENT | &quot;TRANSPARENT&quot; |



