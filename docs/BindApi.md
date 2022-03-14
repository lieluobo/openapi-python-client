# lieluobo.BindApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_company**](BindApi.md#bind_company) | **POST** /bind/company | 
[**bind_user**](BindApi.md#bind_user) | **POST** /bind/user | 
[**get_company**](BindApi.md#get_company) | **GET** /bind/company/{uniqueId} | 
[**get_user**](BindApi.md#get_user) | **GET** /bind/user/{uniqueId}/{mobile} | 

# **bind_company**
> Company bind_company(body=body)



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
api_instance = lieluobo.BindApi(lieluobo.ApiClient(configuration))
body = lieluobo.Company() # Company |  (optional)

try:
    api_response = api_instance.bind_company(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->bind_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Company**](Company.md)|  | [optional] 

### Return type

[**Company**](Company.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bind_user**
> User bind_user(body=body)



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
api_instance = lieluobo.BindApi(lieluobo.ApiClient(configuration))
body = lieluobo.User() # User |  (optional)

try:
    api_response = api_instance.bind_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->bind_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> Company get_company(unique_id)



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
api_instance = lieluobo.BindApi(lieluobo.ApiClient(configuration))
unique_id = 'unique_id_example' # str | 

try:
    api_response = api_instance.get_company(unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  | 

### Return type

[**Company**](Company.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(mobile, unique_id)



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
api_instance = lieluobo.BindApi(lieluobo.ApiClient(configuration))
mobile = 'mobile_example' # str | 
unique_id = 'unique_id_example' # str | 

try:
    api_response = api_instance.get_user(mobile, unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BindApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile** | **str**|  | 
 **unique_id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

