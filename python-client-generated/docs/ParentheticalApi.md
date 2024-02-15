# swagger_client.ParentheticalApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parenthetical_delete**](ParentheticalApi.md#parenthetical_delete) | **DELETE** /parenthetical | 
[**parenthetical_get**](ParentheticalApi.md#parenthetical_get) | **GET** /parenthetical | 
[**parenthetical_patch**](ParentheticalApi.md#parenthetical_patch) | **PATCH** /parenthetical | 
[**parenthetical_post**](ParentheticalApi.md#parenthetical_post) | **POST** /parenthetical | 

# **parenthetical_delete**
> parenthetical_delete(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.parenthetical_delete(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)
except ApiException as e:
    print("Exception when calling ParentheticalApi->parenthetical_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
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

# **parenthetical_get**
> list[Parenthetical] parenthetical_get(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
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
    api_response = api_instance.parenthetical_get(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParentheticalApi->parenthetical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
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

[**list[Parenthetical]**](Parenthetical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parenthetical_patch**
> parenthetical_patch(body=body, prefer=prefer, parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
body = swagger_client.Parenthetical() # Parenthetical | parenthetical (optional)
prefer = 'prefer_example' # str | Preference (optional)
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)

try:
    api_instance.parenthetical_patch(body=body, prefer=prefer, parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text)
except ApiException as e:
    print("Exception when calling ParentheticalApi->parenthetical_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Parenthetical**](Parenthetical.md)| parenthetical | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
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

# **parenthetical_post**
> parenthetical_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
body = swagger_client.Parenthetical() # Parenthetical | parenthetical (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.parenthetical_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ParentheticalApi->parenthetical_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Parenthetical**](Parenthetical.md)| parenthetical | [optional] 
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

