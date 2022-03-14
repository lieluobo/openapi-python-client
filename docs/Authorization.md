# 认证

## 请求签名


* `timestamp` 生成精确到毫秒的unix时间戳，`timestamp`要求与猎萝卜服务端时间相差不超过30分钟。
* `method` 请求的方法，大写。支持 `POST`,`GET`, `PUT`, `DELETE`, `HEAD`
* `path` 请求的`path`部分
* `key_list` 请求的`query_string`的`key`按照字典序正序排列，用英文半角逗号`,`分隔。
* `value_list` 请求的`query_string`的`key`按照字典序正序排列，对应的`value`(同一个`key`有多个`value`的， 多个`value`按照字典序，正序排列)，用英文半角逗号`,`分隔。
* `digest`, 生成摘要，`timestamp`, `method`, `path`, `key_list`, `value_list`使用英文半角分号`;`连接。计算其`sha512`的**16进制小写字符串**
* `signature`, 生成签名，使用 `secret_key`作为`key`, 对 `digest`计算`hmac-sha512`值的**16进制小写字符串**
* 拼接认证字符串 'ApiKey timestamp=$timestamp&ak=$secret_id&signature=$signature'
* 把请求头`Authorization`设置为上一步拼接的认证字符串。


详情请参考 [**lieluobo/authenticator.py**](../lieluobo/authenticator.py)  