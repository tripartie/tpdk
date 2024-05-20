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


package com.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
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
 * Access directly our resolution center without having used the safe-checkout feature.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-20T08:05:14.680974Z[Etc/UTC]", comments = "Generator version: 7.5.0")
public class DisputePostCreationRead {
  public static final String SERIALIZED_NAME_ULID = "ulid";
  @SerializedName(SERIALIZED_NAME_ULID)
  private String ulid;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public static final String SERIALIZED_NAME_BUYER_ID = "buyerId";
  @SerializedName(SERIALIZED_NAME_BUYER_ID)
  private Integer buyerId;

  public static final String SERIALIZED_NAME_SELLER_ID = "sellerId";
  @SerializedName(SERIALIZED_NAME_SELLER_ID)
  private Integer sellerId;

  public static final String SERIALIZED_NAME_OFFER_ULID = "offerUlid";
  @SerializedName(SERIALIZED_NAME_OFFER_ULID)
  private String offerUlid;

  public DisputePostCreationRead() {
  }

  public DisputePostCreationRead(
     Integer buyerId, 
     Integer sellerId, 
     String offerUlid
  ) {
    this();
    this.buyerId = buyerId;
    this.sellerId = sellerId;
    this.offerUlid = offerUlid;
  }

  public DisputePostCreationRead ulid(String ulid) {
    this.ulid = ulid;
    return this;
  }

   /**
   * Get ulid
   * @return ulid
  **/
  @javax.annotation.Nullable
  public String getUlid() {
    return ulid;
  }

  public void setUlid(String ulid) {
    this.ulid = ulid;
  }


  public DisputePostCreationRead url(String url) {
    this.url = url;
    return this;
  }

   /**
   * Get url
   * @return url
  **/
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }


   /**
   * Get buyerId
   * @return buyerId
  **/
  @javax.annotation.Nullable
  public Integer getBuyerId() {
    return buyerId;
  }



   /**
   * Get sellerId
   * @return sellerId
  **/
  @javax.annotation.Nullable
  public Integer getSellerId() {
    return sellerId;
  }



   /**
   * Get offerUlid
   * @return offerUlid
  **/
  @javax.annotation.Nullable
  public String getOfferUlid() {
    return offerUlid;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DisputePostCreationRead disputePostCreationRead = (DisputePostCreationRead) o;
    return Objects.equals(this.ulid, disputePostCreationRead.ulid) &&
        Objects.equals(this.url, disputePostCreationRead.url) &&
        Objects.equals(this.buyerId, disputePostCreationRead.buyerId) &&
        Objects.equals(this.sellerId, disputePostCreationRead.sellerId) &&
        Objects.equals(this.offerUlid, disputePostCreationRead.offerUlid);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(ulid, url, buyerId, sellerId, offerUlid);
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
    sb.append("class DisputePostCreationRead {\n");
    sb.append("    ulid: ").append(toIndentedString(ulid)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    buyerId: ").append(toIndentedString(buyerId)).append("\n");
    sb.append("    sellerId: ").append(toIndentedString(sellerId)).append("\n");
    sb.append("    offerUlid: ").append(toIndentedString(offerUlid)).append("\n");
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
    openapiFields.add("ulid");
    openapiFields.add("url");
    openapiFields.add("buyerId");
    openapiFields.add("sellerId");
    openapiFields.add("offerUlid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to DisputePostCreationRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DisputePostCreationRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DisputePostCreationRead is not found in the empty JSON string", DisputePostCreationRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DisputePostCreationRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DisputePostCreationRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ulid") != null && !jsonObj.get("ulid").isJsonNull()) && !jsonObj.get("ulid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ulid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ulid").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if ((jsonObj.get("offerUlid") != null && !jsonObj.get("offerUlid").isJsonNull()) && !jsonObj.get("offerUlid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `offerUlid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("offerUlid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DisputePostCreationRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DisputePostCreationRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DisputePostCreationRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DisputePostCreationRead.class));

       return (TypeAdapter<T>) new TypeAdapter<DisputePostCreationRead>() {
           @Override
           public void write(JsonWriter out, DisputePostCreationRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DisputePostCreationRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of DisputePostCreationRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of DisputePostCreationRead
  * @throws IOException if the JSON string is invalid with respect to DisputePostCreationRead
  */
  public static DisputePostCreationRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DisputePostCreationRead.class);
  }

 /**
  * Convert an instance of DisputePostCreationRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

