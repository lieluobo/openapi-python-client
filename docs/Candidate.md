# Candidate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | 用于标识第三方系统候选人的唯一ID，不可重复 | 
**name** | **str** | 姓名 | [optional] 
**gender** | [**AllOfCandidateGender**](AllOfCandidateGender.md) |  | [optional] 
**age** | **int** | 年龄 | [optional] 
**mobile** | **str** | 手机号 | [optional] 
**email** | **str** | 邮箱 | [optional] 
**birthday** | **date** | 出生年月 | [optional] 
**salary** | **float** | 当前年薪 | [optional] 
**introduce** | **str** | 个人简介 | [optional] 
**location** | **str** | 所在城市 | [optional] 
**languages** | **list[str]** | 语言 | [optional] 
**skills** | **list[str]** | 技能 | [optional] 
**intended_industries** | **list[str]** | 意向行业 | [optional] 
**intended_positions** | **list[str]** | 意向职位 | [optional] 
**intended_locations** | **list[str]** | 意向城市 | [optional] 
**experiences** | [**list[Experience]**](Experience.md) | 工作经验 | [optional] 
**educations** | [**list[Education]**](Education.md) | 教育经历 | [optional] 
**projects** | [**list[Project]**](Project.md) | 项目经历 | [optional] 
**notify_url** | **str** | 回调地址 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

