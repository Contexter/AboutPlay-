# swagger_client.SceneApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scene_delete**](SceneApi.md#scene_delete) | **DELETE** /scene | 
[**scene_get**](SceneApi.md#scene_get) | **GET** /scene | 
[**scene_patch**](SceneApi.md#scene_patch) | **PATCH** /scene | 
[**scene_post**](SceneApi.md#scene_post) | **POST** /scene | 

# **scene_delete**
> scene_delete(scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SceneApi()
scene_id = 'scene_id_example' # str |  (optional)
act_id = 'act_id_example' # str |  (optional)
scene_number = 'scene_number_example' # str |  (optional)
synopsis = 'synopsis_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.scene_delete(scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes, prefer=prefer)
except ApiException as e:
    print("Exception when calling SceneApi->scene_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**|  | [optional] 
 **act_id** | **str**|  | [optional] 
 **scene_number** | **str**|  | [optional] 
 **synopsis** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scene_get**
> list[Scene] scene_get(scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SceneApi()
scene_id = 'scene_id_example' # str |  (optional)
act_id = 'act_id_example' # str |  (optional)
scene_number = 'scene_number_example' # str |  (optional)
synopsis = 'synopsis_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.scene_get(scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SceneApi->scene_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**|  | [optional] 
 **act_id** | **str**|  | [optional] 
 **scene_number** | **str**|  | [optional] 
 **synopsis** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Scene]**](Scene.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scene_patch**
> scene_patch(body=body, prefer=prefer, scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SceneApi()
body = swagger_client.Scene() # Scene | scene (optional)
prefer = 'prefer_example' # str | Preference (optional)
scene_id = 'scene_id_example' # str |  (optional)
act_id = 'act_id_example' # str |  (optional)
scene_number = 'scene_number_example' # str |  (optional)
synopsis = 'synopsis_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)

try:
    api_instance.scene_patch(body=body, prefer=prefer, scene_id=scene_id, act_id=act_id, scene_number=scene_number, synopsis=synopsis, notes=notes)
except ApiException as e:
    print("Exception when calling SceneApi->scene_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scene**](Scene.md)| scene | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **scene_id** | **str**|  | [optional] 
 **act_id** | **str**|  | [optional] 
 **scene_number** | **str**|  | [optional] 
 **synopsis** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scene_post**
> scene_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SceneApi()
body = swagger_client.Scene() # Scene | scene (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.scene_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling SceneApi->scene_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scene**](Scene.md)| scene | [optional] 
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

