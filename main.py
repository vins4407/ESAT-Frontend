import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from helper import hash,defaultConfig
import plotly.express as px 
import plotly.graph_objs as go
from streamlit_lottie import st_lottie
import pandas as pd
from services import get_userdeatils
import json
defaultConfig()

noDataFigure = go.Figure()

emails = ["yamen@gmail.com"]

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

 
def homepage():
    leftt,rightt=st.columns(2)
    with leftt:
        st.title("DashBoard :chart_with_upwards_trend:")
        st.caption("Empower your organization with a cutting-edge security testing tool that exposes vulnerabilities and reinforces employee vigilance")
    with rightt:
        st_lottie(
        load_lottiefile("./98723-search-users.json"),
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=230,
        width=230,
        key=None,
    )

    # lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
    # lottie_json = load_lottieurl(lottie_url)
    # st_lottie(lottie_json,w);
   
    st.subheader(f"Welcome Yameen :wave:")
    data =pd.DataFrame(get_userdeatils())
    left_column, right_column = st.columns(2)
    
    if data.empty:
        left_column.plotly_chart(noDataFigure, use_container_width=True)
    else:
        open_ports = px.bar(data, x='ipaddress', y='open_ports')
        open_ports.update_layout(title="<b>Open ports </b>")
        left_column.plotly_chart(open_ports, use_container_width=True)   
        
    if data.empty:
            right_column.plotly_chart(noDataFigure, use_container_width=True)
    else:
        severty_level = px.bar(data, y='ipaddress', x='open_ports',orientation="h")
        severty_level.update_layout(title="<b> Severty </b>")
        right_column.plotly_chart(severty_level, use_container_width=True)   
    print(data)
    st.table(data)



credentials = {
    
    "usernames":{
    "yameen":{
    "name":"Yameen",
    "email":"yameen@gmail.com",
    "password":hash("yameen")
    }
    }
}

noDataFigure.update_layout(
    annotations=[
        go.layout.Annotation(
            x=2,
            y=2,
            text="No data available",
            showarrow=False,
            font=dict(size=30)
        )
    ],
    title="<b>No data Available</b>",
    template="plotly_white",
)


status = st.empty()

authenticator = stauth.Authenticate(credentials,"TheifDetection","4587368413", preauthorized=emails)

with status.container():

    selected = option_menu(
        menu_title=None, 
        options=["Login", "Register"],
        icons=["box-arrow-in-right", "door-open"],  
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        key="option_menu"
    )


    if selected == "Login":
        name, authentication_status, username = authenticator.login('Login', 'main')


    if selected == "Register":
        try:
            # credentials = loadUser()
            if authenticator.register_user('Register user', preauthorization=False):
                st.write("autheicated")
                # newUsernames = authenticator.credentials['usernames'].keys()
                # for userName in newUsernames:
                #     if userName not in list(credentials['usernames'].keys()):
                #         # print("add user list")
                #         userDict = authenticator.credentials['usernames'][userName]
                #         # print("userDict",userDict)
                #         updateUser(userName, userDict)
                #         st.success('User registered successfully, Please Login to Continue')
                #         st.balloons()
                #         break
        except Exception as e:
            st.error(e)

if st.session_state["authentication_status"]:
    # status.empty()
    # authenticator.logout('Logout', 'sidebar')
    # userName = st.session_state["name"]
    # if userName:
    #     homePage(userName)
    status.empty()
    homepage()
    authenticator.logout('Logout', 'sidebar')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    
    
    
