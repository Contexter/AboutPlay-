# swagger_client.ActionApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_delete**](ActionApi.md#action_delete) | **DELETE** /action | 
[**action_get**](ActionApi.md#action_get) | **GET** /action | 
[**action_patch**](ActionApi.md#action_patch) | **PATCH** /action | 
[**action_post**](ActionApi.md#action_post) | **POST** /action | 

# **action_delete**
> action_delete(action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
action_id = 'action_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.action_delete(action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)
except ApiException as e:
    print("Exception when calling ActionApi->action_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_get**
> list[Action] action_get(action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
action_id = 'action_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.action_get(action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->action_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Action]**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_patch**
> action_patch(body=body, prefer=prefer, action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
body = swagger_client.Action() # Action | action (optional)
prefer = 'prefer_example' # str | Preference (optional)
action_id = 'action_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)

try:
    api_instance.action_patch(body=body, prefer=prefer, action_id=action_id, scene_id=scene_id, character_id=character_id, original_text=original_text, modernized_text=modernized_text)
except ApiException as e:
    print("Exception when calling ActionApi->action_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Action**](Action.md)| action | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **action_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_post**
> action_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
body = swagger_client.Action() # Action | action (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.action_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ActionApi->action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Action**](Action.md)| action | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **select** | **str**| Filtering Columns | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

