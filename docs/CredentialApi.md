# lieluobo.CredentialApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grant**](CredentialApi.md#grant) | **PUT** /credential/grant | 
[**list**](CredentialApi.md#list) | **GET** /credential | 
[**revoke**](CredentialApi.md#revoke) | **PUT** /credential/revoke | 

# **grant**
> Credential grant()



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
api_instance = lieluobo.CredentialApi(lieluobo.ApiClient(configuration))

try:
    api_response = api_instance.grant()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->grant: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Credential**](Credential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[Credential] list()



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
api_instance = lieluobo.CredentialApi(lieluobo.ApiClient(configuration))

try:
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Credential]**](Credential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**
> revoke()



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
api_instance = lieluobo.CredentialApi(lieluobo.ApiClient(configuration))

try:
    api_instance.revoke()
except ApiException as e:
    print("Exception when calling CredentialApi->revoke: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

