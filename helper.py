import bcrypt
import streamlit as st

def hash(password:str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

if __name__ == "__main__":
    hash()
    
    
def defaultConfig(pagesize:int=1) -> None:
    if pagesize == 0:
        st.set_page_config(layout="wide")
    elif pagesize == 1:
        st.set_page_config(layout="centered")
        
    hide_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)