

# OfferIndependentWrite

An Offer object represent a public listening

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publicUrl** | **URI** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. |  [optional] |
|**seller** | [**PersonaIndependentWrite**](PersonaIndependentWrite.md) | If the seller is actually YOUR organization, set it to NULL. |  |
|**nature** | [**NatureEnum**](#NatureEnum) | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. |  [optional] |
|**title** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**unitPrice** | **BigDecimal** |  |  [optional] |
|**currencyCode** | **String** |  |  [optional] |
|**itemCount** | **Integer** |  |  [optional] |
|**condition** | [**ConditionEnum**](#ConditionEnum) |  |  [optional] |
|**weightInGram** | **Integer** |  |  [optional] |
|**eanCode** | **String** |  |  [optional] |
|**metadata** | [**List&lt;MetadataIndependentWrite&gt;**](MetadataIndependentWrite.md) |  |  [optional] |



## Enum: NatureEnum

| Name | Value |
|---- | -----|
| SERVICE | &quot;service&quot; |
| PHYSICAL_ITEM | &quot;physical_item&quot; |
| DEMATERIALIZED_ITEM | &quot;dematerialized_item&quot; |
| RENT_ITEM | &quot;rent_item&quot; |



## Enum: ConditionEnum

| Name | Value |
|---- | -----|
| NEW | &quot;NEW&quot; |
| USED | &quot;USED&quot; |
| DAMAGED | &quot;DAMAGED&quot; |
| DETERIORATED | &quot;DETERIORATED&quot; |
| UNRECOVERABLE | &quot;UNRECOVERABLE&quot; |



