import streamlit as st
from io import BytesIO
from docx import Document
from helper import defaultConfig
from docx.shared import Inches

defaultConfig()

def Report():
    st.title("Generate Report :memo:")
    
    st.selectbox("Select the IP",[0,1,2])
    ip ="10.76.15.153"
    mac="94:08:53:9b:37:d7"

    document = Document()
    
    document.add_heading('E-sat Report', 0)
    para = document.add_paragraph('The EMPLOYEE SECURITY AWARENESS TESTING TOOL is a security testing tool aimed at testing the security awareness of employees in an organization. The tool is designed to run on a local network and tests the security of the employees devices connected to the network, without their knowl')
    para.paragraph_format.line_spacing = Inches(0.2)
    document.add_heading(f'IP :- {ip}', 3,)
    document.add_heading('MAC :- {mac}', 3)
    
    document.add_heading('PORT', 3)
    document.add_paragraph('port')
    
    document.add_heading('VULNERABILITY', 3,)
    document.add_paragraph('vulnerability')
    
    document.add_heading('PHISHING', 3)
    document.add_paragraph('phishing')
    
    document.add_heading('TRAFFIC', 3)
    document.add_paragraph('traffic')

    
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