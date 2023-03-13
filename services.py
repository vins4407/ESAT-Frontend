import requests as rq

users=rq.get('http://0.0.0.0:8000/list-connected-device')
 
print(users)

