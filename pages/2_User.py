import streamlit as st
import pandas as pd
from helper import defaultConfig
from services import get_user,upload_ipmac
defaultConfig()

def clear_cache():
    st.legacy_caching.caching.clear_cache()


def updateList(users):
    newTemp = []
    temp=None
    for i in users:
        temp = i
        temp["status"] = False
        newTemp.append(temp)
    return newTemp
    

def User():
  
    st.title("Select User :dart:")
    
    if st.button("Refresh"):  
        st.cache_data.clear()   
       
        
    if "userList" not in st.session_state:
        st.session_state["userList"]= None
        
                 
    with st.spinner("Please wait"):
        
        data = get_user()
        if data:
            st.session_state["userList"]= data
            print(st.session_state["userList"])
        
    if st.session_state["userList"]:
        print("data check",st.session_state["userList"])
        df = pd.DataFrame(updateList(st.session_state["userList"]))
        print(df)
        edited_df = st.experimental_data_editor(df, use_container_width=True)
        
        updated_df = edited_df.loc[edited_df["status"] == True]
        print("numpy array data",updated_df.to_numpy())
        submitted=st.button(label="submit")
        if submitted:
            for i in  updated_df.to_numpy():
                print(i[0], i[1])
                upload_ipmac(ip = i[0],mac = i[1])
             

        
        


if __name__ == "__main__":
    if st.session_state["authentication_status"]:
        User()
    else:
        st.warning("Logging to acess the page")