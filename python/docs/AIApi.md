# tpdk.AIApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_ai_hints_post**](AIApi.md#api_ai_hints_post) | **POST** /ai-hints | Dedicated endpoint for our artificial intelligence bot


# **api_ai_hints_post**
> AiHint api_ai_hints_post(ai_hint)

Dedicated endpoint for our artificial intelligence bot

Creates a AiHint resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.ai_hint import AiHint
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
    api_instance = tpdk.AIApi(api_client)
    ai_hint = tpdk.AiHint() # AiHint | The new AiHint resource

    try:
        # Dedicated endpoint for our artificial intelligence bot
        api_response = api_instance.api_ai_hints_post(ai_hint)
        print("The response of AIApi->api_ai_hints_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIApi->api_ai_hints_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_hint** | [**AiHint**](AiHint.md)| The new AiHint resource | 

### Return type

[**AiHint**](AiHint.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AiHint resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

