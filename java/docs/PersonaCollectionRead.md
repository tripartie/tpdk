

# PersonaCollectionRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**riskLevel** | [**RiskLevelEnum**](#RiskLevelEnum) | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**offerCount** | **Integer** | Issued Offers count owned by a given Persona |  [optional] [readonly] |
|**purchaseCount** | **Integer** |  |  [optional] [readonly] |



## Enum: RiskLevelEnum

| Name | Value |
|---- | -----|
| WEAK | &quot;WEAK&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| NULL | &quot;null&quot; |



