

# EvidenceRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** |  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**media** | [**MediaRead**](MediaRead.md) |  |  [optional] |
|**additionalInformation** | **String** | Description of what the evidence actually is. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**publisher** | [**PublisherEnum**](#PublisherEnum) | Shortcut to whomever sent the evidence |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;SUBMITTED&quot; |
| CORRELATED | &quot;CORRELATED&quot; |
| UNRELATED | &quot;UNRELATED&quot; |
| PENDING | &quot;PENDING&quot; |
| TEMPERED | &quot;TEMPERED&quot; |
| REJECTED | &quot;REJECTED&quot; |



## Enum: PublisherEnum

| Name | Value |
|---- | -----|
| BUYER | &quot;BUYER&quot; |
| PLATFORM | &quot;PLATFORM&quot; |
| SELLER | &quot;SELLER&quot; |



