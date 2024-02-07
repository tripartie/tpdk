/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.178
 * Contact: noc@tripartie.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.tripartie.tpdk.api;

import com.tripartie.tpdk.ApiCallback;
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.ApiResponse;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.Pair;
import com.tripartie.tpdk.ProgressRequestBody;
import com.tripartie.tpdk.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.OrganizationCollectionRead;
import com.tripartie.tpdk.model.OrganizationRead;
import com.tripartie.tpdk.model.RateLimitError;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OrganizationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public OrganizationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public OrganizationApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for apiOrganizationsGetCollection
     * @param page The collection page number (optional, default to 1)
     * @param itemsPerPage The number of items per page (optional, default to 30)
     * @param name  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization collection </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiOrganizationsGetCollectionCall(Integer page, Integer itemsPerPage, String name, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/organizations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (itemsPerPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("itemsPerPage", itemsPerPage));
        }

        if (name != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("name", name));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "jwtPersonalKey", "personaAuthKey", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiOrganizationsGetCollectionValidateBeforeCall(Integer page, Integer itemsPerPage, String name, final ApiCallback _callback) throws ApiException {
        return apiOrganizationsGetCollectionCall(page, itemsPerPage, name, _callback);

    }

    /**
     * Retrieves the collection of Organization resources.
     * Retrieves the collection of Organization resources.
     * @param page The collection page number (optional, default to 1)
     * @param itemsPerPage The number of items per page (optional, default to 30)
     * @param name  (optional)
     * @return List&lt;OrganizationCollectionRead&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization collection </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public List<OrganizationCollectionRead> apiOrganizationsGetCollection(Integer page, Integer itemsPerPage, String name) throws ApiException {
        ApiResponse<List<OrganizationCollectionRead>> localVarResp = apiOrganizationsGetCollectionWithHttpInfo(page, itemsPerPage, name);
        return localVarResp.getData();
    }

    /**
     * Retrieves the collection of Organization resources.
     * Retrieves the collection of Organization resources.
     * @param page The collection page number (optional, default to 1)
     * @param itemsPerPage The number of items per page (optional, default to 30)
     * @param name  (optional)
     * @return ApiResponse&lt;List&lt;OrganizationCollectionRead&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization collection </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<OrganizationCollectionRead>> apiOrganizationsGetCollectionWithHttpInfo(Integer page, Integer itemsPerPage, String name) throws ApiException {
        okhttp3.Call localVarCall = apiOrganizationsGetCollectionValidateBeforeCall(page, itemsPerPage, name, null);
        Type localVarReturnType = new TypeToken<List<OrganizationCollectionRead>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieves the collection of Organization resources. (asynchronously)
     * Retrieves the collection of Organization resources.
     * @param page The collection page number (optional, default to 1)
     * @param itemsPerPage The number of items per page (optional, default to 30)
     * @param name  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization collection </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  * Content-Range - HTTP standardized header for partial content, used for the pagination <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiOrganizationsGetCollectionAsync(Integer page, Integer itemsPerPage, String name, final ApiCallback<List<OrganizationCollectionRead>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiOrganizationsGetCollectionValidateBeforeCall(page, itemsPerPage, name, _callback);
        Type localVarReturnType = new TypeToken<List<OrganizationCollectionRead>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiOrganizationsIdGet
     * @param id Organization identifier (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiOrganizationsIdGetCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/organizations/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "jwtPersonalKey", "personaAuthKey", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiOrganizationsIdGetValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiOrganizationsIdGet(Async)");
        }

        return apiOrganizationsIdGetCall(id, _callback);

    }

    /**
     * Retrieves a Organization resource.
     * Retrieves a Organization resource.
     * @param id Organization identifier (required)
     * @return OrganizationRead
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public OrganizationRead apiOrganizationsIdGet(String id) throws ApiException {
        ApiResponse<OrganizationRead> localVarResp = apiOrganizationsIdGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Retrieves a Organization resource.
     * Retrieves a Organization resource.
     * @param id Organization identifier (required)
     * @return ApiResponse&lt;OrganizationRead&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OrganizationRead> apiOrganizationsIdGetWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = apiOrganizationsIdGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<OrganizationRead>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieves a Organization resource. (asynchronously)
     * Retrieves a Organization resource.
     * @param id Organization identifier (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Organization resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiOrganizationsIdGetAsync(String id, final ApiCallback<OrganizationRead> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiOrganizationsIdGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<OrganizationRead>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
