# swagger_client.PropsApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**props_delete**](PropsApi.md#props_delete) | **DELETE** /props | 
[**props_get**](PropsApi.md#props_get) | **GET** /props | 
[**props_patch**](PropsApi.md#props_patch) | **PATCH** /props | 
[**props_post**](PropsApi.md#props_post) | **POST** /props | 

# **props_delete**
> props_delete(prop_id=prop_id, scene_id=scene_id, description=description, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PropsApi()
prop_id = 'prop_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.props_delete(prop_id=prop_id, scene_id=scene_id, description=description, prefer=prefer)
except ApiException as e:
    print("Exception when calling PropsApi->props_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **props_get**
> list[Props] props_get(prop_id=prop_id, scene_id=scene_id, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PropsApi()
prop_id = 'prop_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.props_get(prop_id=prop_id, scene_id=scene_id, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropsApi->props_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Props]**](Props.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **props_patch**
> props_patch(body=body, prefer=prefer, prop_id=prop_id, scene_id=scene_id, description=description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PropsApi()
body = swagger_client.Props() # Props | props (optional)
prefer = 'prefer_example' # str | Preference (optional)
prop_id = 'prop_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    api_instance.props_patch(body=body, prefer=prefer, prop_id=prop_id, scene_id=scene_id, description=description)
except ApiException as e:
    print("Exception when calling PropsApi->props_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Props**](Props.md)| props | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **prop_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **props_post**
> props_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PropsApi()
body = swagger_client.Props() # Props | props (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.props_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling PropsApi->props_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Props**](Props.md)| props | [optional] 
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

