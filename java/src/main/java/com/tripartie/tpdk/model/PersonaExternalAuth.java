/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.202
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-26T18:54:19.017757Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class PersonaExternalAuth {
  public static final String SERIALIZED_NAME_CAPTCHA = "captcha";
  @SerializedName(SERIALIZED_NAME_CAPTCHA)
  private String captcha;

  public static final String SERIALIZED_NAME_TARGET_URL = "targetUrl";
  @SerializedName(SERIALIZED_NAME_TARGET_URL)
  private String targetUrl;

  public static final String SERIALIZED_NAME_PLAIN_PASSWORD = "plainPassword";
  @SerializedName(SERIALIZED_NAME_PLAIN_PASSWORD)
  private String plainPassword;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_MOBILE_PHONE_NUMBER = "mobilePhoneNumber";
  @SerializedName(SERIALIZED_NAME_MOBILE_PHONE_NUMBER)
  private String mobilePhoneNumber;

  public PersonaExternalAuth() {
  }

  public PersonaExternalAuth captcha(String captcha) {
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


  public PersonaExternalAuth targetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
    return this;
  }

   /**
   * The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona.
   * @return targetUrl
  **/
  @javax.annotation.Nullable
  public String getTargetUrl() {
    return targetUrl;
  }

  public void setTargetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
  }


  public PersonaExternalAuth plainPassword(String plainPassword) {
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


  public PersonaExternalAuth email(String email) {
    this.email = email;
    return this;
  }

   /**
   * Get email
   * @return email
  **/
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public PersonaExternalAuth mobilePhoneNumber(String mobilePhoneNumber) {
    this.mobilePhoneNumber = mobilePhoneNumber;
    return this;
  }

   /**
   * Get mobilePhoneNumber
   * @return mobilePhoneNumber
  **/
  @javax.annotation.Nullable
  public String getMobilePhoneNumber() {
    return mobilePhoneNumber;
  }

  public void setMobilePhoneNumber(String mobilePhoneNumber) {
    this.mobilePhoneNumber = mobilePhoneNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PersonaExternalAuth personaExternalAuth = (PersonaExternalAuth) o;
    return Objects.equals(this.captcha, personaExternalAuth.captcha) &&
        Objects.equals(this.targetUrl, personaExternalAuth.targetUrl) &&
        Objects.equals(this.plainPassword, personaExternalAuth.plainPassword) &&
        Objects.equals(this.email, personaExternalAuth.email) &&
        Objects.equals(this.mobilePhoneNumber, personaExternalAuth.mobilePhoneNumber);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(captcha, targetUrl, plainPassword, email, mobilePhoneNumber);
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
    sb.append("class PersonaExternalAuth {\n");
    sb.append("    captcha: ").append(toIndentedString(captcha)).append("\n");
    sb.append("    targetUrl: ").append(toIndentedString(targetUrl)).append("\n");
    sb.append("    plainPassword: ").append(toIndentedString(plainPassword)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    mobilePhoneNumber: ").append(toIndentedString(mobilePhoneNumber)).append("\n");
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
    openapiFields.add("targetUrl");
    openapiFields.add("plainPassword");
    openapiFields.add("email");
    openapiFields.add("mobilePhoneNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to PersonaExternalAuth
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PersonaExternalAuth.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PersonaExternalAuth is not found in the empty JSON string", PersonaExternalAuth.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PersonaExternalAuth.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PersonaExternalAuth` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("captcha") != null && !jsonObj.get("captcha").isJsonNull()) && !jsonObj.get("captcha").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `captcha` to be a primitive type in the JSON string but got `%s`", jsonObj.get("captcha").toString()));
      }
      if ((jsonObj.get("targetUrl") != null && !jsonObj.get("targetUrl").isJsonNull()) && !jsonObj.get("targetUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetUrl").toString()));
      }
      if ((jsonObj.get("plainPassword") != null && !jsonObj.get("plainPassword").isJsonNull()) && !jsonObj.get("plainPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `plainPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("plainPassword").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("mobilePhoneNumber") != null && !jsonObj.get("mobilePhoneNumber").isJsonNull()) && !jsonObj.get("mobilePhoneNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobilePhoneNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobilePhoneNumber").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PersonaExternalAuth.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PersonaExternalAuth' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PersonaExternalAuth> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PersonaExternalAuth.class));

       return (TypeAdapter<T>) new TypeAdapter<PersonaExternalAuth>() {
           @Override
           public void write(JsonWriter out, PersonaExternalAuth value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PersonaExternalAuth read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of PersonaExternalAuth given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of PersonaExternalAuth
  * @throws IOException if the JSON string is invalid with respect to PersonaExternalAuth
  */
  public static PersonaExternalAuth fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PersonaExternalAuth.class);
  }

 /**
  * Convert an instance of PersonaExternalAuth to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

