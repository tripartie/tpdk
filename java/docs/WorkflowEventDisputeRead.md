

# WorkflowEventDisputeRead



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** |  |  |
|**from** | **String** |  |  [optional] |
|**to** | **String** |  |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**occurredAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**initiator** | **String** |  |  [optional] [readonly] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| DISPUTE_OPENED | &quot;dispute.opened&quot; |
| DISPUTE_SUBMITTED | &quot;dispute.submitted&quot; |
| DISPUTE_CREATED | &quot;dispute.created&quot; |
| DISPUTE_ABANDONED | &quot;dispute.abandoned&quot; |
| DISPUTE_SETTLEMENT | &quot;dispute.settlement&quot; |
| DISPUTE_CLOSED | &quot;dispute.closed&quot; |
| DISPUTE_EXPIRED | &quot;dispute.expired&quot; |
| DISPUTE_MANUAL_ARBITRATION_REQUIRED | &quot;dispute.manual_arbitration_required&quot; |
| DISPUTE_UPDATED | &quot;dispute.updated&quot; |
| DISPUTE_REMINDER | &quot;dispute.reminder&quot; |
| OFFER_CREATED | &quot;offer.created&quot; |
| OFFER_EXPIRED | &quot;offer.expired&quot; |
| OFFER_UPDATED | &quot;offer.updated&quot; |
| OFFER_CRAWL_FAILURE | &quot;offer.crawl_failure&quot; |
| OFFER_TRANSACTION_AUTHORIZED | &quot;offer.transaction.authorized&quot; |
| OFFER_TRANSACTION_RECONCILED | &quot;offer.transaction.reconciled&quot; |
| OFFER_TRANSACTION_ABANDONED | &quot;offer.transaction.abandoned&quot; |
| OFFER_CLOSED | &quot;offer.closed&quot; |
| OFFER_TRANSACTION_REFUND | &quot;offer.transaction.refund&quot; |
| PERSONA_ADDED | &quot;persona.added&quot; |
| NULL | &quot;null&quot; |



