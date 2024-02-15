# swagger_client.ScriptApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**script_delete**](ScriptApi.md#script_delete) | **DELETE** /script | 
[**script_get**](ScriptApi.md#script_get) | **GET** /script | 
[**script_patch**](ScriptApi.md#script_patch) | **PATCH** /script | 
[**script_post**](ScriptApi.md#script_post) | **POST** /script | 

# **script_delete**
> script_delete(script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptApi()
script_id = 'script_id_example' # str |  (optional)
title = 'title_example' # str |  (optional)
author_id = 'author_id_example' # str |  (optional)
url = 'url_example' # str |  (optional)
metadata_id = 'metadata_id_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.script_delete(script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id, prefer=prefer)
except ApiException as e:
    print("Exception when calling ScriptApi->script_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **author_id** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **metadata_id** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_get**
> list[Script] script_get(script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptApi()
script_id = 'script_id_example' # str |  (optional)
title = 'title_example' # str |  (optional)
author_id = 'author_id_example' # str |  (optional)
url = 'url_example' # str |  (optional)
metadata_id = 'metadata_id_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.script_get(script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->script_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **author_id** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **metadata_id** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Script]**](Script.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_patch**
> script_patch(body=body, prefer=prefer, script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptApi()
body = swagger_client.Script() # Script | script (optional)
prefer = 'prefer_example' # str | Preference (optional)
script_id = 'script_id_example' # str |  (optional)
title = 'title_example' # str |  (optional)
author_id = 'author_id_example' # str |  (optional)
url = 'url_example' # str |  (optional)
metadata_id = 'metadata_id_example' # str |  (optional)

try:
    api_instance.script_patch(body=body, prefer=prefer, script_id=script_id, title=title, author_id=author_id, url=url, metadata_id=metadata_id)
except ApiException as e:
    print("Exception when calling ScriptApi->script_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Script**](Script.md)| script | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **script_id** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **author_id** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **metadata_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_post**
> script_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptApi()
body = swagger_client.Script() # Script | script (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.script_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ScriptApi->script_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Script**](Script.md)| script | [optional] 
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

