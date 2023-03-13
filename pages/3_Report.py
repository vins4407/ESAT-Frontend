import streamlit as st
from io import BytesIO
from docx import Document
from helper import defaultConfig

defaultConfig()

def Report():
    para= "gs g";
    st.title("Generate Report")
    
    st.selectbox("Select the IP",[0,1,2])

    document = Document()
    document.add_paragraph( para)
    stream = BytesIO()

    document.save(stream)
    stream.seek(0)
                
    st.download_button(
                    label="Download report file",
                    data= stream,
                    file_name='report.docx',
                    mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )


if __name__ == "__main__":
    if st.session_state["authentication_status"]:
        Report()
    else:
        st.warning("Logging to acess the page")