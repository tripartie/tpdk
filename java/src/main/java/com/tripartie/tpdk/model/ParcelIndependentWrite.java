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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T15:33:34.209225Z[Etc/UTC]")
public class ParcelIndependentWrite {
  /**
   * Gets or Sets carrier
   */
  @JsonAdapter(CarrierEnum.Adapter.class)
  public enum CarrierEnum {
    SWISSPOST("SwissPost"),
    
    MONDIALRELAY("MondialRelay"),
    
    COLISSIMO("Colissimo"),
    
    DHL("Dhl"),
    
    CHRONOPOST("Chronopost"),
    
    COLISPRIVE("ColisPrive"),
    
    DPD("Dpd"),
    
    UPS("Ups"),
    
    FEDEX("FedEx"),
    
    RELAISCOLIS("RelaisColis");

    private String value;

    CarrierEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CarrierEnum fromValue(String value) {
      for (CarrierEnum b : CarrierEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CarrierEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CarrierEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CarrierEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CarrierEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CarrierEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CARRIER = "carrier";
  @SerializedName(SERIALIZED_NAME_CARRIER)
  private CarrierEnum carrier;

  public static final String SERIALIZED_NAME_IDENTIFIER = "identifier";
  @SerializedName(SERIALIZED_NAME_IDENTIFIER)
  private String identifier;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private BigDecimal price;

  public static final String SERIALIZED_NAME_REFUNDABLE = "refundable";
  @SerializedName(SERIALIZED_NAME_REFUNDABLE)
  private Boolean refundable;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency = "EUR";

  public ParcelIndependentWrite() {
  }

  public ParcelIndependentWrite carrier(CarrierEnum carrier) {
    this.carrier = carrier;
    return this;
  }

   /**
   * Get carrier
   * @return carrier
  **/
  @javax.annotation.Nullable
  public CarrierEnum getCarrier() {
    return carrier;
  }

  public void setCarrier(CarrierEnum carrier) {
    this.carrier = carrier;
  }


  public ParcelIndependentWrite identifier(String identifier) {
    this.identifier = identifier;
    return this;
  }

   /**
   * Get identifier
   * @return identifier
  **/
  @javax.annotation.Nullable
  public String getIdentifier() {
    return identifier;
  }

  public void setIdentifier(String identifier) {
    this.identifier = identifier;
  }


  public ParcelIndependentWrite price(BigDecimal price) {
    this.price = price;
    return this;
  }

   /**
   * Get price
   * @return price
  **/
  @javax.annotation.Nullable
  public BigDecimal getPrice() {
    return price;
  }

  public void setPrice(BigDecimal price) {
    this.price = price;
  }


  public ParcelIndependentWrite refundable(Boolean refundable) {
    this.refundable = refundable;
    return this;
  }

   /**
   * Get refundable
   * @return refundable
  **/
  @javax.annotation.Nonnull
  public Boolean getRefundable() {
    return refundable;
  }

  public void setRefundable(Boolean refundable) {
    this.refundable = refundable;
  }


  public ParcelIndependentWrite currency(String currency) {
    this.currency = currency;
    return this;
  }

   /**
   * Get currency
   * @return currency
  **/
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ParcelIndependentWrite parcelIndependentWrite = (ParcelIndependentWrite) o;
    return Objects.equals(this.carrier, parcelIndependentWrite.carrier) &&
        Objects.equals(this.identifier, parcelIndependentWrite.identifier) &&
        Objects.equals(this.price, parcelIndependentWrite.price) &&
        Objects.equals(this.refundable, parcelIndependentWrite.refundable) &&
        Objects.equals(this.currency, parcelIndependentWrite.currency);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(carrier, identifier, price, refundable, currency);
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
    sb.append("class ParcelIndependentWrite {\n");
    sb.append("    carrier: ").append(toIndentedString(carrier)).append("\n");
    sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    refundable: ").append(toIndentedString(refundable)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
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
    openapiFields.add("carrier");
    openapiFields.add("identifier");
    openapiFields.add("price");
    openapiFields.add("refundable");
    openapiFields.add("currency");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("refundable");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to ParcelIndependentWrite
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ParcelIndependentWrite.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ParcelIndependentWrite is not found in the empty JSON string", ParcelIndependentWrite.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ParcelIndependentWrite.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ParcelIndependentWrite` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ParcelIndependentWrite.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("carrier") != null && !jsonObj.get("carrier").isJsonNull()) && !jsonObj.get("carrier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier").toString()));
      }
      // validate the optional field `carrier`
      if (jsonObj.get("carrier") != null && !jsonObj.get("carrier").isJsonNull()) {
        CarrierEnum.validateJsonElement(jsonObj.get("carrier"));
      }
      if ((jsonObj.get("identifier") != null && !jsonObj.get("identifier").isJsonNull()) && !jsonObj.get("identifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `identifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("identifier").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ParcelIndependentWrite.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ParcelIndependentWrite' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ParcelIndependentWrite> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ParcelIndependentWrite.class));

       return (TypeAdapter<T>) new TypeAdapter<ParcelIndependentWrite>() {
           @Override
           public void write(JsonWriter out, ParcelIndependentWrite value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ParcelIndependentWrite read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of ParcelIndependentWrite given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of ParcelIndependentWrite
  * @throws IOException if the JSON string is invalid with respect to ParcelIndependentWrite
  */
  public static ParcelIndependentWrite fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ParcelIndependentWrite.class);
  }

 /**
  * Convert an instance of ParcelIndependentWrite to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}
