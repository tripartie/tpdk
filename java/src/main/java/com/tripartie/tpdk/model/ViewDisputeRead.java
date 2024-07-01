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
import java.io.IOException;
import java.time.OffsetDateTime;
import java.util.Arrays;

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
public class ViewDisputeRead {
  public static final String SERIALIZED_NAME_HIT_COUNT = "hitCount";
  @SerializedName(SERIALIZED_NAME_HIT_COUNT)
  private Integer hitCount = 1;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  /**
   * Gets or Sets namedSource
   */
  @JsonAdapter(NamedSourceEnum.Adapter.class)
  public enum NamedSourceEnum {
    BUYER("BUYER"),
    
    PLATFORM("PLATFORM"),
    
    SELLER("SELLER"),
    
    OTHER("OTHER");

    private String value;

    NamedSourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NamedSourceEnum fromValue(String value) {
      for (NamedSourceEnum b : NamedSourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NamedSourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NamedSourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NamedSourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NamedSourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NamedSourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NAMED_SOURCE = "namedSource";
  @SerializedName(SERIALIZED_NAME_NAMED_SOURCE)
  private NamedSourceEnum namedSource;

  public ViewDisputeRead() {
  }

  public ViewDisputeRead(
     OffsetDateTime createdAt, 
     NamedSourceEnum namedSource
  ) {
    this();
    this.createdAt = createdAt;
    this.namedSource = namedSource;
  }

  public ViewDisputeRead hitCount(Integer hitCount) {
    this.hitCount = hitCount;
    return this;
  }

   /**
   * Get hitCount
   * @return hitCount
  **/
  @javax.annotation.Nonnull
  public Integer getHitCount() {
    return hitCount;
  }

  public void setHitCount(Integer hitCount) {
    this.hitCount = hitCount;
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
   * Get namedSource
   * @return namedSource
  **/
  @javax.annotation.Nullable
  public NamedSourceEnum getNamedSource() {
    return namedSource;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ViewDisputeRead viewDisputeRead = (ViewDisputeRead) o;
    return Objects.equals(this.hitCount, viewDisputeRead.hitCount) &&
        Objects.equals(this.createdAt, viewDisputeRead.createdAt) &&
        Objects.equals(this.namedSource, viewDisputeRead.namedSource);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hitCount, createdAt, namedSource);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ViewDisputeRead {\n");
    sb.append("    hitCount: ").append(toIndentedString(hitCount)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    namedSource: ").append(toIndentedString(namedSource)).append("\n");
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
    openapiFields.add("hitCount");
    openapiFields.add("createdAt");
    openapiFields.add("namedSource");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("hitCount");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to ViewDisputeRead
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ViewDisputeRead.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ViewDisputeRead is not found in the empty JSON string", ViewDisputeRead.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ViewDisputeRead.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ViewDisputeRead` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ViewDisputeRead.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("namedSource") != null && !jsonObj.get("namedSource").isJsonNull()) && !jsonObj.get("namedSource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `namedSource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("namedSource").toString()));
      }
      // validate the optional field `namedSource`
      if (jsonObj.get("namedSource") != null && !jsonObj.get("namedSource").isJsonNull()) {
        NamedSourceEnum.validateJsonElement(jsonObj.get("namedSource"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ViewDisputeRead.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ViewDisputeRead' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ViewDisputeRead> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ViewDisputeRead.class));

       return (TypeAdapter<T>) new TypeAdapter<ViewDisputeRead>() {
           @Override
           public void write(JsonWriter out, ViewDisputeRead value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ViewDisputeRead read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of ViewDisputeRead given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of ViewDisputeRead
  * @throws IOException if the JSON string is invalid with respect to ViewDisputeRead
  */
  public static ViewDisputeRead fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ViewDisputeRead.class);
  }

 /**
  * Convert an instance of ViewDisputeRead to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

