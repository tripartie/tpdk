# Tripartie\Tpdk\ResolutionCenterApi

All URIs are relative to https://staging-api.tripartie.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiDisputesGetCollection()**](ResolutionCenterApi.md#apiDisputesGetCollection) | **GET** /disputes | Retrieves the collection of Dispute resources. |
| [**apiDisputesPost()**](ResolutionCenterApi.md#apiDisputesPost) | **POST** /disputes | Draft a standalone Dispute |
| [**apiDisputesUlidDelete()**](ResolutionCenterApi.md#apiDisputesUlidDelete) | **DELETE** /disputes/{ulid} | Abandon claims on Dispute |
| [**apiDisputesUlidGet()**](ResolutionCenterApi.md#apiDisputesUlidGet) | **GET** /disputes/{ulid} | Retrieves a Dispute resource. |
| [**apiDisputesUlidPatch()**](ResolutionCenterApi.md#apiDisputesUlidPatch) | **PATCH** /disputes/{ulid} | Updates the Dispute resource. |
| [**apiDisputesUlidevaluationsPost()**](ResolutionCenterApi.md#apiDisputesUlidevaluationsPost) | **POST** /disputes/{ulid}/evaluations | Submit an Evaluation for the Dispute |
| [**apiDisputesUlidevidencesGetCollection()**](ResolutionCenterApi.md#apiDisputesUlidevidencesGetCollection) | **GET** /disputes/{ulid}/evidences | Retrieve all Evidences in Dispute |
| [**apiDisputesUlidevidencesIdDelete()**](ResolutionCenterApi.md#apiDisputesUlidevidencesIdDelete) | **DELETE** /disputes/{ulid}/evidences/{id} | Withdraw an Evidence from a Dispute |
| [**apiDisputesUlidevidencesIdmediaPost()**](ResolutionCenterApi.md#apiDisputesUlidevidencesIdmediaPost) | **POST** /disputes/{ulid}/evidences/{id}/media | Upload attachment in regard of described Evidence |
| [**apiDisputesUlidevidencesPost()**](ResolutionCenterApi.md#apiDisputesUlidevidencesPost) | **POST** /disputes/{ulid}/evidences | Submit an Evidence to the Dispute case |
| [**apiDisputesUlidparcelsGetCollection()**](ResolutionCenterApi.md#apiDisputesUlidparcelsGetCollection) | **GET** /disputes/{ulid}/parcels | Retrieves the collection of Parcel resources. |
| [**apiDisputesUlidparcelsIdDelete()**](ResolutionCenterApi.md#apiDisputesUlidparcelsIdDelete) | **DELETE** /disputes/{ulid}/parcels/{id} | Removes the Parcel resource. |
| [**apiDisputesUlidparcelsPost()**](ResolutionCenterApi.md#apiDisputesUlidparcelsPost) | **POST** /disputes/{ulid}/parcels | Creates a Parcel resource. |
| [**apiOffersUlidmediasPost()**](ResolutionCenterApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer |


## `apiDisputesGetCollection()`

```php
apiDisputesGetCollection($page, $orderCreatedAt, $orderStatus, $orderUpdatedAt, $transactionOfferTitle, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $status, $transactionStatus, $existsRecommendedSolution, $existsChosenSolution, $existsCounterSolution, $existsPlatformSolution, $metadata, $transactionMetadata, $transactionOfferMetadata): \Tripartie\Tpdk\Model\DisputeCollectionRead[]
```

Retrieves the collection of Dispute resources.

Retrieves the collection of Dispute resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The collection page number
$orderCreatedAt = 'orderCreatedAt_example'; // string | 
$orderStatus = 'orderStatus_example'; // string | 
$orderUpdatedAt = 'orderUpdatedAt_example'; // string | 
$transactionOfferTitle = 'transactionOfferTitle_example'; // string | 
$createdAtBefore = 'createdAtBefore_example'; // string | 
$createdAtStrictlyBefore = 'createdAtStrictlyBefore_example'; // string | 
$createdAtAfter = 'createdAtAfter_example'; // string | 
$createdAtStrictlyAfter = 'createdAtStrictlyAfter_example'; // string | 
$status = CREATED; // string | Filter on a limited subset of status
$transactionStatus = CREATED; // string | Filter on a limited subset of transaction.status
$existsRecommendedSolution = True; // bool | 
$existsChosenSolution = True; // bool | 
$existsCounterSolution = True; // bool | 
$existsPlatformSolution = True; // bool | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$transactionMetadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$transactionOfferMetadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.

try {
    $result = $apiInstance->apiDisputesGetCollection($page, $orderCreatedAt, $orderStatus, $orderUpdatedAt, $transactionOfferTitle, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $status, $transactionStatus, $existsRecommendedSolution, $existsChosenSolution, $existsCounterSolution, $existsPlatformSolution, $metadata, $transactionMetadata, $transactionOfferMetadata);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The collection page number | [optional] [default to 1] |
| **orderCreatedAt** | **string**|  | [optional] |
| **orderStatus** | **string**|  | [optional] |
| **orderUpdatedAt** | **string**|  | [optional] |
| **transactionOfferTitle** | **string**|  | [optional] |
| **createdAtBefore** | **string**|  | [optional] |
| **createdAtStrictlyBefore** | **string**|  | [optional] |
| **createdAtAfter** | **string**|  | [optional] |
| **createdAtStrictlyAfter** | **string**|  | [optional] |
| **status** | **string**| Filter on a limited subset of status | [optional] |
| **transactionStatus** | **string**| Filter on a limited subset of transaction.status | [optional] |
| **existsRecommendedSolution** | **bool**|  | [optional] |
| **existsChosenSolution** | **bool**|  | [optional] |
| **existsCounterSolution** | **bool**|  | [optional] |
| **existsPlatformSolution** | **bool**|  | [optional] |
| **metadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **transactionMetadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **transactionOfferMetadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\DisputeCollectionRead[]**](../Model/DisputeCollectionRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiDisputesPost()`

```php
apiDisputesPost($disputeIndependentWrite): \Tripartie\Tpdk\Model\DisputePostCreationRead
```

Draft a standalone Dispute

Create a draft dispute to be filled by an alleged aggrieved customer. Do not use that endpoint if the transaction took place using our safe-checkout tunnel. This endpoint return a unique URL that can be accessed by both the complainant and seller (if individual).  **Note:** You can generate at your own discretion tokens for both parties, thus avoiding the secondary authentication.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$disputeIndependentWrite = new \Tripartie\Tpdk\Model\DisputeIndependentWrite(); // \Tripartie\Tpdk\Model\DisputeIndependentWrite | The new Dispute resource

try {
    $result = $apiInstance->apiDisputesPost($disputeIndependentWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **disputeIndependentWrite** | [**\Tripartie\Tpdk\Model\DisputeIndependentWrite**](../Model/DisputeIndependentWrite.md)| The new Dispute resource | |

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

## `apiDisputesUlidDelete()`

```php
apiDisputesUlidDelete($ulid)
```

Abandon claims on Dispute

**Only the buyer/complainant** can dismiss the case immediately. Otherwise, the support can but in a limited ranges of Dispute status.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier

try {
    $apiInstance->apiDisputesUlidDelete($ulid);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |

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

## `apiDisputesUlidGet()`

```php
apiDisputesUlidGet($ulid): \Tripartie\Tpdk\Model\DisputeRead
```

Retrieves a Dispute resource.

Retrieves a Dispute resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier

try {
    $result = $apiInstance->apiDisputesUlidGet($ulid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |

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

## `apiDisputesUlidPatch()`

```php
apiDisputesUlidPatch($ulid, $disputeUpdate): \Tripartie\Tpdk\Model\DisputeRead
```

Updates the Dispute resource.

Updates the Dispute resource.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$disputeUpdate = new \Tripartie\Tpdk\Model\DisputeUpdate(); // \Tripartie\Tpdk\Model\DisputeUpdate | The updated Dispute resource

try {
    $result = $apiInstance->apiDisputesUlidPatch($ulid, $disputeUpdate);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **disputeUpdate** | [**\Tripartie\Tpdk\Model\DisputeUpdate**](../Model/DisputeUpdate.md)| The updated Dispute resource | |

### Return type

[**\Tripartie\Tpdk\Model\DisputeRead**](../Model/DisputeRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiDisputesUlidevaluationsPost()`

```php
apiDisputesUlidevaluationsPost($ulid, $evaluationWrite): \Tripartie\Tpdk\Model\EvaluationRead
```

Submit an Evaluation for the Dispute

**Only authenticated** complainant and seller **CAN** issue an evaluation **WHEN** the dispute reached a final state.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$evaluationWrite = new \Tripartie\Tpdk\Model\EvaluationWrite(); // \Tripartie\Tpdk\Model\EvaluationWrite | The new Evaluation resource

try {
    $result = $apiInstance->apiDisputesUlidevaluationsPost($ulid, $evaluationWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidevaluationsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
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

## `apiDisputesUlidevidencesGetCollection()`

```php
apiDisputesUlidevidencesGetCollection($ulid, $page): \Tripartie\Tpdk\Model\EvidenceRead[]
```

Retrieve all Evidences in Dispute

Retrieves the collection of Evidence resources.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$page = 1; // int | The collection page number

try {
    $result = $apiInstance->apiDisputesUlidevidencesGetCollection($ulid, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidevidencesGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |

### Return type

[**\Tripartie\Tpdk\Model\EvidenceRead[]**](../Model/EvidenceRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiDisputesUlidevidencesIdDelete()`

```php
apiDisputesUlidevidencesIdDelete($ulid, $id)
```

Withdraw an Evidence from a Dispute

Removes the Evidence resource.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$id = 'id_example'; // string | Evidence identifier

try {
    $apiInstance->apiDisputesUlidevidencesIdDelete($ulid, $id);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidevidencesIdDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **id** | **string**| Evidence identifier | |

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

## `apiDisputesUlidevidencesIdmediaPost()`

```php
apiDisputesUlidevidencesIdmediaPost($ulid, $id, $file): \Tripartie\Tpdk\Model\MediaRead
```

Upload attachment in regard of described Evidence

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$id = 'id_example'; // string | Evidence identifier
$file = "/path/to/file.txt"; // \SplFileObject

try {
    $result = $apiInstance->apiDisputesUlidevidencesIdmediaPost($ulid, $id, $file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidevidencesIdmediaPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **id** | **string**| Evidence identifier | |
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

## `apiDisputesUlidevidencesPost()`

```php
apiDisputesUlidevidencesPost($ulid, $evidenceWrite): \Tripartie\Tpdk\Model\EvidenceRead
```

Submit an Evidence to the Dispute case

This action does not held the actual upload, you will have to do the upload in a dedicated request.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$evidenceWrite = new \Tripartie\Tpdk\Model\EvidenceWrite(); // \Tripartie\Tpdk\Model\EvidenceWrite | The new Evidence resource

try {
    $result = $apiInstance->apiDisputesUlidevidencesPost($ulid, $evidenceWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidevidencesPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
| **evidenceWrite** | [**\Tripartie\Tpdk\Model\EvidenceWrite**](../Model/EvidenceWrite.md)| The new Evidence resource | |

### Return type

[**\Tripartie\Tpdk\Model\EvidenceRead**](../Model/EvidenceRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiDisputesUlidparcelsGetCollection()`

```php
apiDisputesUlidparcelsGetCollection($ulid, $page): object[]
```

Retrieves the collection of Parcel resources.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$page = 1; // int | The collection page number

try {
    $result = $apiInstance->apiDisputesUlidparcelsGetCollection($ulid, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidparcelsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
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

## `apiDisputesUlidparcelsIdDelete()`

```php
apiDisputesUlidparcelsIdDelete($ulid, $id)
```

Removes the Parcel resource.

Removes the Parcel resource.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$id = 'id_example'; // string | Parcel identifier

try {
    $apiInstance->apiDisputesUlidparcelsIdDelete($ulid, $id);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidparcelsIdDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
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

## `apiDisputesUlidparcelsPost()`

```php
apiDisputesUlidparcelsPost($ulid, $parcelWrite): \Tripartie\Tpdk\Model\ParcelRead
```

Creates a Parcel resource.

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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ulid = 'ulid_example'; // string | Dispute identifier
$parcelWrite = new \Tripartie\Tpdk\Model\ParcelWrite(); // \Tripartie\Tpdk\Model\ParcelWrite | The new Parcel resource

try {
    $result = $apiInstance->apiDisputesUlidparcelsPost($ulid, $parcelWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResolutionCenterApi->apiDisputesUlidparcelsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ulid** | **string**| Dispute identifier | |
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


$apiInstance = new Tripartie\Tpdk\Api\ResolutionCenterApi(
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
    echo 'Exception when calling ResolutionCenterApi->apiOffersUlidmediasPost: ', $e->getMessage(), PHP_EOL;
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
