/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.199
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


import com.tripartie.tpdk.model.Evidence;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.RateLimitError;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EvidenceApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public EvidenceApi() {
        this(Configuration.getDefaultApiClient());
    }

    public EvidenceApi(ApiClient apiClient) {
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

    private okhttp3.Call apiEvidencesIdGetCall(String id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/evidences/{id}"
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
    private okhttp3.Call apiEvidencesIdGetValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiEvidencesIdGet(Async)");
        }

        return apiEvidencesIdGetCall(id, _callback);

    }


    private ApiResponse<Evidence> apiEvidencesIdGetWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = apiEvidencesIdGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<Evidence>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    private okhttp3.Call apiEvidencesIdGetAsync(String id, final ApiCallback<Evidence> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiEvidencesIdGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<Evidence>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }

    public class APIapiEvidencesIdGetRequest {
        private final String id;

        private APIapiEvidencesIdGetRequest(String id) {
            this.id = id;
        }

        /**
         * Build call for apiEvidencesIdGet
         * @param _callback ApiCallback API callback
         * @return Call to execute
         * @throws ApiException If fail to serialize the request body object
         * @http.response.details
         <table summary="Response Details" border="1">
            <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
            <tr><td> 200 </td><td> Evidence resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
            <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
         </table>
         */
        public okhttp3.Call buildCall(final ApiCallback _callback) throws ApiException {
            return apiEvidencesIdGetCall(id, _callback);
        }

        /**
         * Execute apiEvidencesIdGet request
         * @return Evidence
         * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
         * @http.response.details
         <table summary="Response Details" border="1">
            <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
            <tr><td> 200 </td><td> Evidence resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
            <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
         </table>
         */
        public Evidence execute() throws ApiException {
            ApiResponse<Evidence> localVarResp = apiEvidencesIdGetWithHttpInfo(id);
            return localVarResp.getData();
        }

        /**
         * Execute apiEvidencesIdGet request with HTTP info returned
         * @return ApiResponse&lt;Evidence&gt;
         * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
         * @http.response.details
         <table summary="Response Details" border="1">
            <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
            <tr><td> 200 </td><td> Evidence resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
            <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
         </table>
         */
        public ApiResponse<Evidence> executeWithHttpInfo() throws ApiException {
            return apiEvidencesIdGetWithHttpInfo(id);
        }

        /**
         * Execute apiEvidencesIdGet request (asynchronously)
         * @param _callback The callback to be executed when the API call finishes
         * @return The request call
         * @throws ApiException If fail to process the API call, e.g. serializing the request body object
         * @http.response.details
         <table summary="Response Details" border="1">
            <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
            <tr><td> 200 </td><td> Evidence resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
            <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
            <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
         </table>
         */
        public okhttp3.Call executeAsync(final ApiCallback<Evidence> _callback) throws ApiException {
            return apiEvidencesIdGetAsync(id, _callback);
        }
    }

    /**
     * Retrieves a Evidence resource.
     * Retrieves a Evidence resource.
     * @param id Evidence identifier (required)
     * @return APIapiEvidencesIdGetRequest
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Evidence resource </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  * X-Rate-Limit - HTTP standardized header for rate limit consumption status <br>  </td></tr>
        <tr><td> 429 </td><td> Rate limit exhausted </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected server error </td><td>  -  </td></tr>
     </table>
     */
    public APIapiEvidencesIdGetRequest apiEvidencesIdGet(String id) {
        return new APIapiEvidencesIdGetRequest(id);
    }
}
