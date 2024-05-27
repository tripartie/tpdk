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
import com.tripartie.tpdk.model.DisputeMediaRead;
import com.tripartie.tpdk.model.DisputeOrganizationRead;
import com.tripartie.tpdk.model.DisputePersonaRead;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-27T05:16:17.029359Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class DisputeOfferRead {
  public static final String SERIALIZED_NAME_ULID = "ulid";
  @SerializedName(SERIALIZED_NAME_ULID)
  private String ulid;

  public static final String SERIALIZED_NAME_PUBLIC_URL = "publicUrl";
  @SerializedName(SERIALIZED_NAME_PUBLIC_URL)
  private String publicUrl;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private DisputeOrganizationRead organization;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private DisputePersonaRead seller;

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

  public static final String SERIALIZED_NAME_MEDIAS = "medias";
  @SerializedName(SERIALIZED_NAME_MEDIAS)
  private List<DisputeMediaRead> medias = new ArrayList<>();

  public DisputeOfferRead() {
  }

  public DisputeOfferRead ulid(String ulid) {
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


  public DisputeOfferRead publicUrl(String publicUrl) {
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


  public DisputeOfferRead organization(DisputeOrganizationRead organization) {
    this.organization = organization;
    return this;
  }

   /**
   * Get organization
   * @return organization
  **/
  @javax.annotation.Nullable
  public DisputeOrganizationRead getOrganization() {
    return organization;
  }

  public void setOrganization(DisputeOrganizationRead organization) {
    this.organization = organization;
  }


  public DisputeOfferRead seller(DisputePersonaRead seller) {
    this.seller = seller;
    return this;
  }

   /**
   * If the seller is actually YOUR organization, set it to NULL.
   * @return seller
  **/
  @javax.annotation.Nonnull
  public DisputePersonaRead getSeller() {
    return seller;
  }

  public void setSeller(DisputePersonaRead seller) {
    this.seller = seller;
  }


  public DisputeOfferRead nature(NatureEnum nature) {
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


  public DisputeOfferRead title(String title) {
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


  public DisputeOfferRead description(String description) {
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


  public DisputeOfferRead unitPrice(BigDecimal unitPrice) {
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


  public DisputeOfferRead currencyCode(String currencyCode) {
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


  public DisputeOfferRead itemCount(Integer itemCount) {
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


  public DisputeOfferRead condition(ConditionEnum condition) {
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


  public DisputeOfferRead medias(List<DisputeMediaRead> medias) {
    this.medias = medias;
    return this;
  }

  public DisputeOfferRead addMediasItem(DisputeMediaRead mediasItem) {
    if (this.medias == null) {
      this.medias = new ArrayList<>();
    }
    this.medias.add(mediasItem);
    return this;
  }

   /**
   * Get medias
   * @return medias
  **/
  @javax.annotation.Nonnull
  public List<DisputeMediaRead> getMedias() {
    return medias;
  }

  public void setMedias(List<DisputeMediaRead> medias) {
    this.medias = medias;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DisputeOfferRead disputeOfferRead = (DisputeOfferRead) o;
    return Objects.equals(this.ulid, disputeOfferRead.ulid) &&
        Objects.equals(this.publicUrl, disputeOfferRead.publicUrl) &&
        Objects.equals(this.organization, disputeOfferRead.organization) &&
        Objects.equals(this.seller, disputeOfferRead.seller) &&
        Objects.equals(this.nature, disputeOfferRead.nature) &&
        Objects.equals(this.title, disputeOfferRead.title) &&
        Objects.equals(this.description, disputeOfferRead.description) &&
        Objects.equals(this.unitPrice, disputeOfferRead.unitPrice) &&
        Objects.equals(this.currencyCode, disputeOfferRead.currencyCode) &&
        Objects.equals(this.itemCount, disputeOfferRead.itemCount) &&
        Objects.equals(this.condition, disputeOfferRead.condition) &&
        Objects.equals(this.medias, disputeOfferRead.medias);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(ulid, publicUrl, organization, seller, nature, title, description, unitPrice, currencyCode, itemCount, condition, medias);
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
    sb.append("class DisputeOfferRead {\n");
    sb.append("    ulid: ").append(toIndentedString(ulid)).append("\n");
    sb.append("    publicUrl: ").append(toIndentedString(publicUrl)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    nature: ").append(toIndentedString(nature)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    itemCount: ").append(toIndentedString(itemCount)).append("\n");
    sb.append("    condition: ").append(toIndentedString(condition)).append("\n");
    sb.append("    medias: ").append(toIndentedString(medias)).append("\n");
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
    openapiFields.add("publicUrl");
    openapiFields.add("organization");
    openapiFields.add("seller");
    openapiFields.add("nature");
    openapiFields.add("title");
    openapiFields.add("description");
    openapiFields.add("unitPrice");
    openapiFields.add("currencyCode");
    openapiFields.add("itemCount");
    openapiFields.add("condition");
    openapiFields.add("medias");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ulid");
    openapiRequiredFields.add("seller");
    openapiRequiredFields.add("nature");
    openapiRequiredFields.add("medias");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to DisputeOfferRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DisputeOfferRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DisputeOfferRead is not found in the empty JSON string", DisputeOfferRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DisputeOfferRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DisputeOfferRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DisputeOfferRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("ulid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ulid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ulid").toString()));
      }
      if ((jsonObj.get("publicUrl") != null && !jsonObj.get("publicUrl").isJsonNull()) && !jsonObj.get("publicUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicUrl").toString()));
      }
      // validate the optional field `organization`
      if (jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonNull()) {
        DisputeOrganizationRead.validateJsonElement(jsonObj.get("organization"));
      }
      // validate the required field `seller`
      DisputePersonaRead.validateJsonElement(jsonObj.get("seller"));
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
      // ensure the json data is an array
      if (!jsonObj.get("medias").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `medias` to be an array in the JSON string but got `%s`", jsonObj.get("medias").toString()));
      }

      JsonArray jsonArraymedias = jsonObj.getAsJsonArray("medias");
      // validate the required field `medias` (array)
      for (int i = 0; i < jsonArraymedias.size(); i++) {
        DisputeMediaRead.validateJsonElement(jsonArraymedias.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DisputeOfferRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DisputeOfferRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DisputeOfferRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DisputeOfferRead.class));

       return (TypeAdapter<T>) new TypeAdapter<DisputeOfferRead>() {
           @Override
           public void write(JsonWriter out, DisputeOfferRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DisputeOfferRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of DisputeOfferRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of DisputeOfferRead
  * @throws IOException if the JSON string is invalid with respect to DisputeOfferRead
  */
  public static DisputeOfferRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DisputeOfferRead.class);
  }

 /**
  * Convert an instance of DisputeOfferRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

