# AuthenticationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**totp_input** | **str** |  | [optional] 

## Example

```python
from tpdk.models.authentication_post_request import AuthenticationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationPostRequest from a JSON string
authentication_post_request_instance = AuthenticationPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthenticationPostRequest.to_json()

# convert the object into a dict
authentication_post_request_dict = authentication_post_request_instance.to_dict()
# create an instance of AuthenticationPostRequest from a dict
authentication_post_request_form_dict = authentication_post_request.from_dict(authentication_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


