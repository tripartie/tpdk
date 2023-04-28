# # WebhookObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **string** |  |
**transaction** | [**\Tripartie\Tpdk\Model\TransactionRead**](TransactionRead.md) |  | [optional]
**status** | **string** |  | [default to 'CREATED']
**itemCount** | **int** |  | [default to 1]
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
**parcels** | [**\Tripartie\Tpdk\Model\ParcelRead[]**](ParcelRead.md) |  |
**createdAt** | **\DateTime** |  | [optional] [readonly]
**updatedAt** | **\DateTime** |  | [optional] [readonly]
**iri** | **string** |  | [optional] [readonly]
**messageCount** | **int** |  | [optional] [readonly]
**id** | **int** |  | [optional] [readonly]
**firstName** | **string** |  | [optional]
**lastName** | **string** |  | [optional]
**gender** | **string** |  | [optional] [default to 'RATHER_NOT_SAY']
**dateOfBirth** | **\DateTime** |  | [optional]
**language** | **string** | That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements. | [optional]
**email** | **string** |  | [optional]
**mobilePhoneNumber** | **string** |  | [optional]
**address** | [**\Tripartie\Tpdk\Model\PersonaReadAddress**](PersonaReadAddress.md) |  | [optional]
**riskLevel** | **string** | We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore. | [optional]
**riskScore** | **int** | That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky. | [optional]
**externalPurchaseCount** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional]
**externalSellCount** | **int** | Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed. | [optional]
**metadata** | [**\Tripartie\Tpdk\Model\MetadataRead[]**](MetadataRead.md) | You can assign different meta to your Persona object for different purposes. eg. Ease searching. |
**offerCount** | **int** | Issued Offers count owned by a given Persona | [optional] [readonly]
**purchaseCount** | **int** |  | [optional] [readonly]
**publicUrl** | **string** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional]
**nature** | **string** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **string** |  | [optional]
**description** | **string** |  | [optional]
**unitPrice** | **float** |  | [optional]
**currencyCode** | **string** |  | [optional] [default to 'EUR']
**condition** | **string** |  | [default to 'USED']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
