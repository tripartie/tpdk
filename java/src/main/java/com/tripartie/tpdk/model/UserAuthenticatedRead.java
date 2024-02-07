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


package com.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.tripartie.tpdk.model.MediaAuthenticatedRead;
import com.tripartie.tpdk.model.OrganizationAuthenticatedRead;
import java.io.IOException;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.jackson.nullable.JsonNullable;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import com.tripartie.tpdk.JSON;

/**
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T14:46:42.159671Z[Etc/UTC]")
public class UserAuthenticatedRead {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_PUBLIC_NAME = "publicName";
  @SerializedName(SERIALIZED_NAME_PUBLIC_NAME)
  private String publicName;

  public static final String SERIALIZED_NAME_ROLE_IN_COMPANY = "roleInCompany";
  @SerializedName(SERIALIZED_NAME_ROLE_IN_COMPANY)
  private String roleInCompany;

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private OffsetDateTime birthday;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  /**
   * Gets or Sets roles
   */
  @JsonAdapter(RolesEnum.Adapter.class)
  public enum RolesEnum {
    ORGANIZATION_OWNER("ROLE_ORGANIZATION_OWNER"),
    
    ADMIN("ROLE_ADMIN"),
    
    CONSULTANT("ROLE_CONSULTANT"),
    
    ACCOUNTING_MANAGER("ROLE_ACCOUNTING_MANAGER"),
    
    BILLING_MANAGER("ROLE_BILLING_MANAGER"),
    
    CUSTOMER_SERVICE("ROLE_CUSTOMER_SERVICE"),
    
    PLATFORM_SUPPORT("ROLE_PLATFORM_SUPPORT"),
    
    PLATFORM_ADMIN("ROLE_PLATFORM_ADMIN"),
    
    USER("ROLE_USER");

    private String value;

    RolesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RolesEnum fromValue(String value) {
      for (RolesEnum b : RolesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RolesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RolesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RolesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RolesEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RolesEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ROLES = "roles";
  @SerializedName(SERIALIZED_NAME_ROLES)
  private List<RolesEnum> roles = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTP_ENABLED = "totpEnabled";
  @SerializedName(SERIALIZED_NAME_TOTP_ENABLED)
  private Boolean totpEnabled;

  public static final String SERIALIZED_NAME_INTL_PHONE_NUMBER = "intlPhoneNumber";
  @SerializedName(SERIALIZED_NAME_INTL_PHONE_NUMBER)
  private String intlPhoneNumber;

  public static final String SERIALIZED_NAME_ORIGIN_COUNTRY = "originCountry";
  @SerializedName(SERIALIZED_NAME_ORIGIN_COUNTRY)
  private String originCountry;

  public static final String SERIALIZED_NAME_PREFERRED_LANGUAGE = "preferredLanguage";
  @SerializedName(SERIALIZED_NAME_PREFERRED_LANGUAGE)
  private String preferredLanguage;

  public static final String SERIALIZED_NAME_LAST_SUCCESSFUL_LOG_IN = "lastSuccessfulLogIn";
  @SerializedName(SERIALIZED_NAME_LAST_SUCCESSFUL_LOG_IN)
  private OffsetDateTime lastSuccessfulLogIn;

  public static final String SERIALIZED_NAME_AVATAR = "avatar";
  @SerializedName(SERIALIZED_NAME_AVATAR)
  private MediaAuthenticatedRead avatar;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_CONSENT_MAIL_NOTIFICATION = "consentMailNotification";
  @SerializedName(SERIALIZED_NAME_CONSENT_MAIL_NOTIFICATION)
  private Boolean consentMailNotification;

  public static final String SERIALIZED_NAME_CONSENT_MAIL_ADS = "consentMailAds";
  @SerializedName(SERIALIZED_NAME_CONSENT_MAIL_ADS)
  private Boolean consentMailAds;

  public static final String SERIALIZED_NAME_LOCKDOWN = "lockdown";
  @SerializedName(SERIALIZED_NAME_LOCKDOWN)
  private Boolean lockdown;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private OrganizationAuthenticatedRead organization;

  public static final String SERIALIZED_NAME_IRI = "iri";
  @SerializedName(SERIALIZED_NAME_IRI)
  private String iri;

  public static final String SERIALIZED_NAME_IMPERSONATING_ORGANIZATION = "impersonatingOrganization";
  @SerializedName(SERIALIZED_NAME_IMPERSONATING_ORGANIZATION)
  private Boolean impersonatingOrganization;

  public static final String SERIALIZED_NAME_2FA = "2fa";
  @SerializedName(SERIALIZED_NAME_2FA)
  private Boolean _2fa;

  public UserAuthenticatedRead() {
  }

  public UserAuthenticatedRead(
     Integer id, 
     OffsetDateTime createdAt, 
     OffsetDateTime updatedAt, 
     String iri, 
     Boolean impersonatingOrganization, 
     Boolean _2fa
  ) {
    this();
    this.id = id;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
    this.iri = iri;
    this.impersonatingOrganization = impersonatingOrganization;
    this._2fa = _2fa;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public UserAuthenticatedRead firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

   /**
   * Get firstName
   * @return firstName
  **/
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public UserAuthenticatedRead lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

   /**
   * Get lastName
   * @return lastName
  **/
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public UserAuthenticatedRead publicName(String publicName) {
    this.publicName = publicName;
    return this;
  }

   /**
   * Get publicName
   * @return publicName
  **/
  @javax.annotation.Nullable
  public String getPublicName() {
    return publicName;
  }

  public void setPublicName(String publicName) {
    this.publicName = publicName;
  }


  public UserAuthenticatedRead roleInCompany(String roleInCompany) {
    this.roleInCompany = roleInCompany;
    return this;
  }

   /**
   * Get roleInCompany
   * @return roleInCompany
  **/
  @javax.annotation.Nullable
  public String getRoleInCompany() {
    return roleInCompany;
  }

  public void setRoleInCompany(String roleInCompany) {
    this.roleInCompany = roleInCompany;
  }


  public UserAuthenticatedRead birthday(OffsetDateTime birthday) {
    this.birthday = birthday;
    return this;
  }

   /**
   * Get birthday
   * @return birthday
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getBirthday() {
    return birthday;
  }

  public void setBirthday(OffsetDateTime birthday) {
    this.birthday = birthday;
  }


  public UserAuthenticatedRead email(String email) {
    this.email = email;
    return this;
  }

   /**
   * Get email
   * @return email
  **/
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public UserAuthenticatedRead roles(List<RolesEnum> roles) {
    this.roles = roles;
    return this;
  }

  public UserAuthenticatedRead addRolesItem(RolesEnum rolesItem) {
    if (this.roles == null) {
      this.roles = new ArrayList<>();
    }
    this.roles.add(rolesItem);
    return this;
  }

   /**
   * Get roles
   * @return roles
  **/
  @javax.annotation.Nonnull
  public List<RolesEnum> getRoles() {
    return roles;
  }

  public void setRoles(List<RolesEnum> roles) {
    this.roles = roles;
  }


  public UserAuthenticatedRead totpEnabled(Boolean totpEnabled) {
    this.totpEnabled = totpEnabled;
    return this;
  }

   /**
   * Get totpEnabled
   * @return totpEnabled
  **/
  @javax.annotation.Nullable
  public Boolean getTotpEnabled() {
    return totpEnabled;
  }

  public void setTotpEnabled(Boolean totpEnabled) {
    this.totpEnabled = totpEnabled;
  }


  public UserAuthenticatedRead intlPhoneNumber(String intlPhoneNumber) {
    this.intlPhoneNumber = intlPhoneNumber;
    return this;
  }

   /**
   * Get intlPhoneNumber
   * @return intlPhoneNumber
  **/
  @javax.annotation.Nullable
  public String getIntlPhoneNumber() {
    return intlPhoneNumber;
  }

  public void setIntlPhoneNumber(String intlPhoneNumber) {
    this.intlPhoneNumber = intlPhoneNumber;
  }


  public UserAuthenticatedRead originCountry(String originCountry) {
    this.originCountry = originCountry;
    return this;
  }

   /**
   * The originating country
   * @return originCountry
  **/
  @javax.annotation.Nullable
  public String getOriginCountry() {
    return originCountry;
  }

  public void setOriginCountry(String originCountry) {
    this.originCountry = originCountry;
  }


  public UserAuthenticatedRead preferredLanguage(String preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
    return this;
  }

   /**
   * Get preferredLanguage
   * @return preferredLanguage
  **/
  @javax.annotation.Nullable
  public String getPreferredLanguage() {
    return preferredLanguage;
  }

  public void setPreferredLanguage(String preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
  }


  public UserAuthenticatedRead lastSuccessfulLogIn(OffsetDateTime lastSuccessfulLogIn) {
    this.lastSuccessfulLogIn = lastSuccessfulLogIn;
    return this;
  }

   /**
   * Get lastSuccessfulLogIn
   * @return lastSuccessfulLogIn
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getLastSuccessfulLogIn() {
    return lastSuccessfulLogIn;
  }

  public void setLastSuccessfulLogIn(OffsetDateTime lastSuccessfulLogIn) {
    this.lastSuccessfulLogIn = lastSuccessfulLogIn;
  }


  public UserAuthenticatedRead avatar(MediaAuthenticatedRead avatar) {
    this.avatar = avatar;
    return this;
  }

   /**
   * Get avatar
   * @return avatar
  **/
  @javax.annotation.Nullable
  public MediaAuthenticatedRead getAvatar() {
    return avatar;
  }

  public void setAvatar(MediaAuthenticatedRead avatar) {
    this.avatar = avatar;
  }


   /**
   * Get createdAt
   * @return createdAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



   /**
   * Get updatedAt
   * @return updatedAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  public UserAuthenticatedRead consentMailNotification(Boolean consentMailNotification) {
    this.consentMailNotification = consentMailNotification;
    return this;
  }

   /**
   * Get consentMailNotification
   * @return consentMailNotification
  **/
  @javax.annotation.Nonnull
  public Boolean getConsentMailNotification() {
    return consentMailNotification;
  }

  public void setConsentMailNotification(Boolean consentMailNotification) {
    this.consentMailNotification = consentMailNotification;
  }


  public UserAuthenticatedRead consentMailAds(Boolean consentMailAds) {
    this.consentMailAds = consentMailAds;
    return this;
  }

   /**
   * Get consentMailAds
   * @return consentMailAds
  **/
  @javax.annotation.Nonnull
  public Boolean getConsentMailAds() {
    return consentMailAds;
  }

  public void setConsentMailAds(Boolean consentMailAds) {
    this.consentMailAds = consentMailAds;
  }


  public UserAuthenticatedRead lockdown(Boolean lockdown) {
    this.lockdown = lockdown;
    return this;
  }

   /**
   * Get lockdown
   * @return lockdown
  **/
  @javax.annotation.Nonnull
  public Boolean getLockdown() {
    return lockdown;
  }

  public void setLockdown(Boolean lockdown) {
    this.lockdown = lockdown;
  }


  public UserAuthenticatedRead organization(OrganizationAuthenticatedRead organization) {
    this.organization = organization;
    return this;
  }

   /**
   * Get organization
   * @return organization
  **/
  @javax.annotation.Nullable
  public OrganizationAuthenticatedRead getOrganization() {
    return organization;
  }

  public void setOrganization(OrganizationAuthenticatedRead organization) {
    this.organization = organization;
  }


   /**
   * Get iri
   * @return iri
  **/
  @javax.annotation.Nullable
  public String getIri() {
    return iri;
  }



   /**
   * Get impersonatingOrganization
   * @return impersonatingOrganization
  **/
  @javax.annotation.Nullable
  public Boolean getImpersonatingOrganization() {
    return impersonatingOrganization;
  }



   /**
   * Get _2fa
   * @return _2fa
  **/
  @javax.annotation.Nullable
  public Boolean get2fa() {
    return _2fa;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserAuthenticatedRead userAuthenticatedRead = (UserAuthenticatedRead) o;
    return Objects.equals(this.id, userAuthenticatedRead.id) &&
        Objects.equals(this.firstName, userAuthenticatedRead.firstName) &&
        Objects.equals(this.lastName, userAuthenticatedRead.lastName) &&
        Objects.equals(this.publicName, userAuthenticatedRead.publicName) &&
        Objects.equals(this.roleInCompany, userAuthenticatedRead.roleInCompany) &&
        Objects.equals(this.birthday, userAuthenticatedRead.birthday) &&
        Objects.equals(this.email, userAuthenticatedRead.email) &&
        Objects.equals(this.roles, userAuthenticatedRead.roles) &&
        Objects.equals(this.totpEnabled, userAuthenticatedRead.totpEnabled) &&
        Objects.equals(this.intlPhoneNumber, userAuthenticatedRead.intlPhoneNumber) &&
        Objects.equals(this.originCountry, userAuthenticatedRead.originCountry) &&
        Objects.equals(this.preferredLanguage, userAuthenticatedRead.preferredLanguage) &&
        Objects.equals(this.lastSuccessfulLogIn, userAuthenticatedRead.lastSuccessfulLogIn) &&
        Objects.equals(this.avatar, userAuthenticatedRead.avatar) &&
        Objects.equals(this.createdAt, userAuthenticatedRead.createdAt) &&
        Objects.equals(this.updatedAt, userAuthenticatedRead.updatedAt) &&
        Objects.equals(this.consentMailNotification, userAuthenticatedRead.consentMailNotification) &&
        Objects.equals(this.consentMailAds, userAuthenticatedRead.consentMailAds) &&
        Objects.equals(this.lockdown, userAuthenticatedRead.lockdown) &&
        Objects.equals(this.organization, userAuthenticatedRead.organization) &&
        Objects.equals(this.iri, userAuthenticatedRead.iri) &&
        Objects.equals(this.impersonatingOrganization, userAuthenticatedRead.impersonatingOrganization) &&
        Objects.equals(this._2fa, userAuthenticatedRead._2fa);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, firstName, lastName, publicName, roleInCompany, birthday, email, roles, totpEnabled, intlPhoneNumber, originCountry, preferredLanguage, lastSuccessfulLogIn, avatar, createdAt, updatedAt, consentMailNotification, consentMailAds, lockdown, organization, iri, impersonatingOrganization, _2fa);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserAuthenticatedRead {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    publicName: ").append(toIndentedString(publicName)).append("\n");
    sb.append("    roleInCompany: ").append(toIndentedString(roleInCompany)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    roles: ").append(toIndentedString(roles)).append("\n");
    sb.append("    totpEnabled: ").append(toIndentedString(totpEnabled)).append("\n");
    sb.append("    intlPhoneNumber: ").append(toIndentedString(intlPhoneNumber)).append("\n");
    sb.append("    originCountry: ").append(toIndentedString(originCountry)).append("\n");
    sb.append("    preferredLanguage: ").append(toIndentedString(preferredLanguage)).append("\n");
    sb.append("    lastSuccessfulLogIn: ").append(toIndentedString(lastSuccessfulLogIn)).append("\n");
    sb.append("    avatar: ").append(toIndentedString(avatar)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    consentMailNotification: ").append(toIndentedString(consentMailNotification)).append("\n");
    sb.append("    consentMailAds: ").append(toIndentedString(consentMailAds)).append("\n");
    sb.append("    lockdown: ").append(toIndentedString(lockdown)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
    sb.append("    iri: ").append(toIndentedString(iri)).append("\n");
    sb.append("    impersonatingOrganization: ").append(toIndentedString(impersonatingOrganization)).append("\n");
    sb.append("    _2fa: ").append(toIndentedString(_2fa)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("id");
    openapiFields.add("firstName");
    openapiFields.add("lastName");
    openapiFields.add("publicName");
    openapiFields.add("roleInCompany");
    openapiFields.add("birthday");
    openapiFields.add("email");
    openapiFields.add("roles");
    openapiFields.add("totpEnabled");
    openapiFields.add("intlPhoneNumber");
    openapiFields.add("originCountry");
    openapiFields.add("preferredLanguage");
    openapiFields.add("lastSuccessfulLogIn");
    openapiFields.add("avatar");
    openapiFields.add("createdAt");
    openapiFields.add("updatedAt");
    openapiFields.add("consentMailNotification");
    openapiFields.add("consentMailAds");
    openapiFields.add("lockdown");
    openapiFields.add("organization");
    openapiFields.add("iri");
    openapiFields.add("impersonatingOrganization");
    openapiFields.add("2fa");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("roles");
    openapiRequiredFields.add("consentMailNotification");
    openapiRequiredFields.add("consentMailAds");
    openapiRequiredFields.add("lockdown");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to UserAuthenticatedRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserAuthenticatedRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserAuthenticatedRead is not found in the empty JSON string", UserAuthenticatedRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserAuthenticatedRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserAuthenticatedRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UserAuthenticatedRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if ((jsonObj.get("publicName") != null && !jsonObj.get("publicName").isJsonNull()) && !jsonObj.get("publicName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicName").toString()));
      }
      if ((jsonObj.get("roleInCompany") != null && !jsonObj.get("roleInCompany").isJsonNull()) && !jsonObj.get("roleInCompany").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `roleInCompany` to be a primitive type in the JSON string but got `%s`", jsonObj.get("roleInCompany").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("roles") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("roles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `roles` to be an array in the JSON string but got `%s`", jsonObj.get("roles").toString()));
      }
      if ((jsonObj.get("intlPhoneNumber") != null && !jsonObj.get("intlPhoneNumber").isJsonNull()) && !jsonObj.get("intlPhoneNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `intlPhoneNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("intlPhoneNumber").toString()));
      }
      if ((jsonObj.get("originCountry") != null && !jsonObj.get("originCountry").isJsonNull()) && !jsonObj.get("originCountry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `originCountry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("originCountry").toString()));
      }
      if ((jsonObj.get("preferredLanguage") != null && !jsonObj.get("preferredLanguage").isJsonNull()) && !jsonObj.get("preferredLanguage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferredLanguage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferredLanguage").toString()));
      }
      // validate the optional field `avatar`
      if (jsonObj.get("avatar") != null && !jsonObj.get("avatar").isJsonNull()) {
        MediaAuthenticatedRead.validateJsonElement(jsonObj.get("avatar"));
      }
      // validate the optional field `organization`
      if (jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonNull()) {
        OrganizationAuthenticatedRead.validateJsonElement(jsonObj.get("organization"));
      }
      if ((jsonObj.get("iri") != null && !jsonObj.get("iri").isJsonNull()) && !jsonObj.get("iri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserAuthenticatedRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserAuthenticatedRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserAuthenticatedRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserAuthenticatedRead.class));

       return (TypeAdapter<T>) new TypeAdapter<UserAuthenticatedRead>() {
           @Override
           public void write(JsonWriter out, UserAuthenticatedRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserAuthenticatedRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of UserAuthenticatedRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of UserAuthenticatedRead
  * @throws IOException if the JSON string is invalid with respect to UserAuthenticatedRead
  */
  public static UserAuthenticatedRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserAuthenticatedRead.class);
  }

 /**
  * Convert an instance of UserAuthenticatedRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

