# Tripartie\Tpdk\SafeCheckoutApi

All URIs are relative to https://staging-api.tripartie.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiOffersGetCollection()**](SafeCheckoutApi.md#apiOffersGetCollection) | **GET** /offers | Read issued Offers |
| [**apiOffersPost()**](SafeCheckoutApi.md#apiOffersPost) | **POST** /offers | Create an Offer and retrieve url |
| [**apiOffersUlidGet()**](SafeCheckoutApi.md#apiOffersUlidGet) | **GET** /offers/{ulid} | Read an Offer |
| [**apiOffersUlidmediasIdDelete()**](SafeCheckoutApi.md#apiOffersUlidmediasIdDelete) | **DELETE** /offers/{ulid}/medias/{id} | Removes the Media resource. |
| [**apiOffersUlidmediasPost()**](SafeCheckoutApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer |
| [**apiOffersUlidtransactionsGetCollection()**](SafeCheckoutApi.md#apiOffersUlidtransactionsGetCollection) | **GET** /offers/{ulid}/transactions | Retrieve Payment Intents for Offer |
| [**apiOffersUlidtransactionsIdevaluationsPost()**](SafeCheckoutApi.md#apiOffersUlidtransactionsIdevaluationsPost) | **POST** /offers/{ulid}/transactions/{id}/evaluations | Submit an Evaluation for the Offer |
| [**apiOffersUlidtransactionsPost()**](SafeCheckoutApi.md#apiOffersUlidtransactionsPost) | **POST** /offers/{ulid}/transactions | Create a Payment Intent for Offer |
| [**apiPersonasIdoffersDelete()**](SafeCheckoutApi.md#apiPersonasIdoffersDelete) | **DELETE** /personas/{id}/offers | Revoke an Offer for given Persona |
| [**apiPersonasIdoffersGetCollection()**](SafeCheckoutApi.md#apiPersonasIdoffersGetCollection) | **GET** /personas/{id}/offers | List or Search Offers for given Persona |
| [**apiPersonasIdoffersPatch()**](SafeCheckoutApi.md#apiPersonasIdoffersPatch) | **PATCH** /personas/{id}/offers | Update an Offer for given Persona |
| [**apiPersonasIdoffersPost()**](SafeCheckoutApi.md#apiPersonasIdoffersPost) | **POST** /personas/{id}/offers | Create an Offer for given Persona |
| [**apiTransactionsUliddisputeDelete()**](SafeCheckoutApi.md#apiTransactionsUliddisputeDelete) | **DELETE** /transactions/{ulid}/dispute | Abandon claims on Dispute |
| [**apiTransactionsUliddisputeGet()**](SafeCheckoutApi.md#apiTransactionsUliddisputeGet) | **GET** /transactions/{ulid}/dispute | Read Dispute from existing Transaction |
| [**apiTransactionsUliddisputePatch()**](SafeCheckoutApi.md#apiTransactionsUliddisputePatch) | **PATCH** /transactions/{ulid}/dispute | Interact with a Dispute |
| [**apiTransactionsUliddisputePost()**](SafeCheckoutApi.md#apiTransactionsUliddisputePost) | **POST** /transactions/{ulid}/dispute | Open a Dispute related to existing Transaction |
| [**apiTransactionsUlidparcelsGetCollection()**](SafeCheckoutApi.md#apiTransactionsUlidparcelsGetCollection) | **GET** /transactions/{ulid}/parcels | Read shipments from Transaction |
| [**apiTransactionsUlidparcelsIdDelete()**](SafeCheckoutApi.md#apiTransactionsUlidparcelsIdDelete) | **DELETE** /transactions/{ulid}/parcels/{id} | Withdraw shipment from Transaction |
| [**apiTransactionsUlidparcelsPost()**](SafeCheckoutApi.md#apiTransactionsUlidparcelsPost) | **POST** /transactions/{ulid}/parcels | Manually declare package shipped for Transaction |


## `apiOffersGetCollection()`

```php
apiOffersGetCollection($page, $title, $publicUrl, $publicUrl2, $unitPrice, $unitPrice2, $itemCount, $itemCount2, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata, $offerMetadata, $nature, $condition, $shippingAllowed): \Tripartie\Tpdk\Model\OfferCollectionRead[]
```

Read issued Offers

Retrieves the collection of Offer resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The collection page number
$title = 'title_example'; // string | 
$publicUrl = 'publicUrl_example'; // string | 
$publicUrl2 = array('publicUrl_example'); // string[] | 
$unitPrice = 3.4; // float | 
$unitPrice2 = array(3.4); // float[] | 
$itemCount = 56; // int | 
$itemCount2 = array(56); // int[] | 
$createdAtBefore = 'createdAtBefore_example'; // string | 
$createdAtStrictlyBefore = 'createdAtStrictlyBefore_example'; // string | 
$createdAtAfter = 'createdAtAfter_example'; // string | 
$createdAtStrictlyAfter = 'createdAtStrictlyAfter_example'; // string | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$offerMetadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$nature = service; // string | Filter on a limited subset of nature
$condition = NEW; // string | Filter on a limited subset of condition
$shippingAllowed = True; // bool | 

try {
    $result = $apiInstance->apiOffersGetCollection($page, $title, $publicUrl, $publicUrl2, $unitPrice, $unitPrice2, $itemCount, $itemCount2, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata, $offerMetadata, $nature, $condition, $shippingAllowed);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The collection page number | [optional] [default to 1] |
| **title** | **string**|  | [optional] |
| **publicUrl** | **string**|  | [optional] |
| **publicUrl2** | [**string[]**](../Model/string.md)|  | [optional] |
| **unitPrice** | **float**|  | [optional] |
| **unitPrice2** | [**float[]**](../Model/float.md)|  | [optional] |
| **itemCount** | **int**|  | [optional] |
| **itemCount2** | [**int[]**](../Model/int.md)|  | [optional] |
| **createdAtBefore** | **string**|  | [optional] |
| **createdAtStrictlyBefore** | **string**|  | [optional] |
| **createdAtAfter** | **string**|  | [optional] |
| **createdAtStrictlyAfter** | **string**|  | [optional] |
| **metadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **offerMetadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **nature** | **string**| Filter on a limited subset of nature | [optional] |
| **condition** | **string**| Filter on a limited subset of condition | [optional] |
| **shippingAllowed** | **bool**|  | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\OfferCollectionRead[]**](../Model/OfferCollectionRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersPost()`

```php
apiOffersPost($offerIndependentWrite): \Tripartie\Tpdk\Model\OfferPostCreationRead
```

Create an Offer and retrieve url

Publish an offer so that you can safely retrieve a safe-checkout unique link from us

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$offerIndependentWrite = new \Tripartie\Tpdk\Model\OfferIndependentWrite(); // \Tripartie\Tpdk\Model\OfferIndependentWrite | The new Offer resource

try {
    $result = $apiInstance->apiOffersPost($offerIndependentWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offerIndependentWrite** | [**\Tripartie\Tpdk\Model\OfferIndependentWrite**](../Model/OfferIndependentWrite.md)| The new Offer resource | |

### Return type

[**\Tripartie\Tpdk\Model\OfferPostCreationRead**](../Model/OfferPostCreationRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidGet()`

```php
apiOffersUlidGet($ulid): \Tripartie\Tpdk\Model\OfferRead
```

Read an Offer

Retrieves a Offer resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Offer identifier

try {
    $result = $apiInstance->apiOffersUlidGet($ulid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Offer identifier | |

### Return type

[**\Tripartie\Tpdk\Model\OfferRead**](../Model/OfferRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidmediasIdDelete()`

```php
apiOffersUlidmediasIdDelete($ulid, $id)
```

Removes the Media resource.

Removes the Media resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Offer identifier
$id = 'id_example'; // string | Media identifier

try {
    $apiInstance->apiOffersUlidmediasIdDelete($ulid, $id);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidmediasIdDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Offer identifier | |
| **id** | **string**| Media identifier | |

### Return type

void (empty response body)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidmediasPost()`

```php
apiOffersUlidmediasPost($ulid, $file): \Tripartie\Tpdk\Model\MediaRead
```

Upload a picture for a given Offer

Creates a Media resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Offer identifier
$file = "/path/to/file.txt"; // \SplFileObject

try {
    $result = $apiInstance->apiOffersUlidmediasPost($ulid, $file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidmediasPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Offer identifier | |
| **file** | **\SplFileObject****\SplFileObject**|  | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\MediaRead**](../Model/MediaRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidtransactionsGetCollection()`

```php
apiOffersUlidtransactionsGetCollection($ulid, $page, $orderStatus, $metadata, $status, $existsDispute): \Tripartie\Tpdk\Model\TransactionCollectionRead[]
```

Retrieve Payment Intents for Offer

Retrieves the collection of Transaction resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Offer identifier
$page = 1; // int | The collection page number
$orderStatus = 'orderStatus_example'; // string | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$status = CREATED; // string | Filter on a limited subset of status
$existsDispute = True; // bool | 

try {
    $result = $apiInstance->apiOffersUlidtransactionsGetCollection($ulid, $page, $orderStatus, $metadata, $status, $existsDispute);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidtransactionsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Offer identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |
| **orderStatus** | **string**|  | [optional] |
| **metadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **status** | **string**| Filter on a limited subset of status | [optional] |
| **existsDispute** | **bool**|  | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\TransactionCollectionRead[]**](../Model/TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidtransactionsIdevaluationsPost()`

```php
apiOffersUlidtransactionsIdevaluationsPost($ulid, $id, $evaluationWrite): \Tripartie\Tpdk\Model\EvaluationRead
```

Submit an Evaluation for the Offer

**Only authenticated** buyer and seller **CAN** issue an evaluation **WHEN** the transaction reached a final state.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$id = 'id_example'; // string | Transaction identifier
$evaluationWrite = new \Tripartie\Tpdk\Model\EvaluationWrite(); // \Tripartie\Tpdk\Model\EvaluationWrite | The new Evaluation resource

try {
    $result = $apiInstance->apiOffersUlidtransactionsIdevaluationsPost($ulid, $id, $evaluationWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidtransactionsIdevaluationsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **id** | **string**| Transaction identifier | |
| **evaluationWrite** | [**\Tripartie\Tpdk\Model\EvaluationWrite**](../Model/EvaluationWrite.md)| The new Evaluation resource | |

### Return type

[**\Tripartie\Tpdk\Model\EvaluationRead**](../Model/EvaluationRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiOffersUlidtransactionsPost()`

```php
apiOffersUlidtransactionsPost($ulid, $body): \Tripartie\Tpdk\Model\TransactionRead
```

Create a Payment Intent for Offer

Cannot be used outside of a Persona (buyer)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Offer identifier
$body = array('key' => new \stdClass); // object | The new Transaction resource

try {
    $result = $apiInstance->apiOffersUlidtransactionsPost($ulid, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiOffersUlidtransactionsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Offer identifier | |
| **body** | **object**| The new Transaction resource | |

### Return type

[**\Tripartie\Tpdk\Model\TransactionRead**](../Model/TransactionRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdoffersDelete()`

```php
apiPersonasIdoffersDelete($id)
```

Revoke an Offer for given Persona

That goes without says, if that **Offer** have a _Transaction_ **that is ongoing**, you **MAY NOT** revoke the **Offer**.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier

try {
    $apiInstance->apiPersonasIdoffersDelete($id);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiPersonasIdoffersDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdoffersGetCollection()`

```php
apiPersonasIdoffersGetCollection($id, $page, $title, $publicUrl, $publicUrl2, $unitPrice, $unitPrice2, $itemCount, $itemCount2, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata, $offerMetadata, $nature, $condition, $shippingAllowed): \Tripartie\Tpdk\Model\OfferCollectionRead[]
```

List or Search Offers for given Persona

Retrieves the collection of Offer resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$page = 1; // int | The collection page number
$title = 'title_example'; // string | 
$publicUrl = 'publicUrl_example'; // string | 
$publicUrl2 = array('publicUrl_example'); // string[] | 
$unitPrice = 3.4; // float | 
$unitPrice2 = array(3.4); // float[] | 
$itemCount = 56; // int | 
$itemCount2 = array(56); // int[] | 
$createdAtBefore = 'createdAtBefore_example'; // string | 
$createdAtStrictlyBefore = 'createdAtStrictlyBefore_example'; // string | 
$createdAtAfter = 'createdAtAfter_example'; // string | 
$createdAtStrictlyAfter = 'createdAtStrictlyAfter_example'; // string | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$offerMetadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$nature = service; // string | Filter on a limited subset of nature
$condition = NEW; // string | Filter on a limited subset of condition
$shippingAllowed = True; // bool | 

try {
    $result = $apiInstance->apiPersonasIdoffersGetCollection($id, $page, $title, $publicUrl, $publicUrl2, $unitPrice, $unitPrice2, $itemCount, $itemCount2, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata, $offerMetadata, $nature, $condition, $shippingAllowed);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiPersonasIdoffersGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |
| **title** | **string**|  | [optional] |
| **publicUrl** | **string**|  | [optional] |
| **publicUrl2** | [**string[]**](../Model/string.md)|  | [optional] |
| **unitPrice** | **float**|  | [optional] |
| **unitPrice2** | [**float[]**](../Model/float.md)|  | [optional] |
| **itemCount** | **int**|  | [optional] |
| **itemCount2** | [**int[]**](../Model/int.md)|  | [optional] |
| **createdAtBefore** | **string**|  | [optional] |
| **createdAtStrictlyBefore** | **string**|  | [optional] |
| **createdAtAfter** | **string**|  | [optional] |
| **createdAtStrictlyAfter** | **string**|  | [optional] |
| **metadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **offerMetadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **nature** | **string**| Filter on a limited subset of nature | [optional] |
| **condition** | **string**| Filter on a limited subset of condition | [optional] |
| **shippingAllowed** | **bool**|  | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\OfferCollectionRead[]**](../Model/OfferCollectionRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdoffersPatch()`

```php
apiPersonasIdoffersPatch($id, $offerUpdate): \Tripartie\Tpdk\Model\OfferRead
```

Update an Offer for given Persona

Updates the Offer resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$offerUpdate = new \Tripartie\Tpdk\Model\OfferUpdate(); // \Tripartie\Tpdk\Model\OfferUpdate | The updated Offer resource

try {
    $result = $apiInstance->apiPersonasIdoffersPatch($id, $offerUpdate);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiPersonasIdoffersPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **offerUpdate** | [**\Tripartie\Tpdk\Model\OfferUpdate**](../Model/OfferUpdate.md)| The updated Offer resource | |

### Return type

[**\Tripartie\Tpdk\Model\OfferRead**](../Model/OfferRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdoffersPost()`

```php
apiPersonasIdoffersPost($id, $offerWrite): \Tripartie\Tpdk\Model\OfferPostCreationRead
```

Create an Offer for given Persona

Creates a Offer resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$offerWrite = new \Tripartie\Tpdk\Model\OfferWrite(); // \Tripartie\Tpdk\Model\OfferWrite | The new Offer resource

try {
    $result = $apiInstance->apiPersonasIdoffersPost($id, $offerWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiPersonasIdoffersPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **offerWrite** | [**\Tripartie\Tpdk\Model\OfferWrite**](../Model/OfferWrite.md)| The new Offer resource | |

### Return type

[**\Tripartie\Tpdk\Model\OfferPostCreationRead**](../Model/OfferPostCreationRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUliddisputeDelete()`

```php
apiTransactionsUliddisputeDelete($ulid)
```

Abandon claims on Dispute

**Only the buyer/complainant** can dismiss the case immediately. Otherwise, the support can but in a limited ranges of Dispute status.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier

try {
    $apiInstance->apiTransactionsUliddisputeDelete($ulid);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUliddisputeDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUliddisputeGet()`

```php
apiTransactionsUliddisputeGet($ulid): \Tripartie\Tpdk\Model\DisputeRead
```

Read Dispute from existing Transaction

Retrieves a Dispute resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier

try {
    $result = $apiInstance->apiTransactionsUliddisputeGet($ulid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUliddisputeGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |

### Return type

[**\Tripartie\Tpdk\Model\DisputeRead**](../Model/DisputeRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUliddisputePatch()`

```php
apiTransactionsUliddisputePatch($ulid, $disputeUpdate): \Tripartie\Tpdk\Model\DisputeRead
```

Interact with a Dispute

Only authenticated Persona can interact with a Dispute object. Usually through our web application.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier
$disputeUpdate = new \Tripartie\Tpdk\Model\DisputeUpdate(); // \Tripartie\Tpdk\Model\DisputeUpdate | The updated Dispute resource

try {
    $result = $apiInstance->apiTransactionsUliddisputePatch($ulid, $disputeUpdate);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUliddisputePatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |
| **disputeUpdate** | [**\Tripartie\Tpdk\Model\DisputeUpdate**](../Model/DisputeUpdate.md)| The updated Dispute resource | |

### Return type

[**\Tripartie\Tpdk\Model\DisputeRead**](../Model/DisputeRead.md)

### Authorization

[personaAuthKey](../../README.md#personaAuthKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUliddisputePost()`

```php
apiTransactionsUliddisputePost($ulid, $disputeWrite): \Tripartie\Tpdk\Model\DisputePostCreationRead
```

Open a Dispute related to existing Transaction

Creates a Dispute resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier
$disputeWrite = new \Tripartie\Tpdk\Model\DisputeWrite(); // \Tripartie\Tpdk\Model\DisputeWrite | The new Dispute resource

try {
    $result = $apiInstance->apiTransactionsUliddisputePost($ulid, $disputeWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUliddisputePost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |
| **disputeWrite** | [**\Tripartie\Tpdk\Model\DisputeWrite**](../Model/DisputeWrite.md)| The new Dispute resource | |

### Return type

[**\Tripartie\Tpdk\Model\DisputePostCreationRead**](../Model/DisputePostCreationRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUlidparcelsGetCollection()`

```php
apiTransactionsUlidparcelsGetCollection($ulid, $page): object[]
```

Read shipments from Transaction

Retrieves the collection of Parcel resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier
$page = 1; // int | The collection page number

try {
    $result = $apiInstance->apiTransactionsUlidparcelsGetCollection($ulid, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUlidparcelsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |

### Return type

**object[]**

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUlidparcelsIdDelete()`

```php
apiTransactionsUlidparcelsIdDelete($ulid, $id)
```

Withdraw shipment from Transaction

No one except the support can do that manoeuvre.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier
$id = 'id_example'; // string | Parcel identifier

try {
    $apiInstance->apiTransactionsUlidparcelsIdDelete($ulid, $id);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUlidparcelsIdDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |
| **id** | **string**| Parcel identifier | |

### Return type

void (empty response body)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiTransactionsUlidparcelsPost()`

```php
apiTransactionsUlidparcelsPost($ulid, $parcelWrite): \Tripartie\Tpdk\Model\ParcelRead
```

Manually declare package shipped for Transaction

Creates a Parcel resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: jwtPersonalKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

// Configure API key authorization: personaAuthKey
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKey('X-Persona-Auth', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-Persona-Auth', 'Bearer');

// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\SafeCheckoutApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Transaction identifier
$parcelWrite = new \Tripartie\Tpdk\Model\ParcelWrite(); // \Tripartie\Tpdk\Model\ParcelWrite | The new Parcel resource

try {
    $result = $apiInstance->apiTransactionsUlidparcelsPost($ulid, $parcelWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SafeCheckoutApi->apiTransactionsUlidparcelsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Transaction identifier | |
| **parcelWrite** | [**\Tripartie\Tpdk\Model\ParcelWrite**](../Model/ParcelWrite.md)| The new Parcel resource | |

### Return type

[**\Tripartie\Tpdk\Model\ParcelRead**](../Model/ParcelRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
