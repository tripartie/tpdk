

# DisputeCollectionRead

Access directly our resolution center without having used the safe-checkout feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ulid** | **String** |  |  |
|**transaction** | [**DisputeTransactionCollectionRead**](DisputeTransactionCollectionRead.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**itemCount** | **Integer** | The dispute may concern only PART of the package. Specify it there. |  [optional] |
|**issueType** | [**IssueTypeEnum**](#IssueTypeEnum) |  |  [optional] |
|**issueInDescriptionType** | [**IssueInDescriptionTypeEnum**](#IssueInDescriptionTypeEnum) | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. |  [optional] |
|**issueMentionedInOffer** | **Boolean** |  |  [optional] |
|**complainantStake** | [**ComplainantStakeEnum**](#ComplainantStakeEnum) |  |  [optional] |
|**inferredStake** | [**InferredStakeEnum**](#InferredStakeEnum) |  |  [optional] |
|**chosenSolution** | [**ChosenSolutionEnum**](#ChosenSolutionEnum) |  |  [optional] |
|**chosenPartialRefundAmount** | **Integer** |  |  [optional] |
|**platformSolution** | [**PlatformSolutionEnum**](#PlatformSolutionEnum) |  |  [optional] |
|**platformPartialRefundAmount** | **Integer** |  |  [optional] |
|**platformApproval** | **Boolean** |  |  [optional] |
|**platformActorType** | [**PlatformActorTypeEnum**](#PlatformActorTypeEnum) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**statusExpiration** | **OffsetDateTime** | Yield if eligible the date-time at which the dispute state expire. |  [optional] [readonly] |
|**awaitedParty** | [**AwaitedPartyEnum**](#AwaitedPartyEnum) | Determine who is awaited (actor) for the next transition |  [optional] [readonly] |
|**iri** | **String** |  |  [optional] [readonly] |
|**messageCount** | **Integer** |  |  [optional] [readonly] |
|**closedInFavorOf** | [**ClosedInFavorOfEnum**](#ClosedInFavorOfEnum) | Determine who won the case, if not specified, then it is ongoing. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;CREATED&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| OPENED | &quot;OPENED&quot; |
| ABANDONED | &quot;ABANDONED&quot; |
| OBJECTED | &quot;OBJECTED&quot; |
| PENDING_SHIPMENT | &quot;PENDING_SHIPMENT&quot; |
| SHIPPED | &quot;SHIPPED&quot; |
| IN_TRANSIT | &quot;IN_TRANSIT&quot; |
| RETURNED | &quot;RETURNED&quot; |
| DISMISSED | &quot;DISMISSED&quot; |
| RESOLVED | &quot;RESOLVED&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: IssueTypeEnum

| Name | Value |
|---- | -----|
| NOT_AS_DESCRIBED | &quot;NOT_AS_DESCRIBED&quot; |
| DOES_NOT_WORK | &quot;DOES_NOT_WORK&quot; |
| IS_INCOMPLETE | &quot;IS_INCOMPLETE&quot; |
| DELIVERY_ISSUE | &quot;DELIVERY_ISSUE&quot; |
| ALLEGED_FRAUD | &quot;ALLEGED_FRAUD&quot; |
| NULL | &quot;null&quot; |



## Enum: IssueInDescriptionTypeEnum

| Name | Value |
|---- | -----|
| WRONG_COLOUR | &quot;WRONG_COLOUR&quot; |
| DAMAGED_OR_USED | &quot;DAMAGED_OR_USED&quot; |
| INCORRECT_FORMAT_OR_SIZE | &quot;INCORRECT_FORMAT_OR_SIZE&quot; |
| DIFFERENT_MATERIAL | &quot;DIFFERENT_MATERIAL&quot; |
| NULL | &quot;null&quot; |



## Enum: ComplainantStakeEnum

| Name | Value |
|---- | -----|
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| NULL | &quot;null&quot; |



## Enum: InferredStakeEnum

| Name | Value |
|---- | -----|
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| NULL | &quot;null&quot; |



## Enum: ChosenSolutionEnum

| Name | Value |
|---- | -----|
| PARTIAL_REFUND_WITH_PARTIAL_RETURN | &quot;PARTIAL_REFUND_WITH_PARTIAL_RETURN&quot; |
| PARTIAL_REFUND_WITHOUT_RETURN | &quot;PARTIAL_REFUND_WITHOUT_RETURN&quot; |
| COMPLETE_REFUND_WITH_RETURN | &quot;COMPLETE_REFUND_WITH_RETURN&quot; |
| COMPLETE_REFUND_WITHOUT_RETURN | &quot;COMPLETE_REFUND_WITHOUT_RETURN&quot; |
| ABANDON_CLAIM | &quot;ABANDON_CLAIM&quot; |
| NULL | &quot;null&quot; |



## Enum: PlatformSolutionEnum

| Name | Value |
|---- | -----|
| PARTIAL_REFUND_WITH_PARTIAL_RETURN | &quot;PARTIAL_REFUND_WITH_PARTIAL_RETURN&quot; |
| PARTIAL_REFUND_WITHOUT_RETURN | &quot;PARTIAL_REFUND_WITHOUT_RETURN&quot; |
| COMPLETE_REFUND_WITH_RETURN | &quot;COMPLETE_REFUND_WITH_RETURN&quot; |
| COMPLETE_REFUND_WITHOUT_RETURN | &quot;COMPLETE_REFUND_WITHOUT_RETURN&quot; |
| ABANDON_CLAIM | &quot;ABANDON_CLAIM&quot; |
| NULL | &quot;null&quot; |



## Enum: PlatformActorTypeEnum

| Name | Value |
|---- | -----|
| RULING | &quot;RULING&quot; |
| AI | &quot;AI&quot; |
| CUSTOMER_CARE | &quot;CUSTOMER_CARE&quot; |
| PLATFORM_SUPPORT | &quot;PLATFORM_SUPPORT&quot; |
| NULL | &quot;null&quot; |



## Enum: AwaitedPartyEnum

| Name | Value |
|---- | -----|
| BUYER | &quot;BUYER&quot; |
| PLATFORM | &quot;PLATFORM&quot; |
| SELLER | &quot;SELLER&quot; |



## Enum: ClosedInFavorOfEnum

| Name | Value |
|---- | -----|
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



