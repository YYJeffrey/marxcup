# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 20:18
# @Author  : Jeffrey
import requests
import json
import random
import time

# login_url = 'https://www.qingsuyun.com/h5/107515/pc/exam/collection/#paperId=1803217582'
answerId = input('您的answerId：')
score_str = input('您想要的分数：')
delay_second = input('您每题想要几秒完成：')

url = 'https://www.qingsuyun.com/h5/actions/exam/execute/find-exam.json'
data = {'answerId': answerId, 'queryItems': True}
r = requests.post(url, data=data)
json_data = json.loads(r.text)['body']['examItems']
false_answer = []
if (int(score_str) >= 40) and (int(score_str) <= 100):
    false_answer = random.sample(range(0, 60), 100 - int(score_str))  # 随机错误答案，根据您输入的分数而定

for j in range(80):
    questionId = json_data[j]['questionId']
    if 'single' in json_data[j]['jsonData']:
        questions = json_data[j]['jsonData']['single']['options']
    else:
        questions = json_data[j]['jsonData']['multiple']['options']

    answer = []
    if j in false_answer:
        for i in range(4):
            if not questions[i]['rightAnswers']:
                answer.append(i)
                break
    else:
        for i in range(4):
            if questions[i]['rightAnswers']:
                answer.append(i)

    time.sleep(random.uniform(int(delay_second)-1, int(delay_second)+1))    # 波动延迟防BAN
    answer_url = 'https://www.qingsuyun.com/h5/actions/exam/execute/submit-answer.json'
    answer_data = {'answerId': answerId, 'questionId': questionId, 'answerContent': answer}
    result = requests.post(url=answer_url, data=answer_data)
    print(result.text + '已答完第{0}题'.format(j+1))

result_url = 'https://www.qingsuyun.com/h5/actions/exam/execute/finish-exam.json'
result_data = {'answerId': answerId, 'interrupt': False}
print(requests.post(url=result_url, data=result_data).text)
print('您的最终成绩: ' + 'https://www.qingsuyun.com/h5/107515/pc/exam/exam-detail/#id={0}'.format(answerId))
