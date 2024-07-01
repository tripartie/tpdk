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
import com.tripartie.tpdk.model.DisputeMetadataIndependentWrite;
import com.tripartie.tpdk.model.DisputePersonaIndependentWrite;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-07-01T08:05:26.133830Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class DisputeOfferIndependentWrite {
  public static final String SERIALIZED_NAME_PUBLIC_URL = "publicUrl";
  @SerializedName(SERIALIZED_NAME_PUBLIC_URL)
  private String publicUrl;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private DisputePersonaIndependentWrite seller;

  /**
   * This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information.
   */
  @JsonAdapter(NatureEnum.Adapter.class)
  public enum NatureEnum {
    SERVICE("service"),
    
    PHYSICAL_ITEM("physical_item"),
    
    DEMATERIALIZED_ITEM("dematerialized_item"),
    
    RENT_ITEM("rent_item");

    private String value;

    NatureEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NatureEnum fromValue(String value) {
      for (NatureEnum b : NatureEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NatureEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NatureEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NatureEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NatureEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NatureEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NATURE = "nature";
  @SerializedName(SERIALIZED_NAME_NATURE)
  private NatureEnum nature = NatureEnum.PHYSICAL_ITEM;

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

  /**
   * Gets or Sets condition
   */
  @JsonAdapter(ConditionEnum.Adapter.class)
  public enum ConditionEnum {
    NEW("NEW"),
    
    USED("USED"),
    
    DAMAGED("DAMAGED"),
    
    DETERIORATED("DETERIORATED"),
    
    UNRECOVERABLE("UNRECOVERABLE");

    private String value;

    ConditionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ConditionEnum fromValue(String value) {
      for (ConditionEnum b : ConditionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ConditionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ConditionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ConditionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ConditionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ConditionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CONDITION = "condition";
  @SerializedName(SERIALIZED_NAME_CONDITION)
  private ConditionEnum condition = ConditionEnum.USED;

  public static final String SERIALIZED_NAME_WEIGHT_IN_GRAM = "weightInGram";
  @SerializedName(SERIALIZED_NAME_WEIGHT_IN_GRAM)
  private Integer weightInGram;

  public static final String SERIALIZED_NAME_EAN_CODE = "eanCode";
  @SerializedName(SERIALIZED_NAME_EAN_CODE)
  private String eanCode;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private List<DisputeMetadataIndependentWrite> metadata = new ArrayList<>();

  public DisputeOfferIndependentWrite() {
  }

  public DisputeOfferIndependentWrite publicUrl(String publicUrl) {
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


  public DisputeOfferIndependentWrite seller(DisputePersonaIndependentWrite seller) {
    this.seller = seller;
    return this;
  }

   /**
   * If the seller is actually YOUR organization, set it to NULL.
   * @return seller
  **/
  @javax.annotation.Nonnull
  public DisputePersonaIndependentWrite getSeller() {
    return seller;
  }

  public void setSeller(DisputePersonaIndependentWrite seller) {
    this.seller = seller;
  }


  public DisputeOfferIndependentWrite nature(NatureEnum nature) {
    this.nature = nature;
    return this;
  }

   /**
   * This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information.
   * @return nature
  **/
  @javax.annotation.Nonnull
  public NatureEnum getNature() {
    return nature;
  }

  public void setNature(NatureEnum nature) {
    this.nature = nature;
  }


  public DisputeOfferIndependentWrite title(String title) {
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


  public DisputeOfferIndependentWrite description(String description) {
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


  public DisputeOfferIndependentWrite unitPrice(BigDecimal unitPrice) {
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


  public DisputeOfferIndependentWrite currencyCode(String currencyCode) {
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


  public DisputeOfferIndependentWrite itemCount(Integer itemCount) {
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


  public DisputeOfferIndependentWrite condition(ConditionEnum condition) {
    this.condition = condition;
    return this;
  }

   /**
   * Get condition
   * @return condition
  **/
  @javax.annotation.Nullable
  public ConditionEnum getCondition() {
    return condition;
  }

  public void setCondition(ConditionEnum condition) {
    this.condition = condition;
  }


  public DisputeOfferIndependentWrite weightInGram(Integer weightInGram) {
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


  public DisputeOfferIndependentWrite eanCode(String eanCode) {
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


  public DisputeOfferIndependentWrite metadata(List<DisputeMetadataIndependentWrite> metadata) {
    this.metadata = metadata;
    return this;
  }

  public DisputeOfferIndependentWrite addMetadataItem(DisputeMetadataIndependentWrite metadataItem) {
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
  public List<DisputeMetadataIndependentWrite> getMetadata() {
    return metadata;
  }

  public void setMetadata(List<DisputeMetadataIndependentWrite> metadata) {
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
    DisputeOfferIndependentWrite disputeOfferIndependentWrite = (DisputeOfferIndependentWrite) o;
    return Objects.equals(this.publicUrl, disputeOfferIndependentWrite.publicUrl) &&
        Objects.equals(this.seller, disputeOfferIndependentWrite.seller) &&
        Objects.equals(this.nature, disputeOfferIndependentWrite.nature) &&
        Objects.equals(this.title, disputeOfferIndependentWrite.title) &&
        Objects.equals(this.description, disputeOfferIndependentWrite.description) &&
        Objects.equals(this.unitPrice, disputeOfferIndependentWrite.unitPrice) &&
        Objects.equals(this.currencyCode, disputeOfferIndependentWrite.currencyCode) &&
        Objects.equals(this.itemCount, disputeOfferIndependentWrite.itemCount) &&
        Objects.equals(this.condition, disputeOfferIndependentWrite.condition) &&
        Objects.equals(this.weightInGram, disputeOfferIndependentWrite.weightInGram) &&
        Objects.equals(this.eanCode, disputeOfferIndependentWrite.eanCode) &&
        Objects.equals(this.metadata, disputeOfferIndependentWrite.metadata);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(publicUrl, seller, nature, title, description, unitPrice, currencyCode, itemCount, condition, weightInGram, eanCode, metadata);
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
    sb.append("class DisputeOfferIndependentWrite {\n");
    sb.append("    publicUrl: ").append(toIndentedString(publicUrl)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    nature: ").append(toIndentedString(nature)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    itemCount: ").append(toIndentedString(itemCount)).append("\n");
    sb.append("    condition: ").append(toIndentedString(condition)).append("\n");
    sb.append("    weightInGram: ").append(toIndentedString(weightInGram)).append("\n");
    sb.append("    eanCode: ").append(toIndentedString(eanCode)).append("\n");
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
    openapiFields.add("seller");
    openapiFields.add("nature");
    openapiFields.add("title");
    openapiFields.add("description");
    openapiFields.add("unitPrice");
    openapiFields.add("currencyCode");
    openapiFields.add("itemCount");
    openapiFields.add("condition");
    openapiFields.add("weightInGram");
    openapiFields.add("eanCode");
    openapiFields.add("metadata");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("seller");
    openapiRequiredFields.add("nature");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to DisputeOfferIndependentWrite
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DisputeOfferIndependentWrite.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DisputeOfferIndependentWrite is not found in the empty JSON string", DisputeOfferIndependentWrite.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DisputeOfferIndependentWrite.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DisputeOfferIndependentWrite` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DisputeOfferIndependentWrite.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("publicUrl") != null && !jsonObj.get("publicUrl").isJsonNull()) && !jsonObj.get("publicUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicUrl").toString()));
      }
      // validate the required field `seller`
      DisputePersonaIndependentWrite.validateJsonElement(jsonObj.get("seller"));
      if (!jsonObj.get("nature").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nature` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nature").toString()));
      }
      // validate the required field `nature`
      NatureEnum.validateJsonElement(jsonObj.get("nature"));
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("currencyCode") != null && !jsonObj.get("currencyCode").isJsonNull()) && !jsonObj.get("currencyCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currencyCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currencyCode").toString()));
      }
      if ((jsonObj.get("condition") != null && !jsonObj.get("condition").isJsonNull()) && !jsonObj.get("condition").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `condition` to be a primitive type in the JSON string but got `%s`", jsonObj.get("condition").toString()));
      }
      // validate the optional field `condition`
      if (jsonObj.get("condition") != null && !jsonObj.get("condition").isJsonNull()) {
        ConditionEnum.validateJsonElement(jsonObj.get("condition"));
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
            DisputeMetadataIndependentWrite.validateJsonElement(jsonArraymetadata.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DisputeOfferIndependentWrite.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DisputeOfferIndependentWrite' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DisputeOfferIndependentWrite> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DisputeOfferIndependentWrite.class));

       return (TypeAdapter<T>) new TypeAdapter<DisputeOfferIndependentWrite>() {
           @Override
           public void write(JsonWriter out, DisputeOfferIndependentWrite value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DisputeOfferIndependentWrite read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of DisputeOfferIndependentWrite given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of DisputeOfferIndependentWrite
  * @throws IOException if the JSON string is invalid with respect to DisputeOfferIndependentWrite
  */
  public static DisputeOfferIndependentWrite fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DisputeOfferIndependentWrite.class);
  }

 /**
  * Convert an instance of DisputeOfferIndependentWrite to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}
