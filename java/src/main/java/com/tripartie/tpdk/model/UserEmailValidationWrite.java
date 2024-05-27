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
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-27T05:16:17.029359Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class UserEmailValidationWrite {
  public static final String SERIALIZED_NAME_CAPTCHA = "captcha";
  @SerializedName(SERIALIZED_NAME_CAPTCHA)
  private String captcha;

  public static final String SERIALIZED_NAME_PLAIN_PASSWORD = "plainPassword";
  @SerializedName(SERIALIZED_NAME_PLAIN_PASSWORD)
  private String plainPassword;

  public static final String SERIALIZED_NAME_EMAIL_VERIFICATION_INPUT = "emailVerificationInput";
  @SerializedName(SERIALIZED_NAME_EMAIL_VERIFICATION_INPUT)
  private String emailVerificationInput;

  public UserEmailValidationWrite() {
  }

  public UserEmailValidationWrite captcha(String captcha) {
    this.captcha = captcha;
    return this;
  }

   /**
   * Get captcha
   * @return captcha
  **/
  @javax.annotation.Nullable
  public String getCaptcha() {
    return captcha;
  }

  public void setCaptcha(String captcha) {
    this.captcha = captcha;
  }


  public UserEmailValidationWrite plainPassword(String plainPassword) {
    this.plainPassword = plainPassword;
    return this;
  }

   /**
   * Get plainPassword
   * @return plainPassword
  **/
  @javax.annotation.Nullable
  public String getPlainPassword() {
    return plainPassword;
  }

  public void setPlainPassword(String plainPassword) {
    this.plainPassword = plainPassword;
  }


  public UserEmailValidationWrite emailVerificationInput(String emailVerificationInput) {
    this.emailVerificationInput = emailVerificationInput;
    return this;
  }

   /**
   * Get emailVerificationInput
   * @return emailVerificationInput
  **/
  @javax.annotation.Nullable
  public String getEmailVerificationInput() {
    return emailVerificationInput;
  }

  public void setEmailVerificationInput(String emailVerificationInput) {
    this.emailVerificationInput = emailVerificationInput;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserEmailValidationWrite userEmailValidationWrite = (UserEmailValidationWrite) o;
    return Objects.equals(this.captcha, userEmailValidationWrite.captcha) &&
        Objects.equals(this.plainPassword, userEmailValidationWrite.plainPassword) &&
        Objects.equals(this.emailVerificationInput, userEmailValidationWrite.emailVerificationInput);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(captcha, plainPassword, emailVerificationInput);
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
    sb.append("class UserEmailValidationWrite {\n");
    sb.append("    captcha: ").append(toIndentedString(captcha)).append("\n");
    sb.append("    plainPassword: ").append(toIndentedString(plainPassword)).append("\n");
    sb.append("    emailVerificationInput: ").append(toIndentedString(emailVerificationInput)).append("\n");
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
    openapiFields.add("captcha");
    openapiFields.add("plainPassword");
    openapiFields.add("emailVerificationInput");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("captcha");
    openapiRequiredFields.add("emailVerificationInput");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to UserEmailValidationWrite
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserEmailValidationWrite.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserEmailValidationWrite is not found in the empty JSON string", UserEmailValidationWrite.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserEmailValidationWrite.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserEmailValidationWrite` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UserEmailValidationWrite.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("captcha") != null && !jsonObj.get("captcha").isJsonNull()) && !jsonObj.get("captcha").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `captcha` to be a primitive type in the JSON string but got `%s`", jsonObj.get("captcha").toString()));
      }
      if ((jsonObj.get("plainPassword") != null && !jsonObj.get("plainPassword").isJsonNull()) && !jsonObj.get("plainPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `plainPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("plainPassword").toString()));
      }
      if ((jsonObj.get("emailVerificationInput") != null && !jsonObj.get("emailVerificationInput").isJsonNull()) && !jsonObj.get("emailVerificationInput").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emailVerificationInput` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emailVerificationInput").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserEmailValidationWrite.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserEmailValidationWrite' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserEmailValidationWrite> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserEmailValidationWrite.class));

       return (TypeAdapter<T>) new TypeAdapter<UserEmailValidationWrite>() {
           @Override
           public void write(JsonWriter out, UserEmailValidationWrite value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserEmailValidationWrite read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of UserEmailValidationWrite given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of UserEmailValidationWrite
  * @throws IOException if the JSON string is invalid with respect to UserEmailValidationWrite
  */
  public static UserEmailValidationWrite fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserEmailValidationWrite.class);
  }

 /**
  * Convert an instance of UserEmailValidationWrite to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

