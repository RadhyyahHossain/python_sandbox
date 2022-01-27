import requests
API_KEY = "669195ff1db9d1c75d4ee6ce849c"
from datetime import datetime
URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=669195ff1db9d1c75d4ee6ce849c"
exampleReq = requests.get(URL)
Max_duration = 600000
duration = 0
startTime = datetime.now()
task = {"duration":0, "pages":[], "startTime":0}
overtimetask = {"duration":0, "pages":[], "startTime":0}
data = exampleReq.json()['events']

groupa = []
groupb = []

for i in data:
    duration = i['timestamp']
    if duration < 600000:
        duration = duration + 0
        task = {"duration":duration, "pages":[], "startTime":100}
        groupa.append(task)
    elif duration > 600000:
        overduration = duration + 0
        overtimetask = {"duration": overduration, "pages":[], "startTime":100}
        groupb.append(overtimetask)

answer = {
    "Groupa": groupa,
    "Groupb": groupb
}

POST_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=669195ff1db9d1c75d4ee6ce849c"
x = requests.post(POST_URL)



