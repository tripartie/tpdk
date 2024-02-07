/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.177
 * Contact: noc@tripartie.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.tripartie.tpdk.api;

import org.tripartie.tpdk.ApiException;
import org.tripartie.tpdk.model.AccessError;
import org.tripartie.tpdk.model.AuthError;
import org.tripartie.tpdk.model.GenericError;
import org.tripartie.tpdk.model.InvalidQueryError;
import org.tripartie.tpdk.model.NotFoundError;
import org.tripartie.tpdk.model.RateLimitError;
import org.tripartie.tpdk.model.UnprocessableEntity;
import org.tripartie.tpdk.model.WebhookHistoryCollectionRead;
import org.tripartie.tpdk.model.WebhookHistoryRead;
import org.tripartie.tpdk.model.WebhookSubscriptionRead;
import org.tripartie.tpdk.model.WebhookSubscriptionWrite;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for WebhookApi
 */
@Disabled
public class WebhookApiTest {

    private final WebhookApi api = new WebhookApi();

    /**
     * Retrieves the collection of WebhookHistory resources.
     *
     * Retrieves the collection of WebhookHistory resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookHistoriesGetCollectionTest() throws ApiException {
        Integer page = null;
        String event = null;
        List<String> event2 = null;
        String objectId = null;
        List<String> objectId2 = null;
        List<WebhookHistoryCollectionRead> response = api.apiWebhookHistoriesGetCollection(page, event, event2, objectId, objectId2);
        // TODO: test validations
    }

    /**
     * Retrieves a WebhookHistory resource.
     *
     * Retrieves a WebhookHistory resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookHistoriesIdGetTest() throws ApiException {
        String id = null;
        WebhookHistoryRead response = api.apiWebhookHistoriesIdGet(id);
        // TODO: test validations
    }

    /**
     * Replay a Webhook that ended up in failure
     *
     * Replaces the WebhookHistory resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookHistoriesIdPutTest() throws ApiException {
        String id = null;
        Object body = null;
        WebhookHistoryRead response = api.apiWebhookHistoriesIdPut(id, body);
        // TODO: test validations
    }

    /**
     * Retrieves the collection of WebhookSubscription resources.
     *
     * Retrieves the collection of WebhookSubscription resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookSubscriptionsGetCollectionTest() throws ApiException {
        Integer page = null;
        String event = null;
        List<WebhookSubscriptionRead> response = api.apiWebhookSubscriptionsGetCollection(page, event);
        // TODO: test validations
    }

    /**
     * Removes the WebhookSubscription resource.
     *
     * Removes the WebhookSubscription resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookSubscriptionsIdDeleteTest() throws ApiException {
        String id = null;
        api.apiWebhookSubscriptionsIdDelete(id);
        // TODO: test validations
    }

    /**
     * Subscribe to Event(s)
     *
     * Creates a WebhookSubscription resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiWebhookSubscriptionsPostTest() throws ApiException {
        WebhookSubscriptionWrite webhookSubscriptionWrite = null;
        WebhookSubscriptionRead response = api.apiWebhookSubscriptionsPost(webhookSubscriptionWrite);
        // TODO: test validations
    }

}
