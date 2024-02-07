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
import com.tripartie.tpdk.model.Metadata;
import com.tripartie.tpdk.model.View;
import java.io.IOException;
import java.math.BigDecimal;
import java.net.URI;
import java.time.OffsetDateTime;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-02-07T15:33:34.209225Z[Etc/UTC]")
public class Offer {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_ULID = "ulid";
  @SerializedName(SERIALIZED_NAME_ULID)
  private String ulid;

  public static final String SERIALIZED_NAME_PUBLIC_URL = "publicUrl";
  @SerializedName(SERIALIZED_NAME_PUBLIC_URL)
  private String publicUrl;

  public static final String SERIALIZED_NAME_ENFORCE_PERSONA_AUTH = "enforcePersonaAuth";
  @SerializedName(SERIALIZED_NAME_ENFORCE_PERSONA_AUTH)
  private Boolean enforcePersonaAuth = true;

  public static final String SERIALIZED_NAME_OVERRIDE_RATE_COMMISSION_SAFE_CHECKOUT = "overrideRateCommissionSafeCheckout";
  @SerializedName(SERIALIZED_NAME_OVERRIDE_RATE_COMMISSION_SAFE_CHECKOUT)
  private BigDecimal overrideRateCommissionSafeCheckout;

  public static final String SERIALIZED_NAME_REDIRECT_URL = "redirectUrl";
  @SerializedName(SERIALIZED_NAME_REDIRECT_URL)
  private String redirectUrl;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private URI url;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private String organization;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private String seller;

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

  public static final String SERIALIZED_NAME_SHIPPING_ALLOWED = "shippingAllowed";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ALLOWED)
  private Boolean shippingAllowed;

  public static final String SERIALIZED_NAME_HAND_DELIVERY_ALLOWED = "handDeliveryAllowed";
  @SerializedName(SERIALIZED_NAME_HAND_DELIVERY_ALLOWED)
  private Boolean handDeliveryAllowed = true;

  /**
   * Gets or Sets shippingCarriers
   */
  @JsonAdapter(ShippingCarriersEnum.Adapter.class)
  public enum ShippingCarriersEnum {
    SWISSPOST("SwissPost"),
    
    COLISSIMO("Colissimo"),
    
    MONDIALRELAY("MondialRelay");

    private String value;

    ShippingCarriersEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ShippingCarriersEnum fromValue(String value) {
      for (ShippingCarriersEnum b : ShippingCarriersEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ShippingCarriersEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ShippingCarriersEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ShippingCarriersEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ShippingCarriersEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ShippingCarriersEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SHIPPING_CARRIERS = "shippingCarriers";
  @SerializedName(SERIALIZED_NAME_SHIPPING_CARRIERS)
  private List<ShippingCarriersEnum> shippingCarriers;

  public static final String SERIALIZED_NAME_EAN_CODE = "eanCode";
  @SerializedName(SERIALIZED_NAME_EAN_CODE)
  private String eanCode;

  public static final String SERIALIZED_NAME_CAN_BE_SOLD_SEPARATELY = "canBeSoldSeparately";
  @SerializedName(SERIALIZED_NAME_CAN_BE_SOLD_SEPARATELY)
  private Boolean canBeSoldSeparately = true;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private List<Metadata> metadata;

  public static final String SERIALIZED_NAME_MEDIAS = "medias";
  @SerializedName(SERIALIZED_NAME_MEDIAS)
  private List<String> medias = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIEWS = "views";
  @SerializedName(SERIALIZED_NAME_VIEWS)
  private List<View> views = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_IRI = "iri";
  @SerializedName(SERIALIZED_NAME_IRI)
  private String iri;

  public static final String SERIALIZED_NAME_HALF_PRICE_POINT = "halfPricePoint";
  @SerializedName(SERIALIZED_NAME_HALF_PRICE_POINT)
  private BigDecimal halfPricePoint;

  public Offer() {
  }

  public Offer(
     Integer id, 
     URI url, 
     OffsetDateTime createdAt, 
     OffsetDateTime updatedAt, 
     String iri, 
     BigDecimal halfPricePoint
  ) {
    this();
    this.id = id;
    this.url = url;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
    this.iri = iri;
    this.halfPricePoint = halfPricePoint;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public Offer ulid(String ulid) {
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


  public Offer publicUrl(String publicUrl) {
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


  public Offer enforcePersonaAuth(Boolean enforcePersonaAuth) {
    this.enforcePersonaAuth = enforcePersonaAuth;
    return this;
  }

   /**
   * Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration.
   * @return enforcePersonaAuth
  **/
  @javax.annotation.Nonnull
  public Boolean getEnforcePersonaAuth() {
    return enforcePersonaAuth;
  }

  public void setEnforcePersonaAuth(Boolean enforcePersonaAuth) {
    this.enforcePersonaAuth = enforcePersonaAuth;
  }


  public Offer overrideRateCommissionSafeCheckout(BigDecimal overrideRateCommissionSafeCheckout) {
    this.overrideRateCommissionSafeCheckout = overrideRateCommissionSafeCheckout;
    return this;
  }

   /**
   * Override YOUR platform fees for that particular Offer.
   * @return overrideRateCommissionSafeCheckout
  **/
  @javax.annotation.Nullable
  public BigDecimal getOverrideRateCommissionSafeCheckout() {
    return overrideRateCommissionSafeCheckout;
  }

  public void setOverrideRateCommissionSafeCheckout(BigDecimal overrideRateCommissionSafeCheckout) {
    this.overrideRateCommissionSafeCheckout = overrideRateCommissionSafeCheckout;
  }


  public Offer redirectUrl(String redirectUrl) {
    this.redirectUrl = redirectUrl;
    return this;
  }

   /**
   * Fill-in that field IF you intend to redirect your customer instead of using a WebView.
   * @return redirectUrl
  **/
  @javax.annotation.Nullable
  public String getRedirectUrl() {
    return redirectUrl;
  }

  public void setRedirectUrl(String redirectUrl) {
    this.redirectUrl = redirectUrl;
  }


   /**
   * Get url
   * @return url
  **/
  @javax.annotation.Nullable
  public URI getUrl() {
    return url;
  }



  public Offer organization(String organization) {
    this.organization = organization;
    return this;
  }

   /**
   * Get organization
   * @return organization
  **/
  @javax.annotation.Nullable
  public String getOrganization() {
    return organization;
  }

  public void setOrganization(String organization) {
    this.organization = organization;
  }


  public Offer seller(String seller) {
    this.seller = seller;
    return this;
  }

   /**
   * If the seller is actually YOUR organization, set it to NULL.
   * @return seller
  **/
  @javax.annotation.Nonnull
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }


  public Offer nature(NatureEnum nature) {
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


  public Offer title(String title) {
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


  public Offer description(String description) {
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


  public Offer unitPrice(BigDecimal unitPrice) {
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


  public Offer currencyCode(String currencyCode) {
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


  public Offer itemCount(Integer itemCount) {
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


  public Offer condition(ConditionEnum condition) {
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


  public Offer weightInGram(Integer weightInGram) {
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


  public Offer shippingAllowed(Boolean shippingAllowed) {
    this.shippingAllowed = shippingAllowed;
    return this;
  }

   /**
   * That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined.
   * @return shippingAllowed
  **/
  @javax.annotation.Nonnull
  public Boolean getShippingAllowed() {
    return shippingAllowed;
  }

  public void setShippingAllowed(Boolean shippingAllowed) {
    this.shippingAllowed = shippingAllowed;
  }


  public Offer handDeliveryAllowed(Boolean handDeliveryAllowed) {
    this.handDeliveryAllowed = handDeliveryAllowed;
    return this;
  }

   /**
   * Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product.
   * @return handDeliveryAllowed
  **/
  @javax.annotation.Nonnull
  public Boolean getHandDeliveryAllowed() {
    return handDeliveryAllowed;
  }

  public void setHandDeliveryAllowed(Boolean handDeliveryAllowed) {
    this.handDeliveryAllowed = handDeliveryAllowed;
  }


  public Offer shippingCarriers(List<ShippingCarriersEnum> shippingCarriers) {
    this.shippingCarriers = shippingCarriers;
    return this;
  }

  public Offer addShippingCarriersItem(ShippingCarriersEnum shippingCarriersItem) {
    if (this.shippingCarriers == null) {
      this.shippingCarriers = new ArrayList<>();
    }
    this.shippingCarriers.add(shippingCarriersItem);
    return this;
  }

   /**
   * If you wish to enable automated shipping label generation through a specific provider, specify it there.
   * @return shippingCarriers
  **/
  @javax.annotation.Nullable
  public List<ShippingCarriersEnum> getShippingCarriers() {
    return shippingCarriers;
  }

  public void setShippingCarriers(List<ShippingCarriersEnum> shippingCarriers) {
    this.shippingCarriers = shippingCarriers;
  }


  public Offer eanCode(String eanCode) {
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


  public Offer canBeSoldSeparately(Boolean canBeSoldSeparately) {
    this.canBeSoldSeparately = canBeSoldSeparately;
    return this;
  }

   /**
   * Set this flag to false to forbid a potential buyer to acquire this item separately.          This is only useful in a BulkOffer context.
   * @return canBeSoldSeparately
  **/
  @javax.annotation.Nonnull
  public Boolean getCanBeSoldSeparately() {
    return canBeSoldSeparately;
  }

  public void setCanBeSoldSeparately(Boolean canBeSoldSeparately) {
    this.canBeSoldSeparately = canBeSoldSeparately;
  }


  public Offer metadata(List<Metadata> metadata) {
    this.metadata = metadata;
    return this;
  }

  public Offer addMetadataItem(Metadata metadataItem) {
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
  public List<Metadata> getMetadata() {
    return metadata;
  }

  public void setMetadata(List<Metadata> metadata) {
    this.metadata = metadata;
  }


  public Offer medias(List<String> medias) {
    this.medias = medias;
    return this;
  }

  public Offer addMediasItem(String mediasItem) {
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
  public List<String> getMedias() {
    return medias;
  }

  public void setMedias(List<String> medias) {
    this.medias = medias;
  }


  public Offer views(List<View> views) {
    this.views = views;
    return this;
  }

  public Offer addViewsItem(View viewsItem) {
    if (this.views == null) {
      this.views = new ArrayList<>();
    }
    this.views.add(viewsItem);
    return this;
  }

   /**
   * Get views
   * @return views
  **/
  @javax.annotation.Nonnull
  public List<View> getViews() {
    return views;
  }

  public void setViews(List<View> views) {
    this.views = views;
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
   * Get iri
   * @return iri
  **/
  @javax.annotation.Nullable
  public String getIri() {
    return iri;
  }



   /**
   * Get halfPricePoint
   * @return halfPricePoint
  **/
  @javax.annotation.Nullable
  public BigDecimal getHalfPricePoint() {
    return halfPricePoint;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Offer offer = (Offer) o;
    return Objects.equals(this.id, offer.id) &&
        Objects.equals(this.ulid, offer.ulid) &&
        Objects.equals(this.publicUrl, offer.publicUrl) &&
        Objects.equals(this.enforcePersonaAuth, offer.enforcePersonaAuth) &&
        Objects.equals(this.overrideRateCommissionSafeCheckout, offer.overrideRateCommissionSafeCheckout) &&
        Objects.equals(this.redirectUrl, offer.redirectUrl) &&
        Objects.equals(this.url, offer.url) &&
        Objects.equals(this.organization, offer.organization) &&
        Objects.equals(this.seller, offer.seller) &&
        Objects.equals(this.nature, offer.nature) &&
        Objects.equals(this.title, offer.title) &&
        Objects.equals(this.description, offer.description) &&
        Objects.equals(this.unitPrice, offer.unitPrice) &&
        Objects.equals(this.currencyCode, offer.currencyCode) &&
        Objects.equals(this.itemCount, offer.itemCount) &&
        Objects.equals(this.condition, offer.condition) &&
        Objects.equals(this.weightInGram, offer.weightInGram) &&
        Objects.equals(this.shippingAllowed, offer.shippingAllowed) &&
        Objects.equals(this.handDeliveryAllowed, offer.handDeliveryAllowed) &&
        Objects.equals(this.shippingCarriers, offer.shippingCarriers) &&
        Objects.equals(this.eanCode, offer.eanCode) &&
        Objects.equals(this.canBeSoldSeparately, offer.canBeSoldSeparately) &&
        Objects.equals(this.metadata, offer.metadata) &&
        Objects.equals(this.medias, offer.medias) &&
        Objects.equals(this.views, offer.views) &&
        Objects.equals(this.createdAt, offer.createdAt) &&
        Objects.equals(this.updatedAt, offer.updatedAt) &&
        Objects.equals(this.iri, offer.iri) &&
        Objects.equals(this.halfPricePoint, offer.halfPricePoint);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, ulid, publicUrl, enforcePersonaAuth, overrideRateCommissionSafeCheckout, redirectUrl, url, organization, seller, nature, title, description, unitPrice, currencyCode, itemCount, condition, weightInGram, shippingAllowed, handDeliveryAllowed, shippingCarriers, eanCode, canBeSoldSeparately, metadata, medias, views, createdAt, updatedAt, iri, halfPricePoint);
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
    sb.append("class Offer {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    ulid: ").append(toIndentedString(ulid)).append("\n");
    sb.append("    publicUrl: ").append(toIndentedString(publicUrl)).append("\n");
    sb.append("    enforcePersonaAuth: ").append(toIndentedString(enforcePersonaAuth)).append("\n");
    sb.append("    overrideRateCommissionSafeCheckout: ").append(toIndentedString(overrideRateCommissionSafeCheckout)).append("\n");
    sb.append("    redirectUrl: ").append(toIndentedString(redirectUrl)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    nature: ").append(toIndentedString(nature)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    itemCount: ").append(toIndentedString(itemCount)).append("\n");
    sb.append("    condition: ").append(toIndentedString(condition)).append("\n");
    sb.append("    weightInGram: ").append(toIndentedString(weightInGram)).append("\n");
    sb.append("    shippingAllowed: ").append(toIndentedString(shippingAllowed)).append("\n");
    sb.append("    handDeliveryAllowed: ").append(toIndentedString(handDeliveryAllowed)).append("\n");
    sb.append("    shippingCarriers: ").append(toIndentedString(shippingCarriers)).append("\n");
    sb.append("    eanCode: ").append(toIndentedString(eanCode)).append("\n");
    sb.append("    canBeSoldSeparately: ").append(toIndentedString(canBeSoldSeparately)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    medias: ").append(toIndentedString(medias)).append("\n");
    sb.append("    views: ").append(toIndentedString(views)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    iri: ").append(toIndentedString(iri)).append("\n");
    sb.append("    halfPricePoint: ").append(toIndentedString(halfPricePoint)).append("\n");
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
    openapiFields.add("ulid");
    openapiFields.add("publicUrl");
    openapiFields.add("enforcePersonaAuth");
    openapiFields.add("overrideRateCommissionSafeCheckout");
    openapiFields.add("redirectUrl");
    openapiFields.add("url");
    openapiFields.add("organization");
    openapiFields.add("seller");
    openapiFields.add("nature");
    openapiFields.add("title");
    openapiFields.add("description");
    openapiFields.add("unitPrice");
    openapiFields.add("currencyCode");
    openapiFields.add("itemCount");
    openapiFields.add("condition");
    openapiFields.add("weightInGram");
    openapiFields.add("shippingAllowed");
    openapiFields.add("handDeliveryAllowed");
    openapiFields.add("shippingCarriers");
    openapiFields.add("eanCode");
    openapiFields.add("canBeSoldSeparately");
    openapiFields.add("metadata");
    openapiFields.add("medias");
    openapiFields.add("views");
    openapiFields.add("createdAt");
    openapiFields.add("updatedAt");
    openapiFields.add("iri");
    openapiFields.add("halfPricePoint");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ulid");
    openapiRequiredFields.add("enforcePersonaAuth");
    openapiRequiredFields.add("url");
    openapiRequiredFields.add("seller");
    openapiRequiredFields.add("nature");
    openapiRequiredFields.add("shippingAllowed");
    openapiRequiredFields.add("handDeliveryAllowed");
    openapiRequiredFields.add("canBeSoldSeparately");
    openapiRequiredFields.add("medias");
    openapiRequiredFields.add("views");
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to Offer
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Offer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Offer is not found in the empty JSON string", Offer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Offer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Offer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Offer.openapiRequiredFields) {
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
      if ((jsonObj.get("redirectUrl") != null && !jsonObj.get("redirectUrl").isJsonNull()) && !jsonObj.get("redirectUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `redirectUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("redirectUrl").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if ((jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonNull()) && !jsonObj.get("organization").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `organization` to be a primitive type in the JSON string but got `%s`", jsonObj.get("organization").toString()));
      }
      if (!jsonObj.get("seller").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seller` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seller").toString()));
      }
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
      // ensure the optional json data is an array if present
      if (jsonObj.get("shippingCarriers") != null && !jsonObj.get("shippingCarriers").isJsonNull() && !jsonObj.get("shippingCarriers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `shippingCarriers` to be an array in the JSON string but got `%s`", jsonObj.get("shippingCarriers").toString()));
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
            Metadata.validateJsonElement(jsonArraymetadata.get(i));
          };
        }
      }
      // ensure the required json array is present
      if (jsonObj.get("medias") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("medias").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `medias` to be an array in the JSON string but got `%s`", jsonObj.get("medias").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("views").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `views` to be an array in the JSON string but got `%s`", jsonObj.get("views").toString()));
      }

      JsonArray jsonArrayviews = jsonObj.getAsJsonArray("views");
      // validate the required field `views` (array)
      for (int i = 0; i < jsonArrayviews.size(); i++) {
        View.validateJsonElement(jsonArrayviews.get(i));
      };
      if ((jsonObj.get("iri") != null && !jsonObj.get("iri").isJsonNull()) && !jsonObj.get("iri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Offer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Offer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Offer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Offer.class));

       return (TypeAdapter<T>) new TypeAdapter<Offer>() {
           @Override
           public void write(JsonWriter out, Offer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Offer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of Offer given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of Offer
  * @throws IOException if the JSON string is invalid with respect to Offer
  */
  public static Offer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Offer.class);
  }

 /**
  * Convert an instance of Offer to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

