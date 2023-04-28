# Tripartie\Tpdk\PersonaApi

All URIs are relative to https://staging-api.tripartie.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiPersonasGetCollection()**](PersonaApi.md#apiPersonasGetCollection) | **GET** /personas | Retrieves the collection of Persona resources. |
| [**apiPersonasIdDelete()**](PersonaApi.md#apiPersonasIdDelete) | **DELETE** /personas/{id} | Unregister a Persona (Your customer) |
| [**apiPersonasIdGet()**](PersonaApi.md#apiPersonasIdGet) | **GET** /personas/{id} | Retrieves a Persona resource. |
| [**apiPersonasIdPatch()**](PersonaApi.md#apiPersonasIdPatch) | **PATCH** /personas/{id} | Updates the Persona resource. |
| [**apiPersonasIdtokenPost()**](PersonaApi.md#apiPersonasIdtokenPost) | **POST** /personas/{id}/token | Issue authenticated URL for single end-user |
| [**apiPersonasPost()**](PersonaApi.md#apiPersonasPost) | **POST** /personas | Register a Persona (Your customer) |


## `apiPersonasGetCollection()`

```php
apiPersonasGetCollection($page, $firstName, $lastName, $dateOfBirth, $dateOfBirth2, $email, $mobilePhoneNumber, $mobilePhoneNumber2, $gender, $orderCreatedAt, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata): \Tripartie\Tpdk\Model\PersonaCollectionRead[]
```

Retrieves the collection of Persona resources.

Retrieves the collection of Persona resources.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The collection page number
$firstName = 'firstName_example'; // string | 
$lastName = 'lastName_example'; // string | 
$dateOfBirth = 'dateOfBirth_example'; // string | 
$dateOfBirth2 = 'dateOfBirth_example'; // string | 
$email = 'email_example'; // string | 
$mobilePhoneNumber = 'mobilePhoneNumber_example'; // string | 
$mobilePhoneNumber2 = array('mobilePhoneNumber_example'); // string[] | 
$gender = MALE; // string | Filter on a limited subset of gender
$orderCreatedAt = 'orderCreatedAt_example'; // string | 
$createdAtBefore = 'createdAtBefore_example'; // string | 
$createdAtStrictlyBefore = 'createdAtStrictlyBefore_example'; // string | 
$createdAtAfter = 'createdAtAfter_example'; // string | 
$createdAtStrictlyAfter = 'createdAtStrictlyAfter_example'; // string | 
$metadata = ["External-ID","1254A"]; // string[] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.

try {
    $result = $apiInstance->apiPersonasGetCollection($page, $firstName, $lastName, $dateOfBirth, $dateOfBirth2, $email, $mobilePhoneNumber, $mobilePhoneNumber2, $gender, $orderCreatedAt, $createdAtBefore, $createdAtStrictlyBefore, $createdAtAfter, $createdAtStrictlyAfter, $metadata);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasGetCollection: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The collection page number | [optional] [default to 1] |
| **firstName** | **string**|  | [optional] |
| **lastName** | **string**|  | [optional] |
| **dateOfBirth** | **string**|  | [optional] |
| **dateOfBirth2** | **string**|  | [optional] |
| **email** | **string**|  | [optional] |
| **mobilePhoneNumber** | **string**|  | [optional] |
| **mobilePhoneNumber2** | [**string[]**](../Model/string.md)|  | [optional] |
| **gender** | **string**| Filter on a limited subset of gender | [optional] |
| **orderCreatedAt** | **string**|  | [optional] |
| **createdAtBefore** | **string**|  | [optional] |
| **createdAtStrictlyBefore** | **string**|  | [optional] |
| **createdAtAfter** | **string**|  | [optional] |
| **createdAtStrictlyAfter** | **string**|  | [optional] |
| **metadata** | [**string[]**](../Model/string.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |

### Return type

[**\Tripartie\Tpdk\Model\PersonaCollectionRead[]**](../Model/PersonaCollectionRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdDelete()`

```php
apiPersonasIdDelete($id)
```

Unregister a Persona (Your customer)

You **MAY** unregister (or free the email/phone number) your Persona entry using that endpoint. *Please note that* this operation will fail if that Persona have any ongoing operations.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier

try {
    $apiInstance->apiPersonasIdDelete($id);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasIdDelete: ', $e->getMessage(), PHP_EOL;
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

## `apiPersonasIdGet()`

```php
apiPersonasIdGet($id): \Tripartie\Tpdk\Model\PersonaRead
```

Retrieves a Persona resource.

Retrieves a Persona resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier

try {
    $result = $apiInstance->apiPersonasIdGet($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |

### Return type

[**\Tripartie\Tpdk\Model\PersonaRead**](../Model/PersonaRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdPatch()`

```php
apiPersonasIdPatch($id, $personaUpdate): \Tripartie\Tpdk\Model\PersonaRead
```

Updates the Persona resource.

Update your Persona (eg. your customer/user entry) through that API call. _Beware that updating_ **email** and/or the **mobile phone number** must be done using non reserved values. Otherwise this operation will be rejected.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$personaUpdate = new \Tripartie\Tpdk\Model\PersonaUpdate(); // \Tripartie\Tpdk\Model\PersonaUpdate | The updated Persona resource

try {
    $result = $apiInstance->apiPersonasIdPatch($id, $personaUpdate);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasIdPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **personaUpdate** | [**\Tripartie\Tpdk\Model\PersonaUpdate**](../Model/PersonaUpdate.md)| The updated Persona resource | |

### Return type

[**\Tripartie\Tpdk\Model\PersonaRead**](../Model/PersonaRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasIdtokenPost()`

```php
apiPersonasIdtokenPost($id, $personaWrite): \Tripartie\Tpdk\Model\PersonaPostAuthRead
```

Issue authenticated URL for single end-user

Without this, your users may be required to pass a MFA challenge even if they are already logged-in from your website. Pass the URL you wish your user access, either a Dispute or Safe-checkout resource.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Persona identifier
$personaWrite = new \Tripartie\Tpdk\Model\PersonaWrite(); // \Tripartie\Tpdk\Model\PersonaWrite | The new Persona resource

try {
    $result = $apiInstance->apiPersonasIdtokenPost($id, $personaWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasIdtokenPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Persona identifier | |
| **personaWrite** | [**\Tripartie\Tpdk\Model\PersonaWrite**](../Model/PersonaWrite.md)| The new Persona resource | |

### Return type

[**\Tripartie\Tpdk\Model\PersonaPostAuthRead**](../Model/PersonaPostAuthRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `apiPersonasPost()`

```php
apiPersonasPost($personaWrite): \Tripartie\Tpdk\Model\PersonaRead
```

Register a Persona (Your customer)

You should not register your whole database of users, only those who are concerned by a Safe-checkout or Dispute operation. One Persona entry for your organization can be assigned as a seller or buyer.  **Notes:**   - (i) There is a unique constraint for the mobile phone numbers and email.   - (ii) You will have to issue a DELETE operation on a Persona that withhold a specific phone number or email.   - (iii) You are NOT REQUIRED to provide email OR a mobile phone number but it is highly recommended, if none provided the email will be generated as '{ulid}@your-domain.tld'. In that case, please specify at least one metadata in order to find your entry with ease.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = Tripartie\Tpdk\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Tripartie\Tpdk\Api\PersonaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$personaWrite = new \Tripartie\Tpdk\Model\PersonaWrite(); // \Tripartie\Tpdk\Model\PersonaWrite | The new Persona resource

try {
    $result = $apiInstance->apiPersonasPost($personaWrite);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PersonaApi->apiPersonasPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **personaWrite** | [**\Tripartie\Tpdk\Model\PersonaWrite**](../Model/PersonaWrite.md)| The new Persona resource | |

### Return type

[**\Tripartie\Tpdk\Model\PersonaRead**](../Model/PersonaRead.md)

### Authorization

[oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
