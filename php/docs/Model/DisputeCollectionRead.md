# # DisputeCollectionRead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **string** |  |
**transaction** | [**\Tripartie\Tpdk\Model\TransactionCollectionRead**](TransactionCollectionRead.md) |  | [optional]
**status** | **string** |  | [default to 'CREATED']
**itemCount** | **int** | The dispute may concern only PART of the package. Specify it there. | [optional]
**issueType** | **string** |  |
**issueInDescriptionType** | **string** | To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED. | [optional]
**complainantStake** | **string** |  |
**inferredStake** | **string** |  | [optional]
**createdAt** | **\DateTime** |  | [optional] [readonly]
**updatedAt** | **\DateTime** |  | [optional] [readonly]
**iri** | **string** |  | [optional] [readonly]
**messageCount** | **int** |  | [optional] [readonly]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
