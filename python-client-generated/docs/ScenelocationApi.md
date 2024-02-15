# swagger_client.ScenelocationApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scenelocation_delete**](ScenelocationApi.md#scenelocation_delete) | **DELETE** /scenelocation | 
[**scenelocation_get**](ScenelocationApi.md#scenelocation_get) | **GET** /scenelocation | 
[**scenelocation_patch**](ScenelocationApi.md#scenelocation_patch) | **PATCH** /scenelocation | 
[**scenelocation_post**](ScenelocationApi.md#scenelocation_post) | **POST** /scenelocation | 

# **scenelocation_delete**
> scenelocation_delete(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.scenelocation_delete(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, prefer=prefer)
except ApiException as e:
    print("Exception when calling ScenelocationApi->scenelocation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenelocation_get**
> list[Scenelocation] scenelocation_get(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.scenelocation_get(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenelocationApi->scenelocation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Scenelocation]**](Scenelocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenelocation_patch**
> scenelocation_patch(body=body, prefer=prefer, location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
body = swagger_client.Scenelocation() # Scenelocation | scenelocation (optional)
prefer = 'prefer_example' # str | Preference (optional)
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)

try:
    api_instance.scenelocation_patch(body=body, prefer=prefer, location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance)
except ApiException as e:
    print("Exception when calling ScenelocationApi->scenelocation_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenelocation**](Scenelocation.md)| scenelocation | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenelocation_post**
> scenelocation_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
body = swagger_client.Scenelocation() # Scenelocation | scenelocation (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.scenelocation_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ScenelocationApi->scenelocation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenelocation**](Scenelocation.md)| scenelocation | [optional] 
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

