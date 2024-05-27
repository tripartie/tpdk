

# WebhookObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ulid** | **String** |  |  |
|**transaction** | [**DisputeTransactionRead**](DisputeTransactionRead.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**redirectUrl** | **String** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. |  [optional] |
|**itemCount** | **Integer** | The dispute may concern only PART of the package. Specify it there. |  [optional] |
|**issueType** | [**IssueTypeEnum**](#IssueTypeEnum) |  |  [optional] |
|**issueInDescriptionType** | [**IssueInDescriptionTypeEnum**](#IssueInDescriptionTypeEnum) | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. |  [optional] |
|**issueMentionedInOffer** | **Boolean** |  |  [optional] |
|**issueDetails** | **String** |  |  [optional] |
|**complainantTruthfulnessScore** | **Integer** |  |  |
|**sellerTruthfulnessScore** | **Integer** |  |  |
|**complainantStake** | [**ComplainantStakeEnum**](#ComplainantStakeEnum) |  |  [optional] |
|**inferredStake** | [**InferredStakeEnum**](#InferredStakeEnum) |  |  [optional] |
|**recommendedSolution** | [**RecommendedSolutionEnum**](#RecommendedSolutionEnum) |  |  [optional] |
|**recommendedPartialRefundAmount** | **Integer** |  |  [optional] |
|**chosenSolution** | [**ChosenSolutionEnum**](#ChosenSolutionEnum) |  |  [optional] |
|**chosenPartialRefundAmount** | **Integer** |  |  [optional] |
|**counterSolution** | [**CounterSolutionEnum**](#CounterSolutionEnum) |  |  [optional] |
|**counterPartialRefundAmount** | **Integer** |  |  [optional] |
|**sellerNotes** | **String** |  |  [optional] |
|**sellerRejectionReason** | [**SellerRejectionReasonEnum**](#SellerRejectionReasonEnum) |  |  [optional] |
|**complainantApproval** | **Boolean** |  |  [optional] |
|**sellerApproval** | **Boolean** |  |  [optional] |
|**platformSolution** | [**PlatformSolutionEnum**](#PlatformSolutionEnum) |  |  [optional] |
|**platformPartialRefundAmount** | **Integer** |  |  [optional] |
|**platformApproval** | **Boolean** |  |  [optional] |
|**platformActorType** | [**PlatformActorTypeEnum**](#PlatformActorTypeEnum) |  |  [optional] |
|**platformReasoning** | **String** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. |  [optional] |
|**arbitrationBy** | **String** |  |  [optional] |
|**parcels** | [**List&lt;DisputeParcelRead&gt;**](DisputeParcelRead.md) |  |  |
|**views** | [**List&lt;DisputeViewRead&gt;**](DisputeViewRead.md) |  |  |
|**metadata** | [**List&lt;PersonaMetadataRead&gt;**](PersonaMetadataRead.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. |  |
|**events** | [**List&lt;DisputeWorkflowEventRead&gt;**](DisputeWorkflowEventRead.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**viewCount** | **Integer** |  |  [optional] [readonly] |
|**statusExpiration** | **OffsetDateTime** | Yield if eligible the date-time at which the dispute state expire. |  [optional] [readonly] |
|**awaitedParty** | [**AwaitedPartyEnum**](#AwaitedPartyEnum) | Determine who is awaited (actor) for the next transition |  [optional] [readonly] |
|**iri** | **String** |  |  [optional] [readonly] |
|**messageCount** | **Integer** |  |  [optional] [readonly] |
|**closedInFavorOf** | [**ClosedInFavorOfEnum**](#ClosedInFavorOfEnum) | Determine who won the case, if not specified, then it is ongoing. |  [optional] [readonly] |
|**disbursedByBuyer** | **BigDecimal** | Total amount disbursed by the buyer to acquire the item. |  [optional] [readonly] |
|**maxRefundableForBuyer** | **BigDecimal** | How much the buyer can actually receive back in case of a full refund. |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**dateOfBirth** | **LocalDate** |  |  [optional] |
|**language** | **String** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. |  [optional] |
|**email** | **String** |  |  [optional] |
|**mobilePhoneNumber** | **String** |  |  [optional] |
|**address** | [**PersonaAddressRead**](PersonaAddressRead.md) |  |  [optional] |
|**riskLevel** | [**RiskLevelEnum**](#RiskLevelEnum) | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. |  [optional] |
|**riskScore** | **Integer** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. |  [optional] |
|**externalPurchaseCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**externalSellCount** | **Integer** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. |  [optional] |
|**offerCount** | **Integer** | Issued Offers count owned by a given Persona |  [optional] [readonly] |
|**purchaseCount** | **Integer** |  |  [optional] [readonly] |



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



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| OTHER | &quot;OTHER&quot; |
| RATHER_NOT_SAY | &quot;RATHER_NOT_SAY&quot; |



## Enum: RiskLevelEnum

| Name | Value |
|---- | -----|
| WEAK | &quot;WEAK&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| NULL | &quot;null&quot; |



