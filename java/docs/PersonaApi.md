# PersonaApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPersonasGetCollection**](PersonaApi.md#apiPersonasGetCollection) | **GET** /personas | Retrieves the collection of Persona resources. |
| [**apiPersonasIdDelete**](PersonaApi.md#apiPersonasIdDelete) | **DELETE** /personas/{id} | Unregister a Persona (Your customer) |
| [**apiPersonasIdGet**](PersonaApi.md#apiPersonasIdGet) | **GET** /personas/{id} | Retrieves a Persona resource. |
| [**apiPersonasIdPatch**](PersonaApi.md#apiPersonasIdPatch) | **PATCH** /personas/{id} | Updates the Persona resource. |
| [**apiPersonasIdtokenPost**](PersonaApi.md#apiPersonasIdtokenPost) | **POST** /personas/{id}/token | Issue authenticated URL for single end-user |
| [**apiPersonasPost**](PersonaApi.md#apiPersonasPost) | **POST** /personas | Register a Persona (Your customer) |


<a id="apiPersonasGetCollection"></a>
# **apiPersonasGetCollection**
> List&lt;PersonaCollectionRead&gt; apiPersonasGetCollection().page(page).firstName(firstName).lastName(lastName).email(email).email2(email2).mobilePhoneNumber(mobilePhoneNumber).mobilePhoneNumber2(mobilePhoneNumber2).gender(gender).orderCreatedAt(orderCreatedAt).createdAtBefore(createdAtBefore).createdAtStrictlyBefore(createdAtStrictlyBefore).createdAtAfter(createdAtAfter).createdAtStrictlyAfter(createdAtStrictlyAfter).dateOfBirthBefore(dateOfBirthBefore).dateOfBirthStrictlyBefore(dateOfBirthStrictlyBefore).dateOfBirthAfter(dateOfBirthAfter).dateOfBirthStrictlyAfter(dateOfBirthStrictlyAfter).metadata(metadata).execute();

Retrieves the collection of Persona resources.

Retrieves the collection of Persona resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String firstName = "firstName_example"; // String | 
    String lastName = "lastName_example"; // String | 
    String email = "email_example"; // String | 
    List<String> email2 = Arrays.asList(); // List<String> | 
    String mobilePhoneNumber = "mobilePhoneNumber_example"; // String | 
    List<String> mobilePhoneNumber2 = Arrays.asList(); // List<String> | 
    String gender = "MALE"; // String | Filter on a limited subset of gender
    String orderCreatedAt = "asc"; // String | 
    String createdAtBefore = "createdAtBefore_example"; // String | 
    String createdAtStrictlyBefore = "createdAtStrictlyBefore_example"; // String | 
    String createdAtAfter = "createdAtAfter_example"; // String | 
    String createdAtStrictlyAfter = "createdAtStrictlyAfter_example"; // String | 
    String dateOfBirthBefore = "dateOfBirthBefore_example"; // String | 
    String dateOfBirthStrictlyBefore = "dateOfBirthStrictlyBefore_example"; // String | 
    String dateOfBirthAfter = "dateOfBirthAfter_example"; // String | 
    String dateOfBirthStrictlyAfter = "dateOfBirthStrictlyAfter_example"; // String | 
    List<String> metadata = Arrays.asList(new ArrayList<>()); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    try {
      List<PersonaCollectionRead> result = apiInstance.apiPersonasGetCollection()
            .page(page)
            .firstName(firstName)
            .lastName(lastName)
            .email(email)
            .email2(email2)
            .mobilePhoneNumber(mobilePhoneNumber)
            .mobilePhoneNumber2(mobilePhoneNumber2)
            .gender(gender)
            .orderCreatedAt(orderCreatedAt)
            .createdAtBefore(createdAtBefore)
            .createdAtStrictlyBefore(createdAtStrictlyBefore)
            .createdAtAfter(createdAtAfter)
            .createdAtStrictlyAfter(createdAtStrictlyAfter)
            .dateOfBirthBefore(dateOfBirthBefore)
            .dateOfBirthStrictlyBefore(dateOfBirthStrictlyBefore)
            .dateOfBirthAfter(dateOfBirthAfter)
            .dateOfBirthStrictlyAfter(dateOfBirthStrictlyAfter)
            .metadata(metadata)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasGetCollection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **firstName** | **String**|  | [optional] |
| **lastName** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **email2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **mobilePhoneNumber** | **String**|  | [optional] |
| **mobilePhoneNumber2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **gender** | **String**| Filter on a limited subset of gender | [optional] [enum: MALE, FEMALE, OTHER, RATHER_NOT_SAY] |
| **orderCreatedAt** | **String**|  | [optional] [enum: asc, desc] |
| **createdAtBefore** | **String**|  | [optional] |
| **createdAtStrictlyBefore** | **String**|  | [optional] |
| **createdAtAfter** | **String**|  | [optional] |
| **createdAtStrictlyAfter** | **String**|  | [optional] |
| **dateOfBirthBefore** | **String**|  | [optional] |
| **dateOfBirthStrictlyBefore** | **String**|  | [optional] |
| **dateOfBirthAfter** | **String**|  | [optional] |
| **dateOfBirthStrictlyAfter** | **String**|  | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |

### Return type

[**List&lt;PersonaCollectionRead&gt;**](PersonaCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Persona collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdDelete"></a>
# **apiPersonasIdDelete**
> apiPersonasIdDelete(id).execute();

Unregister a Persona (Your customer)

You **MAY** unregister (or free the email/phone number) your Persona entry using that endpoint. *Please note that* this operation will fail if that Persona have any ongoing operations.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    try {
      apiInstance.apiPersonasIdDelete(id)
            .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Persona identifier | |

### Return type

null (empty response body)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Persona resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdGet"></a>
# **apiPersonasIdGet**
> PersonaRead apiPersonasIdGet(id).execute();

Retrieves a Persona resource.

Retrieves a Persona resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    try {
      PersonaRead result = apiInstance.apiPersonasIdGet(id)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Persona identifier | |

### Return type

[**PersonaRead**](PersonaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Persona resource |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdPatch"></a>
# **apiPersonasIdPatch**
> PersonaRead apiPersonasIdPatch(id, personaUpdate).execute();

Updates the Persona resource.

Update your Persona (eg. your customer/user entry) through that API call. _Beware that updating_ **email** and/or the **mobile phone number** must be done using non reserved values. Otherwise this operation will be rejected.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    PersonaUpdate personaUpdate = new PersonaUpdate(); // PersonaUpdate | The updated Persona resource
    try {
      PersonaRead result = apiInstance.apiPersonasIdPatch(id, personaUpdate)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasIdPatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Persona identifier | |
| **personaUpdate** | [**PersonaUpdate**](PersonaUpdate.md)| The updated Persona resource | |

### Return type

[**PersonaRead**](PersonaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Persona resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdtokenPost"></a>
# **apiPersonasIdtokenPost**
> PersonaPostAuthRead apiPersonasIdtokenPost(id, personaTokenWrite).execute();

Issue authenticated URL for single end-user

Without this, your users may be required to pass a MFA challenge even if they are already logged-in from your website. Pass the URL you wish your user access, either a Dispute or Safe-checkout resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    PersonaTokenWrite personaTokenWrite = new PersonaTokenWrite(); // PersonaTokenWrite | The new Persona resource
    try {
      PersonaPostAuthRead result = apiInstance.apiPersonasIdtokenPost(id, personaTokenWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasIdtokenPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Persona identifier | |
| **personaTokenWrite** | [**PersonaTokenWrite**](PersonaTokenWrite.md)| The new Persona resource | |

### Return type

[**PersonaPostAuthRead**](PersonaPostAuthRead.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Persona resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasPost"></a>
# **apiPersonasPost**
> PersonaRead apiPersonasPost(personaWrite).execute();

Register a Persona (Your customer)

You should not register your whole database of users, only those who are concerned by a Safe-checkout or Dispute operation. One Persona entry for your organization can be assigned as a seller or buyer.  **Notes:**   - (i) There is a unique constraint for the mobile phone numbers and email.   - (ii) You will have to issue a DELETE operation on a Persona that withhold a specific phone number or email.   - (iii) You are NOT REQUIRED to provide email OR a mobile phone number but it is highly recommended, if none provided the email will be generated as &#39;{ulid}@your-domain.tld&#39;. In that case, please specify at least one metadata in order to find your entry with ease.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    PersonaWrite personaWrite = new PersonaWrite(); // PersonaWrite | The new Persona resource
    try {
      PersonaRead result = apiInstance.apiPersonasPost(personaWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#apiPersonasPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **personaWrite** | [**PersonaWrite**](PersonaWrite.md)| The new Persona resource | |

### Return type

[**PersonaRead**](PersonaRead.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Persona resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

