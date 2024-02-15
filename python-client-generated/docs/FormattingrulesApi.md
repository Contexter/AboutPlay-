# swagger_client.FormattingrulesApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formattingrules_delete**](FormattingrulesApi.md#formattingrules_delete) | **DELETE** /formattingrules | 
[**formattingrules_get**](FormattingrulesApi.md#formattingrules_get) | **GET** /formattingrules | 
[**formattingrules_patch**](FormattingrulesApi.md#formattingrules_patch) | **PATCH** /formattingrules | 
[**formattingrules_post**](FormattingrulesApi.md#formattingrules_post) | **POST** /formattingrules | 

# **formattingrules_delete**
> formattingrules_delete(rule_id=rule_id, script_id=script_id, rule_description=rule_description, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.formattingrules_delete(rule_id=rule_id, script_id=script_id, rule_description=rule_description, prefer=prefer)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->formattingrules_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **formattingrules_get**
> list[Formattingrules] formattingrules_get(rule_id=rule_id, script_id=script_id, rule_description=rule_description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.formattingrules_get(rule_id=rule_id, script_id=script_id, rule_description=rule_description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->formattingrules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Formattingrules]**](Formattingrules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **formattingrules_patch**
> formattingrules_patch(body=body, prefer=prefer, rule_id=rule_id, script_id=script_id, rule_description=rule_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
body = swagger_client.Formattingrules() # Formattingrules | formattingrules (optional)
prefer = 'prefer_example' # str | Preference (optional)
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)

try:
    api_instance.formattingrules_patch(body=body, prefer=prefer, rule_id=rule_id, script_id=script_id, rule_description=rule_description)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->formattingrules_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Formattingrules**](Formattingrules.md)| formattingrules | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **formattingrules_post**
> formattingrules_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
body = swagger_client.Formattingrules() # Formattingrules | formattingrules (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.formattingrules_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->formattingrules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Formattingrules**](Formattingrules.md)| formattingrules | [optional] 
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

