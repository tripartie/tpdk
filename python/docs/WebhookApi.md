# tpdk.WebhookApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_webhook_histories_get_collection**](WebhookApi.md#api_webhook_histories_get_collection) | **GET** /webhook-histories | Retrieves the collection of WebhookHistory resources.
[**api_webhook_histories_id_get**](WebhookApi.md#api_webhook_histories_id_get) | **GET** /webhook-histories/{id} | Retrieves a WebhookHistory resource.
[**api_webhook_histories_id_put**](WebhookApi.md#api_webhook_histories_id_put) | **PUT** /webhook-histories/{id} | Replay a Webhook that ended in failure
[**api_webhook_subscriptions_get_collection**](WebhookApi.md#api_webhook_subscriptions_get_collection) | **GET** /webhook-subscriptions | Retrieves the collection of WebhookSubscription resources.
[**api_webhook_subscriptions_id_delete**](WebhookApi.md#api_webhook_subscriptions_id_delete) | **DELETE** /webhook-subscriptions/{id} | Removes the WebhookSubscription resource.
[**api_webhook_subscriptions_post**](WebhookApi.md#api_webhook_subscriptions_post) | **POST** /webhook-subscriptions | Subscribe to Event(s)


# **api_webhook_histories_get_collection**
> List[WebhookHistoryCollectionRead] api_webhook_histories_get_collection(page=page, event=event, event2=event2)

Retrieves the collection of WebhookHistory resources.

Retrieves the collection of WebhookHistory resources.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'event_example' # str |  (optional)
    event2 = ['event_example'] # List[str] |  (optional)

    try:
        # Retrieves the collection of WebhookHistory resources.
        api_response = api_instance.api_webhook_histories_get_collection(page=page, event=event, event2=event2)
        print("The response of WebhookApi->api_webhook_histories_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_get_collection: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'event_example' # str |  (optional)
    event2 = ['event_example'] # List[str] |  (optional)

    try:
        # Retrieves the collection of WebhookHistory resources.
        api_response = api_instance.api_webhook_histories_get_collection(page=page, event=event, event2=event2)
        print("The response of WebhookApi->api_webhook_histories_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_get_collection: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'event_example' # str |  (optional)
    event2 = ['event_example'] # List[str] |  (optional)

    try:
        # Retrieves the collection of WebhookHistory resources.
        api_response = api_instance.api_webhook_histories_get_collection(page=page, event=event, event2=event2)
        print("The response of WebhookApi->api_webhook_histories_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **event** | **str**|  | [optional] 
 **event2** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WebhookHistoryCollectionRead]**](WebhookHistoryCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebhookHistory collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_webhook_histories_id_get**
> WebhookHistoryRead api_webhook_histories_id_get(id)

Retrieves a WebhookHistory resource.

Retrieves a WebhookHistory resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier

    try:
        # Retrieves a WebhookHistory resource.
        api_response = api_instance.api_webhook_histories_id_get(id)
        print("The response of WebhookApi->api_webhook_histories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_get: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier

    try:
        # Retrieves a WebhookHistory resource.
        api_response = api_instance.api_webhook_histories_id_get(id)
        print("The response of WebhookApi->api_webhook_histories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_get: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier

    try:
        # Retrieves a WebhookHistory resource.
        api_response = api_instance.api_webhook_histories_id_get(id)
        print("The response of WebhookApi->api_webhook_histories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WebhookHistory identifier | 

### Return type

[**WebhookHistoryRead**](WebhookHistoryRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebhookHistory resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_webhook_histories_id_put**
> WebhookHistoryRead api_webhook_histories_id_put(id, body)

Replay a Webhook that ended in failure

Replaces the WebhookHistory resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier
    body = None # object | The updated WebhookHistory resource

    try:
        # Replay a Webhook that ended in failure
        api_response = api_instance.api_webhook_histories_id_put(id, body)
        print("The response of WebhookApi->api_webhook_histories_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_put: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier
    body = None # object | The updated WebhookHistory resource

    try:
        # Replay a Webhook that ended in failure
        api_response = api_instance.api_webhook_histories_id_put(id, body)
        print("The response of WebhookApi->api_webhook_histories_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_put: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookHistory identifier
    body = None # object | The updated WebhookHistory resource

    try:
        # Replay a Webhook that ended in failure
        api_response = api_instance.api_webhook_histories_id_put(id, body)
        print("The response of WebhookApi->api_webhook_histories_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_histories_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WebhookHistory identifier | 
 **body** | **object**| The updated WebhookHistory resource | 

### Return type

[**WebhookHistoryRead**](WebhookHistoryRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebhookHistory resource updated |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_webhook_subscriptions_get_collection**
> List[WebhookSubscriptionRead] api_webhook_subscriptions_get_collection(page=page, event=event)

Retrieves the collection of WebhookSubscription resources.

Retrieves the collection of WebhookSubscription resources.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'dispute.opened' # str | Filter on a limited subset of event (optional)

    try:
        # Retrieves the collection of WebhookSubscription resources.
        api_response = api_instance.api_webhook_subscriptions_get_collection(page=page, event=event)
        print("The response of WebhookApi->api_webhook_subscriptions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_get_collection: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'dispute.opened' # str | Filter on a limited subset of event (optional)

    try:
        # Retrieves the collection of WebhookSubscription resources.
        api_response = api_instance.api_webhook_subscriptions_get_collection(page=page, event=event)
        print("The response of WebhookApi->api_webhook_subscriptions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_get_collection: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    event = 'dispute.opened' # str | Filter on a limited subset of event (optional)

    try:
        # Retrieves the collection of WebhookSubscription resources.
        api_response = api_instance.api_webhook_subscriptions_get_collection(page=page, event=event)
        print("The response of WebhookApi->api_webhook_subscriptions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **event** | **str**| Filter on a limited subset of event | [optional] 

### Return type

[**List[WebhookSubscriptionRead]**](WebhookSubscriptionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebhookSubscription collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_webhook_subscriptions_id_delete**
> api_webhook_subscriptions_id_delete(id)

Removes the WebhookSubscription resource.

Removes the WebhookSubscription resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookSubscription identifier

    try:
        # Removes the WebhookSubscription resource.
        api_instance.api_webhook_subscriptions_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_id_delete: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookSubscription identifier

    try:
        # Removes the WebhookSubscription resource.
        api_instance.api_webhook_subscriptions_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_id_delete: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    id = 'id_example' # str | WebhookSubscription identifier

    try:
        # Removes the WebhookSubscription resource.
        api_instance.api_webhook_subscriptions_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WebhookSubscription identifier | 

### Return type

void (empty response body)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | WebhookSubscription resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_webhook_subscriptions_post**
> WebhookSubscriptionRead api_webhook_subscriptions_post(webhook_subscription_write)

Subscribe to Event(s)

Creates a WebhookSubscription resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    webhook_subscription_write = tpdk.WebhookSubscriptionWrite() # WebhookSubscriptionWrite | The new WebhookSubscription resource

    try:
        # Subscribe to Event(s)
        api_response = api_instance.api_webhook_subscriptions_post(webhook_subscription_write)
        print("The response of WebhookApi->api_webhook_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_post: %s\n" % e)
```

* Api Key Authentication (personaAuthKey):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    webhook_subscription_write = tpdk.WebhookSubscriptionWrite() # WebhookSubscriptionWrite | The new WebhookSubscription resource

    try:
        # Subscribe to Event(s)
        api_response = api_instance.api_webhook_subscriptions_post(webhook_subscription_write)
        print("The response of WebhookApi->api_webhook_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_post: %s\n" % e)
```

* OAuth Authentication (oauth):
```python
from __future__ import print_function
import time
import os
import tpdk
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
    api_instance = tpdk.WebhookApi(api_client)
    webhook_subscription_write = tpdk.WebhookSubscriptionWrite() # WebhookSubscriptionWrite | The new WebhookSubscription resource

    try:
        # Subscribe to Event(s)
        api_response = api_instance.api_webhook_subscriptions_post(webhook_subscription_write)
        print("The response of WebhookApi->api_webhook_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->api_webhook_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_subscription_write** | [**WebhookSubscriptionWrite**](WebhookSubscriptionWrite.md)| The new WebhookSubscription resource | 

### Return type

[**WebhookSubscriptionRead**](WebhookSubscriptionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WebhookSubscription resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

