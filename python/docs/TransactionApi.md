# tpdk.TransactionApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_transactions_get_collection**](TransactionApi.md#api_transactions_get_collection) | **GET** /transactions | Retrieves the collection of Transaction resources.


# **api_transactions_get_collection**
> List[TransactionCollectionRead] api_transactions_get_collection(page=page, order_status=order_status, metadata=metadata, status=status, exists_dispute=exists_dispute)

Retrieves the collection of Transaction resources.

Retrieves the collection of Transaction resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.transaction_collection_read import TransactionCollectionRead
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
    api_instance = tpdk.TransactionApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    order_status = 'order_status_example' # str |  (optional)
    metadata = ['[\"External-ID\",\"1254A\"]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    status = 'CREATED' # str | Filter on a limited subset of status (optional)
    exists_dispute = True # bool |  (optional)

    try:
        # Retrieves the collection of Transaction resources.
        api_response = api_instance.api_transactions_get_collection(page=page, order_status=order_status, metadata=metadata, status=status, exists_dispute=exists_dispute)
        print("The response of TransactionApi->api_transactions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->api_transactions_get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **order_status** | **str**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **status** | **str**| Filter on a limited subset of status | [optional] 
 **exists_dispute** | **bool**|  | [optional] 

### Return type

[**List[TransactionCollectionRead]**](TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

