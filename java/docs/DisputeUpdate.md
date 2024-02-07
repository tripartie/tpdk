

# DisputeUpdate

Access directly our resolution center without having used the safe-checkout feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemCount** | **Integer** | The dispute may concern only PART of the package. Specify it there. |  [optional] |
|**issueType** | [**IssueTypeEnum**](#IssueTypeEnum) |  |  [optional] |
|**issueInDescriptionType** | [**IssueInDescriptionTypeEnum**](#IssueInDescriptionTypeEnum) | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. |  [optional] |
|**issueMentionedInOffer** | **Boolean** |  |  [optional] |
|**issueDetails** | **String** |  |  [optional] |
|**complainantStake** | [**ComplainantStakeEnum**](#ComplainantStakeEnum) |  |  [optional] |
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
|**platformReasoning** | **String** | Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care. |  [optional] |



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



