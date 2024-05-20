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
import com.tripartie.tpdk.model.MediaRead;
import java.io.IOException;
import java.time.OffsetDateTime;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-20T08:05:14.680974Z[Etc/UTC]", comments = "Generator version: 7.5.0")
public class EvidenceRead {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    SUBMITTED("SUBMITTED"),
    
    CORRELATED("CORRELATED"),
    
    UNRELATED("UNRELATED"),
    
    PENDING("PENDING"),
    
    TEMPERED("TEMPERED"),
    
    REJECTED("REJECTED");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status = StatusEnum.SUBMITTED;

  public static final String SERIALIZED_NAME_MEDIA = "media";
  @SerializedName(SERIALIZED_NAME_MEDIA)
  private MediaRead media;

  public static final String SERIALIZED_NAME_ADDITIONAL_INFORMATION = "additionalInformation";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_INFORMATION)
  private String additionalInformation;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  /**
   * Shortcut to whomever sent the evidence
   */
  @JsonAdapter(PublisherEnum.Adapter.class)
  public enum PublisherEnum {
    BUYER("BUYER"),
    
    PLATFORM("PLATFORM"),
    
    SELLER("SELLER");

    private String value;

    PublisherEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PublisherEnum fromValue(String value) {
      for (PublisherEnum b : PublisherEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PublisherEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PublisherEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PublisherEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PublisherEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PublisherEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PUBLISHER = "publisher";
  @SerializedName(SERIALIZED_NAME_PUBLISHER)
  private PublisherEnum publisher;

  public EvidenceRead() {
  }

  public EvidenceRead(
     Integer id, 
     OffsetDateTime createdAt, 
     OffsetDateTime updatedAt, 
     PublisherEnum publisher
  ) {
    this();
    this.id = id;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
    this.publisher = publisher;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public EvidenceRead status(StatusEnum status) {
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public EvidenceRead media(MediaRead media) {
    this.media = media;
    return this;
  }

   /**
   * Get media
   * @return media
  **/
  @javax.annotation.Nullable
  public MediaRead getMedia() {
    return media;
  }

  public void setMedia(MediaRead media) {
    this.media = media;
  }


  public EvidenceRead additionalInformation(String additionalInformation) {
    this.additionalInformation = additionalInformation;
    return this;
  }

   /**
   * Description of what the evidence actually is.
   * @return additionalInformation
  **/
  @javax.annotation.Nullable
  public String getAdditionalInformation() {
    return additionalInformation;
  }

  public void setAdditionalInformation(String additionalInformation) {
    this.additionalInformation = additionalInformation;
  }


   /**
   * Get createdAt
   * @return createdAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



   /**
   * Get updatedAt
   * @return updatedAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



   /**
   * Shortcut to whomever sent the evidence
   * @return publisher
  **/
  @javax.annotation.Nullable
  public PublisherEnum getPublisher() {
    return publisher;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EvidenceRead evidenceRead = (EvidenceRead) o;
    return Objects.equals(this.id, evidenceRead.id) &&
        Objects.equals(this.status, evidenceRead.status) &&
        Objects.equals(this.media, evidenceRead.media) &&
        Objects.equals(this.additionalInformation, evidenceRead.additionalInformation) &&
        Objects.equals(this.createdAt, evidenceRead.createdAt) &&
        Objects.equals(this.updatedAt, evidenceRead.updatedAt) &&
        Objects.equals(this.publisher, evidenceRead.publisher);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, status, media, additionalInformation, createdAt, updatedAt, publisher);
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
    sb.append("class EvidenceRead {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    media: ").append(toIndentedString(media)).append("\n");
    sb.append("    additionalInformation: ").append(toIndentedString(additionalInformation)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    publisher: ").append(toIndentedString(publisher)).append("\n");
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
    openapiFields.add("status");
    openapiFields.add("media");
    openapiFields.add("additionalInformation");
    openapiFields.add("createdAt");
    openapiFields.add("updatedAt");
    openapiFields.add("publisher");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("status");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to EvidenceRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EvidenceRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EvidenceRead is not found in the empty JSON string", EvidenceRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EvidenceRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EvidenceRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EvidenceRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      // validate the optional field `media`
      if (jsonObj.get("media") != null && !jsonObj.get("media").isJsonNull()) {
        MediaRead.validateJsonElement(jsonObj.get("media"));
      }
      if ((jsonObj.get("additionalInformation") != null && !jsonObj.get("additionalInformation").isJsonNull()) && !jsonObj.get("additionalInformation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `additionalInformation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("additionalInformation").toString()));
      }
      if ((jsonObj.get("publisher") != null && !jsonObj.get("publisher").isJsonNull()) && !jsonObj.get("publisher").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publisher` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publisher").toString()));
      }
      // validate the optional field `publisher`
      if (jsonObj.get("publisher") != null && !jsonObj.get("publisher").isJsonNull()) {
        PublisherEnum.validateJsonElement(jsonObj.get("publisher"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EvidenceRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EvidenceRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EvidenceRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EvidenceRead.class));

       return (TypeAdapter<T>) new TypeAdapter<EvidenceRead>() {
           @Override
           public void write(JsonWriter out, EvidenceRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EvidenceRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of EvidenceRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of EvidenceRead
  * @throws IOException if the JSON string is invalid with respect to EvidenceRead
  */
  public static EvidenceRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EvidenceRead.class);
  }

 /**
  * Convert an instance of EvidenceRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

