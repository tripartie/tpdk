# NotificationApi

All URIs are relative to *https://staging-api.tripartie.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPersonasIdnotificationsGetCollection**](NotificationApi.md#apiPersonasIdnotificationsGetCollection) | **GET** /personas/{id}/notifications | Retrieve pending notifications for Persona |
| [**apiPersonasPersonaIdnotificationsIdPatch**](NotificationApi.md#apiPersonasPersonaIdnotificationsIdPatch) | **PATCH** /personas/{personaId}/notifications/{id} | Mark as read/unread a notification for Persona |
| [**apiUsersIdnotificationsGetCollection**](NotificationApi.md#apiUsersIdnotificationsGetCollection) | **GET** /users/{id}/notifications | Retrieves the collection of Notification resources. |
| [**apiUsersUserIdnotificationsIdPatch**](NotificationApi.md#apiUsersUserIdnotificationsIdPatch) | **PATCH** /users/{userId}/notifications/{id} | Mark as read/unread a notification for User |


<a id="apiPersonasIdnotificationsGetCollection"></a>
# **apiPersonasIdnotificationsGetCollection**
> List&lt;NotificationRead&gt; apiPersonasIdnotificationsGetCollection(id).page(page).execute();

Retrieve pending notifications for Persona

Retrieves the collection of Notification resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String id = "id_example"; // String | Notification identifier
    Integer page = 1; // Integer | The collection page number
    try {
      List<NotificationRead> result = apiInstance.apiPersonasIdnotificationsGetCollection(id)
            .page(page)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#apiPersonasIdnotificationsGetCollection");
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
| **id** | **String**| Notification identifier | |
| **page** | **Integer**| The collection page number | [optional] [default to 1] |

### Return type

[**List&lt;NotificationRead&gt;**](NotificationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiPersonasPersonaIdnotificationsIdPatch"></a>
# **apiPersonasPersonaIdnotificationsIdPatch**
> NotificationRead apiPersonasPersonaIdnotificationsIdPatch(personaId, id, notificationUpdate).execute();

Mark as read/unread a notification for Persona

Updates the Notification resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: personaAuthKey
    ApiKeyAuth personaAuthKey = (ApiKeyAuth) defaultClient.getAuthentication("personaAuthKey");
    personaAuthKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //personaAuthKey.setApiKeyPrefix("Token");

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String personaId = "personaId_example"; // String | Notification identifier
    String id = "id_example"; // String | Notification identifier
    NotificationUpdate notificationUpdate = new NotificationUpdate(); // NotificationUpdate | The updated Notification resource
    try {
      NotificationRead result = apiInstance.apiPersonasPersonaIdnotificationsIdPatch(personaId, id, notificationUpdate)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#apiPersonasPersonaIdnotificationsIdPatch");
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
| **personaId** | **String**| Notification identifier | |
| **id** | **String**| Notification identifier | |
| **notificationUpdate** | [**NotificationUpdate**](NotificationUpdate.md)| The updated Notification resource | |

### Return type

[**NotificationRead**](NotificationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiUsersIdnotificationsGetCollection"></a>
# **apiUsersIdnotificationsGetCollection**
> List&lt;NotificationRead&gt; apiUsersIdnotificationsGetCollection(id).page(page).execute();

Retrieves the collection of Notification resources.

Retrieves the collection of Notification resources.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.NotificationApi;

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

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String id = "id_example"; // String | Notification identifier
    Integer page = 1; // Integer | The collection page number
    try {
      List<NotificationRead> result = apiInstance.apiUsersIdnotificationsGetCollection(id)
            .page(page)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#apiUsersIdnotificationsGetCollection");
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
| **id** | **String**| Notification identifier | |
| **page** | **Integer**| The collection page number | [optional] [default to 1] |

### Return type

[**List&lt;NotificationRead&gt;**](NotificationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

<a id="apiUsersUserIdnotificationsIdPatch"></a>
# **apiUsersUserIdnotificationsIdPatch**
> NotificationRead apiUsersUserIdnotificationsIdPatch(userId, id, notificationUpdate).execute();

Mark as read/unread a notification for User

Updates the Notification resource.

### Example
```java
// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    NotificationApi apiInstance = new NotificationApi(defaultClient);
    String userId = "userId_example"; // String | Notification identifier
    String id = "id_example"; // String | Notification identifier
    NotificationUpdate notificationUpdate = new NotificationUpdate(); // NotificationUpdate | The updated Notification resource
    try {
      NotificationRead result = apiInstance.apiUsersUserIdnotificationsIdPatch(userId, id, notificationUpdate)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationApi#apiUsersUserIdnotificationsIdPatch");
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
| **userId** | **String**| Notification identifier | |
| **id** | **String**| Notification identifier | |
| **notificationUpdate** | [**NotificationUpdate**](NotificationUpdate.md)| The updated Notification resource | |

### Return type

[**NotificationRead**](NotificationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
| **401** | Authentication required |  -  |
| **403** | Unauthorized access |  -  |
| **429** | Rate limit exhausted |  -  |
| **500** | Unexpected server error |  -  |

