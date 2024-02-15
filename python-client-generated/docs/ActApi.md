# swagger_client.ActApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**act_delete**](ActApi.md#act_delete) | **DELETE** /act | 
[**act_get**](ActApi.md#act_get) | **GET** /act | 
[**act_patch**](ActApi.md#act_patch) | **PATCH** /act | 
[**act_post**](ActApi.md#act_post) | **POST** /act | 

# **act_delete**
> act_delete(act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
act_id = 'act_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
act_number = 'act_number_example' # str |  (optional)
synopsis = 'synopsis_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.act_delete(act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes, prefer=prefer)
except ApiException as e:
    print("Exception when calling ActApi->act_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **act_number** | **str**|  | [optional] 
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

# **act_get**
> list[Act] act_get(act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
act_id = 'act_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
act_number = 'act_number_example' # str |  (optional)
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
    api_response = api_instance.act_get(act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActApi->act_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **act_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **act_number** | **str**|  | [optional] 
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

[**list[Act]**](Act.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **act_patch**
> act_patch(body=body, prefer=prefer, act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
body = swagger_client.Act() # Act | act (optional)
prefer = 'prefer_example' # str | Preference (optional)
act_id = 'act_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
act_number = 'act_number_example' # str |  (optional)
synopsis = 'synopsis_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)

try:
    api_instance.act_patch(body=body, prefer=prefer, act_id=act_id, script_id=script_id, act_number=act_number, synopsis=synopsis, notes=notes)
except ApiException as e:
    print("Exception when calling ActApi->act_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Act**](Act.md)| act | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **act_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **act_number** | **str**|  | [optional] 
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

# **act_post**
> act_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActApi()
body = swagger_client.Act() # Act | act (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.act_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ActApi->act_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Act**](Act.md)| act | [optional] 
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

