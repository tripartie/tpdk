# tpdk.UserApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organizations_id_patch**](UserApi.md#api_organizations_id_patch) | **PATCH** /organizations/{id} | Update your Organization details, branding or parameters
[**api_personasauthentication_post**](UserApi.md#api_personasauthentication_post) | **POST** /personas/authentication | Persona Authentication
[**api_personasregister_post**](UserApi.md#api_personasregister_post) | **POST** /personas/register | Persona external registration
[**api_register_post**](UserApi.md#api_register_post) | **POST** /register | Organization onboarding
[**api_users_get_collection**](UserApi.md#api_users_get_collection) | **GET** /users | Retrieves the collection of User resources.
[**api_users_id_get**](UserApi.md#api_users_id_get) | **GET** /users/{id} | Retrieves a User resource.
[**api_users_idemail_validation_patch**](UserApi.md#api_users_idemail_validation_patch) | **PATCH** /users/{id}/email-validation | Validate email ownership


# **api_organizations_id_patch**
> OrganizationRead api_organizations_id_patch(id, organization_update)

Update your Organization details, branding or parameters

Updates the Organization resource.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.UserApi(api_client)
    id = 'id_example' # str | Organization identifier
    organization_update = tpdk.OrganizationUpdate() # OrganizationUpdate | The updated Organization resource

    try:
        # Update your Organization details, branding or parameters
        api_response = api_instance.api_organizations_id_patch(id, organization_update)
        print("The response of UserApi->api_organizations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_organizations_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization identifier | 
 **organization_update** | [**OrganizationUpdate**](OrganizationUpdate.md)| The updated Organization resource | 

### Return type

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization resource updated |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personasauthentication_post**
> Persona api_personasauthentication_post(persona)

Persona Authentication

Main route for Persona (Organization customers) to authenticate themselves. Public access, captcha protected and MFA mandatory.

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
    api_instance = tpdk.UserApi(api_client)
    persona = tpdk.Persona() # Persona | The new Persona resource

    try:
        # Persona Authentication
        api_response = api_instance.api_personasauthentication_post(persona)
        print("The response of UserApi->api_personasauthentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasauthentication_post: %s\n" % e)
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
    api_instance = tpdk.UserApi(api_client)
    persona = tpdk.Persona() # Persona | The new Persona resource

    try:
        # Persona Authentication
        api_response = api_instance.api_personasauthentication_post(persona)
        print("The response of UserApi->api_personasauthentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasauthentication_post: %s\n" % e)
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
    api_instance = tpdk.UserApi(api_client)
    persona = tpdk.Persona() # Persona | The new Persona resource

    try:
        # Persona Authentication
        api_response = api_instance.api_personasauthentication_post(persona)
        print("The response of UserApi->api_personasauthentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_personasauthentication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona** | [**Persona**](Persona.md)| The new Persona resource | 

### Return type

[**Persona**](Persona.md)

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

# **api_personasregister_post**
> PersonaRead api_personasregister_post(persona_register)

Persona external registration

Creates a Persona resource.

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
**201** | User resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_get_collection**
> List[UserSupportRead] api_users_get_collection(page=page)

Retrieves the collection of User resources.

Retrieves the collection of User resources.

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

[**List[UserSupportRead]**](UserSupportRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

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

# **api_users_idemail_validation_patch**
> UserPostRegisterRead api_users_idemail_validation_patch(id, user_email_validation_write)

Validate email ownership

Updates the User resource.

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
**404** | Resource not found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

