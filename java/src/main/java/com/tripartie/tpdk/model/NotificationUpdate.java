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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T15:33:34.209225Z[Etc/UTC]")
public class NotificationUpdate {
  public static final String SERIALIZED_NAME_SEEN = "seen";
  @SerializedName(SERIALIZED_NAME_SEEN)
  private Boolean seen;

  public NotificationUpdate() {
  }

  public NotificationUpdate seen(Boolean seen) {
    this.seen = seen;
    return this;
  }

   /**
   * Get seen
   * @return seen
  **/
  @javax.annotation.Nonnull
  public Boolean getSeen() {
    return seen;
  }

  public void setSeen(Boolean seen) {
    this.seen = seen;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NotificationUpdate notificationUpdate = (NotificationUpdate) o;
    return Objects.equals(this.seen, notificationUpdate.seen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(seen);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NotificationUpdate {\n");
    sb.append("    seen: ").append(toIndentedString(seen)).append("\n");
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
    openapiFields.add("seen");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("seen");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to NotificationUpdate
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NotificationUpdate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NotificationUpdate is not found in the empty JSON string", NotificationUpdate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NotificationUpdate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NotificationUpdate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NotificationUpdate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NotificationUpdate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NotificationUpdate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NotificationUpdate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NotificationUpdate.class));

       return (TypeAdapter<T>) new TypeAdapter<NotificationUpdate>() {
           @Override
           public void write(JsonWriter out, NotificationUpdate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NotificationUpdate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of NotificationUpdate given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of NotificationUpdate
  * @throws IOException if the JSON string is invalid with respect to NotificationUpdate
  */
  public static NotificationUpdate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NotificationUpdate.class);
  }

 /**
  * Convert an instance of NotificationUpdate to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}
