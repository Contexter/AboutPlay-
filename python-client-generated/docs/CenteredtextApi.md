# swagger_client.CenteredtextApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**centeredtext_delete**](CenteredtextApi.md#centeredtext_delete) | **DELETE** /centeredtext | 
[**centeredtext_get**](CenteredtextApi.md#centeredtext_get) | **GET** /centeredtext | 
[**centeredtext_patch**](CenteredtextApi.md#centeredtext_patch) | **PATCH** /centeredtext | 
[**centeredtext_post**](CenteredtextApi.md#centeredtext_post) | **POST** /centeredtext | 

# **centeredtext_delete**
> centeredtext_delete(centered_id=centered_id, script_id=script_id, text=text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CenteredtextApi()
centered_id = 'centered_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.centeredtext_delete(centered_id=centered_id, script_id=script_id, text=text, prefer=prefer)
except ApiException as e:
    print("Exception when calling CenteredtextApi->centeredtext_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **centered_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **centeredtext_get**
> list[Centeredtext] centeredtext_get(centered_id=centered_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CenteredtextApi()
centered_id = 'centered_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.centeredtext_get(centered_id=centered_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CenteredtextApi->centeredtext_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **centered_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Centeredtext]**](Centeredtext.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **centeredtext_patch**
> centeredtext_patch(body=body, prefer=prefer, centered_id=centered_id, script_id=script_id, text=text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CenteredtextApi()
body = swagger_client.Centeredtext() # Centeredtext | centeredtext (optional)
prefer = 'prefer_example' # str | Preference (optional)
centered_id = 'centered_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)

try:
    api_instance.centeredtext_patch(body=body, prefer=prefer, centered_id=centered_id, script_id=script_id, text=text)
except ApiException as e:
    print("Exception when calling CenteredtextApi->centeredtext_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Centeredtext**](Centeredtext.md)| centeredtext | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **centered_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **centeredtext_post**
> centeredtext_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CenteredtextApi()
body = swagger_client.Centeredtext() # Centeredtext | centeredtext (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.centeredtext_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling CenteredtextApi->centeredtext_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Centeredtext**](Centeredtext.md)| centeredtext | [optional] 
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

