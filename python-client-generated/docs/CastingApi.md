# swagger_client.CastingApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**casting_delete**](CastingApi.md#casting_delete) | **DELETE** /casting | 
[**casting_get**](CastingApi.md#casting_get) | **GET** /casting | 
[**casting_patch**](CastingApi.md#casting_patch) | **PATCH** /casting | 
[**casting_post**](CastingApi.md#casting_post) | **POST** /casting | 

# **casting_delete**
> casting_delete(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.casting_delete(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, prefer=prefer)
except ApiException as e:
    print("Exception when calling CastingApi->casting_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **casting_get**
> list[Casting] casting_get(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.casting_get(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastingApi->casting_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Casting]**](Casting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **casting_patch**
> casting_patch(body=body, prefer=prefer, casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
body = swagger_client.Casting() # Casting | casting (optional)
prefer = 'prefer_example' # str | Preference (optional)
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)

try:
    api_instance.casting_patch(body=body, prefer=prefer, casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices)
except ApiException as e:
    print("Exception when calling CastingApi->casting_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Casting**](Casting.md)| casting | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **casting_post**
> casting_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
body = swagger_client.Casting() # Casting | casting (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.casting_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling CastingApi->casting_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Casting**](Casting.md)| casting | [optional] 
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

