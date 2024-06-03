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
import com.tripartie.tpdk.model.OrganizationAddressUpdate;
import java.io.IOException;
import java.net.URI;
import java.util.Arrays;
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
public class OrganizationUpdate {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_VAT_NUMBER = "vatNumber";
  @SerializedName(SERIALIZED_NAME_VAT_NUMBER)
  private String vatNumber;

  public static final String SERIALIZED_NAME_COMMERCIAL_REGISTRY_NUMBER = "commercialRegistryNumber";
  @SerializedName(SERIALIZED_NAME_COMMERCIAL_REGISTRY_NUMBER)
  private String commercialRegistryNumber;

  public static final String SERIALIZED_NAME_WEBSITE_URL = "websiteUrl";
  @SerializedName(SERIALIZED_NAME_WEBSITE_URL)
  private URI websiteUrl;

  public static final String SERIALIZED_NAME_CUSTOM_BASE_URL = "customBaseUrl";
  @SerializedName(SERIALIZED_NAME_CUSTOM_BASE_URL)
  private URI customBaseUrl;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private OrganizationAddressUpdate billingAddress;

  public static final String SERIALIZED_NAME_PRIMARY_COLOR = "primaryColor";
  @SerializedName(SERIALIZED_NAME_PRIMARY_COLOR)
  private String primaryColor;

  public static final String SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE = "directNotificationToggle";
  @SerializedName(SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE)
  private Boolean directNotificationToggle = true;

  /**
   * Gets or Sets anonymityLevel
   */
  @JsonAdapter(AnonymityLevelEnum.Adapter.class)
  public enum AnonymityLevelEnum {
    COMPLETE("COMPLETE"),
    
    PARTIAL_FIRST_NAME("PARTIAL_FIRST_NAME"),
    
    TRANSPARENT("TRANSPARENT");

    private String value;

    AnonymityLevelEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AnonymityLevelEnum fromValue(String value) {
      for (AnonymityLevelEnum b : AnonymityLevelEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AnonymityLevelEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AnonymityLevelEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AnonymityLevelEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AnonymityLevelEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AnonymityLevelEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ANONYMITY_LEVEL = "anonymityLevel";
  @SerializedName(SERIALIZED_NAME_ANONYMITY_LEVEL)
  private AnonymityLevelEnum anonymityLevel = AnonymityLevelEnum.PARTIAL_FIRST_NAME;

  public static final String SERIALIZED_NAME_INTERNAL_MESSAGING_TOGGLE = "internalMessagingToggle";
  @SerializedName(SERIALIZED_NAME_INTERNAL_MESSAGING_TOGGLE)
  private Boolean internalMessagingToggle = true;

  public static final String SERIALIZED_NAME_PERSONA_AUTH_PORTAL_TOGGLE = "personaAuthPortalToggle";
  @SerializedName(SERIALIZED_NAME_PERSONA_AUTH_PORTAL_TOGGLE)
  private Boolean personaAuthPortalToggle;

  public static final String SERIALIZED_NAME_AUTOMATED_RETURN_TOGGLE = "automatedReturnToggle";
  @SerializedName(SERIALIZED_NAME_AUTOMATED_RETURN_TOGGLE)
  private Boolean automatedReturnToggle = true;

  public static final String SERIALIZED_NAME_COUNTER_PROPOSAL_TOGGLE = "counterProposalToggle";
  @SerializedName(SERIALIZED_NAME_COUNTER_PROPOSAL_TOGGLE)
  private Boolean counterProposalToggle = true;

  public static final String SERIALIZED_NAME_FLAT_RATE_ENABLED = "flatRateEnabled";
  @SerializedName(SERIALIZED_NAME_FLAT_RATE_ENABLED)
  private Boolean flatRateEnabled;

  public OrganizationUpdate() {
  }

  public OrganizationUpdate(
     Boolean flatRateEnabled
  ) {
    this();
    this.flatRateEnabled = flatRateEnabled;
  }

  public OrganizationUpdate name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public OrganizationUpdate vatNumber(String vatNumber) {
    this.vatNumber = vatNumber;
    return this;
  }

   /**
   * Get vatNumber
   * @return vatNumber
  **/
  @javax.annotation.Nullable
  public String getVatNumber() {
    return vatNumber;
  }

  public void setVatNumber(String vatNumber) {
    this.vatNumber = vatNumber;
  }


  public OrganizationUpdate commercialRegistryNumber(String commercialRegistryNumber) {
    this.commercialRegistryNumber = commercialRegistryNumber;
    return this;
  }

   /**
   * Get commercialRegistryNumber
   * @return commercialRegistryNumber
  **/
  @javax.annotation.Nullable
  public String getCommercialRegistryNumber() {
    return commercialRegistryNumber;
  }

  public void setCommercialRegistryNumber(String commercialRegistryNumber) {
    this.commercialRegistryNumber = commercialRegistryNumber;
  }


  public OrganizationUpdate websiteUrl(URI websiteUrl) {
    this.websiteUrl = websiteUrl;
    return this;
  }

   /**
   * Get websiteUrl
   * @return websiteUrl
  **/
  @javax.annotation.Nullable
  public URI getWebsiteUrl() {
    return websiteUrl;
  }

  public void setWebsiteUrl(URI websiteUrl) {
    this.websiteUrl = websiteUrl;
  }


  public OrganizationUpdate customBaseUrl(URI customBaseUrl) {
    this.customBaseUrl = customBaseUrl;
    return this;
  }

   /**
   * Get customBaseUrl
   * @return customBaseUrl
  **/
  @javax.annotation.Nullable
  public URI getCustomBaseUrl() {
    return customBaseUrl;
  }

  public void setCustomBaseUrl(URI customBaseUrl) {
    this.customBaseUrl = customBaseUrl;
  }


  public OrganizationUpdate billingAddress(OrganizationAddressUpdate billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

   /**
   * Get billingAddress
   * @return billingAddress
  **/
  @javax.annotation.Nullable
  public OrganizationAddressUpdate getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(OrganizationAddressUpdate billingAddress) {
    this.billingAddress = billingAddress;
  }


  public OrganizationUpdate primaryColor(String primaryColor) {
    this.primaryColor = primaryColor;
    return this;
  }

   /**
   * Get primaryColor
   * @return primaryColor
  **/
  @javax.annotation.Nullable
  public String getPrimaryColor() {
    return primaryColor;
  }

  public void setPrimaryColor(String primaryColor) {
    this.primaryColor = primaryColor;
  }


  public OrganizationUpdate directNotificationToggle(Boolean directNotificationToggle) {
    this.directNotificationToggle = directNotificationToggle;
    return this;
  }

   /**
   * Get directNotificationToggle
   * @return directNotificationToggle
  **/
  @javax.annotation.Nullable
  public Boolean getDirectNotificationToggle() {
    return directNotificationToggle;
  }

  public void setDirectNotificationToggle(Boolean directNotificationToggle) {
    this.directNotificationToggle = directNotificationToggle;
  }


  public OrganizationUpdate anonymityLevel(AnonymityLevelEnum anonymityLevel) {
    this.anonymityLevel = anonymityLevel;
    return this;
  }

   /**
   * Get anonymityLevel
   * @return anonymityLevel
  **/
  @javax.annotation.Nullable
  public AnonymityLevelEnum getAnonymityLevel() {
    return anonymityLevel;
  }

  public void setAnonymityLevel(AnonymityLevelEnum anonymityLevel) {
    this.anonymityLevel = anonymityLevel;
  }


  public OrganizationUpdate internalMessagingToggle(Boolean internalMessagingToggle) {
    this.internalMessagingToggle = internalMessagingToggle;
    return this;
  }

   /**
   * Get internalMessagingToggle
   * @return internalMessagingToggle
  **/
  @javax.annotation.Nullable
  public Boolean getInternalMessagingToggle() {
    return internalMessagingToggle;
  }

  public void setInternalMessagingToggle(Boolean internalMessagingToggle) {
    this.internalMessagingToggle = internalMessagingToggle;
  }


  public OrganizationUpdate personaAuthPortalToggle(Boolean personaAuthPortalToggle) {
    this.personaAuthPortalToggle = personaAuthPortalToggle;
    return this;
  }

   /**
   * Get personaAuthPortalToggle
   * @return personaAuthPortalToggle
  **/
  @javax.annotation.Nullable
  public Boolean getPersonaAuthPortalToggle() {
    return personaAuthPortalToggle;
  }

  public void setPersonaAuthPortalToggle(Boolean personaAuthPortalToggle) {
    this.personaAuthPortalToggle = personaAuthPortalToggle;
  }


  public OrganizationUpdate automatedReturnToggle(Boolean automatedReturnToggle) {
    this.automatedReturnToggle = automatedReturnToggle;
    return this;
  }

   /**
   * Get automatedReturnToggle
   * @return automatedReturnToggle
  **/
  @javax.annotation.Nullable
  public Boolean getAutomatedReturnToggle() {
    return automatedReturnToggle;
  }

  public void setAutomatedReturnToggle(Boolean automatedReturnToggle) {
    this.automatedReturnToggle = automatedReturnToggle;
  }


  public OrganizationUpdate counterProposalToggle(Boolean counterProposalToggle) {
    this.counterProposalToggle = counterProposalToggle;
    return this;
  }

   /**
   * Get counterProposalToggle
   * @return counterProposalToggle
  **/
  @javax.annotation.Nullable
  public Boolean getCounterProposalToggle() {
    return counterProposalToggle;
  }

  public void setCounterProposalToggle(Boolean counterProposalToggle) {
    this.counterProposalToggle = counterProposalToggle;
  }


   /**
   * Get flatRateEnabled
   * @return flatRateEnabled
  **/
  @javax.annotation.Nullable
  public Boolean getFlatRateEnabled() {
    return flatRateEnabled;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrganizationUpdate organizationUpdate = (OrganizationUpdate) o;
    return Objects.equals(this.name, organizationUpdate.name) &&
        Objects.equals(this.vatNumber, organizationUpdate.vatNumber) &&
        Objects.equals(this.commercialRegistryNumber, organizationUpdate.commercialRegistryNumber) &&
        Objects.equals(this.websiteUrl, organizationUpdate.websiteUrl) &&
        Objects.equals(this.customBaseUrl, organizationUpdate.customBaseUrl) &&
        Objects.equals(this.billingAddress, organizationUpdate.billingAddress) &&
        Objects.equals(this.primaryColor, organizationUpdate.primaryColor) &&
        Objects.equals(this.directNotificationToggle, organizationUpdate.directNotificationToggle) &&
        Objects.equals(this.anonymityLevel, organizationUpdate.anonymityLevel) &&
        Objects.equals(this.internalMessagingToggle, organizationUpdate.internalMessagingToggle) &&
        Objects.equals(this.personaAuthPortalToggle, organizationUpdate.personaAuthPortalToggle) &&
        Objects.equals(this.automatedReturnToggle, organizationUpdate.automatedReturnToggle) &&
        Objects.equals(this.counterProposalToggle, organizationUpdate.counterProposalToggle) &&
        Objects.equals(this.flatRateEnabled, organizationUpdate.flatRateEnabled);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, vatNumber, commercialRegistryNumber, websiteUrl, customBaseUrl, billingAddress, primaryColor, directNotificationToggle, anonymityLevel, internalMessagingToggle, personaAuthPortalToggle, automatedReturnToggle, counterProposalToggle, flatRateEnabled);
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
    sb.append("class OrganizationUpdate {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    vatNumber: ").append(toIndentedString(vatNumber)).append("\n");
    sb.append("    commercialRegistryNumber: ").append(toIndentedString(commercialRegistryNumber)).append("\n");
    sb.append("    websiteUrl: ").append(toIndentedString(websiteUrl)).append("\n");
    sb.append("    customBaseUrl: ").append(toIndentedString(customBaseUrl)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    primaryColor: ").append(toIndentedString(primaryColor)).append("\n");
    sb.append("    directNotificationToggle: ").append(toIndentedString(directNotificationToggle)).append("\n");
    sb.append("    anonymityLevel: ").append(toIndentedString(anonymityLevel)).append("\n");
    sb.append("    internalMessagingToggle: ").append(toIndentedString(internalMessagingToggle)).append("\n");
    sb.append("    personaAuthPortalToggle: ").append(toIndentedString(personaAuthPortalToggle)).append("\n");
    sb.append("    automatedReturnToggle: ").append(toIndentedString(automatedReturnToggle)).append("\n");
    sb.append("    counterProposalToggle: ").append(toIndentedString(counterProposalToggle)).append("\n");
    sb.append("    flatRateEnabled: ").append(toIndentedString(flatRateEnabled)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("vatNumber");
    openapiFields.add("commercialRegistryNumber");
    openapiFields.add("websiteUrl");
    openapiFields.add("customBaseUrl");
    openapiFields.add("billingAddress");
    openapiFields.add("primaryColor");
    openapiFields.add("directNotificationToggle");
    openapiFields.add("anonymityLevel");
    openapiFields.add("internalMessagingToggle");
    openapiFields.add("personaAuthPortalToggle");
    openapiFields.add("automatedReturnToggle");
    openapiFields.add("counterProposalToggle");
    openapiFields.add("flatRateEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to OrganizationUpdate
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationUpdate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationUpdate is not found in the empty JSON string", OrganizationUpdate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationUpdate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationUpdate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrganizationUpdate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("vatNumber") != null && !jsonObj.get("vatNumber").isJsonNull()) && !jsonObj.get("vatNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vatNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vatNumber").toString()));
      }
      if ((jsonObj.get("commercialRegistryNumber") != null && !jsonObj.get("commercialRegistryNumber").isJsonNull()) && !jsonObj.get("commercialRegistryNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `commercialRegistryNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("commercialRegistryNumber").toString()));
      }
      if ((jsonObj.get("websiteUrl") != null && !jsonObj.get("websiteUrl").isJsonNull()) && !jsonObj.get("websiteUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteUrl").toString()));
      }
      if ((jsonObj.get("customBaseUrl") != null && !jsonObj.get("customBaseUrl").isJsonNull()) && !jsonObj.get("customBaseUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customBaseUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customBaseUrl").toString()));
      }
      // validate the optional field `billingAddress`
      if (jsonObj.get("billingAddress") != null && !jsonObj.get("billingAddress").isJsonNull()) {
        OrganizationAddressUpdate.validateJsonElement(jsonObj.get("billingAddress"));
      }
      if ((jsonObj.get("primaryColor") != null && !jsonObj.get("primaryColor").isJsonNull()) && !jsonObj.get("primaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primaryColor").toString()));
      }
      if ((jsonObj.get("anonymityLevel") != null && !jsonObj.get("anonymityLevel").isJsonNull()) && !jsonObj.get("anonymityLevel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `anonymityLevel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("anonymityLevel").toString()));
      }
      // validate the optional field `anonymityLevel`
      if (jsonObj.get("anonymityLevel") != null && !jsonObj.get("anonymityLevel").isJsonNull()) {
        AnonymityLevelEnum.validateJsonElement(jsonObj.get("anonymityLevel"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationUpdate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationUpdate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationUpdate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationUpdate.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationUpdate>() {
           @Override
           public void write(JsonWriter out, OrganizationUpdate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationUpdate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of OrganizationUpdate given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of OrganizationUpdate
  * @throws IOException if the JSON string is invalid with respect to OrganizationUpdate
  */
  public static OrganizationUpdate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationUpdate.class);
  }

 /**
  * Convert an instance of OrganizationUpdate to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

