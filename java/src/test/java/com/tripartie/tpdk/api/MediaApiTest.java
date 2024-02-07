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

import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.Media;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.RateLimitError;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MediaApi
 */
@Disabled
public class MediaApiTest {

    private final MediaApi api = new MediaApi();

    /**
     * Retrieves a Media resource.
     *
     * Retrieves a Media resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiMediasIdGetTest() throws ApiException {
        String id = null;
        Media response = api.apiMediasIdGet(id);
        // TODO: test validations
    }

}