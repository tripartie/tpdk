

# WebhookObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ulid** | **Object** |  |  |
|**transaction** | [**TransactionRead**](TransactionRead.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**redirectUrl** | **Object** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. |  [optional] |
|**itemCount** | **Object** |  |  [optional] |
|**issueType** | [**IssueTypeEnum**](#IssueTypeEnum) |  |  [optional] |
|**issueInDescriptionType** | [**IssueInDescriptionTypeEnum**](#IssueInDescriptionTypeEnum) | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. |  [optional] |
|**issueMentionedInOffer** | **Object** |  |  [optional] |
|**issueDetails** | **Object** |  |  [optional] |
|**complainantTruthfulnessScore** | **Object** |  |  |
|**sellerTruthfulnessScore** | **Object** |  |  |
|**complainantStake** | [**ComplainantStakeEnum**](#ComplainantStakeEnum) |  |  [optional] |
|**inferredStake** | [**InferredStakeEnum**](#InferredStakeEnum) |  |  [optional] |
|**recommendedSolution** | [**RecommendedSolutionEnum**](#RecommendedSolutionEnum) |  |  [optional] |
|**recommendedPartialRefundAmount** | **Object** |  |  [optional] |
|**chosenSolution** | [**ChosenSolutionEnum**](#ChosenSolutionEnum) |  |  [optional] |
|**chosenPartialRefundAmount** | **Object** |  |  [optional] |
|**counterSolution** | [**CounterSolutionEnum**](#CounterSolutionEnum) |  |  [optional] |
|**counterPartialRefundAmount** | **Object** |  |  [optional] |
|**sellerNotes** | **Object** |  |  [optional] |
|**sellerRejectionReason** | [**SellerRejectionReasonEnum**](#SellerRejectionReasonEnum) |  |  [optional] |
|**complainantApproval** | **Object** |  |  [optional] |
|**sellerApproval** | **Object** |  |  [optional] |
|**platformSolution** | [**PlatformSolutionEnum**](#PlatformSolutionEnum) |  |  [optional] |
|**platformPartialRefundAmount** | **Object** |  |  [optional] |
|**platformApproval** | **Object** |  |  [optional] |
|**platformActorType** | [**PlatformActorTypeEnum**](#PlatformActorTypeEnum) |  |  [optional] |
|**platformReasoning** | **Object** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. |  [optional] |
|**arbitrationBy** | **Object** |  |  [optional] |
|**parcels** | **Object** |  |  |
|**views** | **Object** |  |  |
|**metadata** | **Object** |  |  |
|**events** | **Object** |  |  [optional] |
|**createdAt** | **Object** |  |  [optional] [readonly] |
|**updatedAt** | **Object** |  |  [optional] [readonly] |
|**viewCount** | **Object** |  |  [optional] [readonly] |
|**statusExpiration** | **Object** | Yield if eligible the date-time at which the dispute state expire. |  [optional] [readonly] |
|**awaitedParty** | [**AwaitedPartyEnum**](#AwaitedPartyEnum) | Determine who is awaited (actor) for the next transition |  [optional] [readonly] |
|**iri** | **Object** |  |  [optional] [readonly] |
|**messageCount** | **Object** |  |  [optional] [readonly] |
|**closedInFavorOf** | [**ClosedInFavorOfEnum**](#ClosedInFavorOfEnum) | Determine who won the case, if not specified, then it is ongoing. |  [optional] [readonly] |
|**disbursedByBuyer** | **Object** | Total amount disbursed by the buyer to acquire the item. |  [optional] [readonly] |
|**maxRefundableForBuyer** | **Object** | How much the buyer can actually receive back in case of a full refund. |  [optional] [readonly] |
|**id** | **Object** |  |  [optional] [readonly] |
|**firstName** | **Object** |  |  [optional] |
|**lastName** | **Object** |  |  [optional] |
|**language** | **Object** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. |  [optional] |
|**email** | **Object** |  |  [optional] |
|**mobilePhoneNumber** | **Object** |  |  [optional] |
|**publicUrl** | **Object** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. |  [optional] |
|**organization** | [**OrganizationRead**](OrganizationRead.md) |  |  [optional] |
|**seller** | [**PersonaRead**](PersonaRead.md) | If the seller is actually YOUR organization, set it to NULL. |  |
|**nature** | [**NatureEnum**](#NatureEnum) | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. |  |
|**title** | **Object** |  |  [optional] |
|**description** | **Object** |  |  [optional] |
|**unitPrice** | **Object** |  |  [optional] |
|**currencyCode** | **Object** |  |  [optional] |
|**condition** | [**ConditionEnum**](#ConditionEnum) |  |  [optional] |
|**medias** | **Object** |  |  |



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



## Enum: RecommendedSolutionEnum

| Name | Value |
|---- | -----|
| PARTIAL_REFUND_WITH_PARTIAL_RETURN | &quot;PARTIAL_REFUND_WITH_PARTIAL_RETURN&quot; |
| PARTIAL_REFUND_WITHOUT_RETURN | &quot;PARTIAL_REFUND_WITHOUT_RETURN&quot; |
| COMPLETE_REFUND_WITH_RETURN | &quot;COMPLETE_REFUND_WITH_RETURN&quot; |
| COMPLETE_REFUND_WITHOUT_RETURN | &quot;COMPLETE_REFUND_WITHOUT_RETURN&quot; |
| ABANDON_CLAIM | &quot;ABANDON_CLAIM&quot; |
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



## Enum: CounterSolutionEnum

| Name | Value |
|---- | -----|
| PARTIAL_REFUND_WITH_PARTIAL_RETURN | &quot;PARTIAL_REFUND_WITH_PARTIAL_RETURN&quot; |
| PARTIAL_REFUND_WITHOUT_RETURN | &quot;PARTIAL_REFUND_WITHOUT_RETURN&quot; |
| COMPLETE_REFUND_WITH_RETURN | &quot;COMPLETE_REFUND_WITH_RETURN&quot; |
| COMPLETE_REFUND_WITHOUT_RETURN | &quot;COMPLETE_REFUND_WITHOUT_RETURN&quot; |
| ABANDON_CLAIM | &quot;ABANDON_CLAIM&quot; |
| NULL | &quot;null&quot; |



## Enum: SellerRejectionReasonEnum

| Name | Value |
|---- | -----|
| UNJUSTIFIED_REQUEST | &quot;UNJUSTIFIED_REQUEST&quot; |
| ABUSIVE_REQUEST | &quot;ABUSIVE_REQUEST&quot; |
| FRAUD_ATTEMPT | &quot;FRAUD_ATTEMPT&quot; |
| OTHER | &quot;OTHER&quot; |
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



