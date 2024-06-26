# ResolutionCenterApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDisputesGetCollection**](ResolutionCenterApi.md#apiDisputesGetCollection) | **GET** /disputes | Retrieves the collection of Dispute resources. |
| [**apiDisputesPost**](ResolutionCenterApi.md#apiDisputesPost) | **POST** /disputes | Draft a standalone Dispute |
| [**apiDisputesUlidDelete**](ResolutionCenterApi.md#apiDisputesUlidDelete) | **DELETE** /disputes/{ulid} | Abandon claims on Dispute |
| [**apiDisputesUlidGet**](ResolutionCenterApi.md#apiDisputesUlidGet) | **GET** /disputes/{ulid} | Retrieves a Dispute resource. |
| [**apiDisputesUlidPatch**](ResolutionCenterApi.md#apiDisputesUlidPatch) | **PATCH** /disputes/{ulid} | Update the Dispute |
| [**apiDisputesUlidevaluationsPost**](ResolutionCenterApi.md#apiDisputesUlidevaluationsPost) | **POST** /disputes/{ulid}/evaluations | Submit an Evaluation for the Dispute |
| [**apiDisputesUlidevidencesGetCollection**](ResolutionCenterApi.md#apiDisputesUlidevidencesGetCollection) | **GET** /disputes/{ulid}/evidences | Retrieve all Evidences in Dispute |
| [**apiDisputesUlidevidencesIdDelete**](ResolutionCenterApi.md#apiDisputesUlidevidencesIdDelete) | **DELETE** /disputes/{ulid}/evidences/{id} | Withdraw an Evidence from a Dispute |
| [**apiDisputesUlidevidencesIdmediaPost**](ResolutionCenterApi.md#apiDisputesUlidevidencesIdmediaPost) | **POST** /disputes/{ulid}/evidences/{id}/media | Upload attachment in regard of described Evidence |
| [**apiDisputesUlidevidencesPost**](ResolutionCenterApi.md#apiDisputesUlidevidencesPost) | **POST** /disputes/{ulid}/evidences | Submit an Evidence to the Dispute case |
| [**apiDisputesUlidparcelsGetCollection**](ResolutionCenterApi.md#apiDisputesUlidparcelsGetCollection) | **GET** /disputes/{ulid}/parcels | Retrieves the collection of Parcel resources. |
| [**apiDisputesUlidparcelsIdDelete**](ResolutionCenterApi.md#apiDisputesUlidparcelsIdDelete) | **DELETE** /disputes/{ulid}/parcels/{id} | Removes the Parcel resource. |
| [**apiDisputesUlidparcelsPost**](ResolutionCenterApi.md#apiDisputesUlidparcelsPost) | **POST** /disputes/{ulid}/parcels | Creates a Parcel resource. |
| [**apiOffersUlidmediasIdDelete**](ResolutionCenterApi.md#apiOffersUlidmediasIdDelete) | **DELETE** /offers/{ulid}/medias/{id} | Removes the Media resource. |
| [**apiOffersUlidmediasPost**](ResolutionCenterApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer |


<a id="apiDisputesGetCollection"></a>
# **apiDisputesGetCollection**
> List&lt;DisputeCollectionRead&gt; apiDisputesGetCollection().page(page).orderCreatedAt(orderCreatedAt).orderStatus(orderStatus).orderUpdatedAt(orderUpdatedAt).transactionOfferPublicUrl(transactionOfferPublicUrl).transactionOfferPublicUrl2(transactionOfferPublicUrl2).transactionOfferTitle(transactionOfferTitle).transactionBuyerId(transactionBuyerId).transactionBuyerId2(transactionBuyerId2).transactionBuyerEmail(transactionBuyerEmail).transactionOfferSellerId(transactionOfferSellerId).transactionOfferSellerId2(transactionOfferSellerId2).transactionOfferSellerEmail(transactionOfferSellerEmail).createdAtBefore(createdAtBefore).createdAtStrictlyBefore(createdAtStrictlyBefore).createdAtAfter(createdAtAfter).createdAtStrictlyAfter(createdAtStrictlyAfter).status(status).transactionStatus(transactionStatus).existsRecommendedSolution(existsRecommendedSolution).existsChosenSolution(existsChosenSolution).existsCounterSolution(existsCounterSolution).existsPlatformSolution(existsPlatformSolution).metadata(metadata).transactionMetadata(transactionMetadata).transactionOfferMetadata(transactionOfferMetadata).execute();

Retrieves the collection of Dispute resources.

Retrieves the collection of Dispute resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String orderCreatedAt = "asc"; // String | 
    String orderStatus = "asc"; // String | 
    String orderUpdatedAt = "asc"; // String | 
    String transactionOfferPublicUrl = "transactionOfferPublicUrl_example"; // String | 
    List<String> transactionOfferPublicUrl2 = Arrays.asList(); // List<String> | 
    String transactionOfferTitle = "transactionOfferTitle_example"; // String | 
    Integer transactionBuyerId = 56; // Integer | 
    List<Integer> transactionBuyerId2 = Arrays.asList(); // List<Integer> | 
    String transactionBuyerEmail = "transactionBuyerEmail_example"; // String | 
    Integer transactionOfferSellerId = 56; // Integer | 
    List<Integer> transactionOfferSellerId2 = Arrays.asList(); // List<Integer> | 
    String transactionOfferSellerEmail = "transactionOfferSellerEmail_example"; // String | 
    String createdAtBefore = "createdAtBefore_example"; // String | 
    String createdAtStrictlyBefore = "createdAtStrictlyBefore_example"; // String | 
    String createdAtAfter = "createdAtAfter_example"; // String | 
    String createdAtStrictlyAfter = "createdAtStrictlyAfter_example"; // String | 
    String status = "CREATED"; // String | Filter on a limited subset of status
    String transactionStatus = "CREATED"; // String | Filter on a limited subset of transaction.status
    Boolean existsRecommendedSolution = true; // Boolean | 
    Boolean existsChosenSolution = true; // Boolean | 
    Boolean existsCounterSolution = true; // Boolean | 
    Boolean existsPlatformSolution = true; // Boolean | 
    List<String> metadata = Arrays.asList(new ArrayList<>()); // List<String> | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    List<String> transactionMetadata = Arrays.asList(new ArrayList<>()); // List<String> | Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    List<String> transactionOfferMetadata = Arrays.asList(new ArrayList<>()); // List<String> | Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value.
    try {
      List<DisputeCollectionRead> result = apiInstance.apiDisputesGetCollection()
            .page(page)
            .orderCreatedAt(orderCreatedAt)
            .orderStatus(orderStatus)
            .orderUpdatedAt(orderUpdatedAt)
            .transactionOfferPublicUrl(transactionOfferPublicUrl)
            .transactionOfferPublicUrl2(transactionOfferPublicUrl2)
            .transactionOfferTitle(transactionOfferTitle)
            .transactionBuyerId(transactionBuyerId)
            .transactionBuyerId2(transactionBuyerId2)
            .transactionBuyerEmail(transactionBuyerEmail)
            .transactionOfferSellerId(transactionOfferSellerId)
            .transactionOfferSellerId2(transactionOfferSellerId2)
            .transactionOfferSellerEmail(transactionOfferSellerEmail)
            .createdAtBefore(createdAtBefore)
            .createdAtStrictlyBefore(createdAtStrictlyBefore)
            .createdAtAfter(createdAtAfter)
            .createdAtStrictlyAfter(createdAtStrictlyAfter)
            .status(status)
            .transactionStatus(transactionStatus)
            .existsRecommendedSolution(existsRecommendedSolution)
            .existsChosenSolution(existsChosenSolution)
            .existsCounterSolution(existsCounterSolution)
            .existsPlatformSolution(existsPlatformSolution)
            .metadata(metadata)
            .transactionMetadata(transactionMetadata)
            .transactionOfferMetadata(transactionOfferMetadata)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesGetCollection");
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
| **orderCreatedAt** | **String**|  | [optional] [enum: asc, desc] |
| **orderStatus** | **String**|  | [optional] [enum: asc, desc] |
| **orderUpdatedAt** | **String**|  | [optional] [enum: asc, desc] |
| **transactionOfferPublicUrl** | **String**|  | [optional] |
| **transactionOfferPublicUrl2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **transactionOfferTitle** | **String**|  | [optional] |
| **transactionBuyerId** | **Integer**|  | [optional] |
| **transactionBuyerId2** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **transactionBuyerEmail** | **String**|  | [optional] |
| **transactionOfferSellerId** | **Integer**|  | [optional] |
| **transactionOfferSellerId2** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **transactionOfferSellerEmail** | **String**|  | [optional] |
| **createdAtBefore** | **String**|  | [optional] |
| **createdAtStrictlyBefore** | **String**|  | [optional] |
| **createdAtAfter** | **String**|  | [optional] |
| **createdAtStrictlyAfter** | **String**|  | [optional] |
| **status** | **String**| Filter on a limited subset of status | [optional] [enum: CREATED, SUBMITTED, OPENED, ABANDONED, OBJECTED, PENDING_SHIPMENT, SHIPPED, IN_TRANSIT, RETURNED, DISMISSED, RESOLVED, PENDING] |
| **transactionStatus** | **String**| Filter on a limited subset of transaction.status | [optional] [enum: CREATED, AUTHORIZED, REFUSED, ACCEPTED, SHIPPED, IN_TRANSIT, DELIVERED, COMPLETED, DISPUTED] |
| **existsRecommendedSolution** | **Boolean**|  | [optional] |
| **existsChosenSolution** | **Boolean**|  | [optional] |
| **existsCounterSolution** | **Boolean**|  | [optional] |
| **existsPlatformSolution** | **Boolean**|  | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **transactionMetadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |
| **transactionOfferMetadata** | [**List&lt;String&gt;**](String.md)| Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] |

### Return type

[**List&lt;DisputeCollectionRead&gt;**](DisputeCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dispute collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiDisputesPost"></a>
# **apiDisputesPost**
> DisputePostCreationRead apiDisputesPost(disputeIndependentWrite).execute();

Draft a standalone Dispute

Create a draft dispute to be filled by an alleged aggrieved customer. Do not use that endpoint if the transaction took place using our safe-checkout tunnel. This endpoint return a unique URL that can be accessed by both the complainant and seller (if individual).  **Note:** You can generate at your own discretion tokens for both parties, thus avoiding the secondary authentication.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    DisputeIndependentWrite disputeIndependentWrite = new DisputeIndependentWrite(); // DisputeIndependentWrite | The new Dispute resource
    try {
      DisputePostCreationRead result = apiInstance.apiDisputesPost(disputeIndependentWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesPost");
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
| **disputeIndependentWrite** | [**DisputeIndependentWrite**](DisputeIndependentWrite.md)| The new Dispute resource | |

### Return type

[**DisputePostCreationRead**](DisputePostCreationRead.md)

### Authorization

[oauth](../README.md#oauth)

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

<a id="apiDisputesUlidDelete"></a>
# **apiDisputesUlidDelete**
> apiDisputesUlidDelete(ulid).execute();

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
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | Dispute identifier
    try {
      apiInstance.apiDisputesUlidDelete(ulid)
            .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidDelete");
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

<a id="apiDisputesUlidGet"></a>
# **apiDisputesUlidGet**
> DisputeRead apiDisputesUlidGet(ulid).execute();

Retrieves a Dispute resource.

Retrieves a Dispute resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | Dispute identifier
    try {
      DisputeRead result = apiInstance.apiDisputesUlidGet(ulid)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidGet");
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

<a id="apiDisputesUlidPatch"></a>
# **apiDisputesUlidPatch**
> DisputeRead apiDisputesUlidPatch(ulid, disputeUpdate).execute();

Update the Dispute

Updates the Dispute resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | Dispute identifier
    DisputeUpdate disputeUpdate = new DisputeUpdate(); // DisputeUpdate | The updated Dispute resource
    try {
      DisputeRead result = apiInstance.apiDisputesUlidPatch(ulid, disputeUpdate)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidPatch");
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
| **disputeUpdate** | [**DisputeUpdate**](DisputeUpdate.md)| The updated Dispute resource | |

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

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

<a id="apiDisputesUlidevaluationsPost"></a>
# **apiDisputesUlidevaluationsPost**
> EvaluationRead apiDisputesUlidevaluationsPost(ulid, evaluationWrite).execute();

Submit an Evaluation for the Dispute

**Only authenticated** complainant and seller **CAN** issue an evaluation **WHEN** the dispute reached a final state.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | Evaluation identifier
    EvaluationWrite evaluationWrite = new EvaluationWrite(); // EvaluationWrite | The new Evaluation resource
    try {
      EvaluationRead result = apiInstance.apiDisputesUlidevaluationsPost(ulid, evaluationWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidevaluationsPost");
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
| **ulid** | **String**| Evaluation identifier | |
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

<a id="apiDisputesUlidevidencesGetCollection"></a>
# **apiDisputesUlidevidencesGetCollection**
> List&lt;EvidenceRead&gt; apiDisputesUlidevidencesGetCollection(ulid).execute();

Retrieve all Evidences in Dispute

Retrieves the collection of Evidence resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    try {
      List<EvidenceRead> result = apiInstance.apiDisputesUlidevidencesGetCollection(ulid)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidevidencesGetCollection");
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

### Return type

[**List&lt;EvidenceRead&gt;**](EvidenceRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Evidence collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiDisputesUlidevidencesIdDelete"></a>
# **apiDisputesUlidevidencesIdDelete**
> apiDisputesUlidevidencesIdDelete(ulid, id).execute();

Withdraw an Evidence from a Dispute

Removes the Evidence resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      apiInstance.apiDisputesUlidevidencesIdDelete(ulid, id)
            .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidevidencesIdDelete");
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

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Evidence resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiDisputesUlidevidencesIdmediaPost"></a>
# **apiDisputesUlidevidencesIdmediaPost**
> MediaRead apiDisputesUlidevidencesIdmediaPost(ulid, id)._file(_file).execute();

Upload attachment in regard of described Evidence

Creates a Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    File _file = new File("/path/to/file"); // File | 
    try {
      MediaRead result = apiInstance.apiDisputesUlidevidencesIdmediaPost(ulid, id)
            ._file(_file)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidevidencesIdmediaPost");
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
| **_file** | **File**|  | [optional] |

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

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

<a id="apiDisputesUlidevidencesPost"></a>
# **apiDisputesUlidevidencesPost**
> EvidenceRead apiDisputesUlidevidencesPost(ulid, evidenceWrite).execute();

Submit an Evidence to the Dispute case

This action does not held the actual upload, you will have to do the upload in a dedicated request.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    EvidenceWrite evidenceWrite = new EvidenceWrite(); // EvidenceWrite | The new Evidence resource
    try {
      EvidenceRead result = apiInstance.apiDisputesUlidevidencesPost(ulid, evidenceWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidevidencesPost");
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
| **evidenceWrite** | [**EvidenceWrite**](EvidenceWrite.md)| The new Evidence resource | |

### Return type

[**EvidenceRead**](EvidenceRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Evidence resource created |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiDisputesUlidparcelsGetCollection"></a>
# **apiDisputesUlidparcelsGetCollection**
> List&lt;Object&gt; apiDisputesUlidparcelsGetCollection(ulid).page(page).execute();

Retrieves the collection of Parcel resources.

Retrieves the collection of Parcel resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer page = 1; // Integer | The collection page number
    try {
      List<Object> result = apiInstance.apiDisputesUlidparcelsGetCollection(ulid)
            .page(page)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidparcelsGetCollection");
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

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

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

<a id="apiDisputesUlidparcelsIdDelete"></a>
# **apiDisputesUlidparcelsIdDelete**
> apiDisputesUlidparcelsIdDelete(ulid, id).execute();

Removes the Parcel resource.

Removes the Parcel resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      apiInstance.apiDisputesUlidparcelsIdDelete(ulid, id)
            .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidparcelsIdDelete");
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

<a id="apiDisputesUlidparcelsPost"></a>
# **apiDisputesUlidparcelsPost**
> Object apiDisputesUlidparcelsPost(ulid, parcelWrite).execute();

Creates a Parcel resource.

Creates a Parcel resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    ParcelWrite parcelWrite = new ParcelWrite(); // ParcelWrite | The new Parcel resource
    try {
      Object result = apiInstance.apiDisputesUlidparcelsPost(ulid, parcelWrite)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiDisputesUlidparcelsPost");
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

**Object**

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

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

<a id="apiOffersUlidmediasIdDelete"></a>
# **apiOffersUlidmediasIdDelete**
> apiOffersUlidmediasIdDelete(ulid, id).execute();

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
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      apiInstance.apiOffersUlidmediasIdDelete(ulid, id)
            .execute();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiOffersUlidmediasIdDelete");
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
> MediaRead apiOffersUlidmediasPost(ulid)._file(_file).execute();

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
import com.tripartie.tpdk.api.ResolutionCenterApi;

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

    ResolutionCenterApi apiInstance = new ResolutionCenterApi(defaultClient);
    String ulid = "ulid_example"; // String | 
    File _file = new File("/path/to/file"); // File | 
    try {
      MediaRead result = apiInstance.apiOffersUlidmediasPost(ulid)
            ._file(_file)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResolutionCenterApi#apiOffersUlidmediasPost");
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

