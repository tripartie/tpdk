# SafeCheckoutApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiOffersGetCollection**](SafeCheckoutApi.md#apiOffersGetCollection) | **GET** /offers | Read issued Offers |
| [**apiOffersPost**](SafeCheckoutApi.md#apiOffersPost) | **POST** /offers | Create an Offer and retrieve url |
| [**apiOffersUlidGet**](SafeCheckoutApi.md#apiOffersUlidGet) | **GET** /offers/{ulid} | Read an Offer |
| [**apiOffersUlidmediasIdDelete**](SafeCheckoutApi.md#apiOffersUlidmediasIdDelete) | **DELETE** /offers/{ulid}/medias/{id} | Removes the Media resource. |
| [**apiOffersUlidmediasPost**](SafeCheckoutApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer |
| [**apiOffersUlidtransactionsGetCollection**](SafeCheckoutApi.md#apiOffersUlidtransactionsGetCollection) | **GET** /offers/{ulid}/transactions | Retrieve Payment Intents for Offer |
| [**apiOffersUlidtransactionsIdevaluationsPost**](SafeCheckoutApi.md#apiOffersUlidtransactionsIdevaluationsPost) | **POST** /offers/{ulid}/transactions/{id}/evaluations | Submit an Evaluation for the Offer |
| [**apiOffersUlidtransactionsPost**](SafeCheckoutApi.md#apiOffersUlidtransactionsPost) | **POST** /offers/{ulid}/transactions | Create a Payment Intent for Offer |
| [**apiPersonasIdoffersDelete**](SafeCheckoutApi.md#apiPersonasIdoffersDelete) | **DELETE** /personas/{id}/offers | Revoke an Offer for given Persona |
| [**apiPersonasIdoffersGetCollection**](SafeCheckoutApi.md#apiPersonasIdoffersGetCollection) | **GET** /personas/{id}/offers | List or Search Offers for given Persona |
| [**apiPersonasIdoffersPatch**](SafeCheckoutApi.md#apiPersonasIdoffersPatch) | **PATCH** /personas/{id}/offers | Update an Offer for given Persona |
| [**apiPersonasIdoffersPost**](SafeCheckoutApi.md#apiPersonasIdoffersPost) | **POST** /personas/{id}/offers | Create an Offer for given Persona |
| [**apiTransactionsGetCollection**](SafeCheckoutApi.md#apiTransactionsGetCollection) | **GET** /transactions | Retrieves the collection of Transaction resources. |
| [**apiTransactionsUliddisputeDelete**](SafeCheckoutApi.md#apiTransactionsUliddisputeDelete) | **DELETE** /transactions/{ulid}/dispute | Abandon claims on Dispute |
| [**apiTransactionsUliddisputeGet**](SafeCheckoutApi.md#apiTransactionsUliddisputeGet) | **GET** /transactions/{ulid}/dispute | Read Dispute from existing Transaction |
| [**apiTransactionsUliddisputePatch**](SafeCheckoutApi.md#apiTransactionsUliddisputePatch) | **PATCH** /transactions/{ulid}/dispute | Interact with a Dispute |
| [**apiTransactionsUliddisputePost**](SafeCheckoutApi.md#apiTransactionsUliddisputePost) | **POST** /transactions/{ulid}/dispute | Open a Dispute related to existing Transaction |
| [**apiTransactionsUlidparcelsGetCollection**](SafeCheckoutApi.md#apiTransactionsUlidparcelsGetCollection) | **GET** /transactions/{ulid}/parcels | Read shipments from Transaction |
| [**apiTransactionsUlidparcelsIdDelete**](SafeCheckoutApi.md#apiTransactionsUlidparcelsIdDelete) | **DELETE** /transactions/{ulid}/parcels/{id} | Withdraw shipment from Transaction |
| [**apiTransactionsUlidparcelsPost**](SafeCheckoutApi.md#apiTransactionsUlidparcelsPost) | **POST** /transactions/{ulid}/parcels | Manually declare package shipped for Transaction |


<a id="apiOffersGetCollection"></a>
# **apiOffersGetCollection**
> List&lt;OfferCollectionRead&gt; apiOffersGetCollection(page, title, publicUrl, publicUrl2, unitPrice, unitPrice2, itemCount, itemCount2, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, metadata, offerMetadata, nature, condition, shippingAllowed)

Read issued Offers

Retrieves the collection of Offer resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String title = "title_example"; // String | 
    String publicUrl = "publicUrl_example"; // String | 
    List<String> publicUrl2 = Arrays.asList(); // List<String> | 
    BigDecimal unitPrice = new BigDecimal(78); // BigDecimal | 
    List<BigDecimal> unitPrice2 = Arrays.asList(); // List<BigDecimal> | 
    Integer itemCount = 56; // Integer | 
    List<Integer> itemCount2 = Arrays.asList(); // List<Integer> | 
    String createdAtBefore = "createdAtBefore_example"; // String | 
    String createdAtStrictlyBefore = "createdAtStrictlyBefore_example"; // String | 
    String createdAtAfter = "createdAtAfter_example"; // String | 
    String createdAtStrictlyAfter = "createdAtStrictlyAfter_example"; // String | 
    List<String> metadata = Arrays.asList(); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    List<String> offerMetadata = Arrays.asList(); // List<String> | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    String nature = "service"; // String | Filter on a limited subset of nature
    String condition = "NEW"; // String | Filter on a limited subset of condition
    Boolean shippingAllowed = true; // Boolean | 
    try {
      List<OfferCollectionRead> result = apiInstance.apiOffersGetCollection(page, title, publicUrl, publicUrl2, unitPrice, unitPrice2, itemCount, itemCount2, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, metadata, offerMetadata, nature, condition, shippingAllowed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersGetCollection");
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
| **title** | **String**|  | [optional] |
| **publicUrl** | **String**|  | [optional] |
| **publicUrl2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **unitPrice** | **BigDecimal**|  | [optional] |
| **unitPrice2** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)|  | [optional] |
| **itemCount** | **Integer**|  | [optional] |
| **itemCount2** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **createdAtBefore** | **String**|  | [optional] |
| **createdAtStrictlyBefore** | **String**|  | [optional] |
| **createdAtAfter** | **String**|  | [optional] |
| **createdAtStrictlyAfter** | **String**|  | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **offerMetadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **nature** | **String**| Filter on a limited subset of nature | [optional] [enum: service, physical_item, dematerialized_item, rent_item] |
| **condition** | **String**| Filter on a limited subset of condition | [optional] [enum: NEW, USED, DAMAGED, DETERIORATED, UNRECOVERABLE] |
| **shippingAllowed** | **Boolean**|  | [optional] |

### Return type

[**List&lt;OfferCollectionRead&gt;**](OfferCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersPost"></a>
# **apiOffersPost**
> OfferPostCreationRead apiOffersPost(offerIndependentWrite)

Create an Offer and retrieve url

Publish an offer so that you can safely retrieve a safe-checkout unique link from us

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    OfferIndependentWrite offerIndependentWrite = new OfferIndependentWrite(); // OfferIndependentWrite | The new Offer resource
    try {
      OfferPostCreationRead result = apiInstance.apiOffersPost(offerIndependentWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersPost");
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
| **offerIndependentWrite** | [**OfferIndependentWrite**](OfferIndependentWrite.md)| The new Offer resource | |

### Return type

[**OfferPostCreationRead**](OfferPostCreationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Offer resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidGet"></a>
# **apiOffersUlidGet**
> OfferRead apiOffersUlidGet(ulid)

Read an Offer

Retrieves a Offer resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Offer identifier
    try {
      OfferRead result = apiInstance.apiOffersUlidGet(ulid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidGet");
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
| **ulid** | **String**| Offer identifier | |

### Return type

[**OfferRead**](OfferRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer resource |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidmediasIdDelete"></a>
# **apiOffersUlidmediasIdDelete**
> apiOffersUlidmediasIdDelete(ulid, id)

Removes the Media resource.

Removes the Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      apiInstance.apiOffersUlidmediasIdDelete(ulid, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidmediasIdDelete");
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
| **ulid** | **String**|  | |
| **id** | **Integer**|  | |

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
| **204** | Media resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidmediasPost"></a>
# **apiOffersUlidmediasPost**
> MediaRead apiOffersUlidmediasPost(ulid, _file)

Upload a picture for a given Offer

Creates a Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    File _file = new File("/path/to/file"); // File | 
    try {
      MediaRead result = apiInstance.apiOffersUlidmediasPost(ulid, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidmediasPost");
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
| **ulid** | **String**|  | |
| **_file** | **File**|  | [optional] |

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Media resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidtransactionsGetCollection"></a>
# **apiOffersUlidtransactionsGetCollection**
> List&lt;TransactionCollectionRead&gt; apiOffersUlidtransactionsGetCollection(ulid, page, orderStatus, metadata, status)

Retrieve Payment Intents for Offer

Retrieves the collection of Transaction resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Offer identifier
    Integer page = 1; // Integer | The collection page number
    String orderStatus = "asc"; // String | 
    List<String> metadata = Arrays.asList(); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    String status = "CREATED"; // String | Filter on a limited subset of status
    try {
      List<TransactionCollectionRead> result = apiInstance.apiOffersUlidtransactionsGetCollection(ulid, page, orderStatus, metadata, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidtransactionsGetCollection");
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
| **ulid** | **String**| Offer identifier | |
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **orderStatus** | **String**|  | [optional] [enum: asc, desc] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **status** | **String**| Filter on a limited subset of status | [optional] [enum: CREATED, AUTHORIZED, REFUSED, ACCEPTED, SHIPPED, IN_TRANSIT, DELIVERED, COMPLETED, DISPUTED] |

### Return type

[**List&lt;TransactionCollectionRead&gt;**](TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidtransactionsIdevaluationsPost"></a>
# **apiOffersUlidtransactionsIdevaluationsPost**
> EvaluationRead apiOffersUlidtransactionsIdevaluationsPost(ulid, id, evaluationWrite)

Submit an Evaluation for the Offer

**Only authenticated** buyer and seller **CAN** issue an evaluation **WHEN** the transaction reached a final state.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Dispute identifier
    String id = "id_example"; // String | Transaction identifier
    EvaluationWrite evaluationWrite = new EvaluationWrite(); // EvaluationWrite | The new Evaluation resource
    try {
      EvaluationRead result = apiInstance.apiOffersUlidtransactionsIdevaluationsPost(ulid, id, evaluationWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidtransactionsIdevaluationsPost");
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
| **ulid** | **String**| Dispute identifier | |
| **id** | **String**| Transaction identifier | |
| **evaluationWrite** | [**EvaluationWrite**](EvaluationWrite.md)| The new Evaluation resource | |

### Return type

[**EvaluationRead**](EvaluationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Evaluation resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOffersUlidtransactionsPost"></a>
# **apiOffersUlidtransactionsPost**
> TransactionRead apiOffersUlidtransactionsPost(ulid, body)

Create a Payment Intent for Offer

Cannot be used outside of a Persona (buyer)

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Offer identifier
    Object body = null; // Object | The new Transaction resource
    try {
      TransactionRead result = apiInstance.apiOffersUlidtransactionsPost(ulid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiOffersUlidtransactionsPost");
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
| **ulid** | **String**| Offer identifier | |
| **body** | **Object**| The new Transaction resource | |

### Return type

[**TransactionRead**](TransactionRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdoffersDelete"></a>
# **apiPersonasIdoffersDelete**
> apiPersonasIdoffersDelete(id)

Revoke an Offer for given Persona

That goes without says, if that **Offer** have a _Transaction_ **that is ongoing**, you **MAY NOT** revoke the **Offer**.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    try {
      apiInstance.apiPersonasIdoffersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiPersonasIdoffersDelete");
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
| **204** | Offer resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdoffersGetCollection"></a>
# **apiPersonasIdoffersGetCollection**
> List&lt;OfferCollectionRead&gt; apiPersonasIdoffersGetCollection(id, page, title, publicUrl, publicUrl2, unitPrice, unitPrice2, itemCount, itemCount2, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, metadata, offerMetadata, nature, condition, shippingAllowed)

List or Search Offers for given Persona

Retrieves the collection of Offer resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    Integer page = 1; // Integer | The collection page number
    String title = "title_example"; // String | 
    String publicUrl = "publicUrl_example"; // String | 
    List<String> publicUrl2 = Arrays.asList(); // List<String> | 
    BigDecimal unitPrice = new BigDecimal(78); // BigDecimal | 
    List<BigDecimal> unitPrice2 = Arrays.asList(); // List<BigDecimal> | 
    Integer itemCount = 56; // Integer | 
    List<Integer> itemCount2 = Arrays.asList(); // List<Integer> | 
    String createdAtBefore = "createdAtBefore_example"; // String | 
    String createdAtStrictlyBefore = "createdAtStrictlyBefore_example"; // String | 
    String createdAtAfter = "createdAtAfter_example"; // String | 
    String createdAtStrictlyAfter = "createdAtStrictlyAfter_example"; // String | 
    List<String> metadata = Arrays.asList(); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    List<String> offerMetadata = Arrays.asList(); // List<String> | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    String nature = "service"; // String | Filter on a limited subset of nature
    String condition = "NEW"; // String | Filter on a limited subset of condition
    Boolean shippingAllowed = true; // Boolean | 
    try {
      List<OfferCollectionRead> result = apiInstance.apiPersonasIdoffersGetCollection(id, page, title, publicUrl, publicUrl2, unitPrice, unitPrice2, itemCount, itemCount2, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, metadata, offerMetadata, nature, condition, shippingAllowed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiPersonasIdoffersGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **title** | **String**|  | [optional] |
| **publicUrl** | **String**|  | [optional] |
| **publicUrl2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **unitPrice** | **BigDecimal**|  | [optional] |
| **unitPrice2** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)|  | [optional] |
| **itemCount** | **Integer**|  | [optional] |
| **itemCount2** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **createdAtBefore** | **String**|  | [optional] |
| **createdAtStrictlyBefore** | **String**|  | [optional] |
| **createdAtAfter** | **String**|  | [optional] |
| **createdAtStrictlyAfter** | **String**|  | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **offerMetadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **nature** | **String**| Filter on a limited subset of nature | [optional] [enum: service, physical_item, dematerialized_item, rent_item] |
| **condition** | **String**| Filter on a limited subset of condition | [optional] [enum: NEW, USED, DAMAGED, DETERIORATED, UNRECOVERABLE] |
| **shippingAllowed** | **Boolean**|  | [optional] |

### Return type

[**List&lt;OfferCollectionRead&gt;**](OfferCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdoffersPatch"></a>
# **apiPersonasIdoffersPatch**
> OfferRead apiPersonasIdoffersPatch(id, offerUpdate)

Update an Offer for given Persona

Updates the Offer resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    OfferUpdate offerUpdate = new OfferUpdate(); // OfferUpdate | The updated Offer resource
    try {
      OfferRead result = apiInstance.apiPersonasIdoffersPatch(id, offerUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiPersonasIdoffersPatch");
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
| **offerUpdate** | [**OfferUpdate**](OfferUpdate.md)| The updated Offer resource | |

### Return type

[**OfferRead**](OfferRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasIdoffersPost"></a>
# **apiPersonasIdoffersPost**
> OfferPostCreationRead apiPersonasIdoffersPost(id, offerWrite)

Create an Offer for given Persona

Creates a Offer resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String id = "id_example"; // String | Persona identifier
    OfferWrite offerWrite = new OfferWrite(); // OfferWrite | The new Offer resource
    try {
      OfferPostCreationRead result = apiInstance.apiPersonasIdoffersPost(id, offerWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiPersonasIdoffersPost");
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
| **offerWrite** | [**OfferWrite**](OfferWrite.md)| The new Offer resource | |

### Return type

[**OfferPostCreationRead**](OfferPostCreationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Offer resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsGetCollection"></a>
# **apiTransactionsGetCollection**
> List&lt;TransactionCollectionRead&gt; apiTransactionsGetCollection(page, orderStatus, metadata, status)

Retrieves the collection of Transaction resources.

Retrieves the collection of Transaction resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String orderStatus = "asc"; // String | 
    List<String> metadata = Arrays.asList(); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    String status = "CREATED"; // String | Filter on a limited subset of status
    try {
      List<TransactionCollectionRead> result = apiInstance.apiTransactionsGetCollection(page, orderStatus, metadata, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsGetCollection");
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
| **orderStatus** | **String**|  | [optional] [enum: asc, desc] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **status** | **String**| Filter on a limited subset of status | [optional] [enum: CREATED, AUTHORIZED, REFUSED, ACCEPTED, SHIPPED, IN_TRANSIT, DELIVERED, COMPLETED, DISPUTED] |

### Return type

[**List&lt;TransactionCollectionRead&gt;**](TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUliddisputeDelete"></a>
# **apiTransactionsUliddisputeDelete**
> apiTransactionsUliddisputeDelete(ulid)

Abandon claims on Dispute

**Only the buyer/complainant** can dismiss the case immediately. Otherwise, the support can but in a limited ranges of Dispute status.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Transaction identifier
    try {
      apiInstance.apiTransactionsUliddisputeDelete(ulid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUliddisputeDelete");
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
| **ulid** | **String**| Transaction identifier | |

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
| **204** | Dispute resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUliddisputeGet"></a>
# **apiTransactionsUliddisputeGet**
> DisputeRead apiTransactionsUliddisputeGet(ulid)

Read Dispute from existing Transaction

Retrieves a Dispute resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Transaction identifier
    try {
      DisputeRead result = apiInstance.apiTransactionsUliddisputeGet(ulid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUliddisputeGet");
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
| **ulid** | **String**| Transaction identifier | |

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dispute resource |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUliddisputePatch"></a>
# **apiTransactionsUliddisputePatch**
> DisputeRead apiTransactionsUliddisputePatch(ulid, disputeUpdate)

Interact with a Dispute

Only authenticated Persona can interact with a Dispute object. Usually through our web application.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Transaction identifier
    DisputeUpdate disputeUpdate = new DisputeUpdate(); // DisputeUpdate | The updated Dispute resource
    try {
      DisputeRead result = apiInstance.apiTransactionsUliddisputePatch(ulid, disputeUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUliddisputePatch");
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
| **ulid** | **String**| Transaction identifier | |
| **disputeUpdate** | [**DisputeUpdate**](DisputeUpdate.md)| The updated Dispute resource | |

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dispute resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUliddisputePost"></a>
# **apiTransactionsUliddisputePost**
> DisputePostCreationRead apiTransactionsUliddisputePost(ulid, disputeWrite)

Open a Dispute related to existing Transaction

Creates a Dispute resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | Transaction identifier
    DisputeWrite disputeWrite = new DisputeWrite(); // DisputeWrite | The new Dispute resource
    try {
      DisputePostCreationRead result = apiInstance.apiTransactionsUliddisputePost(ulid, disputeWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUliddisputePost");
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
| **ulid** | **String**| Transaction identifier | |
| **disputeWrite** | [**DisputeWrite**](DisputeWrite.md)| The new Dispute resource | |

### Return type

[**DisputePostCreationRead**](DisputePostCreationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Dispute resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUlidparcelsGetCollection"></a>
# **apiTransactionsUlidparcelsGetCollection**
> List&lt;Object&gt; apiTransactionsUlidparcelsGetCollection(ulid, page)

Read shipments from Transaction

Retrieves the collection of Parcel resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer page = 1; // Integer | The collection page number
    try {
      List<Object> result = apiInstance.apiTransactionsUlidparcelsGetCollection(ulid, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUlidparcelsGetCollection");
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
| **ulid** | **String**|  | |
| **page** | **Integer**| The collection page number | [optional] [default to 1] |

### Return type

**List&lt;Object&gt;**

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Parcel collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUlidparcelsIdDelete"></a>
# **apiTransactionsUlidparcelsIdDelete**
> apiTransactionsUlidparcelsIdDelete(ulid, id)

Withdraw shipment from Transaction

No one except the support can do that manoeuvre.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      apiInstance.apiTransactionsUlidparcelsIdDelete(ulid, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUlidparcelsIdDelete");
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
| **ulid** | **String**|  | |
| **id** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Parcel resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiTransactionsUlidparcelsPost"></a>
# **apiTransactionsUlidparcelsPost**
> ParcelRead apiTransactionsUlidparcelsPost(ulid, parcelWrite)

Manually declare package shipped for Transaction

Creates a Parcel resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.SafeCheckoutApi;

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

    SafeCheckoutApi apiInstance = new SafeCheckoutApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    ParcelWrite parcelWrite = new ParcelWrite(); // ParcelWrite | The new Parcel resource
    try {
      ParcelRead result = apiInstance.apiTransactionsUlidparcelsPost(ulid, parcelWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SafeCheckoutApi#apiTransactionsUlidparcelsPost");
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
| **ulid** | **String**|  | |
| **parcelWrite** | [**ParcelWrite**](ParcelWrite.md)| The new Parcel resource | |

### Return type

[**ParcelRead**](ParcelRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Parcel resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

