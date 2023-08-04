# tpdk.ResolutionCenterApi

All URIs are relative to *https://staging-api.tripartie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_disputes_get_collection**](ResolutionCenterApi.md#api_disputes_get_collection) | **GET** /disputes | Retrieves the collection of Dispute resources.
[**api_disputes_post**](ResolutionCenterApi.md#api_disputes_post) | **POST** /disputes | Draft a standalone Dispute
[**api_disputes_ulid_delete**](ResolutionCenterApi.md#api_disputes_ulid_delete) | **DELETE** /disputes/{ulid} | Abandon claims on Dispute
[**api_disputes_ulid_get**](ResolutionCenterApi.md#api_disputes_ulid_get) | **GET** /disputes/{ulid} | Retrieves a Dispute resource.
[**api_disputes_ulid_patch**](ResolutionCenterApi.md#api_disputes_ulid_patch) | **PATCH** /disputes/{ulid} | Update the Dispute
[**api_disputes_ulidevaluations_post**](ResolutionCenterApi.md#api_disputes_ulidevaluations_post) | **POST** /disputes/{ulid}/evaluations | Submit an Evaluation for the Dispute
[**api_disputes_ulidevidences_get_collection**](ResolutionCenterApi.md#api_disputes_ulidevidences_get_collection) | **GET** /disputes/{ulid}/evidences | Retrieve all Evidences in Dispute
[**api_disputes_ulidevidences_id_delete**](ResolutionCenterApi.md#api_disputes_ulidevidences_id_delete) | **DELETE** /disputes/{ulid}/evidences/{id} | Withdraw an Evidence from a Dispute
[**api_disputes_ulidevidences_idmedia_post**](ResolutionCenterApi.md#api_disputes_ulidevidences_idmedia_post) | **POST** /disputes/{ulid}/evidences/{id}/media | Upload attachment in regard of described Evidence
[**api_disputes_ulidevidences_post**](ResolutionCenterApi.md#api_disputes_ulidevidences_post) | **POST** /disputes/{ulid}/evidences | Submit an Evidence to the Dispute case
[**api_disputes_ulidparcels_get_collection**](ResolutionCenterApi.md#api_disputes_ulidparcels_get_collection) | **GET** /disputes/{ulid}/parcels | Retrieves the collection of Parcel resources.
[**api_disputes_ulidparcels_id_delete**](ResolutionCenterApi.md#api_disputes_ulidparcels_id_delete) | **DELETE** /disputes/{ulid}/parcels/{id} | Removes the Parcel resource.
[**api_disputes_ulidparcels_id_get**](ResolutionCenterApi.md#api_disputes_ulidparcels_id_get) | **GET** /disputes/{ulid}/parcels/{id} | Read single parcel state
[**api_disputes_ulidparcels_post**](ResolutionCenterApi.md#api_disputes_ulidparcels_post) | **POST** /disputes/{ulid}/parcels | Creates a Parcel resource.
[**api_offers_ulidmedias_post**](ResolutionCenterApi.md#api_offers_ulidmedias_post) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer


# **api_disputes_get_collection**
> List[DisputeCollectionRead] api_disputes_get_collection(page=page, order_created_at=order_created_at, order_status=order_status, order_updated_at=order_updated_at, transaction_offer_title=transaction_offer_title, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, status=status, transaction_status=transaction_status, exists_recommended_solution=exists_recommended_solution, exists_chosen_solution=exists_chosen_solution, exists_counter_solution=exists_counter_solution, exists_platform_solution=exists_platform_solution, metadata=metadata, transaction_metadata=transaction_metadata, transaction_offer_metadata=transaction_offer_metadata)

Retrieves the collection of Dispute resources.

Retrieves the collection of Dispute resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.dispute_collection_read import DisputeCollectionRead
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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)
    order_created_at = 'order_created_at_example' # str |  (optional)
    order_status = 'order_status_example' # str |  (optional)
    order_updated_at = 'order_updated_at_example' # str |  (optional)
    transaction_offer_title = 'transaction_offer_title_example' # str |  (optional)
    created_at_before = 'created_at_before_example' # str |  (optional)
    created_at_strictly_before = 'created_at_strictly_before_example' # str |  (optional)
    created_at_after = 'created_at_after_example' # str |  (optional)
    created_at_strictly_after = 'created_at_strictly_after_example' # str |  (optional)
    status = 'CREATED' # str | Filter on a limited subset of status (optional)
    transaction_status = 'CREATED' # str | Filter on a limited subset of transaction.status (optional)
    exists_recommended_solution = True # bool |  (optional)
    exists_chosen_solution = True # bool |  (optional)
    exists_counter_solution = True # bool |  (optional)
    exists_platform_solution = True # bool |  (optional)
    metadata = ['[\"External-ID\",\"1254A\"]'] # List[str] | Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    transaction_metadata = ['[\"External-ID\",\"1254A\"]'] # List[str] | Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)
    transaction_offer_metadata = ['[\"External-ID\",\"1254A\"]'] # List[str] | Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \"null\" for desired value. (optional)

    try:
        # Retrieves the collection of Dispute resources.
        api_response = api_instance.api_disputes_get_collection(page=page, order_created_at=order_created_at, order_status=order_status, order_updated_at=order_updated_at, transaction_offer_title=transaction_offer_title, created_at_before=created_at_before, created_at_strictly_before=created_at_strictly_before, created_at_after=created_at_after, created_at_strictly_after=created_at_strictly_after, status=status, transaction_status=transaction_status, exists_recommended_solution=exists_recommended_solution, exists_chosen_solution=exists_chosen_solution, exists_counter_solution=exists_counter_solution, exists_platform_solution=exists_platform_solution, metadata=metadata, transaction_metadata=transaction_metadata, transaction_offer_metadata=transaction_offer_metadata)
        print("The response of ResolutionCenterApi->api_disputes_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]
 **order_created_at** | **str**|  | [optional] 
 **order_status** | **str**|  | [optional] 
 **order_updated_at** | **str**|  | [optional] 
 **transaction_offer_title** | **str**|  | [optional] 
 **created_at_before** | **str**|  | [optional] 
 **created_at_strictly_before** | **str**|  | [optional] 
 **created_at_after** | **str**|  | [optional] 
 **created_at_strictly_after** | **str**|  | [optional] 
 **status** | **str**| Filter on a limited subset of status | [optional] 
 **transaction_status** | **str**| Filter on a limited subset of transaction.status | [optional] 
 **exists_recommended_solution** | **bool**|  | [optional] 
 **exists_chosen_solution** | **bool**|  | [optional] 
 **exists_counter_solution** | **bool**|  | [optional] 
 **exists_platform_solution** | **bool**|  | [optional] 
 **metadata** | [**List[str]**](str.md)| Flattened OrderedMap for metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **transaction_metadata** | [**List[str]**](str.md)| Flattened OrderedMap for transaction.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 
 **transaction_offer_metadata** | [**List[str]**](str.md)| Flattened OrderedMap for transaction.offer.metadata. Must be a multiple of two items count. Explicitly set \&quot;null\&quot; for desired value. | [optional] 

### Return type

[**List[DisputeCollectionRead]**](DisputeCollectionRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_post**
> DisputePostCreationRead api_disputes_post(dispute_independent_write)

Draft a standalone Dispute

Create a draft dispute to be filled by an alleged aggrieved customer. Do not use that endpoint if the transaction took place using our safe-checkout tunnel. This endpoint return a unique URL that can be accessed by both the complainant and seller (if individual).  **Note:** You can generate at your own discretion tokens for both parties, thus avoiding the secondary authentication.

### Example

* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.dispute_independent_write import DisputeIndependentWrite
from tpdk.models.dispute_post_creation_read import DisputePostCreationRead
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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    dispute_independent_write = tpdk.DisputeIndependentWrite() # DisputeIndependentWrite | The new Dispute resource

    try:
        # Draft a standalone Dispute
        api_response = api_instance.api_disputes_post(dispute_independent_write)
        print("The response of ResolutionCenterApi->api_disputes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_independent_write** | [**DisputeIndependentWrite**](DisputeIndependentWrite.md)| The new Dispute resource | 

### Return type

[**DisputePostCreationRead**](DisputePostCreationRead.md)

### Authorization

[oauth](../README.md#oauth)

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

# **api_disputes_ulid_delete**
> api_disputes_ulid_delete(ulid)

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier

    try:
        # Abandon claims on Dispute
        api_instance.api_disputes_ulid_delete(ulid)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 

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

# **api_disputes_ulid_get**
> DisputeRead api_disputes_ulid_get(ulid)

Retrieves a Dispute resource.

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier

    try:
        # Retrieves a Dispute resource.
        api_response = api_instance.api_disputes_ulid_get(ulid)
        print("The response of ResolutionCenterApi->api_disputes_ulid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 

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

# **api_disputes_ulid_patch**
> DisputeRead api_disputes_ulid_patch(ulid, dispute_update)

Update the Dispute

Updates the Dispute resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier
    dispute_update = tpdk.DisputeUpdate() # DisputeUpdate | The updated Dispute resource

    try:
        # Update the Dispute
        api_response = api_instance.api_disputes_ulid_patch(ulid, dispute_update)
        print("The response of ResolutionCenterApi->api_disputes_ulid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulid_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 
 **dispute_update** | [**DisputeUpdate**](DisputeUpdate.md)| The updated Dispute resource | 

### Return type

[**DisputeRead**](DisputeRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

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

# **api_disputes_ulidevaluations_post**
> EvaluationRead api_disputes_ulidevaluations_post(ulid, evaluation_write)

Submit an Evaluation for the Dispute

**Only authenticated** complainant and seller **CAN** issue an evaluation **WHEN** the dispute reached a final state.

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier
    evaluation_write = tpdk.EvaluationWrite() # EvaluationWrite | The new Evaluation resource

    try:
        # Submit an Evaluation for the Dispute
        api_response = api_instance.api_disputes_ulidevaluations_post(ulid, evaluation_write)
        print("The response of ResolutionCenterApi->api_disputes_ulidevaluations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidevaluations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 
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

# **api_disputes_ulidevidences_get_collection**
> List[EvidenceRead] api_disputes_ulidevidences_get_collection(ulid)

Retrieve all Evidences in Dispute

Retrieves the collection of Evidence resources.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.evidence_read import EvidenceRead
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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 

    try:
        # Retrieve all Evidences in Dispute
        api_response = api_instance.api_disputes_ulidevidences_get_collection(ulid)
        print("The response of ResolutionCenterApi->api_disputes_ulidevidences_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidevidences_get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 

### Return type

[**List[EvidenceRead]**](EvidenceRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evidence collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_ulidevidences_id_delete**
> api_disputes_ulidevidences_id_delete(ulid, id)

Withdraw an Evidence from a Dispute

Removes the Evidence resource.

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 

    try:
        # Withdraw an Evidence from a Dispute
        api_instance.api_disputes_ulidevidences_id_delete(ulid, id)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidevidences_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Evidence resource deleted |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_ulidevidences_idmedia_post**
> MediaRead api_disputes_ulidevidences_idmedia_post(ulid, id, file=file)

Upload attachment in regard of described Evidence

Creates a Media resource.

### Example

* Api Key Authentication (personaAuthKey):
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

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 
    file = None # bytearray |  (optional)

    try:
        # Upload attachment in regard of described Evidence
        api_response = api_instance.api_disputes_ulidevidences_idmedia_post(ulid, id, file=file)
        print("The response of ResolutionCenterApi->api_disputes_ulidevidences_idmedia_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidevidences_idmedia_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **id** | **int**|  | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**MediaRead**](MediaRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

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

# **api_disputes_ulidevidences_post**
> EvidenceRead api_disputes_ulidevidences_post(ulid, evidence_write)

Submit an Evidence to the Dispute case

This action does not held the actual upload, you will have to do the upload in a dedicated request.

### Example

* Api Key Authentication (personaAuthKey):
```python
import time
import os
import tpdk
from tpdk.models.evidence_read import EvidenceRead
from tpdk.models.evidence_write import EvidenceWrite
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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    evidence_write = tpdk.EvidenceWrite() # EvidenceWrite | The new Evidence resource

    try:
        # Submit an Evidence to the Dispute case
        api_response = api_instance.api_disputes_ulidevidences_post(ulid, evidence_write)
        print("The response of ResolutionCenterApi->api_disputes_ulidevidences_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidevidences_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **evidence_write** | [**EvidenceWrite**](EvidenceWrite.md)| The new Evidence resource | 

### Return type

[**EvidenceRead**](EvidenceRead.md)

### Authorization

[personaAuthKey](../README.md#personaAuthKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable entity |  -  |
**201** | Evidence resource created |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_ulidparcels_get_collection**
> List[object] api_disputes_ulidparcels_get_collection(ulid, page=page)

Retrieves the collection of Parcel resources.

Retrieves the collection of Parcel resources.

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Parcel resources.
        api_response = api_instance.api_disputes_ulidparcels_get_collection(ulid, page=page)
        print("The response of ResolutionCenterApi->api_disputes_ulidparcels_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidparcels_get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

**List[object]**

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parcel collection |  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_ulidparcels_id_delete**
> api_disputes_ulidparcels_id_delete(ulid, id)

Removes the Parcel resource.

Removes the Parcel resource.

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 

    try:
        # Removes the Parcel resource.
        api_instance.api_disputes_ulidparcels_id_delete(ulid, id)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidparcels_id_delete: %s\n" % e)
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

# **api_disputes_ulidparcels_id_get**
> ParcelRead api_disputes_ulidparcels_id_get(ulid, id)

Read single parcel state

Retrieves a Parcel resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
* OAuth Authentication (oauth):
```python
import time
import os
import tpdk
from tpdk.models.parcel_read import ParcelRead
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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    id = 56 # int | 

    try:
        # Read single parcel state
        api_response = api_instance.api_disputes_ulidparcels_id_get(ulid, id)
        print("The response of ResolutionCenterApi->api_disputes_ulidparcels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidparcels_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ParcelRead**](ParcelRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parcel resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_disputes_ulidparcels_post**
> ParcelRead api_disputes_ulidparcels_post(ulid, parcel_write)

Creates a Parcel resource.

Creates a Parcel resource.

### Example

* Api Key Authentication (jwtPersonalKey):
* Api Key Authentication (personaAuthKey):
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

# Configure API key authorization: personaAuthKey
configuration.api_key['personaAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['personaAuthKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tpdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | Dispute identifier
    parcel_write = tpdk.ParcelWrite() # ParcelWrite | The new Parcel resource

    try:
        # Creates a Parcel resource.
        api_response = api_instance.api_disputes_ulidparcels_post(ulid, parcel_write)
        print("The response of ResolutionCenterApi->api_disputes_ulidparcels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_disputes_ulidparcels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ulid** | **str**| Dispute identifier | 
 **parcel_write** | [**ParcelWrite**](ParcelWrite.md)| The new Parcel resource | 

### Return type

[**ParcelRead**](ParcelRead.md)

### Authorization

[jwtPersonalKey](../README.md#jwtPersonalKey), [personaAuthKey](../README.md#personaAuthKey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Parcel resource created |  -  |
**400** | Invalid input |  -  |
**422** | Unprocessable entity |  -  |

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
    api_instance = tpdk.ResolutionCenterApi(api_client)
    ulid = 'ulid_example' # str | 
    file = None # bytearray |  (optional)

    try:
        # Upload a picture for a given Offer
        api_response = api_instance.api_offers_ulidmedias_post(ulid, file=file)
        print("The response of ResolutionCenterApi->api_offers_ulidmedias_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionCenterApi->api_offers_ulidmedias_post: %s\n" % e)
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

