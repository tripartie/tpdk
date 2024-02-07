/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.177
 * Contact: noc@tripartie.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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

import org.tripartie.tpdk.JSON;

/**
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T10:32:44.249249Z[Etc/UTC]")
public class ApiClientWrite {
  public static final String SERIALIZED_NAME_REFERENCE_NAME = "referenceName";
  @SerializedName(SERIALIZED_NAME_REFERENCE_NAME)
  private String referenceName;

  /**
   * Gets or Sets desiredScopes
   */
  @JsonAdapter(DesiredScopesEnum.Adapter.class)
  public enum DesiredScopesEnum {
    OFFER_READ("OFFER_READ"),
    
    OFFER_WRITE("OFFER_WRITE"),
    
    DISPUTE_READ("DISPUTE_READ"),
    
    DISPUTE_WRITE("DISPUTE_WRITE"),
    
    ORGANIZATION_READ("ORGANIZATION_READ"),
    
    PERSONA_READ("PERSONA_READ"),
    
    PERSONA_WRITE("PERSONA_WRITE"),
    
    PERSONA_AUTH("PERSONA_AUTH");

    private String value;

    DesiredScopesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DesiredScopesEnum fromValue(String value) {
      for (DesiredScopesEnum b : DesiredScopesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DesiredScopesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DesiredScopesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DesiredScopesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DesiredScopesEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DesiredScopesEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DESIRED_SCOPES = "desiredScopes";
  @SerializedName(SERIALIZED_NAME_DESIRED_SCOPES)
  private List<DesiredScopesEnum> desiredScopes;

  public ApiClientWrite() {
  }

  public ApiClientWrite referenceName(String referenceName) {
    this.referenceName = referenceName;
    return this;
  }

   /**
   * Get referenceName
   * @return referenceName
  **/
  @javax.annotation.Nullable
  public String getReferenceName() {
    return referenceName;
  }

  public void setReferenceName(String referenceName) {
    this.referenceName = referenceName;
  }


  public ApiClientWrite desiredScopes(List<DesiredScopesEnum> desiredScopes) {
    this.desiredScopes = desiredScopes;
    return this;
  }

  public ApiClientWrite addDesiredScopesItem(DesiredScopesEnum desiredScopesItem) {
    if (this.desiredScopes == null) {
      this.desiredScopes = new ArrayList<>();
    }
    this.desiredScopes.add(desiredScopesItem);
    return this;
  }

   /**
   * Get desiredScopes
   * @return desiredScopes
  **/
  @javax.annotation.Nullable
  public List<DesiredScopesEnum> getDesiredScopes() {
    return desiredScopes;
  }

  public void setDesiredScopes(List<DesiredScopesEnum> desiredScopes) {
    this.desiredScopes = desiredScopes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiClientWrite apiClientWrite = (ApiClientWrite) o;
    return Objects.equals(this.referenceName, apiClientWrite.referenceName) &&
        Objects.equals(this.desiredScopes, apiClientWrite.desiredScopes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(referenceName, desiredScopes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiClientWrite {\n");
    sb.append("    referenceName: ").append(toIndentedString(referenceName)).append("\n");
    sb.append("    desiredScopes: ").append(toIndentedString(desiredScopes)).append("\n");
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
    openapiFields.add("referenceName");
    openapiFields.add("desiredScopes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("referenceName");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to ApiClientWrite
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiClientWrite.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiClientWrite is not found in the empty JSON string", ApiClientWrite.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiClientWrite.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiClientWrite` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ApiClientWrite.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("referenceName") != null && !jsonObj.get("referenceName").isJsonNull()) && !jsonObj.get("referenceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referenceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referenceName").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("desiredScopes") != null && !jsonObj.get("desiredScopes").isJsonNull() && !jsonObj.get("desiredScopes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `desiredScopes` to be an array in the JSON string but got `%s`", jsonObj.get("desiredScopes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiClientWrite.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiClientWrite' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiClientWrite> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiClientWrite.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiClientWrite>() {
           @Override
           public void write(JsonWriter out, ApiClientWrite value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiClientWrite read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of ApiClientWrite given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of ApiClientWrite
  * @throws IOException if the JSON string is invalid with respect to ApiClientWrite
  */
  public static ApiClientWrite fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiClientWrite.class);
  }

 /**
  * Convert an instance of ApiClientWrite to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

