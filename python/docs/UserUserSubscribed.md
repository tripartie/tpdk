# UserUserSubscribed

Disable a user account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**iri** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.user_user_subscribed import UserUserSubscribed

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserSubscribed from a JSON string
user_user_subscribed_instance = UserUserSubscribed.from_json(json)
# print the JSON string representation of the object
print(UserUserSubscribed.to_json())

# convert the object into a dict
user_user_subscribed_dict = user_user_subscribed_instance.to_dict()
# create an instance of UserUserSubscribed from a dict
user_user_subscribed_from_dict = UserUserSubscribed.from_dict(user_user_subscribed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


