import streamlit as st
import pandas as pd
from helper import defaultConfig

defaultConfig()

def User():
    st.title("Select User")
    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "Select": True},
       {"command": "st.balloons", "rating": 5, "Select": False},
       {"command": "st.time_input", "rating": 3, "Select": True},
   ]
    )
    edited_df = st.experimental_data_editor(df, use_container_width=True)
    
    favorite_command = edited_df.loc[edited_df["Select"] == True]
    print(favorite_command.to_numpy())
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

if __name__ == "__main__":
    if st.session_state["authentication_status"]:
        User()
    else:
        st.warning("Logging to acess the page")