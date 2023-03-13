import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from helper import hash,defaultConfig
import plotly.express as px 
import plotly.graph_objs as go
import pandas as pd

defaultConfig()

noDataFigure = go.Figure()


emails = ["yamen@gmail.com"]
 
def homepage():
    st.title("DashBoard")
    st.subheader(f"Welcome Yameen :wave:")

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(noDataFigure, use_container_width=True)
    right_column.plotly_chart(noDataFigure, use_container_width=True)
    data = pd.DataFrame(columns=["Name", "IP", "Mac", "Port","Phising","Traffic"])
    st.table(data)
    st.button("Save", key="save_button")


credentials = {
    
    "usernames":{
    "yameen":{
    "name":"Yameen",
    "email":"yameen@gmail.com",
    "password":hash("yameen")
    }
    }
}

fig_hourly_sales = px.bar(orientation="h",title="<b>Sales by Product Line</b>",)

noDataFigure.update_layout(
    annotations=[
        go.layout.Annotation(
            x=2.5,
            y=2,
            text="No data available",
            showarrow=False,
            font=dict(size=30)
        )
    ],
    title="<b>Sales by Product Line</b>",
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
    
    
    
