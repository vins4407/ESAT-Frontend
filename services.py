import requests as rq
import pandas as pd
import streamlit as st

@st.cache_data
def get_user():
    try:
        users=rq.get('http://192.168.211.241:8000/list-connected-device' ,timeout=60)
        return users.json()["device_info"]
    except:
        return None
    

def upload_ipmac(ip,mac):
    try:
        data={"ip": ip, "mac": mac}
        ip_sent=rq.post('http://192.168.211.241:8000/insert_known',json=data)
        return ip_sent.status_code
    except:
        return None
    
def get_userdeatils():
    try:
        employee=rq.get('http://192.168.211.241:8000/knownTable' )
        return employee.json()
    except:
        return None    
    
    

# def addstatus(x):
#     print(x)
    
# data = pd.DataFrame(get_user()).apply(addstatus,axis=1)
# print(data)
# for i in data:
#  print(data.info)
#  print(data)
# print("Fullg",users.json())




