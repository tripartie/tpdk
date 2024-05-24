# tpdk.NotificationApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_personas_idnotifications_get_collection**](NotificationApi.md#api_personas_idnotifications_get_collection) | **GET** /personas/{id}/notifications | Retrieve pending notifications for Persona
[**api_personas_persona_idnotifications_id_patch**](NotificationApi.md#api_personas_persona_idnotifications_id_patch) | **PATCH** /personas/{personaId}/notifications/{id} | Mark as read/unread a notification for Persona
[**api_users_idnotifications_get_collection**](NotificationApi.md#api_users_idnotifications_get_collection) | **GET** /users/{id}/notifications | Retrieves the collection of Notification resources.
[**api_users_user_idnotifications_id_patch**](NotificationApi.md#api_users_user_idnotifications_id_patch) | **PATCH** /users/{userId}/notifications/{id} | Mark as read/unread a notification for User


# **api_personas_idnotifications_get_collection**
> List[NotificationRead] api_personas_idnotifications_get_collection(id, page=page)

Retrieve pending notifications for Persona

Retrieves the collection of Notification resources.

### Example

* Api Key Authentication (personaAuthKey):

```python
import tpdk
from tpdk.models.notification_read import NotificationRead
from tpdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.tripartie.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tpdk.Configuration(
    host = "https://staging-api.tripartie.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.NotificationApi(api_client)
    id = 'id_example' # str | Notification identifier
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieve pending notifications for Persona
        api_response = api_instance.api_personas_idnotifications_get_collection(id, page=page)
        print("The response of NotificationApi->api_personas_idnotifications_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->api_personas_idnotifications_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Notification identifier | 
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[NotificationRead]**](NotificationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
**401** | Authentication required |  -  |
**403** | Unauthorized access |  -  |
**429** | Rate limit exhausted |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personas_persona_idnotifications_id_patch**
> NotificationRead api_personas_persona_idnotifications_id_patch(persona_id, id, notification_update)

Mark as read/unread a notification for Persona

Updates the Notification resource.

### Example

* Api Key Authentication (personaAuthKey):

```python
import tpdk
from tpdk.models.notification_read import NotificationRead
from tpdk.models.notification_update import NotificationUpdate
from tpdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.tripartie.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tpdk.Configuration(
    host = "https://staging-api.tripartie.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.NotificationApi(api_client)
    persona_id = 'persona_id_example' # str | Notification identifier
    id = 'id_example' # str | Notification identifier
    notification_update = tpdk.NotificationUpdate() # NotificationUpdate | The updated Notification resource

    try:
        # Mark as read/unread a notification for Persona
        api_response = api_instance.api_personas_persona_idnotifications_id_patch(persona_id, id, notification_update)
        print("The response of NotificationApi->api_personas_persona_idnotifications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->api_personas_persona_idnotifications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona_id** | **str**| Notification identifier | 
 **id** | **str**| Notification identifier | 
 **notification_update** | [**NotificationUpdate**](NotificationUpdate.md)| The updated Notification resource | 

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
**200** | Notification resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**401** | Authentication required |  -  |
**403** | Unauthorized access |  -  |
**429** | Rate limit exhausted |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_idnotifications_get_collection**
> List[NotificationRead] api_users_idnotifications_get_collection(id, page=page)

Retrieves the collection of Notification resources.

Retrieves the collection of Notification resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):

```python
import tpdk
from tpdk.models.notification_read import NotificationRead
from tpdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.tripartie.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tpdk.Configuration(
    host = "https://staging-api.tripartie.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwtPersonalKey
configuration.api_key['jwtPersonalKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwtPersonalKey'] = 'Bearer'

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.NotificationApi(api_client)
    id = 'id_example' # str | Notification identifier
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Notification resources.
        api_response = api_instance.api_users_idnotifications_get_collection(id, page=page)
        print("The response of NotificationApi->api_users_idnotifications_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->api_users_idnotifications_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Notification identifier | 
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[NotificationRead]**](NotificationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification collection |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |
**429** | Rate limit exhausted |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_idnotifications_id_patch**
> NotificationRead api_users_user_idnotifications_id_patch(user_id, id, notification_update)

Mark as read/unread a notification for User

Updates the Notification resource.

### Example

* Api Key Authentication (jwtPersonalKey):

```python
import tpdk
from tpdk.models.notification_read import NotificationRead
from tpdk.models.notification_update import NotificationUpdate
from tpdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging-api.tripartie.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tpdk.Configuration(
    host = "https://staging-api.tripartie.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwtPersonalKey
configuration.api_key['jwtPersonalKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwtPersonalKey'] = 'Bearer'

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.NotificationApi(api_client)
    user_id = 'user_id_example' # str | Notification identifier
    id = 'id_example' # str | Notification identifier
    notification_update = tpdk.NotificationUpdate() # NotificationUpdate | The updated Notification resource

    try:
        # Mark as read/unread a notification for User
        api_response = api_instance.api_users_user_idnotifications_id_patch(user_id, id, notification_update)
        print("The response of NotificationApi->api_users_user_idnotifications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->api_users_user_idnotifications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Notification identifier | 
 **id** | **str**| Notification identifier | 
 **notification_update** | [**NotificationUpdate**](NotificationUpdate.md)| The updated Notification resource | 

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
**200** | Notification resource updated |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**400** | Invalid input |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**422** | Unprocessable entity |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**404** | Resource not found |  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  |
**401** | Authentication required |  -  |
**403** | Unauthorized access |  -  |
**429** | Rate limit exhausted |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

