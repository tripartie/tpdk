/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.194
 * Contact: noc@tripartie.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.tripartie.tpdk.api;

import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.model.AccessError;
import com.tripartie.tpdk.model.ApiClientPostCreationRead;
import com.tripartie.tpdk.model.ApiClientRead;
import com.tripartie.tpdk.model.ApiClientWrite;
import com.tripartie.tpdk.model.AuthError;
import java.io.File;
import com.tripartie.tpdk.model.GenericError;
import com.tripartie.tpdk.model.InvalidQueryError;
import com.tripartie.tpdk.model.MediaRead;
import com.tripartie.tpdk.model.MessageError;
import com.tripartie.tpdk.model.NotFoundError;
import com.tripartie.tpdk.model.PersonaAuthReturn;
import com.tripartie.tpdk.model.PersonaExternalAuth;
import com.tripartie.tpdk.model.PersonaRead;
import com.tripartie.tpdk.model.PersonaRegister;
import com.tripartie.tpdk.model.RateLimitError;
import com.tripartie.tpdk.model.UnprocessableEntity;
import com.tripartie.tpdk.model.User;
import com.tripartie.tpdk.model.UserAuthenticatedRead;
import com.tripartie.tpdk.model.UserCollectionRead;
import com.tripartie.tpdk.model.UserEmailValidationWrite;
import com.tripartie.tpdk.model.UserInvite;
import com.tripartie.tpdk.model.UserJwtCreated;
import com.tripartie.tpdk.model.UserJwtWrite;
import com.tripartie.tpdk.model.UserPostRegisterRead;
import com.tripartie.tpdk.model.UserTotpSetupRead;
import com.tripartie.tpdk.model.UserTotpToggleWrite;
import com.tripartie.tpdk.model.UserUpdate;
import com.tripartie.tpdk.model.UserUserEmailUpdate;
import com.tripartie.tpdk.model.UserUserPasswordUpdate;
import com.tripartie.tpdk.model.UserUserRead;
import com.tripartie.tpdk.model.UserUserSubscribed;
import com.tripartie.tpdk.model.UserWrite;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for UserApi
 */
@Disabled
public class UserApiTest {

    private final UserApi api = new UserApi();

    /**
     * Retrieves the collection of ApiClient resources.
     *
     * Retrieves the collection of ApiClient resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiApiClientsGetCollectionTest() throws ApiException {
        Integer page = null;
        List<ApiClientRead> response = api.apiApiClientsGetCollection(page);
        // TODO: test validations
    }

    /**
     * Removes the ApiClient resource.
     *
     * Removes the ApiClient resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiApiClientsIdentifierDeleteTest() throws ApiException {
        String identifier = null;
        api.apiApiClientsIdentifierDelete(identifier);
        // TODO: test validations
    }

    /**
     * Retrieves a ApiClient resource.
     *
     * Retrieves a ApiClient resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiApiClientsIdentifierGetTest() throws ApiException {
        String identifier = null;
        ApiClientRead response = api.apiApiClientsIdentifierGet(identifier);
        // TODO: test validations
    }

    /**
     * Creates a ApiClient resource.
     *
     * Creates a ApiClient resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiApiClientsPostTest() throws ApiException {
        ApiClientWrite apiClientWrite = null;
        ApiClientPostCreationRead response = api.apiApiClientsPost(apiClientWrite);
        // TODO: test validations
    }

    /**
     * Organization invite
     *
     * Invite a user to your organization workspace
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiInvitePostTest() throws ApiException {
        UserInvite userInvite = null;
        UserPostRegisterRead response = api.apiInvitePost(userInvite);
        // TODO: test validations
    }

    /**
     * Retrieves a User resource.
     *
     * Retrieves a User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiMeGetTest() throws ApiException {
        UserAuthenticatedRead response = api.apiMeGet();
        // TODO: test validations
    }

    /**
     * Persona Authentication
     *
     * Main route for Persona (Organization customers) to authenticate themselves. Public access, captcha protected and MFA mandatory.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasauthenticationPostTest() throws ApiException {
        PersonaExternalAuth personaExternalAuth = null;
        PersonaAuthReturn response = api.apiPersonasauthenticationPost(personaExternalAuth);
        // TODO: test validations
    }

    /**
     * Retrieve your authenticated Persona
     *
     * Retrieves a Persona resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasmeGetTest() throws ApiException {
        PersonaRead response = api.apiPersonasmeGet();
        // TODO: test validations
    }

    /**
     * Persona external registration
     *
     * Creates a Persona resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiPersonasregisterPostTest() throws ApiException {
        PersonaRegister personaRegister = null;
        PersonaRead response = api.apiPersonasregisterPost(personaRegister);
        // TODO: test validations
    }

    /**
     * Organization onboarding
     *
     * Internal-use only, protected by a captcha. Organization first-enrollment
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRegisterPostTest() throws ApiException {
        UserWrite userWrite = null;
        UserPostRegisterRead response = api.apiRegisterPost(userWrite);
        // TODO: test validations
    }

    /**
     * Retrieves the collection of User resources.
     *
     * Retrieves the collection of User resources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersGetCollectionTest() throws ApiException {
        Integer page = null;
        List<UserCollectionRead> response = api.apiUsersGetCollection(page);
        // TODO: test validations
    }

    /**
     * Removes the User resource.
     *
     * Removes the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdDeleteTest() throws ApiException {
        String id = null;
        api.apiUsersIdDelete(id);
        // TODO: test validations
    }

    /**
     * Retrieves a User resource.
     *
     * Retrieves a User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdGetTest() throws ApiException {
        String id = null;
        User response = api.apiUsersIdGet(id);
        // TODO: test validations
    }

    /**
     * Updates the User resource.
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdPatchTest() throws ApiException {
        String id = null;
        UserUpdate userUpdate = null;
        UserPostRegisterRead response = api.apiUsersIdPatch(id, userUpdate);
        // TODO: test validations
    }

    /**
     * Unset your personal avatar
     *
     * Removes the Media resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdavatarDeleteTest() throws ApiException {
        Integer id = null;
        api.apiUsersIdavatarDelete(id);
        // TODO: test validations
    }

    /**
     * Upload your personal avatar
     *
     * Creates a Media resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdavatarPostTest() throws ApiException {
        Integer id = null;
        File _file = null;
        MediaRead response = api.apiUsersIdavatarPost(id, _file);
        // TODO: test validations
    }

    /**
     * Update user email
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdemailPatchTest() throws ApiException {
        String id = null;
        UserUserEmailUpdate userUserEmailUpdate = null;
        UserUserRead response = api.apiUsersIdemailPatch(id, userUserEmailUpdate);
        // TODO: test validations
    }

    /**
     * Validate email ownership
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdemailValidationPatchTest() throws ApiException {
        String id = null;
        UserEmailValidationWrite userEmailValidationWrite = null;
        UserPostRegisterRead response = api.apiUsersIdemailValidationPatch(id, userEmailValidationWrite);
        // TODO: test validations
    }

    /**
     * Updates the User resource.
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdenablePatchTest() throws ApiException {
        String id = null;
        Object body = null;
        UserUserSubscribed response = api.apiUsersIdenablePatch(id, body);
        // TODO: test validations
    }

    /**
     * Updates the User resource.
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdpasswordPatchTest() throws ApiException {
        String id = null;
        UserUserPasswordUpdate userUserPasswordUpdate = null;
        UserUserRead response = api.apiUsersIdpasswordPatch(id, userUserPasswordUpdate);
        // TODO: test validations
    }

    /**
     * Updates the User resource.
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdtotpSetupPatchTest() throws ApiException {
        String id = null;
        Object body = null;
        UserTotpSetupRead response = api.apiUsersIdtotpSetupPatch(id, body);
        // TODO: test validations
    }

    /**
     * Updates the User resource.
     *
     * Updates the User resource.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsersIdtotpTogglePatchTest() throws ApiException {
        String id = null;
        UserTotpToggleWrite userTotpToggleWrite = null;
        Object response = api.apiUsersIdtotpTogglePatch(id, userTotpToggleWrite);
        // TODO: test validations
    }

    /**
     * User authentication
     *
     * This endpoint is protected by a captcha, do not try to use it to consume our API. IP/CIDR to be banned upon fraudulent/irregular usage. Follow the oauth 2.0 authentication challenge as described in the documentation.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void authenticationPostTest() throws ApiException {
        UserJwtWrite userJwtWrite = null;
        UserJwtCreated response = api.authenticationPost(userJwtWrite);
        // TODO: test validations
    }

}
