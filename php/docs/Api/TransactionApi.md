# Tripartie\Tpdk\TransactionApi

All URIs are relative to https://staging-api.tripartie.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiTransactionsGetCollection()**](TransactionApi.md#apiTransactionsGetCollection) | **GET** /transactions | Retrieves the collection of Transaction resources. |


## `apiTransactionsGetCollection()`

```php
apiTransactionsGetCollection($page, $orderStatus, $metadata, $status, $existsDispute): \Tripartie\Tpdk\Model\TransactionCollectionRead[]
```

Retrieves the collection of Transaction resources.

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


$apiInstance = new Tripartie\Tpdk\Api\TransactionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The collection page number
$orderStatus = 'orderStatus_example'; // string | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
$status = CREATED; // string | Filter on a limited subset of status
$existsDispute = True; // bool | 

try {
    $result = $apiInstance->apiTransactionsGetCollection($page, $orderStatus, $metadata, $status, $existsDispute);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionApi->apiTransactionsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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
