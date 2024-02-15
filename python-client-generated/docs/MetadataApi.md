# swagger_client.MetadataApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_delete**](MetadataApi.md#metadata_delete) | **DELETE** /metadata | 
[**metadata_get**](MetadataApi.md#metadata_get) | **GET** /metadata | 
[**metadata_patch**](MetadataApi.md#metadata_patch) | **PATCH** /metadata | 
[**metadata_post**](MetadataApi.md#metadata_post) | **POST** /metadata | 

# **metadata_delete**
> metadata_delete(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.metadata_delete(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, prefer=prefer)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get**
> list[Metadata] metadata_get(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.metadata_get(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_patch**
> metadata_patch(body=body, prefer=prefer, metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.Metadata() # Metadata | metadata (optional)
prefer = 'prefer_example' # str | Preference (optional)
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)

try:
    api_instance.metadata_patch(body=body, prefer=prefer, metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| metadata | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_post**
> metadata_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.Metadata() # Metadata | metadata (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.metadata_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| metadata | [optional] 
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

