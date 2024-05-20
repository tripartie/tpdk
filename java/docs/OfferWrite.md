

# OfferWrite



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publicUrl** | **URI** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. |  [optional] |
|**enforcePersonaAuth** | **Boolean** | Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration. |  [optional] |
|**overrideRateCommissionSafeCheckout** | **BigDecimal** | Override YOUR platform fees for that particular Offer. |  [optional] |
|**redirectUrl** | **URI** | Fill-in that field IF you intend to redirect your customer instead of using a WebView. |  [optional] |
|**title** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**unitPrice** | **BigDecimal** |  |  [optional] |
|**currencyCode** | **String** |  |  [optional] |
|**itemCount** | **Integer** |  |  [optional] |
|**condition** | [**ConditionEnum**](#ConditionEnum) |  |  [optional] |
|**weightInGram** | **Integer** |  |  [optional] |
|**shippingAllowed** | **Boolean** | That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined. |  [optional] |
|**handDeliveryAllowed** | **Boolean** | Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product. |  [optional] |
|**shippingCarriers** | [**Set&lt;ShippingCarriersEnum&gt;**](#Set&lt;ShippingCarriersEnum&gt;) | If you wish to enable automated shipping label generation through a specific provider, specify it there. |  [optional] |
|**eanCode** | **String** |  |  [optional] |
|**canBeSoldSeparately** | **Boolean** | Set this flag to false to forbid a potential buyer to acquire this item separately.          This is only useful in a BulkOffer context. |  [optional] |
|**metadata** | [**List&lt;MetadataWrite&gt;**](MetadataWrite.md) |  |  [optional] |



## Enum: ConditionEnum

| Name | Value |
|---- | -----|
| NEW | &quot;NEW&quot; |
| USED | &quot;USED&quot; |
| DAMAGED | &quot;DAMAGED&quot; |
| DETERIORATED | &quot;DETERIORATED&quot; |
| UNRECOVERABLE | &quot;UNRECOVERABLE&quot; |



## Enum: Set&lt;ShippingCarriersEnum&gt;

| Name | Value |
|---- | -----|
| SWISSPOST | &quot;SwissPost&quot; |
| COLISSIMO | &quot;Colissimo&quot; |
| MONDIALRELAY | &quot;MondialRelay&quot; |



