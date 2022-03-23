# lieluobo.OrderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](OrderApi.md#get) | **GET** /order | 
[**make**](OrderApi.md#make) | **POST** /order | 

# **get**
> Order get(job_id=job_id, resume_id=resume_id)



### Example
```python
from __future__ import print_function
import time
import lieluobo
from lieluobo.authenticator import ApiKeyAuthenticator
from lieluobo.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lieluobo.Configuration()
configuration.authenticate = ApiKeyAuthenticator(YOUR_SECRET_ID, YOUR_SECRET_KEY)

# create an instance of the API class
api_instance = lieluobo.OrderApi(lieluobo.ApiClient(configuration))
job_id = 'job_id_example' # str |  (optional)
resume_id = 'resume_id_example' # str |  (optional)

try:
    api_response = api_instance.get(job_id=job_id, resume_id=resume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | [optional] 
 **resume_id** | **str**|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make**
> Order make(body=body)



### Example
```python
from __future__ import print_function
import time
import lieluobo
from lieluobo.authenticator import ApiKeyAuthenticator
from lieluobo.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lieluobo.Configuration()
configuration.authenticate = ApiKeyAuthenticator(YOUR_SECRET_ID, YOUR_SECRET_KEY)

# create an instance of the API class
api_instance = lieluobo.OrderApi(lieluobo.ApiClient(configuration))
body = lieluobo.MakeOrderRequest() # MakeOrderRequest |  (optional)

try:
    api_response = api_instance.make(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->make: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MakeOrderRequest**](MakeOrderRequest.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

