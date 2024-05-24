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


package com.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.tripartie.tpdk.model.OrganizationMediaCollectionRead;
import java.io.IOException;
import java.math.BigDecimal;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-24T14:51:06.458670Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class OrganizationCollectionRead {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

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
  private String websiteUrl;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private OrganizationMediaCollectionRead icon;

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private OrganizationMediaCollectionRead logo;

  public static final String SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE = "directNotificationToggle";
  @SerializedName(SERIALIZED_NAME_DIRECT_NOTIFICATION_TOGGLE)
  private Boolean directNotificationToggle = true;

  public static final String SERIALIZED_NAME_SAFE_CHECKOUT_TOGGLE = "safeCheckoutToggle";
  @SerializedName(SERIALIZED_NAME_SAFE_CHECKOUT_TOGGLE)
  private Boolean safeCheckoutToggle;

  public static final String SERIALIZED_NAME_RESOLUTION_CENTER_TOGGLE = "resolutionCenterToggle";
  @SerializedName(SERIALIZED_NAME_RESOLUTION_CENTER_TOGGLE)
  private Boolean resolutionCenterToggle = true;

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

  public static final String SERIALIZED_NAME_RATE_COMMISSION_SAFE_CHECKOUT = "rateCommissionSafeCheckout";
  @SerializedName(SERIALIZED_NAME_RATE_COMMISSION_SAFE_CHECKOUT)
  private BigDecimal rateCommissionSafeCheckout;

  public OrganizationCollectionRead() {
  }

  public OrganizationCollectionRead(
     Integer id, 
     Boolean flatRateEnabled
  ) {
    this();
    this.id = id;
    this.flatRateEnabled = flatRateEnabled;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public OrganizationCollectionRead name(String name) {
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


  public OrganizationCollectionRead vatNumber(String vatNumber) {
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


  public OrganizationCollectionRead commercialRegistryNumber(String commercialRegistryNumber) {
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


  public OrganizationCollectionRead websiteUrl(String websiteUrl) {
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


  public OrganizationCollectionRead icon(OrganizationMediaCollectionRead icon) {
    this.icon = icon;
    return this;
  }

   /**
   * Get icon
   * @return icon
  **/
  @javax.annotation.Nullable
  public OrganizationMediaCollectionRead getIcon() {
    return icon;
  }

  public void setIcon(OrganizationMediaCollectionRead icon) {
    this.icon = icon;
  }


  public OrganizationCollectionRead logo(OrganizationMediaCollectionRead logo) {
    this.logo = logo;
    return this;
  }

   /**
   * Get logo
   * @return logo
  **/
  @javax.annotation.Nullable
  public OrganizationMediaCollectionRead getLogo() {
    return logo;
  }

  public void setLogo(OrganizationMediaCollectionRead logo) {
    this.logo = logo;
  }


  public OrganizationCollectionRead directNotificationToggle(Boolean directNotificationToggle) {
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


  public OrganizationCollectionRead safeCheckoutToggle(Boolean safeCheckoutToggle) {
    this.safeCheckoutToggle = safeCheckoutToggle;
    return this;
  }

   /**
   * Get safeCheckoutToggle
   * @return safeCheckoutToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getSafeCheckoutToggle() {
    return safeCheckoutToggle;
  }

  public void setSafeCheckoutToggle(Boolean safeCheckoutToggle) {
    this.safeCheckoutToggle = safeCheckoutToggle;
  }


  public OrganizationCollectionRead resolutionCenterToggle(Boolean resolutionCenterToggle) {
    this.resolutionCenterToggle = resolutionCenterToggle;
    return this;
  }

   /**
   * Get resolutionCenterToggle
   * @return resolutionCenterToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getResolutionCenterToggle() {
    return resolutionCenterToggle;
  }

  public void setResolutionCenterToggle(Boolean resolutionCenterToggle) {
    this.resolutionCenterToggle = resolutionCenterToggle;
  }


  public OrganizationCollectionRead internalMessagingToggle(Boolean internalMessagingToggle) {
    this.internalMessagingToggle = internalMessagingToggle;
    return this;
  }

   /**
   * Get internalMessagingToggle
   * @return internalMessagingToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getInternalMessagingToggle() {
    return internalMessagingToggle;
  }

  public void setInternalMessagingToggle(Boolean internalMessagingToggle) {
    this.internalMessagingToggle = internalMessagingToggle;
  }


  public OrganizationCollectionRead personaAuthPortalToggle(Boolean personaAuthPortalToggle) {
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


  public OrganizationCollectionRead automatedReturnToggle(Boolean automatedReturnToggle) {
    this.automatedReturnToggle = automatedReturnToggle;
    return this;
  }

   /**
   * Get automatedReturnToggle
   * @return automatedReturnToggle
  **/
  @javax.annotation.Nonnull
  public Boolean getAutomatedReturnToggle() {
    return automatedReturnToggle;
  }

  public void setAutomatedReturnToggle(Boolean automatedReturnToggle) {
    this.automatedReturnToggle = automatedReturnToggle;
  }


  public OrganizationCollectionRead counterProposalToggle(Boolean counterProposalToggle) {
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



  public OrganizationCollectionRead rateCommissionSafeCheckout(BigDecimal rateCommissionSafeCheckout) {
    this.rateCommissionSafeCheckout = rateCommissionSafeCheckout;
    return this;
  }

   /**
   * Get rateCommissionSafeCheckout
   * @return rateCommissionSafeCheckout
  **/
  @javax.annotation.Nonnull
  public BigDecimal getRateCommissionSafeCheckout() {
    return rateCommissionSafeCheckout;
  }

  public void setRateCommissionSafeCheckout(BigDecimal rateCommissionSafeCheckout) {
    this.rateCommissionSafeCheckout = rateCommissionSafeCheckout;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrganizationCollectionRead organizationCollectionRead = (OrganizationCollectionRead) o;
    return Objects.equals(this.id, organizationCollectionRead.id) &&
        Objects.equals(this.name, organizationCollectionRead.name) &&
        Objects.equals(this.vatNumber, organizationCollectionRead.vatNumber) &&
        Objects.equals(this.commercialRegistryNumber, organizationCollectionRead.commercialRegistryNumber) &&
        Objects.equals(this.websiteUrl, organizationCollectionRead.websiteUrl) &&
        Objects.equals(this.icon, organizationCollectionRead.icon) &&
        Objects.equals(this.logo, organizationCollectionRead.logo) &&
        Objects.equals(this.directNotificationToggle, organizationCollectionRead.directNotificationToggle) &&
        Objects.equals(this.safeCheckoutToggle, organizationCollectionRead.safeCheckoutToggle) &&
        Objects.equals(this.resolutionCenterToggle, organizationCollectionRead.resolutionCenterToggle) &&
        Objects.equals(this.internalMessagingToggle, organizationCollectionRead.internalMessagingToggle) &&
        Objects.equals(this.personaAuthPortalToggle, organizationCollectionRead.personaAuthPortalToggle) &&
        Objects.equals(this.automatedReturnToggle, organizationCollectionRead.automatedReturnToggle) &&
        Objects.equals(this.counterProposalToggle, organizationCollectionRead.counterProposalToggle) &&
        Objects.equals(this.flatRateEnabled, organizationCollectionRead.flatRateEnabled) &&
        Objects.equals(this.rateCommissionSafeCheckout, organizationCollectionRead.rateCommissionSafeCheckout);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, vatNumber, commercialRegistryNumber, websiteUrl, icon, logo, directNotificationToggle, safeCheckoutToggle, resolutionCenterToggle, internalMessagingToggle, personaAuthPortalToggle, automatedReturnToggle, counterProposalToggle, flatRateEnabled, rateCommissionSafeCheckout);
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
    sb.append("class OrganizationCollectionRead {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    vatNumber: ").append(toIndentedString(vatNumber)).append("\n");
    sb.append("    commercialRegistryNumber: ").append(toIndentedString(commercialRegistryNumber)).append("\n");
    sb.append("    websiteUrl: ").append(toIndentedString(websiteUrl)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    directNotificationToggle: ").append(toIndentedString(directNotificationToggle)).append("\n");
    sb.append("    safeCheckoutToggle: ").append(toIndentedString(safeCheckoutToggle)).append("\n");
    sb.append("    resolutionCenterToggle: ").append(toIndentedString(resolutionCenterToggle)).append("\n");
    sb.append("    internalMessagingToggle: ").append(toIndentedString(internalMessagingToggle)).append("\n");
    sb.append("    personaAuthPortalToggle: ").append(toIndentedString(personaAuthPortalToggle)).append("\n");
    sb.append("    automatedReturnToggle: ").append(toIndentedString(automatedReturnToggle)).append("\n");
    sb.append("    counterProposalToggle: ").append(toIndentedString(counterProposalToggle)).append("\n");
    sb.append("    flatRateEnabled: ").append(toIndentedString(flatRateEnabled)).append("\n");
    sb.append("    rateCommissionSafeCheckout: ").append(toIndentedString(rateCommissionSafeCheckout)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("vatNumber");
    openapiFields.add("commercialRegistryNumber");
    openapiFields.add("websiteUrl");
    openapiFields.add("icon");
    openapiFields.add("logo");
    openapiFields.add("directNotificationToggle");
    openapiFields.add("safeCheckoutToggle");
    openapiFields.add("resolutionCenterToggle");
    openapiFields.add("internalMessagingToggle");
    openapiFields.add("personaAuthPortalToggle");
    openapiFields.add("automatedReturnToggle");
    openapiFields.add("counterProposalToggle");
    openapiFields.add("flatRateEnabled");
    openapiFields.add("rateCommissionSafeCheckout");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("directNotificationToggle");
    openapiRequiredFields.add("safeCheckoutToggle");
    openapiRequiredFields.add("resolutionCenterToggle");
    openapiRequiredFields.add("internalMessagingToggle");
    openapiRequiredFields.add("personaAuthPortalToggle");
    openapiRequiredFields.add("automatedReturnToggle");
    openapiRequiredFields.add("counterProposalToggle");
    openapiRequiredFields.add("rateCommissionSafeCheckout");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to OrganizationCollectionRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationCollectionRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationCollectionRead is not found in the empty JSON string", OrganizationCollectionRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationCollectionRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationCollectionRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrganizationCollectionRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
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
      // validate the optional field `icon`
      if (jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) {
        OrganizationMediaCollectionRead.validateJsonElement(jsonObj.get("icon"));
      }
      // validate the optional field `logo`
      if (jsonObj.get("logo") != null && !jsonObj.get("logo").isJsonNull()) {
        OrganizationMediaCollectionRead.validateJsonElement(jsonObj.get("logo"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationCollectionRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationCollectionRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationCollectionRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationCollectionRead.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationCollectionRead>() {
           @Override
           public void write(JsonWriter out, OrganizationCollectionRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationCollectionRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of OrganizationCollectionRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of OrganizationCollectionRead
  * @throws IOException if the JSON string is invalid with respect to OrganizationCollectionRead
  */
  public static OrganizationCollectionRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationCollectionRead.class);
  }

 /**
  * Convert an instance of OrganizationCollectionRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

