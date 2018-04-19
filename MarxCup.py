# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 20:18
# @Author  : Jeffrey
import requests
import json

# login_url = 'https://www.qingsuyun.com/h5/107515/pc/exam/collection/#paperId=1803217582'
answerId = input('请输入answerId：')
url = 'https://www.qingsuyun.com/h5/actions/exam/execute/find-exam.json'
data = {'answerId': answerId, 'queryItems': True}
r = requests.post(url, data=data)
json_data = json.loads(r.text)['body']['examItems']
# print(json_data)

for j in range(80):
    questionId = json_data[j]['questionId']
    if 'single' in json_data[j]['jsonData']:
        questions = json_data[j]['jsonData']['single']['options']
    else:
        questions = json_data[j]['jsonData']['multiple']['options']
    # print(questions)

    answer = []
    for i in range(4):
        if questions[i]['rightAnswers']:
            answer.append(i)

    answer_url = 'https://www.qingsuyun.com/h5/actions/exam/execute/submit-answer.json'
    answer_data = {'answerId': answerId, 'questionId': questionId, 'answerContent': answer}
    result = requests.post(url=answer_url, data=answer_data)
    print(result.text)

result_url = 'https://www.qingsuyun.com/h5/actions/exam/execute/finish-exam.json'
result_data = {'answerId': answerId, 'interrupt': False}
print(requests.post(url=result_url, data=result_data).text)
print('您的最终成绩: ' + 'https://www.qingsuyun.com/h5/107515/pc/exam/exam-detail/#id={0}'.format(answerId))
