/*
 * Tripartie
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.179
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
import com.tripartie.tpdk.model.AddressWrite;
import java.io.IOException;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;



import java.io.IOException;
import java.lang.reflect.Type;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.JsonPrimitive;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonParseException;

import com.tripartie.tpdk.JSON;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-03-04T08:16:59.915280Z[Etc/UTC]")
public class PersonaWriteAddress extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(PersonaWriteAddress.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!PersonaWriteAddress.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'PersonaWriteAddress' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<AddressWrite> adapterAddressWrite = gson.getDelegateAdapter(this, TypeToken.get(AddressWrite.class));
            final TypeAdapter<Object> adapterObject = gson.getDelegateAdapter(this, TypeToken.get(Object.class));

            return (TypeAdapter<T>) new TypeAdapter<PersonaWriteAddress>() {
                @Override
                public void write(JsonWriter out, PersonaWriteAddress value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `AddressWrite`
                    if (value.getActualInstance() instanceof AddressWrite) {
                      JsonElement element = adapterAddressWrite.toJsonTree((AddressWrite)value.getActualInstance());
                      elementAdapter.write(out, element);
                      return;
                    }
                    // check if the actual instance is of the type `Object`
                    if (value.getActualInstance() instanceof Object) {
                      JsonPrimitive primitive = adapterObject.toJsonTree((Object)value.getActualInstance()).getAsJsonPrimitive();
                      elementAdapter.write(out, primitive);
                      return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemae: AddressWrite, Object");
                }

                @Override
                public PersonaWriteAddress read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize AddressWrite
                    try {
                      // validate the JSON object to see if any exception is thrown
                      AddressWrite.validateJsonElement(jsonElement);
                      actualAdapter = adapterAddressWrite;
                      PersonaWriteAddress ret = new PersonaWriteAddress();
                      ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                      return ret;
                    } catch (Exception e) {
                      // deserialization failed, continue
                      errorMessages.add(String.format("Deserialization for AddressWrite failed with `%s`.", e.getMessage()));
                      log.log(Level.FINER, "Input data does not match schema 'AddressWrite'", e);
                    }
                    // deserialize Object
                    try {
                      // validate the JSON object to see if any exception is thrown
                      if(!jsonElement.getAsJsonPrimitive().isNumber()) {
                        throw new IllegalArgumentException(String.format("Expected json element to be of type Number in the JSON string but got `%s`", jsonElement.toString()));
                      }
                      actualAdapter = adapterObject;
                      PersonaWriteAddress ret = new PersonaWriteAddress();
                      ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                      return ret;
                    } catch (Exception e) {
                      // deserialization failed, continue
                      errorMessages.add(String.format("Deserialization for Object failed with `%s`.", e.getMessage()));
                      log.log(Level.FINER, "Input data does not match schema 'Object'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for PersonaWriteAddress: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public PersonaWriteAddress() {
        super("anyOf", Boolean.FALSE);
    }

    public PersonaWriteAddress(AddressWrite o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    public PersonaWriteAddress(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("AddressWrite", AddressWrite.class);
        schemas.put("Object", Object.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return PersonaWriteAddress.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * AddressWrite, Object
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof AddressWrite) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof Object) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be AddressWrite, Object");
    }

    /**
     * Get the actual instance, which can be the following:
     * AddressWrite, Object
     *
     * @return The actual instance (AddressWrite, Object)
     */
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `AddressWrite`. If the actual instance is not `AddressWrite`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `AddressWrite`
     * @throws ClassCastException if the instance is not `AddressWrite`
     */
    public AddressWrite getAddressWrite() throws ClassCastException {
        return (AddressWrite)super.getActualInstance();
    }
    /**
     * Get the actual instance of `Object`. If the actual instance is not `Object`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `Object`
     * @throws ClassCastException if the instance is not `Object`
     */
    public Object getObject() throws ClassCastException {
        return (Object)super.getActualInstance();
    }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to PersonaWriteAddress
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    // validate anyOf schemas one by one
    ArrayList<String> errorMessages = new ArrayList<>();
    // validate the json string with AddressWrite
    try {
      AddressWrite.validateJsonElement(jsonElement);
      return;
    } catch (Exception e) {
      errorMessages.add(String.format("Deserialization for AddressWrite failed with `%s`.", e.getMessage()));
      // continue to the next one
    }
    // validate the json string with Object
    try {
      if(!jsonElement.getAsJsonPrimitive().isNumber()) {
        throw new IllegalArgumentException(String.format("Expected json element to be of type Number in the JSON string but got `%s`", jsonElement.toString()));
      }
      return;
    } catch (Exception e) {
      errorMessages.add(String.format("Deserialization for Object failed with `%s`.", e.getMessage()));
      // continue to the next one
    }
    throw new IOException(String.format("The JSON string is invalid for PersonaWriteAddress with anyOf schemas: AddressWrite, Object. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    
  }

 /**
  * Create an instance of PersonaWriteAddress given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of PersonaWriteAddress
  * @throws IOException if the JSON string is invalid with respect to PersonaWriteAddress
  */
  public static PersonaWriteAddress fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PersonaWriteAddress.class);
  }

 /**
  * Convert an instance of PersonaWriteAddress to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

