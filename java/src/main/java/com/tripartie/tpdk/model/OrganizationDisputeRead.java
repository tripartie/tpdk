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


package com.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.tripartie.tpdk.model.MediaDisputeRead;
import java.io.IOException;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-27T05:16:17.029359Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class OrganizationDisputeRead {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_WEBSITE_URL = "websiteUrl";
  @SerializedName(SERIALIZED_NAME_WEBSITE_URL)
  private String websiteUrl;

  public static final String SERIALIZED_NAME_CUSTOM_BASE_URL = "customBaseUrl";
  @SerializedName(SERIALIZED_NAME_CUSTOM_BASE_URL)
  private String customBaseUrl;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private MediaDisputeRead icon;

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private MediaDisputeRead logo;

  public static final String SERIALIZED_NAME_PRIMARY_COLOR = "primaryColor";
  @SerializedName(SERIALIZED_NAME_PRIMARY_COLOR)
  private String primaryColor;

  public static final String SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE = "directNotificationToggle";
  @SerializedName(SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE)
  private Boolean directNotificationToggle = true;

  public static final String SERIALIZED_NAME_PERSONA_AUTH_PORTAL_TOGGLE = "personaAuthPortalToggle";
  @SerializedName(SERIALIZED_NAME_PERSONA_AUTH_PORTAL_TOGGLE)
  private Boolean personaAuthPortalToggle;

  public static final String SERIALIZED_NAME_COUNTER_PROPOSAL_TOGGLE = "counterProposalToggle";
  @SerializedName(SERIALIZED_NAME_COUNTER_PROPOSAL_TOGGLE)
  private Boolean counterProposalToggle = true;

  public static final String SERIALIZED_NAME_FLAT_RATE_ENABLED = "flatRateEnabled";
  @SerializedName(SERIALIZED_NAME_FLAT_RATE_ENABLED)
  private Boolean flatRateEnabled;

  public OrganizationDisputeRead() {
  }

  public OrganizationDisputeRead(
     Boolean flatRateEnabled
  ) {
    this();
    this.flatRateEnabled = flatRateEnabled;
  }

  public OrganizationDisputeRead name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public OrganizationDisputeRead websiteUrl(String websiteUrl) {
    this.websiteUrl = websiteUrl;
    return this;
  }

   /**
   * Get websiteUrl
   * @return websiteUrl
  **/
  @javax.annotation.Nullable
  public String getWebsiteUrl() {
    return websiteUrl;
  }

  public void setWebsiteUrl(String websiteUrl) {
    this.websiteUrl = websiteUrl;
  }


  public OrganizationDisputeRead customBaseUrl(String customBaseUrl) {
    this.customBaseUrl = customBaseUrl;
    return this;
  }

   /**
   * Get customBaseUrl
   * @return customBaseUrl
  **/
  @javax.annotation.Nullable
  public String getCustomBaseUrl() {
    return customBaseUrl;
  }

  public void setCustomBaseUrl(String customBaseUrl) {
    this.customBaseUrl = customBaseUrl;
  }


  public OrganizationDisputeRead icon(MediaDisputeRead icon) {
    this.icon = icon;
    return this;
  }

   /**
   * Get icon
   * @return icon
  **/
  @javax.annotation.Nullable
  public MediaDisputeRead getIcon() {
    return icon;
  }

  public void setIcon(MediaDisputeRead icon) {
    this.icon = icon;
  }


  public OrganizationDisputeRead logo(MediaDisputeRead logo) {
    this.logo = logo;
    return this;
  }

   /**
   * Get logo
   * @return logo
  **/
  @javax.annotation.Nullable
  public MediaDisputeRead getLogo() {
    return logo;
  }

  public void setLogo(MediaDisputeRead logo) {
    this.logo = logo;
  }


  public OrganizationDisputeRead primaryColor(String primaryColor) {
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


  public OrganizationDisputeRead directNotificationToggle(Boolean directNotificationToggle) {
    this.directNotificationToggle = directNotificationToggle;
    return this;
  }

   /**
   * Get directNotificationToggle
   * @return directNotificationToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getDirectNotificationToggle() {
    return directNotificationToggle;
  }

  public void setDirectNotificationToggle(Boolean directNotificationToggle) {
    this.directNotificationToggle = directNotificationToggle;
  }


  public OrganizationDisputeRead personaAuthPortalToggle(Boolean personaAuthPortalToggle) {
    this.personaAuthPortalToggle = personaAuthPortalToggle;
    return this;
  }

   /**
   * Get personaAuthPortalToggle
   * @return personaAuthPortalToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getPersonaAuthPortalToggle() {
    return personaAuthPortalToggle;
  }

  public void setPersonaAuthPortalToggle(Boolean personaAuthPortalToggle) {
    this.personaAuthPortalToggle = personaAuthPortalToggle;
  }


  public OrganizationDisputeRead counterProposalToggle(Boolean counterProposalToggle) {
    this.counterProposalToggle = counterProposalToggle;
    return this;
  }

   /**
   * Get counterProposalToggle
   * @return counterProposalToggle
  **/
  @javax.annotation.Nonnull
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
    OrganizationDisputeRead organizationDisputeRead = (OrganizationDisputeRead) o;
    return Objects.equals(this.name, organizationDisputeRead.name) &&
        Objects.equals(this.websiteUrl, organizationDisputeRead.websiteUrl) &&
        Objects.equals(this.customBaseUrl, organizationDisputeRead.customBaseUrl) &&
        Objects.equals(this.icon, organizationDisputeRead.icon) &&
        Objects.equals(this.logo, organizationDisputeRead.logo) &&
        Objects.equals(this.primaryColor, organizationDisputeRead.primaryColor) &&
        Objects.equals(this.directNotificationToggle, organizationDisputeRead.directNotificationToggle) &&
        Objects.equals(this.personaAuthPortalToggle, organizationDisputeRead.personaAuthPortalToggle) &&
        Objects.equals(this.counterProposalToggle, organizationDisputeRead.counterProposalToggle) &&
        Objects.equals(this.flatRateEnabled, organizationDisputeRead.flatRateEnabled);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, websiteUrl, customBaseUrl, icon, logo, primaryColor, directNotificationToggle, personaAuthPortalToggle, counterProposalToggle, flatRateEnabled);
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
    sb.append("class OrganizationDisputeRead {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    websiteUrl: ").append(toIndentedString(websiteUrl)).append("\n");
    sb.append("    customBaseUrl: ").append(toIndentedString(customBaseUrl)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    primaryColor: ").append(toIndentedString(primaryColor)).append("\n");
    sb.append("    directNotificationToggle: ").append(toIndentedString(directNotificationToggle)).append("\n");
    sb.append("    personaAuthPortalToggle: ").append(toIndentedString(personaAuthPortalToggle)).append("\n");
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
    openapiFields.add("websiteUrl");
    openapiFields.add("customBaseUrl");
    openapiFields.add("icon");
    openapiFields.add("logo");
    openapiFields.add("primaryColor");
    openapiFields.add("directNotificationToggle");
    openapiFields.add("personaAuthPortalToggle");
    openapiFields.add("counterProposalToggle");
    openapiFields.add("flatRateEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("directNotificationToggle");
    openapiRequiredFields.add("personaAuthPortalToggle");
    openapiRequiredFields.add("counterProposalToggle");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to OrganizationDisputeRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationDisputeRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationDisputeRead is not found in the empty JSON string", OrganizationDisputeRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationDisputeRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationDisputeRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrganizationDisputeRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("websiteUrl") != null && !jsonObj.get("websiteUrl").isJsonNull()) && !jsonObj.get("websiteUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteUrl").toString()));
      }
      if ((jsonObj.get("customBaseUrl") != null && !jsonObj.get("customBaseUrl").isJsonNull()) && !jsonObj.get("customBaseUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customBaseUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customBaseUrl").toString()));
      }
      // validate the optional field `icon`
      if (jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) {
        MediaDisputeRead.validateJsonElement(jsonObj.get("icon"));
      }
      // validate the optional field `logo`
      if (jsonObj.get("logo") != null && !jsonObj.get("logo").isJsonNull()) {
        MediaDisputeRead.validateJsonElement(jsonObj.get("logo"));
      }
      if ((jsonObj.get("primaryColor") != null && !jsonObj.get("primaryColor").isJsonNull()) && !jsonObj.get("primaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primaryColor").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationDisputeRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationDisputeRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationDisputeRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationDisputeRead.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationDisputeRead>() {
           @Override
           public void write(JsonWriter out, OrganizationDisputeRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationDisputeRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of OrganizationDisputeRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of OrganizationDisputeRead
  * @throws IOException if the JSON string is invalid with respect to OrganizationDisputeRead
  */
  public static OrganizationDisputeRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationDisputeRead.class);
  }

 /**
  * Convert an instance of OrganizationDisputeRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

