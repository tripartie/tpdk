# tpdk.BrandingApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organizations_id_patch**](BrandingApi.md#api_organizations_id_patch) | **PATCH** /organizations/{id} | Update your Organization details, branding or parameters
[**api_organizations_idicon_delete**](BrandingApi.md#api_organizations_idicon_delete) | **DELETE** /organizations/{id}/icon | Unset your Organization Icon
[**api_organizations_idicon_post**](BrandingApi.md#api_organizations_idicon_post) | **POST** /organizations/{id}/icon | Upload your Organization Icon
[**api_organizations_idlogo_delete**](BrandingApi.md#api_organizations_idlogo_delete) | **DELETE** /organizations/{id}/logo | Unset your Organization Logo
[**api_organizations_idlogo_post**](BrandingApi.md#api_organizations_idlogo_post) | **POST** /organizations/{id}/logo | Upload your Organization logo


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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    organization_update = tpdk.OrganizationUpdate() # OrganizationUpdate | The updated Organization resource

    try:
        # Update your Organization details, branding or parameters
        api_response = api_instance.api_organizations_id_patch(id, organization_update)
        print("The response of BrandingApi->api_organizations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_id_patch: %s\n" % e)
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

# **api_organizations_idicon_delete**
> api_organizations_idicon_delete(id)

Unset your Organization Icon

Removes the Media resource.

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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Icon
        api_instance.api_organizations_idicon_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_delete: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Icon
        api_instance.api_organizations_idicon_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_delete: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Icon
        api_instance.api_organizations_idicon_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization identifier | 

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
**204** | Media resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_idicon_post**
> MediaRead api_organizations_idicon_post(id, file=file)

Upload your Organization Icon

Creates a Media resource.

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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization Icon
        api_response = api_instance.api_organizations_idicon_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idicon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_post: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization Icon
        api_response = api_instance.api_organizations_idicon_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idicon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_post: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization Icon
        api_response = api_instance.api_organizations_idicon_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idicon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idicon_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization identifier | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Media resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_idlogo_delete**
> api_organizations_idlogo_delete(id)

Unset your Organization Logo

Removes the Media resource.

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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Logo
        api_instance.api_organizations_idlogo_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_delete: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Logo
        api_instance.api_organizations_idlogo_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_delete: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier

    try:
        # Unset your Organization Logo
        api_instance.api_organizations_idlogo_delete(id)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization identifier | 

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
**204** | Media resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organizations_idlogo_post**
> MediaRead api_organizations_idlogo_post(id, file=file)

Upload your Organization logo

Creates a Media resource.

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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization logo
        api_response = api_instance.api_organizations_idlogo_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idlogo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_post: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization logo
        api_response = api_instance.api_organizations_idlogo_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idlogo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_post: %s\n" % e)
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
    api_instance = tpdk.BrandingApi(api_client)
    id = 'id_example' # str | Organization identifier
    file = tpdk.bytearray() # bytearray |  (optional)

    try:
        # Upload your Organization logo
        api_response = api_instance.api_organizations_idlogo_post(id, file=file)
        print("The response of BrandingApi->api_organizations_idlogo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->api_organizations_idlogo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization identifier | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Media resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

