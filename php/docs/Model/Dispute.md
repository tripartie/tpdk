# # Dispute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly]
**ulid** | **string** |  |
**url** | **string** |  | [optional]
**transaction** | **string** |  | [optional]
**status** | **string** |  | [default to 'CREATED']
**redirectUrl** | **string** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional]
**itemCount** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional]
**issueType** | **string** |  |
**issueInDescriptionType** | **string** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional]
**issueDetails** | **string** |  | [optional]
**complainantTruthfulnessScore** | **int** |  | [default to 100]
**sellerTruthfulnessScore** | **int** |  | [default to 100]
**complainantStake** | **string** |  |
**inferredStake** | **string** |  | [optional]
**recommendedSolution** | **string** |  | [optional]
**recommendedPartialRefundAmount** | **int** |  | [optional]
**chosenSolution** | **string** |  | [optional]
**chosenPartialRefundAmount** | **int** |  | [optional]
**counterSolution** | **string** |  | [optional]
**counterPartialRefundAmount** | **int** |  | [optional]
**complainantApproval** | **bool** |  | [optional]
**sellerApproval** | **bool** |  |
**platformSolution** | **string** |  | [optional]
**platformPartialRefundAmount** | **int** |  | [optional]
**platformApproval** | **bool** |  | [optional]
**arbitrationBy** | **string** |  | [optional]
**parcels** | **string[]** |  |
**messages** | [**\Tripartie\Tpdk\Model\Message[]**](Message.md) |  |
**views** | [**\Tripartie\Tpdk\Model\View[]**](View.md) |  |
**metadata** | [**\Tripartie\Tpdk\Model\Metadata[]**](Metadata.md) |  |
**createdAt** | **\DateTime** |  | [optional] [readonly]
**updatedAt** | **\DateTime** |  | [optional] [readonly]
**iri** | **string** |  | [optional] [readonly]
**messageCount** | **int** |  | [optional] [readonly]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
