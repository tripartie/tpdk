# # OfferRead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ulid** | **string** |  |
**publicUrl** | **string** | If specified, there would be not need for you to fill-in details. Must be accessible over WAN. | [optional]
**nature** | **string** | This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information. | [default to 'physical_item']
**title** | **string** |  | [optional]
**description** | **string** |  | [optional]
**unitPrice** | **float** |  | [optional]
**currencyCode** | **string** |  | [optional] [default to 'EUR']
**itemCount** | **int** |  | [default to 1]
**condition** | **string** |  | [default to 'USED']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
