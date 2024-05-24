

# TransactionCollectionRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ulid** | **String** |  |  |
|**offer** | [**TransactionOfferCollectionRead**](TransactionOfferCollectionRead.md) |  |  |
|**buyer** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**fees** | **BigDecimal** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;CREATED&quot; |
| AUTHORIZED | &quot;AUTHORIZED&quot; |
| REFUSED | &quot;REFUSED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| SHIPPED | &quot;SHIPPED&quot; |
| IN_TRANSIT | &quot;IN_TRANSIT&quot; |
| DELIVERED | &quot;DELIVERED&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| DISPUTED | &quot;DISPUTED&quot; |
| NULL | &quot;null&quot; |



