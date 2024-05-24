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
import com.tripartie.tpdk.model.MediaUserRead;
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
public class OrganizationUserRead {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_DOMAIN_VERIFIED = "domainVerified";
  @SerializedName(SERIALIZED_NAME_DOMAIN_VERIFIED)
  private Boolean domainVerified;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private MediaUserRead icon;

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private MediaUserRead logo;

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

  public OrganizationUserRead() {
  }

  public OrganizationUserRead(
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



  public OrganizationUserRead name(String name) {
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


  public OrganizationUserRead domainVerified(Boolean domainVerified) {
    this.domainVerified = domainVerified;
    return this;
  }

   /**
   * Get domainVerified
   * @return domainVerified
  **/
  @javax.annotation.Nonnull
  public Boolean getDomainVerified() {
    return domainVerified;
  }

  public void setDomainVerified(Boolean domainVerified) {
    this.domainVerified = domainVerified;
  }


  public OrganizationUserRead icon(MediaUserRead icon) {
    this.icon = icon;
    return this;
  }

   /**
   * Get icon
   * @return icon
  **/
  @javax.annotation.Nullable
  public MediaUserRead getIcon() {
    return icon;
  }

  public void setIcon(MediaUserRead icon) {
    this.icon = icon;
  }


  public OrganizationUserRead logo(MediaUserRead logo) {
    this.logo = logo;
    return this;
  }

   /**
   * Get logo
   * @return logo
  **/
  @javax.annotation.Nullable
  public MediaUserRead getLogo() {
    return logo;
  }

  public void setLogo(MediaUserRead logo) {
    this.logo = logo;
  }


  public OrganizationUserRead safeCheckoutToggle(Boolean safeCheckoutToggle) {
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


  public OrganizationUserRead resolutionCenterToggle(Boolean resolutionCenterToggle) {
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


  public OrganizationUserRead internalMessagingToggle(Boolean internalMessagingToggle) {
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


  public OrganizationUserRead personaAuthPortalToggle(Boolean personaAuthPortalToggle) {
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


  public OrganizationUserRead automatedReturnToggle(Boolean automatedReturnToggle) {
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


  public OrganizationUserRead counterProposalToggle(Boolean counterProposalToggle) {
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



  public OrganizationUserRead rateCommissionSafeCheckout(BigDecimal rateCommissionSafeCheckout) {
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
    OrganizationUserRead organizationUserRead = (OrganizationUserRead) o;
    return Objects.equals(this.id, organizationUserRead.id) &&
        Objects.equals(this.name, organizationUserRead.name) &&
        Objects.equals(this.domainVerified, organizationUserRead.domainVerified) &&
        Objects.equals(this.icon, organizationUserRead.icon) &&
        Objects.equals(this.logo, organizationUserRead.logo) &&
        Objects.equals(this.safeCheckoutToggle, organizationUserRead.safeCheckoutToggle) &&
        Objects.equals(this.resolutionCenterToggle, organizationUserRead.resolutionCenterToggle) &&
        Objects.equals(this.internalMessagingToggle, organizationUserRead.internalMessagingToggle) &&
        Objects.equals(this.personaAuthPortalToggle, organizationUserRead.personaAuthPortalToggle) &&
        Objects.equals(this.automatedReturnToggle, organizationUserRead.automatedReturnToggle) &&
        Objects.equals(this.counterProposalToggle, organizationUserRead.counterProposalToggle) &&
        Objects.equals(this.flatRateEnabled, organizationUserRead.flatRateEnabled) &&
        Objects.equals(this.rateCommissionSafeCheckout, organizationUserRead.rateCommissionSafeCheckout);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, domainVerified, icon, logo, safeCheckoutToggle, resolutionCenterToggle, internalMessagingToggle, personaAuthPortalToggle, automatedReturnToggle, counterProposalToggle, flatRateEnabled, rateCommissionSafeCheckout);
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
    sb.append("class OrganizationUserRead {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    domainVerified: ").append(toIndentedString(domainVerified)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
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
    openapiFields.add("domainVerified");
    openapiFields.add("icon");
    openapiFields.add("logo");
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
    openapiRequiredFields.add("domainVerified");
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
  * @throws IOException if the JSON Element is invalid with respect to OrganizationUserRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationUserRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationUserRead is not found in the empty JSON string", OrganizationUserRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationUserRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationUserRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrganizationUserRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `icon`
      if (jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) {
        MediaUserRead.validateJsonElement(jsonObj.get("icon"));
      }
      // validate the optional field `logo`
      if (jsonObj.get("logo") != null && !jsonObj.get("logo").isJsonNull()) {
        MediaUserRead.validateJsonElement(jsonObj.get("logo"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationUserRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationUserRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationUserRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationUserRead.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationUserRead>() {
           @Override
           public void write(JsonWriter out, OrganizationUserRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationUserRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of OrganizationUserRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of OrganizationUserRead
  * @throws IOException if the JSON string is invalid with respect to OrganizationUserRead
  */
  public static OrganizationUserRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationUserRead.class);
  }

 /**
  * Convert an instance of OrganizationUserRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

