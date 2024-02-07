# OrganizationApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiOrganizationsGetCollection**](OrganizationApi.md#apiOrganizationsGetCollection) | **GET** /organizations | Retrieves the collection of Organization resources. |
| [**apiOrganizationsIdGet**](OrganizationApi.md#apiOrganizationsIdGet) | **GET** /organizations/{id} | Retrieves a Organization resource. |


<a id="apiOrganizationsGetCollection"></a>
# **apiOrganizationsGetCollection**
> List&lt;OrganizationCollectionRead&gt; apiOrganizationsGetCollection(page, itemsPerPage, name)

Retrieves the collection of Organization resources.

Retrieves the collection of Organization resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.OrganizationApi;

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

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    Integer itemsPerPage = 30; // Integer | The number of items per page
    String name = "name_example"; // String | 
    try {
      List<OrganizationCollectionRead> result = apiInstance.apiOrganizationsGetCollection(page, itemsPerPage, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#apiOrganizationsGetCollection");
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
| **itemsPerPage** | **Integer**| The number of items per page | [optional] [default to 30] |
| **name** | **String**|  | [optional] |

### Return type

[**List&lt;OrganizationCollectionRead&gt;**](OrganizationCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOrganizationsIdGet"></a>
# **apiOrganizationsIdGet**
> OrganizationRead apiOrganizationsIdGet(id)

Retrieves a Organization resource.

Retrieves a Organization resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.OrganizationApi;

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

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String id = "id_example"; // String | Organization identifier
    try {
      OrganizationRead result = apiInstance.apiOrganizationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#apiOrganizationsIdGet");
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
| **id** | **String**| Organization identifier | |

### Return type

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization resource |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

