# tpdk

Tripartie
- API version: 2.0.178
  - Build date: 2024-02-07T15:33:34.209225Z[Etc/UTC]

Our API suite for the **Resolution Center** and the **Safe Checkout** features.
Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

  For more information, please visit [https://tripartie.com](https://tripartie.com)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>com.tripartie</groupId>
  <artifactId>tpdk</artifactId>
  <version>2.0.178</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'tpdk' jar has been published to maven central.
    mavenLocal()       // Needed if the 'tpdk' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "com.tripartie:tpdk:2.0.178"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/tpdk-2.0.178.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import com.tripartie.tpdk.ApiClient;
import com.tripartie.tpdk.ApiException;
import com.tripartie.tpdk.Configuration;
import com.tripartie.tpdk.auth.*;
import com.tripartie.tpdk.models.*;
import com.tripartie.tpdk.api.BrandingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging-api.tripartie.com");
    
    // Configure API key authorization: jwtPersonalKey
    ApiKeyAuth jwtPersonalKey = (ApiKeyAuth) defaultClient.getAuthentication("jwtPersonalKey");
    jwtPersonalKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwtPersonalKey.setApiKeyPrefix("Token");

    BrandingApi apiInstance = new BrandingApi(defaultClient);
    String id = "id_example"; // String | Organization identifier
    OrganizationUpdate organizationUpdate = new OrganizationUpdate(); // OrganizationUpdate | The updated Organization resource
    try {
      OrganizationRead result = apiInstance.apiOrganizationsIdPatch(id, organizationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingApi#apiOrganizationsIdPatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://staging-api.tripartie.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandingApi* | [**apiOrganizationsIdPatch**](docs/BrandingApi.md#apiOrganizationsIdPatch) | **PATCH** /organizations/{id} | Update your Organization details, branding or parameters
*BrandingApi* | [**apiOrganizationsIdiconDelete**](docs/BrandingApi.md#apiOrganizationsIdiconDelete) | **DELETE** /organizations/{id}/icon | Unset your Organization Icon
*BrandingApi* | [**apiOrganizationsIdiconPost**](docs/BrandingApi.md#apiOrganizationsIdiconPost) | **POST** /organizations/{id}/icon | Upload your Organization Icon
*BrandingApi* | [**apiOrganizationsIdlogoDelete**](docs/BrandingApi.md#apiOrganizationsIdlogoDelete) | **DELETE** /organizations/{id}/logo | Unset your Organization Logo
*BrandingApi* | [**apiOrganizationsIdlogoPost**](docs/BrandingApi.md#apiOrganizationsIdlogoPost) | **POST** /organizations/{id}/logo | Upload your Organization logo
*MediaApi* | [**apiMediasIdGet**](docs/MediaApi.md#apiMediasIdGet) | **GET** /medias/{id} | Retrieves a Media resource.
*NotificationApi* | [**apiPersonasIdnotificationsGetCollection**](docs/NotificationApi.md#apiPersonasIdnotificationsGetCollection) | **GET** /personas/{id}/notifications | Retrieve pending notifications for Persona
*NotificationApi* | [**apiPersonasPersonaIdnotificationsIdPatch**](docs/NotificationApi.md#apiPersonasPersonaIdnotificationsIdPatch) | **PATCH** /personas/{personaId}/notifications/{id} | Mark as read/unread a notification for Persona
*NotificationApi* | [**apiUsersIdnotificationsGetCollection**](docs/NotificationApi.md#apiUsersIdnotificationsGetCollection) | **GET** /users/{id}/notifications | Retrieves the collection of Notification resources.
*NotificationApi* | [**apiUsersUserIdnotificationsIdPatch**](docs/NotificationApi.md#apiUsersUserIdnotificationsIdPatch) | **PATCH** /users/{userId}/notifications/{id} | Mark as read/unread a notification for User
*OrganizationApi* | [**apiOrganizationsGetCollection**](docs/OrganizationApi.md#apiOrganizationsGetCollection) | **GET** /organizations | Retrieves the collection of Organization resources.
*OrganizationApi* | [**apiOrganizationsIdGet**](docs/OrganizationApi.md#apiOrganizationsIdGet) | **GET** /organizations/{id} | Retrieves a Organization resource.
*PersonaApi* | [**apiPersonasGetCollection**](docs/PersonaApi.md#apiPersonasGetCollection) | **GET** /personas | Retrieves the collection of Persona resources.
*PersonaApi* | [**apiPersonasIdDelete**](docs/PersonaApi.md#apiPersonasIdDelete) | **DELETE** /personas/{id} | Unregister a Persona (Your customer)
*PersonaApi* | [**apiPersonasIdGet**](docs/PersonaApi.md#apiPersonasIdGet) | **GET** /personas/{id} | Retrieves a Persona resource.
*PersonaApi* | [**apiPersonasIdPatch**](docs/PersonaApi.md#apiPersonasIdPatch) | **PATCH** /personas/{id} | Updates the Persona resource.
*PersonaApi* | [**apiPersonasIdtokenPost**](docs/PersonaApi.md#apiPersonasIdtokenPost) | **POST** /personas/{id}/token | Issue authenticated URL for single end-user
*PersonaApi* | [**apiPersonasPost**](docs/PersonaApi.md#apiPersonasPost) | **POST** /personas | Register a Persona (Your customer)
*ResolutionCenterApi* | [**apiDisputesGetCollection**](docs/ResolutionCenterApi.md#apiDisputesGetCollection) | **GET** /disputes | Retrieves the collection of Dispute resources.
*ResolutionCenterApi* | [**apiDisputesPost**](docs/ResolutionCenterApi.md#apiDisputesPost) | **POST** /disputes | Draft a standalone Dispute
*ResolutionCenterApi* | [**apiDisputesUlidDelete**](docs/ResolutionCenterApi.md#apiDisputesUlidDelete) | **DELETE** /disputes/{ulid} | Abandon claims on Dispute
*ResolutionCenterApi* | [**apiDisputesUlidGet**](docs/ResolutionCenterApi.md#apiDisputesUlidGet) | **GET** /disputes/{ulid} | Retrieves a Dispute resource.
*ResolutionCenterApi* | [**apiDisputesUlidPatch**](docs/ResolutionCenterApi.md#apiDisputesUlidPatch) | **PATCH** /disputes/{ulid} | Update the Dispute
*ResolutionCenterApi* | [**apiDisputesUlidevaluationsPost**](docs/ResolutionCenterApi.md#apiDisputesUlidevaluationsPost) | **POST** /disputes/{ulid}/evaluations | Submit an Evaluation for the Dispute
*ResolutionCenterApi* | [**apiDisputesUlidevidencesGetCollection**](docs/ResolutionCenterApi.md#apiDisputesUlidevidencesGetCollection) | **GET** /disputes/{ulid}/evidences | Retrieve all Evidences in Dispute
*ResolutionCenterApi* | [**apiDisputesUlidevidencesIdDelete**](docs/ResolutionCenterApi.md#apiDisputesUlidevidencesIdDelete) | **DELETE** /disputes/{ulid}/evidences/{id} | Withdraw an Evidence from a Dispute
*ResolutionCenterApi* | [**apiDisputesUlidevidencesIdmediaPost**](docs/ResolutionCenterApi.md#apiDisputesUlidevidencesIdmediaPost) | **POST** /disputes/{ulid}/evidences/{id}/media | Upload attachment in regard of described Evidence
*ResolutionCenterApi* | [**apiDisputesUlidevidencesPost**](docs/ResolutionCenterApi.md#apiDisputesUlidevidencesPost) | **POST** /disputes/{ulid}/evidences | Submit an Evidence to the Dispute case
*ResolutionCenterApi* | [**apiDisputesUlidparcelsGetCollection**](docs/ResolutionCenterApi.md#apiDisputesUlidparcelsGetCollection) | **GET** /disputes/{ulid}/parcels | Retrieves the collection of Parcel resources.
*ResolutionCenterApi* | [**apiDisputesUlidparcelsIdDelete**](docs/ResolutionCenterApi.md#apiDisputesUlidparcelsIdDelete) | **DELETE** /disputes/{ulid}/parcels/{id} | Removes the Parcel resource.
*ResolutionCenterApi* | [**apiDisputesUlidparcelsPost**](docs/ResolutionCenterApi.md#apiDisputesUlidparcelsPost) | **POST** /disputes/{ulid}/parcels | Creates a Parcel resource.
*ResolutionCenterApi* | [**apiOffersUlidmediasPost**](docs/ResolutionCenterApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer
*SafeCheckoutApi* | [**apiOffersGetCollection**](docs/SafeCheckoutApi.md#apiOffersGetCollection) | **GET** /offers | Read issued Offers
*SafeCheckoutApi* | [**apiOffersPost**](docs/SafeCheckoutApi.md#apiOffersPost) | **POST** /offers | Create an Offer and retrieve url
*SafeCheckoutApi* | [**apiOffersUlidGet**](docs/SafeCheckoutApi.md#apiOffersUlidGet) | **GET** /offers/{ulid} | Read an Offer
*SafeCheckoutApi* | [**apiOffersUlidmediasIdDelete**](docs/SafeCheckoutApi.md#apiOffersUlidmediasIdDelete) | **DELETE** /offers/{ulid}/medias/{id} | Removes the Media resource.
*SafeCheckoutApi* | [**apiOffersUlidmediasPost**](docs/SafeCheckoutApi.md#apiOffersUlidmediasPost) | **POST** /offers/{ulid}/medias | Upload a picture for a given Offer
*SafeCheckoutApi* | [**apiOffersUlidtransactionsGetCollection**](docs/SafeCheckoutApi.md#apiOffersUlidtransactionsGetCollection) | **GET** /offers/{ulid}/transactions | Retrieve Payment Intents for Offer
*SafeCheckoutApi* | [**apiOffersUlidtransactionsIdevaluationsPost**](docs/SafeCheckoutApi.md#apiOffersUlidtransactionsIdevaluationsPost) | **POST** /offers/{ulid}/transactions/{id}/evaluations | Submit an Evaluation for the Offer
*SafeCheckoutApi* | [**apiOffersUlidtransactionsPost**](docs/SafeCheckoutApi.md#apiOffersUlidtransactionsPost) | **POST** /offers/{ulid}/transactions | Create a Payment Intent for Offer
*SafeCheckoutApi* | [**apiPersonasIdoffersDelete**](docs/SafeCheckoutApi.md#apiPersonasIdoffersDelete) | **DELETE** /personas/{id}/offers | Revoke an Offer for given Persona
*SafeCheckoutApi* | [**apiPersonasIdoffersGetCollection**](docs/SafeCheckoutApi.md#apiPersonasIdoffersGetCollection) | **GET** /personas/{id}/offers | List or Search Offers for given Persona
*SafeCheckoutApi* | [**apiPersonasIdoffersPatch**](docs/SafeCheckoutApi.md#apiPersonasIdoffersPatch) | **PATCH** /personas/{id}/offers | Update an Offer for given Persona
*SafeCheckoutApi* | [**apiPersonasIdoffersPost**](docs/SafeCheckoutApi.md#apiPersonasIdoffersPost) | **POST** /personas/{id}/offers | Create an Offer for given Persona
*SafeCheckoutApi* | [**apiTransactionsGetCollection**](docs/SafeCheckoutApi.md#apiTransactionsGetCollection) | **GET** /transactions | Retrieves the collection of Transaction resources.
*SafeCheckoutApi* | [**apiTransactionsUliddisputeDelete**](docs/SafeCheckoutApi.md#apiTransactionsUliddisputeDelete) | **DELETE** /transactions/{ulid}/dispute | Abandon claims on Dispute
*SafeCheckoutApi* | [**apiTransactionsUliddisputeGet**](docs/SafeCheckoutApi.md#apiTransactionsUliddisputeGet) | **GET** /transactions/{ulid}/dispute | Read Dispute from existing Transaction
*SafeCheckoutApi* | [**apiTransactionsUliddisputePatch**](docs/SafeCheckoutApi.md#apiTransactionsUliddisputePatch) | **PATCH** /transactions/{ulid}/dispute | Interact with a Dispute
*SafeCheckoutApi* | [**apiTransactionsUliddisputePost**](docs/SafeCheckoutApi.md#apiTransactionsUliddisputePost) | **POST** /transactions/{ulid}/dispute | Open a Dispute related to existing Transaction
*SafeCheckoutApi* | [**apiTransactionsUlidparcelsGetCollection**](docs/SafeCheckoutApi.md#apiTransactionsUlidparcelsGetCollection) | **GET** /transactions/{ulid}/parcels | Read shipments from Transaction
*SafeCheckoutApi* | [**apiTransactionsUlidparcelsIdDelete**](docs/SafeCheckoutApi.md#apiTransactionsUlidparcelsIdDelete) | **DELETE** /transactions/{ulid}/parcels/{id} | Withdraw shipment from Transaction
*SafeCheckoutApi* | [**apiTransactionsUlidparcelsPost**](docs/SafeCheckoutApi.md#apiTransactionsUlidparcelsPost) | **POST** /transactions/{ulid}/parcels | Manually declare package shipped for Transaction
*UserApi* | [**apiApiClientsGetCollection**](docs/UserApi.md#apiApiClientsGetCollection) | **GET** /api-clients | Retrieves the collection of ApiClient resources.
*UserApi* | [**apiApiClientsIdentifierDelete**](docs/UserApi.md#apiApiClientsIdentifierDelete) | **DELETE** /api-clients/{identifier} | Removes the ApiClient resource.
*UserApi* | [**apiApiClientsIdentifierGet**](docs/UserApi.md#apiApiClientsIdentifierGet) | **GET** /api-clients/{identifier} | Retrieves a ApiClient resource.
*UserApi* | [**apiApiClientsPost**](docs/UserApi.md#apiApiClientsPost) | **POST** /api-clients | Creates a ApiClient resource.
*UserApi* | [**apiInvitePost**](docs/UserApi.md#apiInvitePost) | **POST** /invite | Organization invite
*UserApi* | [**apiMeGet**](docs/UserApi.md#apiMeGet) | **GET** /me | Retrieves a User resource.
*UserApi* | [**apiPersonasauthenticationPost**](docs/UserApi.md#apiPersonasauthenticationPost) | **POST** /personas/authentication | Persona Authentication
*UserApi* | [**apiPersonasmeGet**](docs/UserApi.md#apiPersonasmeGet) | **GET** /personas/me | Retrieve your authenticated Persona
*UserApi* | [**apiPersonasregisterPost**](docs/UserApi.md#apiPersonasregisterPost) | **POST** /personas/register | Persona external registration
*UserApi* | [**apiRegisterPost**](docs/UserApi.md#apiRegisterPost) | **POST** /register | Organization onboarding
*UserApi* | [**apiUsersGetCollection**](docs/UserApi.md#apiUsersGetCollection) | **GET** /users | Retrieves the collection of User resources.
*UserApi* | [**apiUsersIdDelete**](docs/UserApi.md#apiUsersIdDelete) | **DELETE** /users/{id} | Removes the User resource.
*UserApi* | [**apiUsersIdGet**](docs/UserApi.md#apiUsersIdGet) | **GET** /users/{id} | Retrieves a User resource.
*UserApi* | [**apiUsersIdPatch**](docs/UserApi.md#apiUsersIdPatch) | **PATCH** /users/{id} | Updates the User resource.
*UserApi* | [**apiUsersIdavatarDelete**](docs/UserApi.md#apiUsersIdavatarDelete) | **DELETE** /users/{id}/avatar | Unset your personal avatar
*UserApi* | [**apiUsersIdavatarPost**](docs/UserApi.md#apiUsersIdavatarPost) | **POST** /users/{id}/avatar | Upload your personal avatar
*UserApi* | [**apiUsersIdemailPatch**](docs/UserApi.md#apiUsersIdemailPatch) | **PATCH** /users/{id}/email | Update user email
*UserApi* | [**apiUsersIdemailValidationPatch**](docs/UserApi.md#apiUsersIdemailValidationPatch) | **PATCH** /users/{id}/email-validation | Validate email ownership
*UserApi* | [**apiUsersIdenablePatch**](docs/UserApi.md#apiUsersIdenablePatch) | **PATCH** /users/{id}/enable | Updates the User resource.
*UserApi* | [**apiUsersIdpasswordPatch**](docs/UserApi.md#apiUsersIdpasswordPatch) | **PATCH** /users/{id}/password | Updates the User resource.
*UserApi* | [**apiUsersIdtotpSetupPatch**](docs/UserApi.md#apiUsersIdtotpSetupPatch) | **PATCH** /users/{id}/totp-setup | Updates the User resource.
*UserApi* | [**apiUsersIdtotpTogglePatch**](docs/UserApi.md#apiUsersIdtotpTogglePatch) | **PATCH** /users/{id}/totp-toggle | Updates the User resource.
*UserApi* | [**authenticationPost**](docs/UserApi.md#authenticationPost) | **POST** /authentication | User authentication
*WebhookApi* | [**apiWebhookHistoriesGetCollection**](docs/WebhookApi.md#apiWebhookHistoriesGetCollection) | **GET** /webhook-histories | Retrieves the collection of WebhookHistory resources.
*WebhookApi* | [**apiWebhookHistoriesIdGet**](docs/WebhookApi.md#apiWebhookHistoriesIdGet) | **GET** /webhook-histories/{id} | Retrieves a WebhookHistory resource.
*WebhookApi* | [**apiWebhookHistoriesIdPut**](docs/WebhookApi.md#apiWebhookHistoriesIdPut) | **PUT** /webhook-histories/{id} | Replay a Webhook that ended up in failure
*WebhookApi* | [**apiWebhookSubscriptionsGetCollection**](docs/WebhookApi.md#apiWebhookSubscriptionsGetCollection) | **GET** /webhook-subscriptions | Retrieves the collection of WebhookSubscription resources.
*WebhookApi* | [**apiWebhookSubscriptionsIdDelete**](docs/WebhookApi.md#apiWebhookSubscriptionsIdDelete) | **DELETE** /webhook-subscriptions/{id} | Removes the WebhookSubscription resource.
*WebhookApi* | [**apiWebhookSubscriptionsPost**](docs/WebhookApi.md#apiWebhookSubscriptionsPost) | **POST** /webhook-subscriptions | Subscribe to Event(s)


## Documentation for Models

 - [AccessError](docs/AccessError.md)
 - [Address](docs/Address.md)
 - [AddressIndependentWrite](docs/AddressIndependentWrite.md)
 - [AddressUpdate](docs/AddressUpdate.md)
 - [AddressWrite](docs/AddressWrite.md)
 - [ApiClientPostCreationRead](docs/ApiClientPostCreationRead.md)
 - [ApiClientRead](docs/ApiClientRead.md)
 - [ApiClientWrite](docs/ApiClientWrite.md)
 - [AuthError](docs/AuthError.md)
 - [DisputeCollectionRead](docs/DisputeCollectionRead.md)
 - [DisputeDisputeRead](docs/DisputeDisputeRead.md)
 - [DisputeIndependentWrite](docs/DisputeIndependentWrite.md)
 - [DisputePostCreationRead](docs/DisputePostCreationRead.md)
 - [DisputeRead](docs/DisputeRead.md)
 - [DisputeUpdate](docs/DisputeUpdate.md)
 - [DisputeWrite](docs/DisputeWrite.md)
 - [EvaluationRead](docs/EvaluationRead.md)
 - [EvaluationWrite](docs/EvaluationWrite.md)
 - [Evidence](docs/Evidence.md)
 - [EvidenceRead](docs/EvidenceRead.md)
 - [EvidenceWrite](docs/EvidenceWrite.md)
 - [GenericError](docs/GenericError.md)
 - [InvalidQueryError](docs/InvalidQueryError.md)
 - [Media](docs/Media.md)
 - [MediaAuthenticatedRead](docs/MediaAuthenticatedRead.md)
 - [MediaCollectionRead](docs/MediaCollectionRead.md)
 - [MediaDisputeRead](docs/MediaDisputeRead.md)
 - [MediaRead](docs/MediaRead.md)
 - [MediaUserRead](docs/MediaUserRead.md)
 - [MessageError](docs/MessageError.md)
 - [Metadata](docs/Metadata.md)
 - [MetadataDisputeRead](docs/MetadataDisputeRead.md)
 - [MetadataIndependentWrite](docs/MetadataIndependentWrite.md)
 - [MetadataRead](docs/MetadataRead.md)
 - [MetadataUpdate](docs/MetadataUpdate.md)
 - [MetadataWrite](docs/MetadataWrite.md)
 - [NotFoundError](docs/NotFoundError.md)
 - [NotificationRead](docs/NotificationRead.md)
 - [NotificationUpdate](docs/NotificationUpdate.md)
 - [Offer](docs/Offer.md)
 - [OfferCollectionRead](docs/OfferCollectionRead.md)
 - [OfferDisputeRead](docs/OfferDisputeRead.md)
 - [OfferIndependentWrite](docs/OfferIndependentWrite.md)
 - [OfferPostCreationRead](docs/OfferPostCreationRead.md)
 - [OfferRead](docs/OfferRead.md)
 - [OfferUpdate](docs/OfferUpdate.md)
 - [OfferWrite](docs/OfferWrite.md)
 - [OrganizationAuthenticatedRead](docs/OrganizationAuthenticatedRead.md)
 - [OrganizationCollectionRead](docs/OrganizationCollectionRead.md)
 - [OrganizationDisputeRead](docs/OrganizationDisputeRead.md)
 - [OrganizationRead](docs/OrganizationRead.md)
 - [OrganizationUpdate](docs/OrganizationUpdate.md)
 - [OrganizationUserRead](docs/OrganizationUserRead.md)
 - [OrganizationWrite](docs/OrganizationWrite.md)
 - [Parcel](docs/Parcel.md)
 - [ParcelDisputeRead](docs/ParcelDisputeRead.md)
 - [ParcelIndependentWrite](docs/ParcelIndependentWrite.md)
 - [ParcelRead](docs/ParcelRead.md)
 - [ParcelWrite](docs/ParcelWrite.md)
 - [Persona](docs/Persona.md)
 - [PersonaAuthReturn](docs/PersonaAuthReturn.md)
 - [PersonaCollectionRead](docs/PersonaCollectionRead.md)
 - [PersonaDisputeRead](docs/PersonaDisputeRead.md)
 - [PersonaExternalAuth](docs/PersonaExternalAuth.md)
 - [PersonaIndependentWrite](docs/PersonaIndependentWrite.md)
 - [PersonaPostAuthRead](docs/PersonaPostAuthRead.md)
 - [PersonaRead](docs/PersonaRead.md)
 - [PersonaRegister](docs/PersonaRegister.md)
 - [PersonaTokenWrite](docs/PersonaTokenWrite.md)
 - [PersonaUpdate](docs/PersonaUpdate.md)
 - [PersonaWrite](docs/PersonaWrite.md)
 - [RateLimitError](docs/RateLimitError.md)
 - [TransactionCollectionRead](docs/TransactionCollectionRead.md)
 - [TransactionDisputeRead](docs/TransactionDisputeRead.md)
 - [TransactionIndependentWrite](docs/TransactionIndependentWrite.md)
 - [TransactionRead](docs/TransactionRead.md)
 - [UnprocessableEntity](docs/UnprocessableEntity.md)
 - [UnprocessableEntityViolationsInner](docs/UnprocessableEntityViolationsInner.md)
 - [User](docs/User.md)
 - [UserAuthenticatedRead](docs/UserAuthenticatedRead.md)
 - [UserCollectionRead](docs/UserCollectionRead.md)
 - [UserEmailValidationWrite](docs/UserEmailValidationWrite.md)
 - [UserInvite](docs/UserInvite.md)
 - [UserJwtCreated](docs/UserJwtCreated.md)
 - [UserJwtWrite](docs/UserJwtWrite.md)
 - [UserPostRegisterRead](docs/UserPostRegisterRead.md)
 - [UserTotpSetupRead](docs/UserTotpSetupRead.md)
 - [UserTotpToggleWrite](docs/UserTotpToggleWrite.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [UserUserEmailUpdate](docs/UserUserEmailUpdate.md)
 - [UserUserPasswordUpdate](docs/UserUserPasswordUpdate.md)
 - [UserUserRead](docs/UserUserRead.md)
 - [UserUserSubscribed](docs/UserUserSubscribed.md)
 - [UserWrite](docs/UserWrite.md)
 - [View](docs/View.md)
 - [ViewDisputeRead](docs/ViewDisputeRead.md)
 - [ViewRead](docs/ViewRead.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookHistoryCollectionRead](docs/WebhookHistoryCollectionRead.md)
 - [WebhookHistoryRead](docs/WebhookHistoryRead.md)
 - [WebhookObject](docs/WebhookObject.md)
 - [WebhookSubscriptionRead](docs/WebhookSubscriptionRead.md)
 - [WebhookSubscriptionWrite](docs/WebhookSubscriptionWrite.md)
 - [WorkflowEventDisputeRead](docs/WorkflowEventDisputeRead.md)
 - [WorkflowEventRead](docs/WorkflowEventRead.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="oauth"></a>
### oauth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
  - OFFER_READ: Read-only operations on safe-checkout offers
  - OFFER_WRITE: Write permissions on safe-checkout offers
  - DISPUTE_READ: Read-only operations on disputes
  - DISPUTE_WRITE: Write permissions on disputes
  - DISPUTE_ARBITRATION: Update permission on disputes for manual arbitration only
  - ORGANIZATION_READ: Read organization details and stats
  - RULING_READ: Read custom rules applied to the dispute resolution program
  - RULING_WRITE: Write custom rules applied to the dispute resolution program
  - PERSONA_READ: Read operations on the shared user-base knowledge
  - PERSONA_WRITE: Write permissions on the shared user-base knowledge
  - PERSONA_AUTH: Capability to issue short-term lived authenticated URL
  - INTERNAL_WRITE: Special internal scope

<a id="jwtPersonalKey"></a>
### jwtPersonalKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="personaAuthKey"></a>
### personaAuthKey

- **Type**: API key
- **API key parameter name**: X-Persona-Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

noc@tripartie.com

