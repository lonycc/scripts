#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
import requests
from requests.adapters import HTTPAdapter
requests.packages.urllib3.disable_warnings()
import os
import json
import time

BASE_URL = 'https://leetcode.cn'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'

# 登录
def login(EMAIL, PASSWORD):
    session = requests.Session()  # 建立会话
    session.mount('http://', HTTPAdapter(max_retries=6))  # 超时重试次数
    session.mount('https://', HTTPAdapter(max_retries=6))  # 超时重试次数
    session.encoding = "utf-8"  # 编码格式

    # 使用账号密码方式登录, 请确保账号密码正确
    login_data = {
        'login': EMAIL,
        'password': PASSWORD
    }

    sign_in_url = f'{BASE_URL}/accounts/login/'
    headers = {'User-Agent': USER_AGENT, 'Connection': 'keep-alive', 'Referer': sign_in_url, "origin": BASE_URL}

    # 发送登录请求
    session.post(sign_in_url, headers=headers, data=login_data, timeout=10, allow_redirects=False)
    is_login = session.cookies.get('LEETCODE_SESSION') != None
    if is_login:
        print("登录成功!")
        return session
    else:
        raise Exception("登录失败, 请检查账号密码是否正确!")


# 获取某个题目的提交记录
def get_submission_list(slug, session):
    url = f'{BASE_URL}/graphql/'

    payload = json.dumps({
        "operationName": "submissions",
        "variables": {
            "offset": 0,
            "limit": 40,
            "lastKey": "null",
            "questionSlug": slug
        },
        "query": "query submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n"
    })

    headers = {"content-type": "application/json", "origin": BASE_URL, "referer": f"{BASE_URL}/progress/", "user-agent": USER_AGENT}

    r = session.post(url, data=payload, headers=headers, verify=False)
    response_data = json.loads(r.text)
    return response_data



# 获取所有通过的题目列表
def get_accepted_problems(session):
    url = f'{BASE_URL}/graphql/'

    payload = json.dumps({
            "operationName": "userProfileQuestions",
            "variables": {
                "status": "ACCEPTED",
                "skip": 0,
                "first": 2000, # 一次返回的数据量
                "sortField": "LAST_SUBMITTED_AT",
                "sortOrder": "DESCENDING",
                "difficulty": [
                ]
            },
            "query": "query userProfileQuestions($status: StatusFilterEnum!, $skip: Int!, $first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!, $keyword: String, $difficulty: [DifficultyEnum!]) {\n  userProfileQuestions(status: $status, skip: $skip, first: $first, sortField: $sortField, sortOrder: $sortOrder, keyword: $keyword, difficulty: $difficulty) {\n    totalNum\n    questions {\n      translatedTitle\n      frontendId\n      titleSlug\n      title\n      difficulty\n      lastSubmittedAt\n      numSubmitted\n      lastSubmissionSrc {\n        sourceType\n        ... on SubmissionSrcLeetbookNode {\n          slug\n          title\n          pageId\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    })

    headers = {"content-type": "application/json", "origin": BASE_URL, "referer": f"{BASE_URL}/progress/", "user-agent": USER_AGENT}

    r = session.post(url, data=payload, headers=headers, verify=False)
    response_data = json.loads(r.text)
    return response_data['data']['userProfileQuestions']


# 获取做题总体分析
def get_session_progress(session):
    url = f'{BASE_URL}/graphql/'

    payload = json.dumps({
            "operationName": "sessionProgress",
            "variables": {},
            "query": "query sessionProgress {\n  userProfileSessionProgress {\n    numAcceptedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    numFailedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    numUntouchedQuestions {\n      difficulty\n      count\n      __typename\n    }\n    numSubmissions\n    numAcSubmissions\n    __typename\n  }\n}\n"
    })

    headers = {"content-type": "application/json", "origin": BASE_URL, "referer": f"{BASE_URL}/progress/", "user-agent": USER_AGENT}

    r = session.post(url, data=payload, headers=headers, verify=False)
    response_data = json.loads(r.text)
    return response_data['data']['userProfileSessionProgress']

# 生成Markdown文本
def generate_markdown_text(summary_data, list_data, session):
    # 相关介绍
    total_num = list_data['totalNum']
    list_data = list_data['questions']
    markdown_text =  "## 相关介绍\n"
    markdown_text += "这是一个简易的LeetCode自动统计程序, 可自动统计最近提交通过的题目, 并以Markdown的形式展示相关的数据。\n"
    markdown_text += "根据个人需求, 我只重点获取**提交次数**和**重刷次数**这两个指标, 目的是为了更好地辅助做题。\n"
    markdown_text +=  "## 使用教程\n"
    markdown_text += "1. Fork本仓库\n"
    markdown_text += "2. 配置GitHub Actions所需的参数\n"
    markdown_text += "    - 点击仓库下的Settings->Secrets->New repository secret, 分别添加以下secret\n"
    markdown_text += "        - Name:LEETCODE_EMAIL  Value:你的LeetCode账号\n"
    markdown_text += "        - Name:LEETCODE_PASSWORD  Value:你的LeetCode密码\n"
    markdown_text += "    - 点击[tokens](https://github.com/settings/tokens)->Generate new token\n"
    markdown_text += "        - Note:GITHUB_TOKEN\n"
    markdown_text += "        - Select scopes:建议全部勾选\n"
    markdown_text += "    - 修改[action.yml](.github/workflows/action.yml)文件的第`42行`, 将`email`更改为你的GitHub邮箱地址\n"
    markdown_text += "    - 修改[action.yml](.github/workflows/action.yml)文件的第`43行`, 将`name`更改为你的GitHub用户名\n"
    markdown_text += "3. 默认配置为12小时更新一次，可根据需求修改[action.yml](.github/workflows/action.yml)文件的第`6行`\n"
    markdown_text +=  "## 补充说明\n"
    markdown_text += "如有其他需求, 欢迎提交PR。\n"
    markdown_text += "\n\n"
    markdown_text += "> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数\n"
    markdown_text += "\n"
    markdown_text += f"> 总提交次数: {summary_data['numSubmissions']}, 总通过次数: {summary_data['numAcSubmissions']}, 已通过题数: {total_num}\n"
    markdown_text += "\n> 已通过题目的难度和数量: "
    for numAccepted in summary_data['numAcceptedQuestions']:
        markdown_text += f"{numAccepted['difficulty']} = {numAccepted['count']}, "

    markdown_text += "\n\n| 最近提交时间 | 题目 | 题目难度 | 提交次数 |\n| ---- | ---- | ---- | ---- |\n"

    for index, sub_data in enumerate(list_data):
        lastSubmittedAt = time.strftime("%Y-%m-%d %H:%M", time.localtime(sub_data['lastSubmittedAt']))
        url = f"https://leetcode-cn.com/problems/{sub_data['titleSlug']}"
        markdown_text += f"| {lastSubmittedAt}  | [{sub_data['translatedTitle']}]({url}) | {sub_data['difficulty']} | {sub_data['numSubmitted']} |\n"

    return markdown_text


if __name__ == '__main__':
    session = login(sys.argv[1], sys.argv[2]) # 登录
    summary_data = get_session_progress(session)  # 获取做题总体数据
    list_data = get_accepted_problems(session) # 获取所有通过的题目列表
    markdown_text = generate_markdown_text(summary_data, list_data, session) # 生成Markdown文本

    # 更新README.md文件
    with open('README.md', mode='w', encoding='utf-8') as f:
        f.write(markdown_text)
