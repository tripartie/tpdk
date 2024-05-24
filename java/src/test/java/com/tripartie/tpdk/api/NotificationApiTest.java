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

import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.model.AccessError;
import com.tripartie.tpdk.model.AuthError;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.InvalidQueryError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.NotificationRead;
import com.tripartie.tpdk.model.NotificationUpdate;
import com.tripartie.tpdk.model.RateLimitError;
import com.tripartie.tpdk.model.UnprocessableEntity;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NotificationApi
 */
@Disabled
public class NotificationApiTest {

    private final NotificationApi api = new NotificationApi();

    /**
     * Retrieve pending notifications for Persona
     *
     * Retrieves the collection of Notification resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasIdnotificationsGetCollectionTest() throws ApiException {
        String id = null;
        Integer page = null;
        List<NotificationRead> response = api.apiPersonasIdnotificationsGetCollection(id)
                .page(page)
                .execute();
        // TODO: test validations
    }

    /**
     * Mark as read/unread a notification for Persona
     *
     * Updates the Notification resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasPersonaIdnotificationsIdPatchTest() throws ApiException {
        String personaId = null;
        String id = null;
        NotificationUpdate notificationUpdate = null;
        NotificationRead response = api.apiPersonasPersonaIdnotificationsIdPatch(personaId, id, notificationUpdate)
                .execute();
        // TODO: test validations
    }

    /**
     * Retrieves the collection of Notification resources.
     *
     * Retrieves the collection of Notification resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdnotificationsGetCollectionTest() throws ApiException {
        String id = null;
        Integer page = null;
        List<NotificationRead> response = api.apiUsersIdnotificationsGetCollection(id)
                .page(page)
                .execute();
        // TODO: test validations
    }

    /**
     * Mark as read/unread a notification for User
     *
     * Updates the Notification resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersUserIdnotificationsIdPatchTest() throws ApiException {
        String userId = null;
        String id = null;
        NotificationUpdate notificationUpdate = null;
        NotificationRead response = api.apiUsersUserIdnotificationsIdPatch(userId, id, notificationUpdate)
                .execute();
        // TODO: test validations
    }

}
