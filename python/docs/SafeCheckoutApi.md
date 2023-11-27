# tpdk.SafeCheckoutApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_offers_get_collection**](SafeCheckoutApi.md#api_offers_get_collection) | **GET** /offers | Read issued Offers
[**api_offers_post**](SafeCheckoutApi.md#api_offers_post) | **POST** /offers | Create an Offer and retrieve url
[**api_offers_ulid_get**](SafeCheckoutApi.md#api_offers_ulid_get) | **GET** /offers/{ulid} | Read an Offer
[**api_offers_ulidmedias_id_delete**](SafeCheckoutApi.md#api_offers_ulidmedias_id_delete) | **DELETE** /offers/{ulid}/medias/{id} | Removes the Media resource.
[**api_offers_ulidmedias_post**](SafeCheckoutApi.md#api_offers_ulidmedias_post) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer
[**api_offers_ulidtransactions_get_collection**](SafeCheckoutApi.md#api_offers_ulidtransactions_get_collection) | **GET** /offers/{ulid}/transactions | Retrieve Payment Intents for Offer
[**api_offers_ulidtransactions_idevaluations_post**](SafeCheckoutApi.md#api_offers_ulidtransactions_idevaluations_post) | **POST** /offers/{ulid}/transactions/{id}/evaluations | Submit an Evaluation for the Offer
[**api_offers_ulidtransactions_post**](SafeCheckoutApi.md#api_offers_ulidtransactions_post) | **POST** /offers/{ulid}/transactions | Create a Payment Intent for Offer
[**api_personas_idoffers_delete**](SafeCheckoutApi.md#api_personas_idoffers_delete) | **DELETE** /personas/{id}/offers | Revoke an Offer for given Persona
[**api_personas_idoffers_get_collection**](SafeCheckoutApi.md#api_personas_idoffers_get_collection) | **GET** /personas/{id}/offers | List or Search Offers for given Persona
[**api_personas_idoffers_patch**](SafeCheckoutApi.md#api_personas_idoffers_patch) | **PATCH** /personas/{id}/offers | Update an Offer for given Persona
[**api_personas_idoffers_post**](SafeCheckoutApi.md#api_personas_idoffers_post) | **POST** /personas/{id}/offers | Create an Offer for given Persona
[**api_transactions_get_collection**](SafeCheckoutApi.md#api_transactions_get_collection) | **GET** /transactions | Retrieves the collection of Transaction resources.
[**api_transactions_uliddispute_delete**](SafeCheckoutApi.md#api_transactions_uliddispute_delete) | **DELETE** /transactions/{ulid}/dispute | Abandon claims on Dispute
[**api_transactions_uliddispute_get**](SafeCheckoutApi.md#api_transactions_uliddispute_get) | **GET** /transactions/{ulid}/dispute | Read Dispute from existing Transaction
[**api_transactions_uliddispute_patch**](SafeCheckoutApi.md#api_transactions_uliddispute_patch) | **PATCH** /transactions/{ulid}/dispute | Interact with a Dispute
[**api_transactions_uliddispute_post**](SafeCheckoutApi.md#api_transactions_uliddispute_post) | **POST** /transactions/{ulid}/dispute | Open a Dispute related to existing Transaction
[**api_transactions_ulidparcels_get_collection**](SafeCheckoutApi.md#api_transactions_ulidparcels_get_collection) | **GET** /transactions/{ulid}/parcels | Read shipments from Transaction
[**api_transactions_ulidparcels_id_delete**](SafeCheckoutApi.md#api_transactions_ulidparcels_id_delete) | **DELETE** /transactions/{ulid}/parcels/{id} | Withdraw shipment from Transaction
[**api_transactions_ulidparcels_post**](SafeCheckoutApi.md#api_transactions_ulidparcels_post) | **POST** /transactions/{ulid}/parcels | Manually declare package shipped for Transaction


# **api_offers_get_collection**
> List[OfferCollectionRead] api_offers_get_collection(page=page, title=title, public_url=public_url, public_url2=public_url2, unit_price=unit_price, unit_price2=unit_price2, item_count=item_count, item_count2=item_count2, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, metadata=metadata, offer_metadata=offer_metadata, nature=nature, condition=condition, shipping_allowed=shipping_allowed)

Read issued Offers

Retrieves the collection of Offer resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_collection_read import OfferCollectionRead
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    title = 'title_example' # str |  (optional)
    public_url = 'public_url_example' # str |  (optional)
    public_url2 = ['public_url_example'] # List[str] |  (optional)
    unit_price = 3.4 # float |  (optional)
    unit_price2 = [3.4] # List[float] |  (optional)
    item_count = 56 # int |  (optional)
    item_count2 = [56] # List[int] |  (optional)
    created_at_before = 'created_at_before_example' # str |  (optional)
    created_at_strictly_before = 'created_at_strictly_before_example' # str |  (optional)
    created_at_after = 'created_at_after_example' # str |  (optional)
    created_at_strictly_after = 'created_at_strictly_after_example' # str |  (optional)
    metadata = ['[External-ID, 1254A]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    offer_metadata = ['[\"External-ID\",\"1254A\"]'] # List[str] | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    nature = 'service' # str | Filter on a limited subset of nature (optional)
    condition = 'NEW' # str | Filter on a limited subset of condition (optional)
    shipping_allowed = True # bool |  (optional)

    try:
        # Read issued Offers
        api_response = api_instance.api_offers_get_collection(page=page, title=title, public_url=public_url, public_url2=public_url2, unit_price=unit_price, unit_price2=unit_price2, item_count=item_count, item_count2=item_count2, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, metadata=metadata, offer_metadata=offer_metadata, nature=nature, condition=condition, shipping_allowed=shipping_allowed)
        print("The response of SafeCheckoutApi->api_offers_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **title** | **str**|  | [optional] 
 **public_url** | **str**|  | [optional] 
 **public_url2** | [**List[str]**](str.md)|  | [optional] 
 **unit_price** | **float**|  | [optional] 
 **unit_price2** | [**List[float]**](float.md)|  | [optional] 
 **item_count** | **int**|  | [optional] 
 **item_count2** | [**List[int]**](int.md)|  | [optional] 
 **created_at_before** | **str**|  | [optional] 
 **created_at_strictly_before** | **str**|  | [optional] 
 **created_at_after** | **str**|  | [optional] 
 **created_at_strictly_after** | **str**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **offer_metadata** | [**List[str]**](str.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **nature** | **str**| Filter on a limited subset of nature | [optional] 
 **condition** | **str**| Filter on a limited subset of condition | [optional] 
 **shipping_allowed** | **bool**|  | [optional] 

### Return type

[**List[OfferCollectionRead]**](OfferCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_post**
> OfferPostCreationRead api_offers_post(offer_independent_write)

Create an Offer and retrieve url

Publish an offer so that you can safely retrieve a safe-checkout unique link from us

### Example

* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_independent_write import OfferIndependentWrite
from tpdk.models.offer_post_creation_read import OfferPostCreationRead
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    offer_independent_write = tpdk.OfferIndependentWrite() # OfferIndependentWrite | The new Offer resource

    try:
        # Create an Offer and retrieve url
        api_response = api_instance.api_offers_post(offer_independent_write)
        print("The response of SafeCheckoutApi->api_offers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_independent_write** | [**OfferIndependentWrite**](OfferIndependentWrite.md)| The new Offer resource | 

### Return type

[**OfferPostCreationRead**](OfferPostCreationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Offer resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_ulid_get**
> OfferRead api_offers_ulid_get(ulid)

Read an Offer

Retrieves a Offer resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_read import OfferRead
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Offer identifier

    try:
        # Read an Offer
        api_response = api_instance.api_offers_ulid_get(ulid)
        print("The response of SafeCheckoutApi->api_offers_ulid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Offer identifier | 

### Return type

[**OfferRead**](OfferRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_ulidmedias_id_delete**
> api_offers_ulidmedias_id_delete(ulid, id)

Removes the Media resource.

Removes the Media resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
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

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 

    try:
        # Removes the Media resource.
        api_instance.api_offers_ulidmedias_id_delete(ulid, id)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulidmedias_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **id** | **int**|  | 

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

# **api_offers_ulidmedias_post**
> MediaRead api_offers_ulidmedias_post(ulid, file=file)

Upload a picture for a given Offer

Creates a Media resource.

### Example

* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.media_read import MediaRead
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | 
    file = None # bytearray |  (optional)

    try:
        # Upload a picture for a given Offer
        api_response = api_instance.api_offers_ulidmedias_post(ulid, file=file)
        print("The response of SafeCheckoutApi->api_offers_ulidmedias_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulidmedias_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Media resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_ulidtransactions_get_collection**
> List[TransactionCollectionRead] api_offers_ulidtransactions_get_collection(ulid, page=page, order_status=order_status, metadata=metadata, status=status)

Retrieve Payment Intents for Offer

Retrieves the collection of Transaction resources.

### Example

* Api Key Authentication (jwtPersonalKey):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Offer identifier
    page = 1 # int | The collection page number (optional) (default to 1)
    order_status = 'order_status_example' # str |  (optional)
    metadata = ['[External-ID, 1254A]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    status = 'CREATED' # str | Filter on a limited subset of status (optional)

    try:
        # Retrieve Payment Intents for Offer
        api_response = api_instance.api_offers_ulidtransactions_get_collection(ulid, page=page, order_status=order_status, metadata=metadata, status=status)
        print("The response of SafeCheckoutApi->api_offers_ulidtransactions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulidtransactions_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Offer identifier | 
 **page** | **int**| The collection page number | [optional] [default to 1]
 **order_status** | **str**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **status** | **str**| Filter on a limited subset of status | [optional] 

### Return type

[**List[TransactionCollectionRead]**](TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_ulidtransactions_idevaluations_post**
> EvaluationRead api_offers_ulidtransactions_idevaluations_post(ulid, id, evaluation_write)

Submit an Evaluation for the Offer

**Only authenticated** buyer and seller **CAN** issue an evaluation **WHEN** the transaction reached a final state.

### Example

* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.evaluation_read import EvaluationRead
from tpdk.models.evaluation_write import EvaluationWrite
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier
    id = 'id_example' # str | Transaction identifier
    evaluation_write = tpdk.EvaluationWrite() # EvaluationWrite | The new Evaluation resource

    try:
        # Submit an Evaluation for the Offer
        api_response = api_instance.api_offers_ulidtransactions_idevaluations_post(ulid, id, evaluation_write)
        print("The response of SafeCheckoutApi->api_offers_ulidtransactions_idevaluations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulidtransactions_idevaluations_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 
 **id** | **str**| Transaction identifier | 
 **evaluation_write** | [**EvaluationWrite**](EvaluationWrite.md)| The new Evaluation resource | 

### Return type

[**EvaluationRead**](EvaluationRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Evaluation resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_offers_ulidtransactions_post**
> TransactionRead api_offers_ulidtransactions_post(ulid, body)

Create a Payment Intent for Offer

Cannot be used outside of a Persona (buyer)

### Example

* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.transaction_read import TransactionRead
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Offer identifier
    body = None # object | The new Transaction resource

    try:
        # Create a Payment Intent for Offer
        api_response = api_instance.api_offers_ulidtransactions_post(ulid, body)
        print("The response of SafeCheckoutApi->api_offers_ulidtransactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_offers_ulidtransactions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Offer identifier | 
 **body** | **object**| The new Transaction resource | 

### Return type

[**TransactionRead**](TransactionRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Transaction resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personas_idoffers_delete**
> api_personas_idoffers_delete(id)

Revoke an Offer for given Persona

That goes without says, if that **Offer** have a _Transaction_ **that is ongoing**, you **MAY NOT** revoke the **Offer**.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
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

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    id = 'id_example' # str | Persona identifier

    try:
        # Revoke an Offer for given Persona
        api_instance.api_personas_idoffers_delete(id)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_personas_idoffers_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Persona identifier | 

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
**204** | Offer resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personas_idoffers_get_collection**
> List[OfferCollectionRead] api_personas_idoffers_get_collection(id, page=page, title=title, public_url=public_url, public_url2=public_url2, unit_price=unit_price, unit_price2=unit_price2, item_count=item_count, item_count2=item_count2, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, metadata=metadata, offer_metadata=offer_metadata, nature=nature, condition=condition, shipping_allowed=shipping_allowed)

List or Search Offers for given Persona

Retrieves the collection of Offer resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_collection_read import OfferCollectionRead
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    id = 'id_example' # str | Persona identifier
    page = 1 # int | The collection page number (optional) (default to 1)
    title = 'title_example' # str |  (optional)
    public_url = 'public_url_example' # str |  (optional)
    public_url2 = ['public_url_example'] # List[str] |  (optional)
    unit_price = 3.4 # float |  (optional)
    unit_price2 = [3.4] # List[float] |  (optional)
    item_count = 56 # int |  (optional)
    item_count2 = [56] # List[int] |  (optional)
    created_at_before = 'created_at_before_example' # str |  (optional)
    created_at_strictly_before = 'created_at_strictly_before_example' # str |  (optional)
    created_at_after = 'created_at_after_example' # str |  (optional)
    created_at_strictly_after = 'created_at_strictly_after_example' # str |  (optional)
    metadata = ['[External-ID, 1254A]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    offer_metadata = ['[External-ID, 1254A]'] # List[str] | Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    nature = 'service' # str | Filter on a limited subset of nature (optional)
    condition = 'NEW' # str | Filter on a limited subset of condition (optional)
    shipping_allowed = True # bool |  (optional)

    try:
        # List or Search Offers for given Persona
        api_response = api_instance.api_personas_idoffers_get_collection(id, page=page, title=title, public_url=public_url, public_url2=public_url2, unit_price=unit_price, unit_price2=unit_price2, item_count=item_count, item_count2=item_count2, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, metadata=metadata, offer_metadata=offer_metadata, nature=nature, condition=condition, shipping_allowed=shipping_allowed)
        print("The response of SafeCheckoutApi->api_personas_idoffers_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_personas_idoffers_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Persona identifier | 
 **page** | **int**| The collection page number | [optional] [default to 1]
 **title** | **str**|  | [optional] 
 **public_url** | **str**|  | [optional] 
 **public_url2** | [**List[str]**](str.md)|  | [optional] 
 **unit_price** | **float**|  | [optional] 
 **unit_price2** | [**List[float]**](float.md)|  | [optional] 
 **item_count** | **int**|  | [optional] 
 **item_count2** | [**List[int]**](int.md)|  | [optional] 
 **created_at_before** | **str**|  | [optional] 
 **created_at_strictly_before** | **str**|  | [optional] 
 **created_at_after** | **str**|  | [optional] 
 **created_at_strictly_after** | **str**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **offer_metadata** | [**List[str]**](str.md)| Flattened OrderedMap for offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **nature** | **str**| Filter on a limited subset of nature | [optional] 
 **condition** | **str**| Filter on a limited subset of condition | [optional] 
 **shipping_allowed** | **bool**|  | [optional] 

### Return type

[**List[OfferCollectionRead]**](OfferCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personas_idoffers_patch**
> OfferRead api_personas_idoffers_patch(id, offer_update)

Update an Offer for given Persona

Updates the Offer resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_read import OfferRead
from tpdk.models.offer_update import OfferUpdate
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    id = 'id_example' # str | Persona identifier
    offer_update = tpdk.OfferUpdate() # OfferUpdate | The updated Offer resource

    try:
        # Update an Offer for given Persona
        api_response = api_instance.api_personas_idoffers_patch(id, offer_update)
        print("The response of SafeCheckoutApi->api_personas_idoffers_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_personas_idoffers_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Persona identifier | 
 **offer_update** | [**OfferUpdate**](OfferUpdate.md)| The updated Offer resource | 

### Return type

[**OfferRead**](OfferRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Offer resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_personas_idoffers_post**
> OfferPostCreationRead api_personas_idoffers_post(id, offer_write)

Create an Offer for given Persona

Creates a Offer resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.offer_post_creation_read import OfferPostCreationRead
from tpdk.models.offer_write import OfferWrite
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    id = 'id_example' # str | Persona identifier
    offer_write = tpdk.OfferWrite() # OfferWrite | The new Offer resource

    try:
        # Create an Offer for given Persona
        api_response = api_instance.api_personas_idoffers_post(id, offer_write)
        print("The response of SafeCheckoutApi->api_personas_idoffers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_personas_idoffers_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Persona identifier | 
 **offer_write** | [**OfferWrite**](OfferWrite.md)| The new Offer resource | 

### Return type

[**OfferPostCreationRead**](OfferPostCreationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Offer resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_get_collection**
> List[TransactionCollectionRead] api_transactions_get_collection(page=page, order_status=order_status, metadata=metadata, status=status)

Retrieves the collection of Transaction resources.

Retrieves the collection of Transaction resources.

### Example

* Api Key Authentication (jwtPersonalKey):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    order_status = 'order_status_example' # str |  (optional)
    metadata = ['[External-ID, 1254A]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    status = 'CREATED' # str | Filter on a limited subset of status (optional)

    try:
        # Retrieves the collection of Transaction resources.
        api_response = api_instance.api_transactions_get_collection(page=page, order_status=order_status, metadata=metadata, status=status)
        print("The response of SafeCheckoutApi->api_transactions_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **order_status** | **str**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **status** | **str**| Filter on a limited subset of status | [optional] 

### Return type

[**List[TransactionCollectionRead]**](TransactionCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_uliddispute_delete**
> api_transactions_uliddispute_delete(ulid)

Abandon claims on Dispute

**Only the buyer/complainant** can dismiss the case immediately. Otherwise, the support can but in a limited ranges of Dispute status.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
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

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Transaction identifier

    try:
        # Abandon claims on Dispute
        api_instance.api_transactions_uliddispute_delete(ulid)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_uliddispute_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Transaction identifier | 

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
**204** | Dispute resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_uliddispute_get**
> DisputeRead api_transactions_uliddispute_get(ulid)

Read Dispute from existing Transaction

Retrieves a Dispute resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.dispute_read import DisputeRead
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Transaction identifier

    try:
        # Read Dispute from existing Transaction
        api_response = api_instance.api_transactions_uliddispute_get(ulid)
        print("The response of SafeCheckoutApi->api_transactions_uliddispute_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_uliddispute_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Transaction identifier | 

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_uliddispute_patch**
> DisputeRead api_transactions_uliddispute_patch(ulid, dispute_update)

Interact with a Dispute

Only authenticated Persona can interact with a Dispute object. Usually through our web application.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.dispute_read import DisputeRead
from tpdk.models.dispute_update import DisputeUpdate
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

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Transaction identifier
    dispute_update = tpdk.DisputeUpdate() # DisputeUpdate | The updated Dispute resource

    try:
        # Interact with a Dispute
        api_response = api_instance.api_transactions_uliddispute_patch(ulid, dispute_update)
        print("The response of SafeCheckoutApi->api_transactions_uliddispute_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_uliddispute_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Transaction identifier | 
 **dispute_update** | [**DisputeUpdate**](DisputeUpdate.md)| The updated Dispute resource | 

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute resource updated |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_uliddispute_post**
> DisputePostCreationRead api_transactions_uliddispute_post(ulid, dispute_write)

Open a Dispute related to existing Transaction

Creates a Dispute resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.dispute_post_creation_read import DisputePostCreationRead
from tpdk.models.dispute_write import DisputeWrite
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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | Transaction identifier
    dispute_write = tpdk.DisputeWrite() # DisputeWrite | The new Dispute resource

    try:
        # Open a Dispute related to existing Transaction
        api_response = api_instance.api_transactions_uliddispute_post(ulid, dispute_write)
        print("The response of SafeCheckoutApi->api_transactions_uliddispute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_uliddispute_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Transaction identifier | 
 **dispute_write** | [**DisputeWrite**](DisputeWrite.md)| The new Dispute resource | 

### Return type

[**DisputePostCreationRead**](DisputePostCreationRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Dispute resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_ulidparcels_get_collection**
> List[object] api_transactions_ulidparcels_get_collection(ulid, page=page)

Read shipments from Transaction

Retrieves the collection of Parcel resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
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

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | 
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Read shipments from Transaction
        api_response = api_instance.api_transactions_ulidparcels_get_collection(ulid, page=page)
        print("The response of SafeCheckoutApi->api_transactions_ulidparcels_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_ulidparcels_get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

**List[object]**

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parcel collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_ulidparcels_id_delete**
> api_transactions_ulidparcels_id_delete(ulid, id)

Withdraw shipment from Transaction

No one except the support can do that manoeuvre.

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
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 

    try:
        # Withdraw shipment from Transaction
        api_instance.api_transactions_ulidparcels_id_delete(ulid, id)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_ulidparcels_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **id** | **int**|  | 

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
**204** | Parcel resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transactions_ulidparcels_post**
> ParcelRead api_transactions_ulidparcels_post(ulid, parcel_write)

Manually declare package shipped for Transaction

Creates a Parcel resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.parcel_read import ParcelRead
from tpdk.models.parcel_write import ParcelWrite
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.SafeCheckoutApi(api_client)
    ulid = 'ulid_example' # str | 
    parcel_write = tpdk.ParcelWrite() # ParcelWrite | The new Parcel resource

    try:
        # Manually declare package shipped for Transaction
        api_response = api_instance.api_transactions_ulidparcels_post(ulid, parcel_write)
        print("The response of SafeCheckoutApi->api_transactions_ulidparcels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SafeCheckoutApi->api_transactions_ulidparcels_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **parcel_write** | [**ParcelWrite**](ParcelWrite.md)| The new Parcel resource | 

### Return type

[**ParcelRead**](ParcelRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Parcel resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

