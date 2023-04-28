# # User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [optional] [readonly]
**captcha** | **string** |  | [optional]
**firstName** | **string** |  | [optional]
**lastName** | **string** |  | [optional]
**publicName** | **string** |  | [optional]
**roleInCompany** | **string** |  | [optional]
**birthday** | **\DateTime** |  |
**email** | **string** |  | [optional]
**roles** | **string[]** |  |
**password** | **string** | The hashed password |
**plainPassword** | **string** |  | [optional]
**intlPhoneNumber** | **string** |  | [optional]
**originCountry** | **string** | The originating country | [optional]
**preferredLanguage** | **string** |  | [optional]
**lastSuccessfulLogIn** | **\DateTime** |  | [optional]
**emailVerificationCode** | **string** |  | [optional]
**emailVerificationInput** | **string** |  | [optional]
**phoneVerificationCode** | **string** |  | [optional]
**phoneVerificationInput** | **string** |  | [optional]
**avatar** | **string** |  | [optional]
**notifications** | **string[]** |  | [optional] [readonly]
**medias** | **string[]** |  | [optional] [readonly]
**views** | [**\Tripartie\Tpdk\Model\View[]**](View.md) |  |
**createdAt** | **\DateTime** |  | [optional] [readonly]
**updatedAt** | **\DateTime** |  | [optional] [readonly]
**consentMailNotification** | **bool** |  |
**consentMailAds** | **bool** |  |
**api** | [**\Tripartie\Tpdk\Model\UserApi**](UserApi.md) |  | [optional]
**organization** | **string** |  | [optional]
**username** | **string** | A visual identifier that represents this user. | [optional] [readonly]
**salt** | **string** |  | [optional] [readonly]
**userIdentifier** | **string** |  | [optional] [readonly]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
