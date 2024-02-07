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


package com.tripartie.tpdk.api;

import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.model.AccessError;
import com.tripartie.tpdk.model.AuthError;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.InvalidQueryError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.PersonaCollectionRead;
import com.tripartie.tpdk.model.PersonaPostAuthRead;
import com.tripartie.tpdk.model.PersonaRead;
import com.tripartie.tpdk.model.PersonaTokenWrite;
import com.tripartie.tpdk.model.PersonaUpdate;
import com.tripartie.tpdk.model.PersonaWrite;
import com.tripartie.tpdk.model.RateLimitError;
import com.tripartie.tpdk.model.UnprocessableEntity;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PersonaApi
 */
@Disabled
public class PersonaApiTest {

    private final PersonaApi api = new PersonaApi();

    /**
     * Retrieves the collection of Persona resources.
     *
     * Retrieves the collection of Persona resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasGetCollectionTest() throws ApiException {
        Integer page = null;
        String firstName = null;
        String lastName = null;
        String email = null;
        List<String> email2 = null;
        String mobilePhoneNumber = null;
        List<String> mobilePhoneNumber2 = null;
        String gender = null;
        String orderCreatedAt = null;
        String createdAtBefore = null;
        String createdAtStrictlyBefore = null;
        String createdAtAfter = null;
        String createdAtStrictlyAfter = null;
        String dateOfBirthBefore = null;
        String dateOfBirthStrictlyBefore = null;
        String dateOfBirthAfter = null;
        String dateOfBirthStrictlyAfter = null;
        List<String> metadata = null;
        List<PersonaCollectionRead> response = api.apiPersonasGetCollection(page, firstName, lastName, email, email2, mobilePhoneNumber, mobilePhoneNumber2, gender, orderCreatedAt, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, dateOfBirthBefore, dateOfBirthStrictlyBefore, dateOfBirthAfter, dateOfBirthStrictlyAfter, metadata);
        // TODO: test validations
    }

    /**
     * Unregister a Persona (Your customer)
     *
     * You **MAY** unregister (or free the email/phone number) your Persona entry using that endpoint. *Please note that* this operation will fail if that Persona have any ongoing operations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasIdDeleteTest() throws ApiException {
        String id = null;
        api.apiPersonasIdDelete(id);
        // TODO: test validations
    }

    /**
     * Retrieves a Persona resource.
     *
     * Retrieves a Persona resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasIdGetTest() throws ApiException {
        String id = null;
        PersonaRead response = api.apiPersonasIdGet(id);
        // TODO: test validations
    }

    /**
     * Updates the Persona resource.
     *
     * Update your Persona (eg. your customer/user entry) through that API call. _Beware that updating_ **email** and/or the **mobile phone number** must be done using non reserved values. Otherwise this operation will be rejected.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasIdPatchTest() throws ApiException {
        String id = null;
        PersonaUpdate personaUpdate = null;
        PersonaRead response = api.apiPersonasIdPatch(id, personaUpdate);
        // TODO: test validations
    }

    /**
     * Issue authenticated URL for single end-user
     *
     * Without this, your users may be required to pass a MFA challenge even if they are already logged-in from your website. Pass the URL you wish your user access, either a Dispute or Safe-checkout resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasIdtokenPostTest() throws ApiException {
        String id = null;
        PersonaTokenWrite personaTokenWrite = null;
        PersonaPostAuthRead response = api.apiPersonasIdtokenPost(id, personaTokenWrite);
        // TODO: test validations
    }

    /**
     * Register a Persona (Your customer)
     *
     * You should not register your whole database of users, only those who are concerned by a Safe-checkout or Dispute operation. One Persona entry for your organization can be assigned as a seller or buyer.  **Notes:**   - (i) There is a unique constraint for the mobile phone numbers and email.   - (ii) You will have to issue a DELETE operation on a Persona that withhold a specific phone number or email.   - (iii) You are NOT REQUIRED to provide email OR a mobile phone number but it is highly recommended, if none provided the email will be generated as &#39;{ulid}@your-domain.tld&#39;. In that case, please specify at least one metadata in order to find your entry with ease.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasPostTest() throws ApiException {
        PersonaWrite personaWrite = null;
        PersonaRead response = api.apiPersonasPost(personaWrite);
        // TODO: test validations
    }

}
