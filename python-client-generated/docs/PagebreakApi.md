# swagger_client.PagebreakApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagebreak_delete**](PagebreakApi.md#pagebreak_delete) | **DELETE** /pagebreak | 
[**pagebreak_get**](PagebreakApi.md#pagebreak_get) | **GET** /pagebreak | 
[**pagebreak_patch**](PagebreakApi.md#pagebreak_patch) | **PATCH** /pagebreak | 
[**pagebreak_post**](PagebreakApi.md#pagebreak_post) | **POST** /pagebreak | 

# **pagebreak_delete**
> pagebreak_delete(page_break_id=page_break_id, script_id=script_id, page_number=page_number, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.pagebreak_delete(page_break_id=page_break_id, script_id=script_id, page_number=page_number, prefer=prefer)
except ApiException as e:
    print("Exception when calling PagebreakApi->pagebreak_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pagebreak_get**
> list[Pagebreak] pagebreak_get(page_break_id=page_break_id, script_id=script_id, page_number=page_number, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.pagebreak_get(page_break_id=page_break_id, script_id=script_id, page_number=page_number, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagebreakApi->pagebreak_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Pagebreak]**](Pagebreak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pagebreak_patch**
> pagebreak_patch(body=body, prefer=prefer, page_break_id=page_break_id, script_id=script_id, page_number=page_number)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
body = swagger_client.Pagebreak() # Pagebreak | pagebreak (optional)
prefer = 'prefer_example' # str | Preference (optional)
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)

try:
    api_instance.pagebreak_patch(body=body, prefer=prefer, page_break_id=page_break_id, script_id=script_id, page_number=page_number)
except ApiException as e:
    print("Exception when calling PagebreakApi->pagebreak_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pagebreak**](Pagebreak.md)| pagebreak | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pagebreak_post**
> pagebreak_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
body = swagger_client.Pagebreak() # Pagebreak | pagebreak (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.pagebreak_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling PagebreakApi->pagebreak_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pagebreak**](Pagebreak.md)| pagebreak | [optional] 
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

