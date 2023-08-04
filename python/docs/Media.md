# Media



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**extension** | **str** |  | 
**filename** | **str** |  | 
**public_url** | **str** |  | 
**file** | **bytearray** |  | [optional] 
**b64_encoded_tmp_file** | **str** |  | [optional] 
**thumbnail** | **str** | Associated 374x374 pixels small thumbnail | [optional] 
**original** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**offers** | **List[str]** |  | [optional] [readonly] 
**thumbnail_url** | **str** |  | [optional] [readonly] 

## Example

```python
from tpdk.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print Media.to_json()

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_form_dict = media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


