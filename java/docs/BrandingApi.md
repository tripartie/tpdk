# BrandingApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiOrganizationsIdPatch**](BrandingApi.md#apiOrganizationsIdPatch) | **PATCH** /organizations/{id} | Update your Organization details, branding or parameters |
| [**apiOrganizationsIdiconDelete**](BrandingApi.md#apiOrganizationsIdiconDelete) | **DELETE** /organizations/{id}/icon | Unset your Organization Icon |
| [**apiOrganizationsIdiconPost**](BrandingApi.md#apiOrganizationsIdiconPost) | **POST** /organizations/{id}/icon | Upload your Organization Icon |
| [**apiOrganizationsIdlogoDelete**](BrandingApi.md#apiOrganizationsIdlogoDelete) | **DELETE** /organizations/{id}/logo | Unset your Organization Logo |
| [**apiOrganizationsIdlogoPost**](BrandingApi.md#apiOrganizationsIdlogoPost) | **POST** /organizations/{id}/logo | Upload your Organization logo |


<a id="apiOrganizationsIdPatch"></a>
# **apiOrganizationsIdPatch**
> OrganizationRead apiOrganizationsIdPatch(id, organizationUpdate)

Update your Organization details, branding or parameters

Updates the Organization resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    String id = "id_example"; // String | Organization identifier
    OrganizationUpdate organizationUpdate = new OrganizationUpdate(); // OrganizationUpdate | The updated Organization resource
    try {
      OrganizationRead result = apiInstance.apiOrganizationsIdPatch(id, organizationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdPatch");
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
| **organizationUpdate** | [**OrganizationUpdate**](OrganizationUpdate.md)| The updated Organization resource | |

### Return type

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOrganizationsIdiconDelete"></a>
# **apiOrganizationsIdiconDelete**
> apiOrganizationsIdiconDelete(id)

Unset your Organization Icon

Removes the Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    Integer id = 56; // Integer | Organization identifier
    try {
      apiInstance.apiOrganizationsIdiconDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdiconDelete");
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
| **id** | **Integer**| Organization identifier | |

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
| **204** | Media resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOrganizationsIdiconPost"></a>
# **apiOrganizationsIdiconPost**
> MediaRead apiOrganizationsIdiconPost(id, _file)

Upload your Organization Icon

Creates a Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    Integer id = 56; // Integer | Organization identifier
    File _file = new File("/path/to/file"); // File | 
    try {
      MediaRead result = apiInstance.apiOrganizationsIdiconPost(id, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdiconPost");
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
| **id** | **Integer**| Organization identifier | |
| **_file** | **File**|  | [optional] |

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

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

<a id="apiOrganizationsIdlogoDelete"></a>
# **apiOrganizationsIdlogoDelete**
> apiOrganizationsIdlogoDelete(id)

Unset your Organization Logo

Removes the Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    Integer id = 56; // Integer | Organization identifier
    try {
      apiInstance.apiOrganizationsIdlogoDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdlogoDelete");
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
| **id** | **Integer**| Organization identifier | |

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
| **204** | Media resource deleted |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiOrganizationsIdlogoPost"></a>
# **apiOrganizationsIdlogoPost**
> MediaRead apiOrganizationsIdlogoPost(id, _file)

Upload your Organization logo

Creates a Media resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    Integer id = 56; // Integer | Organization identifier
    File _file = new File("/path/to/file"); // File | 
    try {
      MediaRead result = apiInstance.apiOrganizationsIdlogoPost(id, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdlogoPost");
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
| **id** | **Integer**| Organization identifier | |
| **_file** | **File**|  | [optional] |

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

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

