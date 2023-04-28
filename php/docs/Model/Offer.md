# # Offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly]
**ulid** | **string** |  |
**publicUrl** | **string** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional]
**enforcePersonaAuth** | **bool** | Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration. |
**overrideRateCommissionSafeCheckout** | **float** | Override YOUR platform fees for that particular Offer. |
**redirectUrl** | **string** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. | [optional]
**url** | **string** |  | [readonly]
**organization** | **string** |  | [optional]
**seller** | **string** | If the seller is actually YOUR organization, set it to NULL. | [optional]
**nature** | **string** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **string** |  | [optional]
**description** | **string** |  | [optional]
**unitPrice** | **float** |  | [optional]
**currencyCode** | **string** |  | [optional] [default to 'EUR']
**itemCount** | **int** |  | [default to 1]
**condition** | **string** |  | [default to 'USED']
**weightInGram** | **int** |  | [optional]
**shippingAllowed** | **bool** | That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined. |
**handDeliveryAllowed** | **bool** | Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product. | [default to true]
**shippingCarriers** | **string[]** | If you wish to enable automated shipping label generation through a specific provider, specify it there. |
**eanCode** | **string** |  | [optional]
**metadata** | [**\Tripartie\Tpdk\Model\Metadata[]**](Metadata.md) |  |
**medias** | **string[]** |  |
**views** | [**\Tripartie\Tpdk\Model\View[]**](View.md) |  |
**createdAt** | **\DateTime** |  | [optional] [readonly]
**updatedAt** | **\DateTime** |  | [optional] [readonly]
**iri** | **string** |  | [optional] [readonly]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
