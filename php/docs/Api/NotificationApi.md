# Tripartie\Tpdk\NotificationApi

All URIs are relative to https://staging-api.tripartie.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiPersonasIdnotificationsGetCollection()**](NotificationApi.md#apiPersonasIdnotificationsGetCollection) | **GET** /personas/{id}/notifications | Retrieves the collection of Notification resources. |
| [**apiPersonasPersonaIdnotificationsIdPatch()**](NotificationApi.md#apiPersonasPersonaIdnotificationsIdPatch) | **PATCH** /personas/{personaId}/notifications/{id} | Updates the Notification resource. |
| [**apiUsersIdnotificationsGetCollection()**](NotificationApi.md#apiUsersIdnotificationsGetCollection) | **GET** /users/{id}/notifications | Retrieves the collection of Notification resources. |
| [**apiUsersUserIdnotificationsIdPatch()**](NotificationApi.md#apiUsersUserIdnotificationsIdPatch) | **PATCH** /users/{userId}/notifications/{id} | Updates the Notification resource. |


## `apiPersonasIdnotificationsGetCollection()`

```php
apiPersonasIdnotificationsGetCollection($id, $page): \Tripartie\Tpdk\Model\Notification[]
```

Retrieves the collection of Notification resources.

Retrieves the collection of Notification resources.

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


$apiInstance = new Tripartie\Tpdk\Api\NotificationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$page = 1; // int | The collection page number

try {
    $result = $apiInstance->apiPersonasIdnotificationsGetCollection($id, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationApi->apiPersonasIdnotificationsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |

### Return type

[**\Tripartie\Tpdk\Model\Notification[]**](../Model/Notification.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasPersonaIdnotificationsIdPatch()`

```php
apiPersonasPersonaIdnotificationsIdPatch($personaId, $id, $notification): \Tripartie\Tpdk\Model\Notification
```

Updates the Notification resource.

Updates the Notification resource.

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


$apiInstance = new Tripartie\Tpdk\Api\NotificationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$personaId = 'personaId_example'; // string | Persona identifier
$id = 'id_example'; // string | Notification identifier
$notification = new \Tripartie\Tpdk\Model\Notification(); // \Tripartie\Tpdk\Model\Notification | The updated Notification resource

try {
    $result = $apiInstance->apiPersonasPersonaIdnotificationsIdPatch($personaId, $id, $notification);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationApi->apiPersonasPersonaIdnotificationsIdPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **personaId** | **string**| Persona identifier | |
| **id** | **string**| Notification identifier | |
| **notification** | [**\Tripartie\Tpdk\Model\Notification**](../Model/Notification.md)| The updated Notification resource | |

### Return type

[**\Tripartie\Tpdk\Model\Notification**](../Model/Notification.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiUsersIdnotificationsGetCollection()`

```php
apiUsersIdnotificationsGetCollection($id, $page): \Tripartie\Tpdk\Model\NotificationRead[]
```

Retrieves the collection of Notification resources.

Retrieves the collection of Notification resources.

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


$apiInstance = new Tripartie\Tpdk\Api\NotificationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | User identifier
$page = 1; // int | The collection page number

try {
    $result = $apiInstance->apiUsersIdnotificationsGetCollection($id, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationApi->apiUsersIdnotificationsGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| User identifier | |
| **page** | **int**| The collection page number | [optional] [default to 1] |

### Return type

[**\Tripartie\Tpdk\Model\NotificationRead[]**](../Model/NotificationRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiUsersUserIdnotificationsIdPatch()`

```php
apiUsersUserIdnotificationsIdPatch($userId, $id, $notificationUpdate): \Tripartie\Tpdk\Model\NotificationRead
```

Updates the Notification resource.

Updates the Notification resource.

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


$apiInstance = new Tripartie\Tpdk\Api\NotificationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$userId = 'userId_example'; // string | User identifier
$id = 'id_example'; // string | Notification identifier
$notificationUpdate = new \Tripartie\Tpdk\Model\NotificationUpdate(); // \Tripartie\Tpdk\Model\NotificationUpdate | The updated Notification resource

try {
    $result = $apiInstance->apiUsersUserIdnotificationsIdPatch($userId, $id, $notificationUpdate);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationApi->apiUsersUserIdnotificationsIdPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **userId** | **string**| User identifier | |
| **id** | **string**| Notification identifier | |
| **notificationUpdate** | [**\Tripartie\Tpdk\Model\NotificationUpdate**](../Model/NotificationUpdate.md)| The updated Notification resource | |

### Return type

[**\Tripartie\Tpdk\Model\NotificationRead**](../Model/NotificationRead.md)

### Authorization

[jwtPersonalKey](../../README.md#jwtPersonalKey), [personaAuthKey](../../README.md#personaAuthKey), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
