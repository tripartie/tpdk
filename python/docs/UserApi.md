# tpdk.UserApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_api_clients_get_collection**](UserApi.md#api_api_clients_get_collection) | **GET** /api-clients | Retrieves the collection of ApiClient resources.
[**api_api_clients_identifier_delete**](UserApi.md#api_api_clients_identifier_delete) | **DELETE** /api-clients/{identifier} | Removes the ApiClient resource.
[**api_api_clients_identifier_get**](UserApi.md#api_api_clients_identifier_get) | **GET** /api-clients/{identifier} | Retrieves a ApiClient resource.
[**api_api_clients_post**](UserApi.md#api_api_clients_post) | **POST** /api-clients | Creates a ApiClient resource.
[**api_invite_post**](UserApi.md#api_invite_post) | **POST** /invite | Organization invite
[**api_me_get**](UserApi.md#api_me_get) | **GET** /me | Retrieves a User resource.
[**api_personasauthentication_post**](UserApi.md#api_personasauthentication_post) | **POST** /personas/authentication | Persona Authentication
[**api_personasme_get**](UserApi.md#api_personasme_get) | **GET** /personas/me | Retrieve your authenticated Persona
[**api_personasregister_post**](UserApi.md#api_personasregister_post) | **POST** /personas/register | Persona external registration
[**api_register_post**](UserApi.md#api_register_post) | **POST** /register | Organization onboarding
[**api_users_get_collection**](UserApi.md#api_users_get_collection) | **GET** /users | Retrieves the collection of User resources.
[**api_users_id_get**](UserApi.md#api_users_id_get) | **GET** /users/{id} | Retrieves a User resource.
[**api_users_id_patch**](UserApi.md#api_users_id_patch) | **PATCH** /users/{id} | Updates the User resource.
[**api_users_idemail_validation_patch**](UserApi.md#api_users_idemail_validation_patch) | **PATCH** /users/{id}/email-validation | Validate email ownership


# **api_api_clients_get_collection**
> List[ApiClientRead] api_api_clients_get_collection(page=page)

Retrieves the collection of ApiClient resources.

Retrieves the collection of ApiClient resources.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
import time
import os
import tpdk
from tpdk.models.api_client_read import ApiClientRead
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
    api_instance = tpdk.UserApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of ApiClient resources.
        api_response = api_instance.api_api_clients_get_collection(page=page)
        print("The response of UserApi->api_api_clients_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_api_clients_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[ApiClientRead]**](ApiClientRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ApiClient collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_api_clients_identifier_delete**
> api_api_clients_identifier_delete(identifier)

Removes the ApiClient resource.

Removes the ApiClient resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
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

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.UserApi(api_client)
    identifier = 'identifier_example' # str | ApiClient identifier

    try:
        # Removes the ApiClient resource.
        api_instance.api_api_clients_identifier_delete(identifier)
    except Exception as e:
        print("Exception when calling UserApi->api_api_clients_identifier_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| ApiClient identifier | 

### Return type

void (empty response body)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | ApiClient resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_api_clients_identifier_get**
> ApiClientRead api_api_clients_identifier_get(identifier)

Retrieves a ApiClient resource.

Retrieves a ApiClient resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
import time
import os
import tpdk
from tpdk.models.api_client_read import ApiClientRead
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
    api_instance = tpdk.UserApi(api_client)
    identifier = 'identifier_example' # str | ApiClient identifier

    try:
        # Retrieves a ApiClient resource.
        api_response = api_instance.api_api_clients_identifier_get(identifier)
        print("The response of UserApi->api_api_clients_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_api_clients_identifier_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| ApiClient identifier | 

### Return type

[**ApiClientRead**](ApiClientRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ApiClient resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_api_clients_post**
> ApiClientPostCreationRead api_api_clients_post(api_client_write)

Creates a ApiClient resource.

Creates a ApiClient resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
import time
import os
import tpdk
from tpdk.models.api_client_post_creation_read import ApiClientPostCreationRead
from tpdk.models.api_client_write import ApiClientWrite
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
    api_instance = tpdk.UserApi(api_client)
    api_client_write = tpdk.ApiClientWrite() # ApiClientWrite | The new ApiClient resource

    try:
        # Creates a ApiClient resource.
        api_response = api_instance.api_api_clients_post(api_client_write)
        print("The response of UserApi->api_api_clients_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_api_clients_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_write** | [**ApiClientWrite**](ApiClientWrite.md)| The new ApiClient resource | 

### Return type

[**ApiClientPostCreationRead**](ApiClientPostCreationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ApiClient resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invite_post**
> UserPostRegisterRead api_invite_post(user_invite)

Organization invite

Invite a user to your organization workspace

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.user_invite import UserInvite
from tpdk.models.user_post_register_read import UserPostRegisterRead
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
    api_instance = tpdk.UserApi(api_client)
    user_invite = tpdk.UserInvite() # UserInvite | The new User resource

    try:
        # Organization invite
        api_response = api_instance.api_invite_post(user_invite)
        print("The response of UserApi->api_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_invite_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite** | [**UserInvite**](UserInvite.md)| The new User resource | 

### Return type

[**UserPostRegisterRead**](UserPostRegisterRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | User resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_me_get**
> UserAuthenticatedRead api_me_get()

Retrieves a User resource.

Retrieves a User resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.user_authenticated_read import UserAuthenticatedRead
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
    api_instance = tpdk.UserApi(api_client)

    try:
        # Retrieves a User resource.
        api_response = api_instance.api_me_get()
        print("The response of UserApi->api_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_me_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAuthenticatedRead**](UserAuthenticatedRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personasauthentication_post**
> PersonaAuthReturn api_personasauthentication_post(persona_external_auth)

Persona Authentication

Main route for Persona (Organization customers) to authenticate themselves. Public access, captcha protected and MFA mandatory.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.persona_auth_return import PersonaAuthReturn
from tpdk.models.persona_external_auth import PersonaExternalAuth
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
    api_instance = tpdk.UserApi(api_client)
    persona_external_auth = tpdk.PersonaExternalAuth() # PersonaExternalAuth | The new Persona resource

    try:
        # Persona Authentication
        api_response = api_instance.api_personasauthentication_post(persona_external_auth)
        print("The response of UserApi->api_personasauthentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasauthentication_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona_external_auth** | [**PersonaExternalAuth**](PersonaExternalAuth.md)| The new Persona resource | 

### Return type

[**PersonaAuthReturn**](PersonaAuthReturn.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Persona resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personasme_get**
> PersonaRead api_personasme_get()

Retrieve your authenticated Persona

Retrieves a Persona resource.

### Example

* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.persona_read import PersonaRead
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
    api_instance = tpdk.UserApi(api_client)

    try:
        # Retrieve your authenticated Persona
        api_response = api_instance.api_personasme_get()
        print("The response of UserApi->api_personasme_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasme_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PersonaRead**](PersonaRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Persona resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personasregister_post**
> PersonaRead api_personasregister_post(persona_register)

Persona external registration

Creates a Persona resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.persona_read import PersonaRead
from tpdk.models.persona_register import PersonaRegister
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
    api_instance = tpdk.UserApi(api_client)
    persona_register = tpdk.PersonaRegister() # PersonaRegister | The new Persona resource

    try:
        # Persona external registration
        api_response = api_instance.api_personasregister_post(persona_register)
        print("The response of UserApi->api_personasregister_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasregister_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona_register** | [**PersonaRegister**](PersonaRegister.md)| The new Persona resource | 

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
**201** | Persona resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_register_post**
> UserPostRegisterRead api_register_post(user_write)

Organization onboarding

Internal-use only, protected by a captcha. Organization first-enrollment

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.user_post_register_read import UserPostRegisterRead
from tpdk.models.user_write import UserWrite
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
    api_instance = tpdk.UserApi(api_client)
    user_write = tpdk.UserWrite() # UserWrite | The new User resource

    try:
        # Organization onboarding
        api_response = api_instance.api_register_post(user_write)
        print("The response of UserApi->api_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_register_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_write** | [**UserWrite**](UserWrite.md)| The new User resource | 

### Return type

[**UserPostRegisterRead**](UserPostRegisterRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | User resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_get_collection**
> List[UserCollectionRead] api_users_get_collection(page=page)

Retrieves the collection of User resources.

Retrieves the collection of User resources.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
import time
import os
import tpdk
from tpdk.models.user_collection_read import UserCollectionRead
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
    api_instance = tpdk.UserApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of User resources.
        api_response = api_instance.api_users_get_collection(page=page)
        print("The response of UserApi->api_users_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[UserCollectionRead]**](UserCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_get**
> User api_users_id_get(id)

Retrieves a User resource.

Retrieves a User resource.

### Example

* Api Key Authentication (jwtPersonalKey):
```python
import time
import os
import tpdk
from tpdk.models.user import User
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
    api_instance = tpdk.UserApi(api_client)
    id = 'id_example' # str | User identifier

    try:
        # Retrieves a User resource.
        api_response = api_instance.api_users_id_get(id)
        print("The response of UserApi->api_users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 

### Return type

[**User**](User.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_patch**
> UserPostRegisterRead api_users_id_patch(id, user_update)

Updates the User resource.

Updates the User resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.user_post_register_read import UserPostRegisterRead
from tpdk.models.user_update import UserUpdate
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
    api_instance = tpdk.UserApi(api_client)
    id = 'id_example' # str | User identifier
    user_update = tpdk.UserUpdate() # UserUpdate | The updated User resource

    try:
        # Updates the User resource.
        api_response = api_instance.api_users_id_patch(id, user_update)
        print("The response of UserApi->api_users_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 
 **user_update** | [**UserUpdate**](UserUpdate.md)| The updated User resource | 

### Return type

[**UserPostRegisterRead**](UserPostRegisterRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_idemail_validation_patch**
> UserPostRegisterRead api_users_idemail_validation_patch(id, user_email_validation_write)

Validate email ownership

Updates the User resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.user_email_validation_write import UserEmailValidationWrite
from tpdk.models.user_post_register_read import UserPostRegisterRead
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
    api_instance = tpdk.UserApi(api_client)
    id = 'id_example' # str | User identifier
    user_email_validation_write = tpdk.UserEmailValidationWrite() # UserEmailValidationWrite | The updated User resource

    try:
        # Validate email ownership
        api_response = api_instance.api_users_idemail_validation_patch(id, user_email_validation_write)
        print("The response of UserApi->api_users_idemail_validation_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_idemail_validation_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 
 **user_email_validation_write** | [**UserEmailValidationWrite**](UserEmailValidationWrite.md)| The updated User resource | 

### Return type

[**UserPostRegisterRead**](UserPostRegisterRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

