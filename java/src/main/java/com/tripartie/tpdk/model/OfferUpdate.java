/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.178
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
import com.tripartie.tpdk.model.MetadataUpdate;
import java.io.IOException;
import java.math.BigDecimal;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T15:33:34.209225Z[Etc/UTC]")
public class OfferUpdate {
  public static final String SERIALIZED_NAME_PUBLIC_URL = "publicUrl";
  @SerializedName(SERIALIZED_NAME_PUBLIC_URL)
  private String publicUrl;

  public static final String SERIALIZED_NAME_ENFORCE_PERSONA_AUTH = "enforcePersonaAuth";
  @SerializedName(SERIALIZED_NAME_ENFORCE_PERSONA_AUTH)
  private Boolean enforcePersonaAuth = true;

  public static final String SERIALIZED_NAME_OVERRIDE_RATE_COMMISSION_SAFE_CHECKOUT = "overrideRateCommissionSafeCheckout";
  @SerializedName(SERIALIZED_NAME_OVERRIDE_RATE_COMMISSION_SAFE_CHECKOUT)
  private BigDecimal overrideRateCommissionSafeCheckout;

  public static final String SERIALIZED_NAME_REDIRECT_URL = "redirectUrl";
  @SerializedName(SERIALIZED_NAME_REDIRECT_URL)
  private String redirectUrl;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_UNIT_PRICE = "unitPrice";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE)
  private BigDecimal unitPrice;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "currencyCode";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode = "EUR";

  public static final String SERIALIZED_NAME_ITEM_COUNT = "itemCount";
  @SerializedName(SERIALIZED_NAME_ITEM_COUNT)
  private Integer itemCount = 1;

  public static final String SERIALIZED_NAME_WEIGHT_IN_GRAM = "weightInGram";
  @SerializedName(SERIALIZED_NAME_WEIGHT_IN_GRAM)
  private Integer weightInGram;

  public static final String SERIALIZED_NAME_SHIPPING_ALLOWED = "shippingAllowed";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ALLOWED)
  private Boolean shippingAllowed;

  public static final String SERIALIZED_NAME_HAND_DELIVERY_ALLOWED = "handDeliveryAllowed";
  @SerializedName(SERIALIZED_NAME_HAND_DELIVERY_ALLOWED)
  private Boolean handDeliveryAllowed = true;

  /**
   * Gets or Sets shippingCarriers
   */
  @JsonAdapter(ShippingCarriersEnum.Adapter.class)
  public enum ShippingCarriersEnum {
    SWISSPOST("SwissPost"),
    
    COLISSIMO("Colissimo"),
    
    MONDIALRELAY("MondialRelay");

    private String value;

    ShippingCarriersEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ShippingCarriersEnum fromValue(String value) {
      for (ShippingCarriersEnum b : ShippingCarriersEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ShippingCarriersEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ShippingCarriersEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ShippingCarriersEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ShippingCarriersEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ShippingCarriersEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SHIPPING_CARRIERS = "shippingCarriers";
  @SerializedName(SERIALIZED_NAME_SHIPPING_CARRIERS)
  private List<ShippingCarriersEnum> shippingCarriers;

  public static final String SERIALIZED_NAME_EAN_CODE = "eanCode";
  @SerializedName(SERIALIZED_NAME_EAN_CODE)
  private String eanCode;

  public static final String SERIALIZED_NAME_CAN_BE_SOLD_SEPARATELY = "canBeSoldSeparately";
  @SerializedName(SERIALIZED_NAME_CAN_BE_SOLD_SEPARATELY)
  private Boolean canBeSoldSeparately = true;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private List<MetadataUpdate> metadata;

  public OfferUpdate() {
  }

  public OfferUpdate publicUrl(String publicUrl) {
    this.publicUrl = publicUrl;
    return this;
  }

   /**
   * If specified, there would be not need for you to fill-in details. Must be accessible over WAN.
   * @return publicUrl
  **/
  @javax.annotation.Nullable
  public String getPublicUrl() {
    return publicUrl;
  }

  public void setPublicUrl(String publicUrl) {
    this.publicUrl = publicUrl;
  }


  public OfferUpdate enforcePersonaAuth(Boolean enforcePersonaAuth) {
    this.enforcePersonaAuth = enforcePersonaAuth;
    return this;
  }

   /**
   * Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration.
   * @return enforcePersonaAuth
  **/
  @javax.annotation.Nullable
  public Boolean getEnforcePersonaAuth() {
    return enforcePersonaAuth;
  }

  public void setEnforcePersonaAuth(Boolean enforcePersonaAuth) {
    this.enforcePersonaAuth = enforcePersonaAuth;
  }


  public OfferUpdate overrideRateCommissionSafeCheckout(BigDecimal overrideRateCommissionSafeCheckout) {
    this.overrideRateCommissionSafeCheckout = overrideRateCommissionSafeCheckout;
    return this;
  }

   /**
   * Override YOUR platform fees for that particular Offer.
   * @return overrideRateCommissionSafeCheckout
  **/
  @javax.annotation.Nullable
  public BigDecimal getOverrideRateCommissionSafeCheckout() {
    return overrideRateCommissionSafeCheckout;
  }

  public void setOverrideRateCommissionSafeCheckout(BigDecimal overrideRateCommissionSafeCheckout) {
    this.overrideRateCommissionSafeCheckout = overrideRateCommissionSafeCheckout;
  }


  public OfferUpdate redirectUrl(String redirectUrl) {
    this.redirectUrl = redirectUrl;
    return this;
  }

   /**
   * Fill-in that field IF you intend to redirect your customer instead of using a WebView.
   * @return redirectUrl
  **/
  @javax.annotation.Nullable
  public String getRedirectUrl() {
    return redirectUrl;
  }

  public void setRedirectUrl(String redirectUrl) {
    this.redirectUrl = redirectUrl;
  }


  public OfferUpdate title(String title) {
    this.title = title;
    return this;
  }

   /**
   * Get title
   * @return title
  **/
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public OfferUpdate description(String description) {
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public OfferUpdate unitPrice(BigDecimal unitPrice) {
    this.unitPrice = unitPrice;
    return this;
  }

   /**
   * Get unitPrice
   * @return unitPrice
  **/
  @javax.annotation.Nullable
  public BigDecimal getUnitPrice() {
    return unitPrice;
  }

  public void setUnitPrice(BigDecimal unitPrice) {
    this.unitPrice = unitPrice;
  }


  public OfferUpdate currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

   /**
   * Get currencyCode
   * @return currencyCode
  **/
  @javax.annotation.Nullable
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public OfferUpdate itemCount(Integer itemCount) {
    this.itemCount = itemCount;
    return this;
  }

   /**
   * Get itemCount
   * @return itemCount
  **/
  @javax.annotation.Nullable
  public Integer getItemCount() {
    return itemCount;
  }

  public void setItemCount(Integer itemCount) {
    this.itemCount = itemCount;
  }


  public OfferUpdate weightInGram(Integer weightInGram) {
    this.weightInGram = weightInGram;
    return this;
  }

   /**
   * Get weightInGram
   * @return weightInGram
  **/
  @javax.annotation.Nullable
  public Integer getWeightInGram() {
    return weightInGram;
  }

  public void setWeightInGram(Integer weightInGram) {
    this.weightInGram = weightInGram;
  }


  public OfferUpdate shippingAllowed(Boolean shippingAllowed) {
    this.shippingAllowed = shippingAllowed;
    return this;
  }

   /**
   * That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined.
   * @return shippingAllowed
  **/
  @javax.annotation.Nullable
  public Boolean getShippingAllowed() {
    return shippingAllowed;
  }

  public void setShippingAllowed(Boolean shippingAllowed) {
    this.shippingAllowed = shippingAllowed;
  }


  public OfferUpdate handDeliveryAllowed(Boolean handDeliveryAllowed) {
    this.handDeliveryAllowed = handDeliveryAllowed;
    return this;
  }

   /**
   * Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product.
   * @return handDeliveryAllowed
  **/
  @javax.annotation.Nullable
  public Boolean getHandDeliveryAllowed() {
    return handDeliveryAllowed;
  }

  public void setHandDeliveryAllowed(Boolean handDeliveryAllowed) {
    this.handDeliveryAllowed = handDeliveryAllowed;
  }


  public OfferUpdate shippingCarriers(List<ShippingCarriersEnum> shippingCarriers) {
    this.shippingCarriers = shippingCarriers;
    return this;
  }

  public OfferUpdate addShippingCarriersItem(ShippingCarriersEnum shippingCarriersItem) {
    if (this.shippingCarriers == null) {
      this.shippingCarriers = new ArrayList<>();
    }
    this.shippingCarriers.add(shippingCarriersItem);
    return this;
  }

   /**
   * If you wish to enable automated shipping label generation through a specific provider, specify it there.
   * @return shippingCarriers
  **/
  @javax.annotation.Nullable
  public List<ShippingCarriersEnum> getShippingCarriers() {
    return shippingCarriers;
  }

  public void setShippingCarriers(List<ShippingCarriersEnum> shippingCarriers) {
    this.shippingCarriers = shippingCarriers;
  }


  public OfferUpdate eanCode(String eanCode) {
    this.eanCode = eanCode;
    return this;
  }

   /**
   * Get eanCode
   * @return eanCode
  **/
  @javax.annotation.Nullable
  public String getEanCode() {
    return eanCode;
  }

  public void setEanCode(String eanCode) {
    this.eanCode = eanCode;
  }


  public OfferUpdate canBeSoldSeparately(Boolean canBeSoldSeparately) {
    this.canBeSoldSeparately = canBeSoldSeparately;
    return this;
  }

   /**
   * Set this flag to false to forbid a potential buyer to acquire this item separately.          This is only useful in a BulkOffer context.
   * @return canBeSoldSeparately
  **/
  @javax.annotation.Nullable
  public Boolean getCanBeSoldSeparately() {
    return canBeSoldSeparately;
  }

  public void setCanBeSoldSeparately(Boolean canBeSoldSeparately) {
    this.canBeSoldSeparately = canBeSoldSeparately;
  }


  public OfferUpdate metadata(List<MetadataUpdate> metadata) {
    this.metadata = metadata;
    return this;
  }

  public OfferUpdate addMetadataItem(MetadataUpdate metadataItem) {
    if (this.metadata == null) {
      this.metadata = new ArrayList<>();
    }
    this.metadata.add(metadataItem);
    return this;
  }

   /**
   * Get metadata
   * @return metadata
  **/
  @javax.annotation.Nullable
  public List<MetadataUpdate> getMetadata() {
    return metadata;
  }

  public void setMetadata(List<MetadataUpdate> metadata) {
    this.metadata = metadata;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OfferUpdate offerUpdate = (OfferUpdate) o;
    return Objects.equals(this.publicUrl, offerUpdate.publicUrl) &&
        Objects.equals(this.enforcePersonaAuth, offerUpdate.enforcePersonaAuth) &&
        Objects.equals(this.overrideRateCommissionSafeCheckout, offerUpdate.overrideRateCommissionSafeCheckout) &&
        Objects.equals(this.redirectUrl, offerUpdate.redirectUrl) &&
        Objects.equals(this.title, offerUpdate.title) &&
        Objects.equals(this.description, offerUpdate.description) &&
        Objects.equals(this.unitPrice, offerUpdate.unitPrice) &&
        Objects.equals(this.currencyCode, offerUpdate.currencyCode) &&
        Objects.equals(this.itemCount, offerUpdate.itemCount) &&
        Objects.equals(this.weightInGram, offerUpdate.weightInGram) &&
        Objects.equals(this.shippingAllowed, offerUpdate.shippingAllowed) &&
        Objects.equals(this.handDeliveryAllowed, offerUpdate.handDeliveryAllowed) &&
        Objects.equals(this.shippingCarriers, offerUpdate.shippingCarriers) &&
        Objects.equals(this.eanCode, offerUpdate.eanCode) &&
        Objects.equals(this.canBeSoldSeparately, offerUpdate.canBeSoldSeparately) &&
        Objects.equals(this.metadata, offerUpdate.metadata);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(publicUrl, enforcePersonaAuth, overrideRateCommissionSafeCheckout, redirectUrl, title, description, unitPrice, currencyCode, itemCount, weightInGram, shippingAllowed, handDeliveryAllowed, shippingCarriers, eanCode, canBeSoldSeparately, metadata);
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
    sb.append("class OfferUpdate {\n");
    sb.append("    publicUrl: ").append(toIndentedString(publicUrl)).append("\n");
    sb.append("    enforcePersonaAuth: ").append(toIndentedString(enforcePersonaAuth)).append("\n");
    sb.append("    overrideRateCommissionSafeCheckout: ").append(toIndentedString(overrideRateCommissionSafeCheckout)).append("\n");
    sb.append("    redirectUrl: ").append(toIndentedString(redirectUrl)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    itemCount: ").append(toIndentedString(itemCount)).append("\n");
    sb.append("    weightInGram: ").append(toIndentedString(weightInGram)).append("\n");
    sb.append("    shippingAllowed: ").append(toIndentedString(shippingAllowed)).append("\n");
    sb.append("    handDeliveryAllowed: ").append(toIndentedString(handDeliveryAllowed)).append("\n");
    sb.append("    shippingCarriers: ").append(toIndentedString(shippingCarriers)).append("\n");
    sb.append("    eanCode: ").append(toIndentedString(eanCode)).append("\n");
    sb.append("    canBeSoldSeparately: ").append(toIndentedString(canBeSoldSeparately)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
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
    openapiFields.add("publicUrl");
    openapiFields.add("enforcePersonaAuth");
    openapiFields.add("overrideRateCommissionSafeCheckout");
    openapiFields.add("redirectUrl");
    openapiFields.add("title");
    openapiFields.add("description");
    openapiFields.add("unitPrice");
    openapiFields.add("currencyCode");
    openapiFields.add("itemCount");
    openapiFields.add("weightInGram");
    openapiFields.add("shippingAllowed");
    openapiFields.add("handDeliveryAllowed");
    openapiFields.add("shippingCarriers");
    openapiFields.add("eanCode");
    openapiFields.add("canBeSoldSeparately");
    openapiFields.add("metadata");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to OfferUpdate
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OfferUpdate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OfferUpdate is not found in the empty JSON string", OfferUpdate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OfferUpdate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OfferUpdate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("publicUrl") != null && !jsonObj.get("publicUrl").isJsonNull()) && !jsonObj.get("publicUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicUrl").toString()));
      }
      if ((jsonObj.get("redirectUrl") != null && !jsonObj.get("redirectUrl").isJsonNull()) && !jsonObj.get("redirectUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `redirectUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("redirectUrl").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("currencyCode") != null && !jsonObj.get("currencyCode").isJsonNull()) && !jsonObj.get("currencyCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currencyCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currencyCode").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("shippingCarriers") != null && !jsonObj.get("shippingCarriers").isJsonNull() && !jsonObj.get("shippingCarriers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `shippingCarriers` to be an array in the JSON string but got `%s`", jsonObj.get("shippingCarriers").toString()));
      }
      if ((jsonObj.get("eanCode") != null && !jsonObj.get("eanCode").isJsonNull()) && !jsonObj.get("eanCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eanCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eanCode").toString()));
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
            MetadataUpdate.validateJsonElement(jsonArraymetadata.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OfferUpdate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OfferUpdate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OfferUpdate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OfferUpdate.class));

       return (TypeAdapter<T>) new TypeAdapter<OfferUpdate>() {
           @Override
           public void write(JsonWriter out, OfferUpdate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OfferUpdate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of OfferUpdate given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of OfferUpdate
  * @throws IOException if the JSON string is invalid with respect to OfferUpdate
  */
  public static OfferUpdate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OfferUpdate.class);
  }

 /**
  * Convert an instance of OfferUpdate to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}
