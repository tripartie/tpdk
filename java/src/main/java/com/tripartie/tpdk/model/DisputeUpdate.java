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
 * Access directly our resolution center without having used the safe-checkout feature.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-05-27T05:16:17.029359Z[Etc/UTC]", comments = "Generator version: 7.6.0")
public class DisputeUpdate {
  public static final String SERIALIZED_NAME_ITEM_COUNT = "itemCount";
  @SerializedName(SERIALIZED_NAME_ITEM_COUNT)
  private Integer itemCount;

  /**
   * Gets or Sets issueType
   */
  @JsonAdapter(IssueTypeEnum.Adapter.class)
  public enum IssueTypeEnum {
    NOT_AS_DESCRIBED("NOT_AS_DESCRIBED"),
    
    DOES_NOT_WORK("DOES_NOT_WORK"),
    
    IS_INCOMPLETE("IS_INCOMPLETE"),
    
    DELIVERY_ISSUE("DELIVERY_ISSUE"),
    
    ALLEGED_FRAUD("ALLEGED_FRAUD"),
    
    NULL("null");

    private String value;

    IssueTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IssueTypeEnum fromValue(String value) {
      for (IssueTypeEnum b : IssueTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<IssueTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IssueTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IssueTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IssueTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IssueTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ISSUE_TYPE = "issueType";
  @SerializedName(SERIALIZED_NAME_ISSUE_TYPE)
  private IssueTypeEnum issueType;

  /**
   * To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED.
   */
  @JsonAdapter(IssueInDescriptionTypeEnum.Adapter.class)
  public enum IssueInDescriptionTypeEnum {
    WRONG_COLOUR("WRONG_COLOUR"),
    
    DAMAGED_OR_USED("DAMAGED_OR_USED"),
    
    INCORRECT_FORMAT_OR_SIZE("INCORRECT_FORMAT_OR_SIZE"),
    
    DIFFERENT_MATERIAL("DIFFERENT_MATERIAL"),
    
    NULL("null");

    private String value;

    IssueInDescriptionTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IssueInDescriptionTypeEnum fromValue(String value) {
      for (IssueInDescriptionTypeEnum b : IssueInDescriptionTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<IssueInDescriptionTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IssueInDescriptionTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IssueInDescriptionTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IssueInDescriptionTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IssueInDescriptionTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ISSUE_IN_DESCRIPTION_TYPE = "issueInDescriptionType";
  @SerializedName(SERIALIZED_NAME_ISSUE_IN_DESCRIPTION_TYPE)
  private IssueInDescriptionTypeEnum issueInDescriptionType;

  public static final String SERIALIZED_NAME_ISSUE_MENTIONED_IN_OFFER = "issueMentionedInOffer";
  @SerializedName(SERIALIZED_NAME_ISSUE_MENTIONED_IN_OFFER)
  private Boolean issueMentionedInOffer;

  public static final String SERIALIZED_NAME_ISSUE_DETAILS = "issueDetails";
  @SerializedName(SERIALIZED_NAME_ISSUE_DETAILS)
  private String issueDetails;

  /**
   * Gets or Sets complainantStake
   */
  @JsonAdapter(ComplainantStakeEnum.Adapter.class)
  public enum ComplainantStakeEnum {
    LOW("LOW"),
    
    MEDIUM("MEDIUM"),
    
    HIGH("HIGH"),
    
    NULL("null");

    private String value;

    ComplainantStakeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ComplainantStakeEnum fromValue(String value) {
      for (ComplainantStakeEnum b : ComplainantStakeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<ComplainantStakeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ComplainantStakeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ComplainantStakeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ComplainantStakeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ComplainantStakeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_COMPLAINANT_STAKE = "complainantStake";
  @SerializedName(SERIALIZED_NAME_COMPLAINANT_STAKE)
  private ComplainantStakeEnum complainantStake;

  /**
   * Gets or Sets chosenSolution
   */
  @JsonAdapter(ChosenSolutionEnum.Adapter.class)
  public enum ChosenSolutionEnum {
    PARTIAL_REFUND_WITH_PARTIAL_RETURN("PARTIAL_REFUND_WITH_PARTIAL_RETURN"),
    
    PARTIAL_REFUND_WITHOUT_RETURN("PARTIAL_REFUND_WITHOUT_RETURN"),
    
    COMPLETE_REFUND_WITH_RETURN("COMPLETE_REFUND_WITH_RETURN"),
    
    COMPLETE_REFUND_WITHOUT_RETURN("COMPLETE_REFUND_WITHOUT_RETURN"),
    
    ABANDON_CLAIM("ABANDON_CLAIM"),
    
    NULL("null");

    private String value;

    ChosenSolutionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ChosenSolutionEnum fromValue(String value) {
      for (ChosenSolutionEnum b : ChosenSolutionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<ChosenSolutionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ChosenSolutionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ChosenSolutionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ChosenSolutionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ChosenSolutionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CHOSEN_SOLUTION = "chosenSolution";
  @SerializedName(SERIALIZED_NAME_CHOSEN_SOLUTION)
  private ChosenSolutionEnum chosenSolution;

  public static final String SERIALIZED_NAME_CHOSEN_PARTIAL_REFUND_AMOUNT = "chosenPartialRefundAmount";
  @SerializedName(SERIALIZED_NAME_CHOSEN_PARTIAL_REFUND_AMOUNT)
  private Integer chosenPartialRefundAmount;

  /**
   * Gets or Sets counterSolution
   */
  @JsonAdapter(CounterSolutionEnum.Adapter.class)
  public enum CounterSolutionEnum {
    PARTIAL_REFUND_WITH_PARTIAL_RETURN("PARTIAL_REFUND_WITH_PARTIAL_RETURN"),
    
    PARTIAL_REFUND_WITHOUT_RETURN("PARTIAL_REFUND_WITHOUT_RETURN"),
    
    COMPLETE_REFUND_WITH_RETURN("COMPLETE_REFUND_WITH_RETURN"),
    
    COMPLETE_REFUND_WITHOUT_RETURN("COMPLETE_REFUND_WITHOUT_RETURN"),
    
    ABANDON_CLAIM("ABANDON_CLAIM"),
    
    NULL("null");

    private String value;

    CounterSolutionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CounterSolutionEnum fromValue(String value) {
      for (CounterSolutionEnum b : CounterSolutionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<CounterSolutionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CounterSolutionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CounterSolutionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CounterSolutionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CounterSolutionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_COUNTER_SOLUTION = "counterSolution";
  @SerializedName(SERIALIZED_NAME_COUNTER_SOLUTION)
  private CounterSolutionEnum counterSolution;

  public static final String SERIALIZED_NAME_COUNTER_PARTIAL_REFUND_AMOUNT = "counterPartialRefundAmount";
  @SerializedName(SERIALIZED_NAME_COUNTER_PARTIAL_REFUND_AMOUNT)
  private Integer counterPartialRefundAmount;

  public static final String SERIALIZED_NAME_SELLER_NOTES = "sellerNotes";
  @SerializedName(SERIALIZED_NAME_SELLER_NOTES)
  private String sellerNotes;

  /**
   * Gets or Sets sellerRejectionReason
   */
  @JsonAdapter(SellerRejectionReasonEnum.Adapter.class)
  public enum SellerRejectionReasonEnum {
    UNJUSTIFIED_REQUEST("UNJUSTIFIED_REQUEST"),
    
    ABUSIVE_REQUEST("ABUSIVE_REQUEST"),
    
    FRAUD_ATTEMPT("FRAUD_ATTEMPT"),
    
    OTHER("OTHER"),
    
    NULL("null");

    private String value;

    SellerRejectionReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SellerRejectionReasonEnum fromValue(String value) {
      for (SellerRejectionReasonEnum b : SellerRejectionReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<SellerRejectionReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SellerRejectionReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SellerRejectionReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SellerRejectionReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SellerRejectionReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SELLER_REJECTION_REASON = "sellerRejectionReason";
  @SerializedName(SERIALIZED_NAME_SELLER_REJECTION_REASON)
  private SellerRejectionReasonEnum sellerRejectionReason;

  public static final String SERIALIZED_NAME_COMPLAINANT_APPROVAL = "complainantApproval";
  @SerializedName(SERIALIZED_NAME_COMPLAINANT_APPROVAL)
  private Boolean complainantApproval;

  public static final String SERIALIZED_NAME_SELLER_APPROVAL = "sellerApproval";
  @SerializedName(SERIALIZED_NAME_SELLER_APPROVAL)
  private Boolean sellerApproval;

  /**
   * Gets or Sets platformSolution
   */
  @JsonAdapter(PlatformSolutionEnum.Adapter.class)
  public enum PlatformSolutionEnum {
    PARTIAL_REFUND_WITH_PARTIAL_RETURN("PARTIAL_REFUND_WITH_PARTIAL_RETURN"),
    
    PARTIAL_REFUND_WITHOUT_RETURN("PARTIAL_REFUND_WITHOUT_RETURN"),
    
    COMPLETE_REFUND_WITH_RETURN("COMPLETE_REFUND_WITH_RETURN"),
    
    COMPLETE_REFUND_WITHOUT_RETURN("COMPLETE_REFUND_WITHOUT_RETURN"),
    
    ABANDON_CLAIM("ABANDON_CLAIM"),
    
    NULL("null");

    private String value;

    PlatformSolutionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PlatformSolutionEnum fromValue(String value) {
      for (PlatformSolutionEnum b : PlatformSolutionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<PlatformSolutionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PlatformSolutionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PlatformSolutionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PlatformSolutionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PlatformSolutionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PLATFORM_SOLUTION = "platformSolution";
  @SerializedName(SERIALIZED_NAME_PLATFORM_SOLUTION)
  private PlatformSolutionEnum platformSolution;

  public static final String SERIALIZED_NAME_PLATFORM_PARTIAL_REFUND_AMOUNT = "platformPartialRefundAmount";
  @SerializedName(SERIALIZED_NAME_PLATFORM_PARTIAL_REFUND_AMOUNT)
  private Integer platformPartialRefundAmount;

  public static final String SERIALIZED_NAME_PLATFORM_APPROVAL = "platformApproval";
  @SerializedName(SERIALIZED_NAME_PLATFORM_APPROVAL)
  private Boolean platformApproval;

  public static final String SERIALIZED_NAME_PLATFORM_REASONING = "platformReasoning";
  @SerializedName(SERIALIZED_NAME_PLATFORM_REASONING)
  private String platformReasoning;

  public DisputeUpdate() {
  }

  public DisputeUpdate itemCount(Integer itemCount) {
    this.itemCount = itemCount;
    return this;
  }

   /**
   * The dispute may concern only PART of the package. Specify it there.
   * @return itemCount
  **/
  @javax.annotation.Nullable
  public Integer getItemCount() {
    return itemCount;
  }

  public void setItemCount(Integer itemCount) {
    this.itemCount = itemCount;
  }


  public DisputeUpdate issueType(IssueTypeEnum issueType) {
    this.issueType = issueType;
    return this;
  }

   /**
   * Get issueType
   * @return issueType
  **/
  @javax.annotation.Nullable
  public IssueTypeEnum getIssueType() {
    return issueType;
  }

  public void setIssueType(IssueTypeEnum issueType) {
    this.issueType = issueType;
  }


  public DisputeUpdate issueInDescriptionType(IssueInDescriptionTypeEnum issueInDescriptionType) {
    this.issueInDescriptionType = issueInDescriptionType;
    return this;
  }

   /**
   * To be set only in conjunction of issueType &#x3D; NOT_AS_DESCRIBED.
   * @return issueInDescriptionType
  **/
  @javax.annotation.Nullable
  public IssueInDescriptionTypeEnum getIssueInDescriptionType() {
    return issueInDescriptionType;
  }

  public void setIssueInDescriptionType(IssueInDescriptionTypeEnum issueInDescriptionType) {
    this.issueInDescriptionType = issueInDescriptionType;
  }


  public DisputeUpdate issueMentionedInOffer(Boolean issueMentionedInOffer) {
    this.issueMentionedInOffer = issueMentionedInOffer;
    return this;
  }

   /**
   * Get issueMentionedInOffer
   * @return issueMentionedInOffer
  **/
  @javax.annotation.Nullable
  public Boolean getIssueMentionedInOffer() {
    return issueMentionedInOffer;
  }

  public void setIssueMentionedInOffer(Boolean issueMentionedInOffer) {
    this.issueMentionedInOffer = issueMentionedInOffer;
  }


  public DisputeUpdate issueDetails(String issueDetails) {
    this.issueDetails = issueDetails;
    return this;
  }

   /**
   * Get issueDetails
   * @return issueDetails
  **/
  @javax.annotation.Nullable
  public String getIssueDetails() {
    return issueDetails;
  }

  public void setIssueDetails(String issueDetails) {
    this.issueDetails = issueDetails;
  }


  public DisputeUpdate complainantStake(ComplainantStakeEnum complainantStake) {
    this.complainantStake = complainantStake;
    return this;
  }

   /**
   * Get complainantStake
   * @return complainantStake
  **/
  @javax.annotation.Nullable
  public ComplainantStakeEnum getComplainantStake() {
    return complainantStake;
  }

  public void setComplainantStake(ComplainantStakeEnum complainantStake) {
    this.complainantStake = complainantStake;
  }


  public DisputeUpdate chosenSolution(ChosenSolutionEnum chosenSolution) {
    this.chosenSolution = chosenSolution;
    return this;
  }

   /**
   * Get chosenSolution
   * @return chosenSolution
  **/
  @javax.annotation.Nullable
  public ChosenSolutionEnum getChosenSolution() {
    return chosenSolution;
  }

  public void setChosenSolution(ChosenSolutionEnum chosenSolution) {
    this.chosenSolution = chosenSolution;
  }


  public DisputeUpdate chosenPartialRefundAmount(Integer chosenPartialRefundAmount) {
    this.chosenPartialRefundAmount = chosenPartialRefundAmount;
    return this;
  }

   /**
   * Get chosenPartialRefundAmount
   * @return chosenPartialRefundAmount
  **/
  @javax.annotation.Nullable
  public Integer getChosenPartialRefundAmount() {
    return chosenPartialRefundAmount;
  }

  public void setChosenPartialRefundAmount(Integer chosenPartialRefundAmount) {
    this.chosenPartialRefundAmount = chosenPartialRefundAmount;
  }


  public DisputeUpdate counterSolution(CounterSolutionEnum counterSolution) {
    this.counterSolution = counterSolution;
    return this;
  }

   /**
   * Get counterSolution
   * @return counterSolution
  **/
  @javax.annotation.Nullable
  public CounterSolutionEnum getCounterSolution() {
    return counterSolution;
  }

  public void setCounterSolution(CounterSolutionEnum counterSolution) {
    this.counterSolution = counterSolution;
  }


  public DisputeUpdate counterPartialRefundAmount(Integer counterPartialRefundAmount) {
    this.counterPartialRefundAmount = counterPartialRefundAmount;
    return this;
  }

   /**
   * Get counterPartialRefundAmount
   * @return counterPartialRefundAmount
  **/
  @javax.annotation.Nullable
  public Integer getCounterPartialRefundAmount() {
    return counterPartialRefundAmount;
  }

  public void setCounterPartialRefundAmount(Integer counterPartialRefundAmount) {
    this.counterPartialRefundAmount = counterPartialRefundAmount;
  }


  public DisputeUpdate sellerNotes(String sellerNotes) {
    this.sellerNotes = sellerNotes;
    return this;
  }

   /**
   * Get sellerNotes
   * @return sellerNotes
  **/
  @javax.annotation.Nullable
  public String getSellerNotes() {
    return sellerNotes;
  }

  public void setSellerNotes(String sellerNotes) {
    this.sellerNotes = sellerNotes;
  }


  public DisputeUpdate sellerRejectionReason(SellerRejectionReasonEnum sellerRejectionReason) {
    this.sellerRejectionReason = sellerRejectionReason;
    return this;
  }

   /**
   * Get sellerRejectionReason
   * @return sellerRejectionReason
  **/
  @javax.annotation.Nullable
  public SellerRejectionReasonEnum getSellerRejectionReason() {
    return sellerRejectionReason;
  }

  public void setSellerRejectionReason(SellerRejectionReasonEnum sellerRejectionReason) {
    this.sellerRejectionReason = sellerRejectionReason;
  }


  public DisputeUpdate complainantApproval(Boolean complainantApproval) {
    this.complainantApproval = complainantApproval;
    return this;
  }

   /**
   * Get complainantApproval
   * @return complainantApproval
  **/
  @javax.annotation.Nullable
  public Boolean getComplainantApproval() {
    return complainantApproval;
  }

  public void setComplainantApproval(Boolean complainantApproval) {
    this.complainantApproval = complainantApproval;
  }


  public DisputeUpdate sellerApproval(Boolean sellerApproval) {
    this.sellerApproval = sellerApproval;
    return this;
  }

   /**
   * Get sellerApproval
   * @return sellerApproval
  **/
  @javax.annotation.Nullable
  public Boolean getSellerApproval() {
    return sellerApproval;
  }

  public void setSellerApproval(Boolean sellerApproval) {
    this.sellerApproval = sellerApproval;
  }


  public DisputeUpdate platformSolution(PlatformSolutionEnum platformSolution) {
    this.platformSolution = platformSolution;
    return this;
  }

   /**
   * Get platformSolution
   * @return platformSolution
  **/
  @javax.annotation.Nullable
  public PlatformSolutionEnum getPlatformSolution() {
    return platformSolution;
  }

  public void setPlatformSolution(PlatformSolutionEnum platformSolution) {
    this.platformSolution = platformSolution;
  }


  public DisputeUpdate platformPartialRefundAmount(Integer platformPartialRefundAmount) {
    this.platformPartialRefundAmount = platformPartialRefundAmount;
    return this;
  }

   /**
   * Get platformPartialRefundAmount
   * @return platformPartialRefundAmount
  **/
  @javax.annotation.Nullable
  public Integer getPlatformPartialRefundAmount() {
    return platformPartialRefundAmount;
  }

  public void setPlatformPartialRefundAmount(Integer platformPartialRefundAmount) {
    this.platformPartialRefundAmount = platformPartialRefundAmount;
  }


  public DisputeUpdate platformApproval(Boolean platformApproval) {
    this.platformApproval = platformApproval;
    return this;
  }

   /**
   * Get platformApproval
   * @return platformApproval
  **/
  @javax.annotation.Nullable
  public Boolean getPlatformApproval() {
    return platformApproval;
  }

  public void setPlatformApproval(Boolean platformApproval) {
    this.platformApproval = platformApproval;
  }


  public DisputeUpdate platformReasoning(String platformReasoning) {
    this.platformReasoning = platformReasoning;
    return this;
  }

   /**
   * Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care.
   * @return platformReasoning
  **/
  @javax.annotation.Nullable
  public String getPlatformReasoning() {
    return platformReasoning;
  }

  public void setPlatformReasoning(String platformReasoning) {
    this.platformReasoning = platformReasoning;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DisputeUpdate disputeUpdate = (DisputeUpdate) o;
    return Objects.equals(this.itemCount, disputeUpdate.itemCount) &&
        Objects.equals(this.issueType, disputeUpdate.issueType) &&
        Objects.equals(this.issueInDescriptionType, disputeUpdate.issueInDescriptionType) &&
        Objects.equals(this.issueMentionedInOffer, disputeUpdate.issueMentionedInOffer) &&
        Objects.equals(this.issueDetails, disputeUpdate.issueDetails) &&
        Objects.equals(this.complainantStake, disputeUpdate.complainantStake) &&
        Objects.equals(this.chosenSolution, disputeUpdate.chosenSolution) &&
        Objects.equals(this.chosenPartialRefundAmount, disputeUpdate.chosenPartialRefundAmount) &&
        Objects.equals(this.counterSolution, disputeUpdate.counterSolution) &&
        Objects.equals(this.counterPartialRefundAmount, disputeUpdate.counterPartialRefundAmount) &&
        Objects.equals(this.sellerNotes, disputeUpdate.sellerNotes) &&
        Objects.equals(this.sellerRejectionReason, disputeUpdate.sellerRejectionReason) &&
        Objects.equals(this.complainantApproval, disputeUpdate.complainantApproval) &&
        Objects.equals(this.sellerApproval, disputeUpdate.sellerApproval) &&
        Objects.equals(this.platformSolution, disputeUpdate.platformSolution) &&
        Objects.equals(this.platformPartialRefundAmount, disputeUpdate.platformPartialRefundAmount) &&
        Objects.equals(this.platformApproval, disputeUpdate.platformApproval) &&
        Objects.equals(this.platformReasoning, disputeUpdate.platformReasoning);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(itemCount, issueType, issueInDescriptionType, issueMentionedInOffer, issueDetails, complainantStake, chosenSolution, chosenPartialRefundAmount, counterSolution, counterPartialRefundAmount, sellerNotes, sellerRejectionReason, complainantApproval, sellerApproval, platformSolution, platformPartialRefundAmount, platformApproval, platformReasoning);
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
    sb.append("class DisputeUpdate {\n");
    sb.append("    itemCount: ").append(toIndentedString(itemCount)).append("\n");
    sb.append("    issueType: ").append(toIndentedString(issueType)).append("\n");
    sb.append("    issueInDescriptionType: ").append(toIndentedString(issueInDescriptionType)).append("\n");
    sb.append("    issueMentionedInOffer: ").append(toIndentedString(issueMentionedInOffer)).append("\n");
    sb.append("    issueDetails: ").append(toIndentedString(issueDetails)).append("\n");
    sb.append("    complainantStake: ").append(toIndentedString(complainantStake)).append("\n");
    sb.append("    chosenSolution: ").append(toIndentedString(chosenSolution)).append("\n");
    sb.append("    chosenPartialRefundAmount: ").append(toIndentedString(chosenPartialRefundAmount)).append("\n");
    sb.append("    counterSolution: ").append(toIndentedString(counterSolution)).append("\n");
    sb.append("    counterPartialRefundAmount: ").append(toIndentedString(counterPartialRefundAmount)).append("\n");
    sb.append("    sellerNotes: ").append(toIndentedString(sellerNotes)).append("\n");
    sb.append("    sellerRejectionReason: ").append(toIndentedString(sellerRejectionReason)).append("\n");
    sb.append("    complainantApproval: ").append(toIndentedString(complainantApproval)).append("\n");
    sb.append("    sellerApproval: ").append(toIndentedString(sellerApproval)).append("\n");
    sb.append("    platformSolution: ").append(toIndentedString(platformSolution)).append("\n");
    sb.append("    platformPartialRefundAmount: ").append(toIndentedString(platformPartialRefundAmount)).append("\n");
    sb.append("    platformApproval: ").append(toIndentedString(platformApproval)).append("\n");
    sb.append("    platformReasoning: ").append(toIndentedString(platformReasoning)).append("\n");
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
    openapiFields.add("itemCount");
    openapiFields.add("issueType");
    openapiFields.add("issueInDescriptionType");
    openapiFields.add("issueMentionedInOffer");
    openapiFields.add("issueDetails");
    openapiFields.add("complainantStake");
    openapiFields.add("chosenSolution");
    openapiFields.add("chosenPartialRefundAmount");
    openapiFields.add("counterSolution");
    openapiFields.add("counterPartialRefundAmount");
    openapiFields.add("sellerNotes");
    openapiFields.add("sellerRejectionReason");
    openapiFields.add("complainantApproval");
    openapiFields.add("sellerApproval");
    openapiFields.add("platformSolution");
    openapiFields.add("platformPartialRefundAmount");
    openapiFields.add("platformApproval");
    openapiFields.add("platformReasoning");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Element and throws an exception if issues found
  *
  * @param jsonElement JSON Element
  * @throws IOException if the JSON Element is invalid with respect to DisputeUpdate
  */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DisputeUpdate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DisputeUpdate is not found in the empty JSON string", DisputeUpdate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DisputeUpdate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DisputeUpdate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("issueType") != null && !jsonObj.get("issueType").isJsonNull()) && !jsonObj.get("issueType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issueType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issueType").toString()));
      }
      // validate the optional field `issueType`
      if (jsonObj.get("issueType") != null && !jsonObj.get("issueType").isJsonNull()) {
        IssueTypeEnum.validateJsonElement(jsonObj.get("issueType"));
      }
      if ((jsonObj.get("issueInDescriptionType") != null && !jsonObj.get("issueInDescriptionType").isJsonNull()) && !jsonObj.get("issueInDescriptionType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issueInDescriptionType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issueInDescriptionType").toString()));
      }
      // validate the optional field `issueInDescriptionType`
      if (jsonObj.get("issueInDescriptionType") != null && !jsonObj.get("issueInDescriptionType").isJsonNull()) {
        IssueInDescriptionTypeEnum.validateJsonElement(jsonObj.get("issueInDescriptionType"));
      }
      if ((jsonObj.get("issueDetails") != null && !jsonObj.get("issueDetails").isJsonNull()) && !jsonObj.get("issueDetails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issueDetails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issueDetails").toString()));
      }
      if ((jsonObj.get("complainantStake") != null && !jsonObj.get("complainantStake").isJsonNull()) && !jsonObj.get("complainantStake").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `complainantStake` to be a primitive type in the JSON string but got `%s`", jsonObj.get("complainantStake").toString()));
      }
      // validate the optional field `complainantStake`
      if (jsonObj.get("complainantStake") != null && !jsonObj.get("complainantStake").isJsonNull()) {
        ComplainantStakeEnum.validateJsonElement(jsonObj.get("complainantStake"));
      }
      if ((jsonObj.get("chosenSolution") != null && !jsonObj.get("chosenSolution").isJsonNull()) && !jsonObj.get("chosenSolution").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `chosenSolution` to be a primitive type in the JSON string but got `%s`", jsonObj.get("chosenSolution").toString()));
      }
      // validate the optional field `chosenSolution`
      if (jsonObj.get("chosenSolution") != null && !jsonObj.get("chosenSolution").isJsonNull()) {
        ChosenSolutionEnum.validateJsonElement(jsonObj.get("chosenSolution"));
      }
      if ((jsonObj.get("counterSolution") != null && !jsonObj.get("counterSolution").isJsonNull()) && !jsonObj.get("counterSolution").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `counterSolution` to be a primitive type in the JSON string but got `%s`", jsonObj.get("counterSolution").toString()));
      }
      // validate the optional field `counterSolution`
      if (jsonObj.get("counterSolution") != null && !jsonObj.get("counterSolution").isJsonNull()) {
        CounterSolutionEnum.validateJsonElement(jsonObj.get("counterSolution"));
      }
      if ((jsonObj.get("sellerNotes") != null && !jsonObj.get("sellerNotes").isJsonNull()) && !jsonObj.get("sellerNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellerNotes").toString()));
      }
      if ((jsonObj.get("sellerRejectionReason") != null && !jsonObj.get("sellerRejectionReason").isJsonNull()) && !jsonObj.get("sellerRejectionReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerRejectionReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellerRejectionReason").toString()));
      }
      // validate the optional field `sellerRejectionReason`
      if (jsonObj.get("sellerRejectionReason") != null && !jsonObj.get("sellerRejectionReason").isJsonNull()) {
        SellerRejectionReasonEnum.validateJsonElement(jsonObj.get("sellerRejectionReason"));
      }
      if ((jsonObj.get("platformSolution") != null && !jsonObj.get("platformSolution").isJsonNull()) && !jsonObj.get("platformSolution").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `platformSolution` to be a primitive type in the JSON string but got `%s`", jsonObj.get("platformSolution").toString()));
      }
      // validate the optional field `platformSolution`
      if (jsonObj.get("platformSolution") != null && !jsonObj.get("platformSolution").isJsonNull()) {
        PlatformSolutionEnum.validateJsonElement(jsonObj.get("platformSolution"));
      }
      if ((jsonObj.get("platformReasoning") != null && !jsonObj.get("platformReasoning").isJsonNull()) && !jsonObj.get("platformReasoning").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `platformReasoning` to be a primitive type in the JSON string but got `%s`", jsonObj.get("platformReasoning").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DisputeUpdate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DisputeUpdate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DisputeUpdate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DisputeUpdate.class));

       return (TypeAdapter<T>) new TypeAdapter<DisputeUpdate>() {
           @Override
           public void write(JsonWriter out, DisputeUpdate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DisputeUpdate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of DisputeUpdate given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of DisputeUpdate
  * @throws IOException if the JSON string is invalid with respect to DisputeUpdate
  */
  public static DisputeUpdate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DisputeUpdate.class);
  }

 /**
  * Convert an instance of DisputeUpdate to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

