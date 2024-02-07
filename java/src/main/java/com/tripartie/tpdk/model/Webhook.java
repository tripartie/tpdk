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


package com.tripartie.tpdk.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.tripartie.tpdk.model.WebhookObject;
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
 * Webhook
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T14:46:42.159671Z[Etc/UTC]")
public class Webhook {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  /**
   * Gets or Sets event
   */
  @JsonAdapter(EventEnum.Adapter.class)
  public enum EventEnum {
    DISPUTE_OPENED("dispute.opened"),
    
    DISPUTE_SUBMITTED("dispute.submitted"),
    
    DISPUTE_CREATED("dispute.created"),
    
    DISPUTE_ABANDONED("dispute.abandoned"),
    
    DISPUTE_SETTLEMENT("dispute.settlement"),
    
    DISPUTE_CLOSED("dispute.closed"),
    
    DISPUTE_EXPIRED("dispute.expired"),
    
    DISPUTE_MANUAL_ARBITRATION_REQUIRED("dispute.manual_arbitration_required"),
    
    DISPUTE_UPDATED("dispute.updated"),
    
    DISPUTE_REMINDER("dispute.reminder"),
    
    OFFER_CREATED("offer.created"),
    
    OFFER_EXPIRED("offer.expired"),
    
    OFFER_UPDATED("offer.updated"),
    
    OFFER_CRAWL_FAILURE("offer.crawl_failure"),
    
    OFFER_TRANSACTION_AUTHORIZED("offer.transaction.authorized"),
    
    OFFER_TRANSACTION_RECONCILED("offer.transaction.reconciled"),
    
    OFFER_TRANSACTION_ABANDONED("offer.transaction.abandoned"),
    
    OFFER_CLOSED("offer.closed"),
    
    OFFER_TRANSACTION_REFUND("offer.transaction.refund"),
    
    PERSONA_ADDED("persona.added");

    private String value;

    EventEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EventEnum fromValue(String value) {
      for (EventEnum b : EventEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EventEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EventEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EventEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EventEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EventEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EVENT = "event";
  @SerializedName(SERIALIZED_NAME_EVENT)
  private EventEnum event;

  public static final String SERIALIZED_NAME_OBJECT_ID = "objectId";
  @SerializedName(SERIALIZED_NAME_OBJECT_ID)
  private String objectId;

  public static final String SERIALIZED_NAME_IRI = "iri";
  @SerializedName(SERIALIZED_NAME_IRI)
  private String iri;

  public static final String SERIALIZED_NAME_OCCURRED_AT = "occurredAt";
  @SerializedName(SERIALIZED_NAME_OCCURRED_AT)
  private OffsetDateTime occurredAt;

  public static final String SERIALIZED_NAME_OBJECT = "object";
  @SerializedName(SERIALIZED_NAME_OBJECT)
  private WebhookObject _object;

  public Webhook() {
  }

  public Webhook id(Integer id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Webhook event(EventEnum event) {
    this.event = event;
    return this;
  }

   /**
   * Get event
   * @return event
  **/
  @javax.annotation.Nullable
  public EventEnum getEvent() {
    return event;
  }

  public void setEvent(EventEnum event) {
    this.event = event;
  }


  public Webhook objectId(String objectId) {
    this.objectId = objectId;
    return this;
  }

   /**
   * Get objectId
   * @return objectId
  **/
  @javax.annotation.Nullable
  public String getObjectId() {
    return objectId;
  }

  public void setObjectId(String objectId) {
    this.objectId = objectId;
  }


  public Webhook iri(String iri) {
    this.iri = iri;
    return this;
  }

   /**
   * Get iri
   * @return iri
  **/
  @javax.annotation.Nullable
  public String getIri() {
    return iri;
  }

  public void setIri(String iri) {
    this.iri = iri;
  }


  public Webhook occurredAt(OffsetDateTime occurredAt) {
    this.occurredAt = occurredAt;
    return this;
  }

   /**
   * Get occurredAt
   * @return occurredAt
  **/
  @javax.annotation.Nullable
  public OffsetDateTime getOccurredAt() {
    return occurredAt;
  }

  public void setOccurredAt(OffsetDateTime occurredAt) {
    this.occurredAt = occurredAt;
  }


  public Webhook _object(WebhookObject _object) {
    this._object = _object;
    return this;
  }

   /**
   * Get _object
   * @return _object
  **/
  @javax.annotation.Nullable
  public WebhookObject getObject() {
    return _object;
  }

  public void setObject(WebhookObject _object) {
    this._object = _object;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Webhook webhook = (Webhook) o;
    return Objects.equals(this.id, webhook.id) &&
        Objects.equals(this.event, webhook.event) &&
        Objects.equals(this.objectId, webhook.objectId) &&
        Objects.equals(this.iri, webhook.iri) &&
        Objects.equals(this.occurredAt, webhook.occurredAt) &&
        Objects.equals(this._object, webhook._object);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, event, objectId, iri, occurredAt, _object);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Webhook {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    event: ").append(toIndentedString(event)).append("\n");
    sb.append("    objectId: ").append(toIndentedString(objectId)).append("\n");
    sb.append("    iri: ").append(toIndentedString(iri)).append("\n");
    sb.append("    occurredAt: ").append(toIndentedString(occurredAt)).append("\n");
    sb.append("    _object: ").append(toIndentedString(_object)).append("\n");
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
    openapiFields.add("event");
    openapiFields.add("objectId");
    openapiFields.add("iri");
    openapiFields.add("occurredAt");
    openapiFields.add("object");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to Webhook
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Webhook.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Webhook is not found in the empty JSON string", Webhook.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Webhook.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Webhook` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("event") != null && !jsonObj.get("event").isJsonNull()) && !jsonObj.get("event").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event").toString()));
      }
      // validate the optional field `event`
      if (jsonObj.get("event") != null && !jsonObj.get("event").isJsonNull()) {
        EventEnum.validateJsonElement(jsonObj.get("event"));
      }
      if ((jsonObj.get("objectId") != null && !jsonObj.get("objectId").isJsonNull()) && !jsonObj.get("objectId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `objectId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("objectId").toString()));
      }
      if ((jsonObj.get("iri") != null && !jsonObj.get("iri").isJsonNull()) && !jsonObj.get("iri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iri").toString()));
      }
      // validate the optional field `object`
      if (jsonObj.get("object") != null && !jsonObj.get("object").isJsonNull()) {
        WebhookObject.validateJsonElement(jsonObj.get("object"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Webhook.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Webhook' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Webhook> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Webhook.class));

       return (TypeAdapter<T>) new TypeAdapter<Webhook>() {
           @Override
           public void write(JsonWriter out, Webhook value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Webhook read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of Webhook given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of Webhook
  * @throws IOException if the JSON string is invalid with respect to Webhook
  */
  public static Webhook fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Webhook.class);
  }

 /**
  * Convert an instance of Webhook to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

