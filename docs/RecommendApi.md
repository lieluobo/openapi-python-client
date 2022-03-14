# lieluobo.RecommendApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](RecommendApi.md#authorize) | **POST** /recommend/authorize | 
[**get_recommend_jobs**](RecommendApi.md#get_recommend_jobs) | **GET** /recommend/job/{uniqueId} | 

# **authorize**
> authorize(body=body)



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
api_instance = lieluobo.RecommendApi(lieluobo.ApiClient(configuration))
body = [lieluobo.Candidate()] # list[Candidate] |  (optional)

try:
    api_instance.authorize(body=body)
except ApiException as e:
    print("Exception when calling RecommendApi->authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Candidate]**](Candidate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_jobs**
> list[Job] get_recommend_jobs(unique_id)



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
api_instance = lieluobo.RecommendApi(lieluobo.ApiClient(configuration))
unique_id = 'unique_id_example' # str | 

try:
    api_response = api_instance.get_recommend_jobs(unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendApi->get_recommend_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  | 

### Return type

[**list[Job]**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

