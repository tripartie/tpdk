

# PersonaAuthReturn



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authUrl** | **String** | Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them. |  [optional] |
|**expireAt** | **OffsetDateTime** | This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour. |  [optional] |



