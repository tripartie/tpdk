/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.204
 * Contact: noc@tripartie.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.tripartie.tpdk.api;

import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.OrganizationCollectionRead;
import com.tripartie.tpdk.model.OrganizationRead;
import com.tripartie.tpdk.model.RateLimitError;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OrganizationApi
 */
@Disabled
public class OrganizationApiTest {

    private final OrganizationApi api = new OrganizationApi();

    /**
     * Retrieves the collection of Organization resources.
     *
     * Retrieves the collection of Organization resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiOrganizationsGetCollectionTest() throws ApiException {
        Integer page = null;
        Integer itemsPerPage = null;
        String name = null;
        List<OrganizationCollectionRead> response = api.apiOrganizationsGetCollection()
                .page(page)
                .itemsPerPage(itemsPerPage)
                .name(name)
                .execute();
        // TODO: test validations
    }

    /**
     * Retrieves a Organization resource.
     *
     * Retrieves a Organization resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiOrganizationsIdGetTest() throws ApiException {
        String id = null;
        OrganizationRead response = api.apiOrganizationsIdGet(id)
                .execute();
        // TODO: test validations
    }

}
