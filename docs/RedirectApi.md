# lieluobo.RedirectApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](RedirectApi.md#get_token) | **GET** /redirect/token | 

# **get_token**
> RedirectToken get_token(company_id=company_id, mobile=mobile)



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
api_instance = lieluobo.RedirectApi(lieluobo.ApiClient(configuration))
company_id = 'company_id_example' # str |  (optional)
mobile = 'mobile_example' # str |  (optional)

try:
    api_response = api_instance.get_token(company_id=company_id, mobile=mobile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | [optional] 
 **mobile** | **str**|  | [optional] 

### Return type

[**RedirectToken**](RedirectToken.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

