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
import com.tripartie.tpdk.model.MetadataRead;
import com.tripartie.tpdk.model.OfferRead;
import com.tripartie.tpdk.model.ParcelRead;
import com.tripartie.tpdk.model.PersonaRead;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-20T08:05:14.680974Z[Etc/UTC]", comments = "Generator version: 7.5.0")
public class TransactionRead {
  public static final String SERIALIZED_NAME_ULID = "ulid";
  @SerializedName(SERIALIZED_NAME_ULID)
  private String ulid;

  public static final String SERIALIZED_NAME_OFFER = "offer";
  @SerializedName(SERIALIZED_NAME_OFFER)
  private OfferRead offer;

  public static final String SERIALIZED_NAME_BUYER = "buyer";
  @SerializedName(SERIALIZED_NAME_BUYER)
  private PersonaRead buyer;

  public static final String SERIALIZED_NAME_FEES = "fees";
  @SerializedName(SERIALIZED_NAME_FEES)
  private BigDecimal fees;

  public static final String SERIALIZED_NAME_REFUNDABLE_FEES = "refundableFees";
  @SerializedName(SERIALIZED_NAME_REFUNDABLE_FEES)
  private Boolean refundableFees;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private List<MetadataRead> metadata = new ArrayList<>();

  public static final String SERIALIZED_NAME_PARCELS = "parcels";
  @SerializedName(SERIALIZED_NAME_PARCELS)
  private List<ParcelRead> parcels = new ArrayList<>();

  public TransactionRead() {
  }

  public TransactionRead ulid(String ulid) {
    this.ulid = ulid;
    return this;
  }

   /**
   * Get ulid
   * @return ulid
  **/
  @javax.annotation.Nonnull
  public String getUlid() {
    return ulid;
  }

  public void setUlid(String ulid) {
    this.ulid = ulid;
  }


  public TransactionRead offer(OfferRead offer) {
    this.offer = offer;
    return this;
  }

   /**
   * Get offer
   * @return offer
  **/
  @javax.annotation.Nonnull
  public OfferRead getOffer() {
    return offer;
  }

  public void setOffer(OfferRead offer) {
    this.offer = offer;
  }


  public TransactionRead buyer(PersonaRead buyer) {
    this.buyer = buyer;
    return this;
  }

   /**
   * Get buyer
   * @return buyer
  **/
  @javax.annotation.Nonnull
  public PersonaRead getBuyer() {
    return buyer;
  }

  public void setBuyer(PersonaRead buyer) {
    this.buyer = buyer;
  }


  public TransactionRead fees(BigDecimal fees) {
    this.fees = fees;
    return this;
  }

   /**
   * Get fees
   * @return fees
  **/
  @javax.annotation.Nullable
  public BigDecimal getFees() {
    return fees;
  }

  public void setFees(BigDecimal fees) {
    this.fees = fees;
  }


  public TransactionRead refundableFees(Boolean refundableFees) {
    this.refundableFees = refundableFees;
    return this;
  }

   /**
   * Get refundableFees
   * @return refundableFees
  **/
  @javax.annotation.Nullable
  public Boolean getRefundableFees() {
    return refundableFees;
  }

  public void setRefundableFees(Boolean refundableFees) {
    this.refundableFees = refundableFees;
  }


  public TransactionRead metadata(List<MetadataRead> metadata) {
    this.metadata = metadata;
    return this;
  }

  public TransactionRead addMetadataItem(MetadataRead metadataItem) {
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
  public List<MetadataRead> getMetadata() {
    return metadata;
  }

  public void setMetadata(List<MetadataRead> metadata) {
    this.metadata = metadata;
  }


  public TransactionRead parcels(List<ParcelRead> parcels) {
    this.parcels = parcels;
    return this;
  }

  public TransactionRead addParcelsItem(ParcelRead parcelsItem) {
    if (this.parcels == null) {
      this.parcels = new ArrayList<>();
    }
    this.parcels.add(parcelsItem);
    return this;
  }

   /**
   * Get parcels
   * @return parcels
  **/
  @javax.annotation.Nullable
  public List<ParcelRead> getParcels() {
    return parcels;
  }

  public void setParcels(List<ParcelRead> parcels) {
    this.parcels = parcels;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TransactionRead transactionRead = (TransactionRead) o;
    return Objects.equals(this.ulid, transactionRead.ulid) &&
        Objects.equals(this.offer, transactionRead.offer) &&
        Objects.equals(this.buyer, transactionRead.buyer) &&
        Objects.equals(this.fees, transactionRead.fees) &&
        Objects.equals(this.refundableFees, transactionRead.refundableFees) &&
        Objects.equals(this.metadata, transactionRead.metadata) &&
        Objects.equals(this.parcels, transactionRead.parcels);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(ulid, offer, buyer, fees, refundableFees, metadata, parcels);
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
    sb.append("class TransactionRead {\n");
    sb.append("    ulid: ").append(toIndentedString(ulid)).append("\n");
    sb.append("    offer: ").append(toIndentedString(offer)).append("\n");
    sb.append("    buyer: ").append(toIndentedString(buyer)).append("\n");
    sb.append("    fees: ").append(toIndentedString(fees)).append("\n");
    sb.append("    refundableFees: ").append(toIndentedString(refundableFees)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    parcels: ").append(toIndentedString(parcels)).append("\n");
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
    openapiFields.add("offer");
    openapiFields.add("buyer");
    openapiFields.add("fees");
    openapiFields.add("refundableFees");
    openapiFields.add("metadata");
    openapiFields.add("parcels");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ulid");
    openapiRequiredFields.add("offer");
    openapiRequiredFields.add("buyer");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to TransactionRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TransactionRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TransactionRead is not found in the empty JSON string", TransactionRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TransactionRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TransactionRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TransactionRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("ulid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ulid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ulid").toString()));
      }
      // validate the required field `offer`
      OfferRead.validateJsonElement(jsonObj.get("offer"));
      // validate the required field `buyer`
      PersonaRead.validateJsonElement(jsonObj.get("buyer"));
      if (jsonObj.get("metadata") != null && !jsonObj.get("metadata").isJsonNull()) {
        JsonArray jsonArraymetadata = jsonObj.getAsJsonArray("metadata");
        if (jsonArraymetadata != null) {
          // ensure the json data is an array
          if (!jsonObj.get("metadata").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `metadata` to be an array in the JSON string but got `%s`", jsonObj.get("metadata").toString()));
          }

          // validate the optional field `metadata` (array)
          for (int i = 0; i < jsonArraymetadata.size(); i++) {
            MetadataRead.validateJsonElement(jsonArraymetadata.get(i));
          };
        }
      }
      if (jsonObj.get("parcels") != null && !jsonObj.get("parcels").isJsonNull()) {
        JsonArray jsonArrayparcels = jsonObj.getAsJsonArray("parcels");
        if (jsonArrayparcels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("parcels").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `parcels` to be an array in the JSON string but got `%s`", jsonObj.get("parcels").toString()));
          }

          // validate the optional field `parcels` (array)
          for (int i = 0; i < jsonArrayparcels.size(); i++) {
            ParcelRead.validateJsonElement(jsonArrayparcels.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TransactionRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TransactionRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TransactionRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TransactionRead.class));

       return (TypeAdapter<T>) new TypeAdapter<TransactionRead>() {
           @Override
           public void write(JsonWriter out, TransactionRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TransactionRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TransactionRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TransactionRead
  * @throws IOException if the JSON string is invalid with respect to TransactionRead
  */
  public static TransactionRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TransactionRead.class);
  }

 /**
  * Convert an instance of TransactionRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

