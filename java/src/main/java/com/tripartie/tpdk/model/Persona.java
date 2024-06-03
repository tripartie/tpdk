/*
 * Resolution Center
 * Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.
 *
 * The version of the OpenAPI document: 2.0.208
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
import com.tripartie.tpdk.model.Address;
import com.tripartie.tpdk.model.Metadata;
import com.tripartie.tpdk.model.View;
import java.io.IOException;
import java.net.URI;
import java.time.LocalDate;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-06-03T08:05:44.815293Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class Persona {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_CAPTCHA = "captcha";
  @SerializedName(SERIALIZED_NAME_CAPTCHA)
  private String captcha;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private String organization;

  public static final String SERIALIZED_NAME_TARGET_URL = "targetUrl";
  @SerializedName(SERIALIZED_NAME_TARGET_URL)
  private String targetUrl;

  public static final String SERIALIZED_NAME_AUTH_URL = "authUrl";
  @SerializedName(SERIALIZED_NAME_AUTH_URL)
  private URI authUrl;

  public static final String SERIALIZED_NAME_EXPIRE_AT = "expireAt";
  @SerializedName(SERIALIZED_NAME_EXPIRE_AT)
  private OffsetDateTime expireAt;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PLAIN_PASSWORD = "plainPassword";
  @SerializedName(SERIALIZED_NAME_PLAIN_PASSWORD)
  private String plainPassword;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  /**
   * Gets or Sets gender
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    MALE("MALE"),
    
    FEMALE("FEMALE"),
    
    OTHER("OTHER"),
    
    RATHER_NOT_SAY("RATHER_NOT_SAY");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GenderEnum fromValue(String value) {
      for (GenderEnum b : GenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private GenderEnum gender = GenderEnum.RATHER_NOT_SAY;

  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "dateOfBirth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private LocalDate dateOfBirth;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_MOBILE_PHONE_NUMBER = "mobilePhoneNumber";
  @SerializedName(SERIALIZED_NAME_MOBILE_PHONE_NUMBER)
  private String mobilePhoneNumber;

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private Address address;

  /**
   * We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore.
   */
  @JsonAdapter(RiskLevelEnum.Adapter.class)
  public enum RiskLevelEnum {
    WEAK("WEAK"),
    
    MEDIUM("MEDIUM"),
    
    HIGH("HIGH"),
    
    NULL("null");

    private String value;

    RiskLevelEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RiskLevelEnum fromValue(String value) {
      for (RiskLevelEnum b : RiskLevelEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<RiskLevelEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RiskLevelEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RiskLevelEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RiskLevelEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RiskLevelEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RISK_LEVEL = "riskLevel";
  @SerializedName(SERIALIZED_NAME_RISK_LEVEL)
  private RiskLevelEnum riskLevel;

  public static final String SERIALIZED_NAME_RISK_SCORE = "riskScore";
  @SerializedName(SERIALIZED_NAME_RISK_SCORE)
  private Integer riskScore;

  public static final String SERIALIZED_NAME_EXTERNAL_PURCHASE_COUNT = "externalPurchaseCount";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_PURCHASE_COUNT)
  private Integer externalPurchaseCount;

  public static final String SERIALIZED_NAME_EXTERNAL_SELL_COUNT = "externalSellCount";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SELL_COUNT)
  private Integer externalSellCount;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private List<Metadata> metadata = new ArrayList<>();

  public static final String SERIALIZED_NAME_OFFERS = "offers";
  @SerializedName(SERIALIZED_NAME_OFFERS)
  private List<String> offers = new ArrayList<>();

  public static final String SERIALIZED_NAME_PURCHASES = "purchases";
  @SerializedName(SERIALIZED_NAME_PURCHASES)
  private List<String> purchases = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIEWS = "views";
  @SerializedName(SERIALIZED_NAME_VIEWS)
  private List<View> views = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_OFFER_COUNT = "offerCount";
  @SerializedName(SERIALIZED_NAME_OFFER_COUNT)
  private Integer offerCount;

  public static final String SERIALIZED_NAME_PURCHASE_COUNT = "purchaseCount";
  @SerializedName(SERIALIZED_NAME_PURCHASE_COUNT)
  private Integer purchaseCount;

  public static final String SERIALIZED_NAME_ROLES = "roles";
  @SerializedName(SERIALIZED_NAME_ROLES)
  private List<String> roles = new ArrayList<>();

  public static final String SERIALIZED_NAME_USER_IDENTIFIER = "userIdentifier";
  @SerializedName(SERIALIZED_NAME_USER_IDENTIFIER)
  private String userIdentifier;

  public Persona() {
  }

  public Persona(
     Integer id, 
     OffsetDateTime createdAt, 
     OffsetDateTime updatedAt, 
     Integer offerCount, 
     Integer purchaseCount, 
     String userIdentifier
  ) {
    this();
    this.id = id;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
    this.offerCount = offerCount;
    this.purchaseCount = purchaseCount;
    this.userIdentifier = userIdentifier;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public Persona captcha(String captcha) {
    this.captcha = captcha;
    return this;
  }

   /**
   * Get captcha
   * @return captcha
  **/
  @javax.annotation.Nullable
  public String getCaptcha() {
    return captcha;
  }

  public void setCaptcha(String captcha) {
    this.captcha = captcha;
  }


  public Persona organization(String organization) {
    this.organization = organization;
    return this;
  }

   /**
   * Get organization
   * @return organization
  **/
  @javax.annotation.Nullable
  public String getOrganization() {
    return organization;
  }

  public void setOrganization(String organization) {
    this.organization = organization;
  }


  public Persona targetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
    return this;
  }

   /**
   * The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona.
   * @return targetUrl
  **/
  @javax.annotation.Nullable
  public String getTargetUrl() {
    return targetUrl;
  }

  public void setTargetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
  }


  public Persona authUrl(URI authUrl) {
    this.authUrl = authUrl;
    return this;
  }

   /**
   * Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them.
   * @return authUrl
  **/
  @javax.annotation.Nullable
  public URI getAuthUrl() {
    return authUrl;
  }

  public void setAuthUrl(URI authUrl) {
    this.authUrl = authUrl;
  }


  public Persona expireAt(OffsetDateTime expireAt) {
    this.expireAt = expireAt;
    return this;
  }

   /**
   * This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour.
   * @return expireAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getExpireAt() {
    return expireAt;
  }

  public void setExpireAt(OffsetDateTime expireAt) {
    this.expireAt = expireAt;
  }


  public Persona password(String password) {
    this.password = password;
    return this;
  }

   /**
   * The hashed password
   * @return password
  **/
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public Persona plainPassword(String plainPassword) {
    this.plainPassword = plainPassword;
    return this;
  }

   /**
   * Get plainPassword
   * @return plainPassword
  **/
  @javax.annotation.Nullable
  public String getPlainPassword() {
    return plainPassword;
  }

  public void setPlainPassword(String plainPassword) {
    this.plainPassword = plainPassword;
  }


  public Persona firstName(String firstName) {
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


  public Persona lastName(String lastName) {
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


  public Persona gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

   /**
   * Get gender
   * @return gender
  **/
  @javax.annotation.Nullable
  public GenderEnum getGender() {
    return gender;
  }

  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }


  public Persona dateOfBirth(LocalDate dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

   /**
   * Get dateOfBirth
   * @return dateOfBirth
  **/
  @javax.annotation.Nullable
  public LocalDate getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(LocalDate dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public Persona language(String language) {
    this.language = language;
    return this;
  }

   /**
   * That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.
   * @return language
  **/
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public Persona email(String email) {
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


  public Persona mobilePhoneNumber(String mobilePhoneNumber) {
    this.mobilePhoneNumber = mobilePhoneNumber;
    return this;
  }

   /**
   * Get mobilePhoneNumber
   * @return mobilePhoneNumber
  **/
  @javax.annotation.Nullable
  public String getMobilePhoneNumber() {
    return mobilePhoneNumber;
  }

  public void setMobilePhoneNumber(String mobilePhoneNumber) {
    this.mobilePhoneNumber = mobilePhoneNumber;
  }


  public Persona address(Address address) {
    this.address = address;
    return this;
  }

   /**
   * Get address
   * @return address
  **/
  @javax.annotation.Nullable
  public Address getAddress() {
    return address;
  }

  public void setAddress(Address address) {
    this.address = address;
  }


  public Persona riskLevel(RiskLevelEnum riskLevel) {
    this.riskLevel = riskLevel;
    return this;
  }

   /**
   * We sort Persona into three distinct risks&#39; category. This is inferred from the riskScore.
   * @return riskLevel
  **/
  @javax.annotation.Nullable
  public RiskLevelEnum getRiskLevel() {
    return riskLevel;
  }

  public void setRiskLevel(RiskLevelEnum riskLevel) {
    this.riskLevel = riskLevel;
  }


  public Persona riskScore(Integer riskScore) {
    this.riskScore = riskScore;
    return this;
  }

   /**
   * That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky.
   * minimum: 0
   * maximum: 100
   * @return riskScore
  **/
  @javax.annotation.Nullable
  public Integer getRiskScore() {
    return riskScore;
  }

  public void setRiskScore(Integer riskScore) {
    this.riskScore = riskScore;
  }


  public Persona externalPurchaseCount(Integer externalPurchaseCount) {
    this.externalPurchaseCount = externalPurchaseCount;
    return this;
  }

   /**
   * Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.
   * @return externalPurchaseCount
  **/
  @javax.annotation.Nullable
  public Integer getExternalPurchaseCount() {
    return externalPurchaseCount;
  }

  public void setExternalPurchaseCount(Integer externalPurchaseCount) {
    this.externalPurchaseCount = externalPurchaseCount;
  }


  public Persona externalSellCount(Integer externalSellCount) {
    this.externalSellCount = externalSellCount;
    return this;
  }

   /**
   * Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.
   * @return externalSellCount
  **/
  @javax.annotation.Nullable
  public Integer getExternalSellCount() {
    return externalSellCount;
  }

  public void setExternalSellCount(Integer externalSellCount) {
    this.externalSellCount = externalSellCount;
  }


  public Persona metadata(List<Metadata> metadata) {
    this.metadata = metadata;
    return this;
  }

  public Persona addMetadataItem(Metadata metadataItem) {
    if (this.metadata == null) {
      this.metadata = new ArrayList<>();
    }
    this.metadata.add(metadataItem);
    return this;
  }

   /**
   * You can assign different meta to your Persona object for different purposes. eg. Ease searching.
   * @return metadata
  **/
  @javax.annotation.Nullable
  public List<Metadata> getMetadata() {
    return metadata;
  }

  public void setMetadata(List<Metadata> metadata) {
    this.metadata = metadata;
  }


  public Persona offers(List<String> offers) {
    this.offers = offers;
    return this;
  }

  public Persona addOffersItem(String offersItem) {
    if (this.offers == null) {
      this.offers = new ArrayList<>();
    }
    this.offers.add(offersItem);
    return this;
  }

   /**
   * Get offers
   * @return offers
  **/
  @javax.annotation.Nonnull
  public List<String> getOffers() {
    return offers;
  }

  public void setOffers(List<String> offers) {
    this.offers = offers;
  }


  public Persona purchases(List<String> purchases) {
    this.purchases = purchases;
    return this;
  }

  public Persona addPurchasesItem(String purchasesItem) {
    if (this.purchases == null) {
      this.purchases = new ArrayList<>();
    }
    this.purchases.add(purchasesItem);
    return this;
  }

   /**
   * Get purchases
   * @return purchases
  **/
  @javax.annotation.Nonnull
  public List<String> getPurchases() {
    return purchases;
  }

  public void setPurchases(List<String> purchases) {
    this.purchases = purchases;
  }


  public Persona views(List<View> views) {
    this.views = views;
    return this;
  }

  public Persona addViewsItem(View viewsItem) {
    if (this.views == null) {
      this.views = new ArrayList<>();
    }
    this.views.add(viewsItem);
    return this;
  }

   /**
   * Get views
   * @return views
  **/
  @javax.annotation.Nonnull
  public List<View> getViews() {
    return views;
  }

  public void setViews(List<View> views) {
    this.views = views;
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



   /**
   * Issued Offers count owned by a given Persona
   * @return offerCount
  **/
  @javax.annotation.Nullable
  public Integer getOfferCount() {
    return offerCount;
  }



   /**
   * Get purchaseCount
   * @return purchaseCount
  **/
  @javax.annotation.Nullable
  public Integer getPurchaseCount() {
    return purchaseCount;
  }



  public Persona roles(List<String> roles) {
    this.roles = roles;
    return this;
  }

  public Persona addRolesItem(String rolesItem) {
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
  @javax.annotation.Nullable
  public List<String> getRoles() {
    return roles;
  }

  public void setRoles(List<String> roles) {
    this.roles = roles;
  }


   /**
   * Either email or the mobile phone number
   * @return userIdentifier
  **/
  @javax.annotation.Nullable
  public String getUserIdentifier() {
    return userIdentifier;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Persona persona = (Persona) o;
    return Objects.equals(this.id, persona.id) &&
        Objects.equals(this.captcha, persona.captcha) &&
        Objects.equals(this.organization, persona.organization) &&
        Objects.equals(this.targetUrl, persona.targetUrl) &&
        Objects.equals(this.authUrl, persona.authUrl) &&
        Objects.equals(this.expireAt, persona.expireAt) &&
        Objects.equals(this.password, persona.password) &&
        Objects.equals(this.plainPassword, persona.plainPassword) &&
        Objects.equals(this.firstName, persona.firstName) &&
        Objects.equals(this.lastName, persona.lastName) &&
        Objects.equals(this.gender, persona.gender) &&
        Objects.equals(this.dateOfBirth, persona.dateOfBirth) &&
        Objects.equals(this.language, persona.language) &&
        Objects.equals(this.email, persona.email) &&
        Objects.equals(this.mobilePhoneNumber, persona.mobilePhoneNumber) &&
        Objects.equals(this.address, persona.address) &&
        Objects.equals(this.riskLevel, persona.riskLevel) &&
        Objects.equals(this.riskScore, persona.riskScore) &&
        Objects.equals(this.externalPurchaseCount, persona.externalPurchaseCount) &&
        Objects.equals(this.externalSellCount, persona.externalSellCount) &&
        Objects.equals(this.metadata, persona.metadata) &&
        Objects.equals(this.offers, persona.offers) &&
        Objects.equals(this.purchases, persona.purchases) &&
        Objects.equals(this.views, persona.views) &&
        Objects.equals(this.createdAt, persona.createdAt) &&
        Objects.equals(this.updatedAt, persona.updatedAt) &&
        Objects.equals(this.offerCount, persona.offerCount) &&
        Objects.equals(this.purchaseCount, persona.purchaseCount) &&
        Objects.equals(this.roles, persona.roles) &&
        Objects.equals(this.userIdentifier, persona.userIdentifier);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, captcha, organization, targetUrl, authUrl, expireAt, password, plainPassword, firstName, lastName, gender, dateOfBirth, language, email, mobilePhoneNumber, address, riskLevel, riskScore, externalPurchaseCount, externalSellCount, metadata, offers, purchases, views, createdAt, updatedAt, offerCount, purchaseCount, roles, userIdentifier);
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
    sb.append("class Persona {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    captcha: ").append(toIndentedString(captcha)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
    sb.append("    targetUrl: ").append(toIndentedString(targetUrl)).append("\n");
    sb.append("    authUrl: ").append(toIndentedString(authUrl)).append("\n");
    sb.append("    expireAt: ").append(toIndentedString(expireAt)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    plainPassword: ").append(toIndentedString(plainPassword)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    mobilePhoneNumber: ").append(toIndentedString(mobilePhoneNumber)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    riskLevel: ").append(toIndentedString(riskLevel)).append("\n");
    sb.append("    riskScore: ").append(toIndentedString(riskScore)).append("\n");
    sb.append("    externalPurchaseCount: ").append(toIndentedString(externalPurchaseCount)).append("\n");
    sb.append("    externalSellCount: ").append(toIndentedString(externalSellCount)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    offers: ").append(toIndentedString(offers)).append("\n");
    sb.append("    purchases: ").append(toIndentedString(purchases)).append("\n");
    sb.append("    views: ").append(toIndentedString(views)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    offerCount: ").append(toIndentedString(offerCount)).append("\n");
    sb.append("    purchaseCount: ").append(toIndentedString(purchaseCount)).append("\n");
    sb.append("    roles: ").append(toIndentedString(roles)).append("\n");
    sb.append("    userIdentifier: ").append(toIndentedString(userIdentifier)).append("\n");
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
    openapiFields.add("captcha");
    openapiFields.add("organization");
    openapiFields.add("targetUrl");
    openapiFields.add("authUrl");
    openapiFields.add("expireAt");
    openapiFields.add("password");
    openapiFields.add("plainPassword");
    openapiFields.add("firstName");
    openapiFields.add("lastName");
    openapiFields.add("gender");
    openapiFields.add("dateOfBirth");
    openapiFields.add("language");
    openapiFields.add("email");
    openapiFields.add("mobilePhoneNumber");
    openapiFields.add("address");
    openapiFields.add("riskLevel");
    openapiFields.add("riskScore");
    openapiFields.add("externalPurchaseCount");
    openapiFields.add("externalSellCount");
    openapiFields.add("metadata");
    openapiFields.add("offers");
    openapiFields.add("purchases");
    openapiFields.add("views");
    openapiFields.add("createdAt");
    openapiFields.add("updatedAt");
    openapiFields.add("offerCount");
    openapiFields.add("purchaseCount");
    openapiFields.add("roles");
    openapiFields.add("userIdentifier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("offers");
    openapiRequiredFields.add("purchases");
    openapiRequiredFields.add("views");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to Persona
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Persona.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Persona is not found in the empty JSON string", Persona.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Persona.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Persona` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Persona.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("captcha") != null && !jsonObj.get("captcha").isJsonNull()) && !jsonObj.get("captcha").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `captcha` to be a primitive type in the JSON string but got `%s`", jsonObj.get("captcha").toString()));
      }
      if ((jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonNull()) && !jsonObj.get("organization").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `organization` to be a primitive type in the JSON string but got `%s`", jsonObj.get("organization").toString()));
      }
      if ((jsonObj.get("targetUrl") != null && !jsonObj.get("targetUrl").isJsonNull()) && !jsonObj.get("targetUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetUrl").toString()));
      }
      if ((jsonObj.get("authUrl") != null && !jsonObj.get("authUrl").isJsonNull()) && !jsonObj.get("authUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authUrl").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("plainPassword") != null && !jsonObj.get("plainPassword").isJsonNull()) && !jsonObj.get("plainPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `plainPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("plainPassword").toString()));
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the optional field `gender`
      if (jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) {
        GenderEnum.validateJsonElement(jsonObj.get("gender"));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("mobilePhoneNumber") != null && !jsonObj.get("mobilePhoneNumber").isJsonNull()) && !jsonObj.get("mobilePhoneNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobilePhoneNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobilePhoneNumber").toString()));
      }
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("address"));
      }
      if ((jsonObj.get("riskLevel") != null && !jsonObj.get("riskLevel").isJsonNull()) && !jsonObj.get("riskLevel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `riskLevel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("riskLevel").toString()));
      }
      // validate the optional field `riskLevel`
      if (jsonObj.get("riskLevel") != null && !jsonObj.get("riskLevel").isJsonNull()) {
        RiskLevelEnum.validateJsonElement(jsonObj.get("riskLevel"));
      }
      if (jsonObj.get("metadata") != null && !jsonObj.get("metadata").isJsonNull()) {
        JsonArray jsonArraymetadata = jsonObj.getAsJsonArray("metadata");
        if (jsonArraymetadata != null) {
          // ensure the json data is an array
          if (!jsonObj.get("metadata").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `metadata` to be an array in the JSON string but got `%s`", jsonObj.get("metadata").toString()));
          }

          // validate the optional field `metadata` (array)
          for (int i = 0; i < jsonArraymetadata.size(); i++) {
            Metadata.validateJsonElement(jsonArraymetadata.get(i));
          };
        }
      }
      // ensure the required json array is present
      if (jsonObj.get("offers") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("offers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `offers` to be an array in the JSON string but got `%s`", jsonObj.get("offers").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("purchases") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("purchases").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `purchases` to be an array in the JSON string but got `%s`", jsonObj.get("purchases").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("views").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `views` to be an array in the JSON string but got `%s`", jsonObj.get("views").toString()));
      }

      JsonArray jsonArrayviews = jsonObj.getAsJsonArray("views");
      // validate the required field `views` (array)
      for (int i = 0; i < jsonArrayviews.size(); i++) {
        View.validateJsonElement(jsonArrayviews.get(i));
      };
      // ensure the optional json data is an array if present
      if (jsonObj.get("roles") != null && !jsonObj.get("roles").isJsonNull() && !jsonObj.get("roles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `roles` to be an array in the JSON string but got `%s`", jsonObj.get("roles").toString()));
      }
      if ((jsonObj.get("userIdentifier") != null && !jsonObj.get("userIdentifier").isJsonNull()) && !jsonObj.get("userIdentifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userIdentifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userIdentifier").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Persona.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Persona' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Persona> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Persona.class));

       return (TypeAdapter<T>) new TypeAdapter<Persona>() {
           @Override
           public void write(JsonWriter out, Persona value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Persona read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of Persona given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of Persona
  * @throws IOException if the JSON string is invalid with respect to Persona
  */
  public static Persona fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Persona.class);
  }

 /**
  * Convert an instance of Persona to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

