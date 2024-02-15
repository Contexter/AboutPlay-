# swagger_client.PlaywrightApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playwright_delete**](PlaywrightApi.md#playwright_delete) | **DELETE** /playwright | 
[**playwright_get**](PlaywrightApi.md#playwright_get) | **GET** /playwright | 
[**playwright_patch**](PlaywrightApi.md#playwright_patch) | **PATCH** /playwright | 
[**playwright_post**](PlaywrightApi.md#playwright_post) | **POST** /playwright | 

# **playwright_delete**
> playwright_delete(author_id=author_id, name=name, biography=biography, contact_information=contact_information, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaywrightApi()
author_id = 'author_id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
biography = 'biography_example' # str |  (optional)
contact_information = 'contact_information_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.playwright_delete(author_id=author_id, name=name, biography=biography, contact_information=contact_information, prefer=prefer)
except ApiException as e:
    print("Exception when calling PlaywrightApi->playwright_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **biography** | **str**|  | [optional] 
 **contact_information** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playwright_get**
> list[Playwright] playwright_get(author_id=author_id, name=name, biography=biography, contact_information=contact_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaywrightApi()
author_id = 'author_id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
biography = 'biography_example' # str |  (optional)
contact_information = 'contact_information_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.playwright_get(author_id=author_id, name=name, biography=biography, contact_information=contact_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaywrightApi->playwright_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **biography** | **str**|  | [optional] 
 **contact_information** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Playwright]**](Playwright.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playwright_patch**
> playwright_patch(body=body, prefer=prefer, author_id=author_id, name=name, biography=biography, contact_information=contact_information)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaywrightApi()
body = swagger_client.Playwright() # Playwright | playwright (optional)
prefer = 'prefer_example' # str | Preference (optional)
author_id = 'author_id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
biography = 'biography_example' # str |  (optional)
contact_information = 'contact_information_example' # str |  (optional)

try:
    api_instance.playwright_patch(body=body, prefer=prefer, author_id=author_id, name=name, biography=biography, contact_information=contact_information)
except ApiException as e:
    print("Exception when calling PlaywrightApi->playwright_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Playwright**](Playwright.md)| playwright | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **author_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **biography** | **str**|  | [optional] 
 **contact_information** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playwright_post**
> playwright_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaywrightApi()
body = swagger_client.Playwright() # Playwright | playwright (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.playwright_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling PlaywrightApi->playwright_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Playwright**](Playwright.md)| playwright | [optional] 
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

