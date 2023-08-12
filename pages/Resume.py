import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(layout="wide")

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
ex1, ex2, ex3 = st.columns([1.5, 0.45, 1.5])
with ex2:
    st.title("Resume")



col1, col2, col3, col4 = st.columns([0.3, 0.5,0.5,0.5]) # returns 2 column objects for webpage
with col1:
    st.write(" ")
with col2:
    st.button("View as a PDF 📄", on_click=open_page, args=('https://docs.google.com/document/d/1sQNKUBIqul0SkLZ4FdtaUubBFYcqnB0inlxDuzaTpbc/edit?usp=sharing',), key='pdf')
with col3:
    st.button("LinkedIn 🤝", on_click=open_page, args=('https://www.linkedin.com/in/raphaelevangelista58/',), key='linkedin')
with col4:
    st.button("Github 💡", on_click=open_page, args=('https://github.com/skythepoppy',), key='github')

st.write('-'*10)


with st.container():
    st.header("Education")
    st.subheader("The University of Texas at Dallas")
    utd_content = """
            * Bachelor of Science Computer Science | 2021 - Expected 2024 
            * Activities:
                * Society of Asian Scientists and Engineers (SASE) - Webmaster
                * Google Developer Student Club (GDSC) - Member
                * Associate of Computing Machinery (ACM) - ACM Education Mentor
                * Asian Student Organization (ASO) - Secretary and Co-Founder
                * Filipino Student Association (FSA) - Cultural Ambassador
            
    """
    st.info(utd_content)
    st.subheader("Texas A&M University - Austin Community College")
    atm_content = """
            * Texas A&M and Austin Community College Chevron Engineering Program | 2019 - 2021
            * Bachelor of Science General Engineering
            * Activities:
                * Associate of Computing Machinery (ACM) - Member
                * Girls Who Code (all are invited) - Member
                * A&M Engineering Entrepreneurship - Member/Contestant
            
    """
    st.info(atm_content)

st.write('-'*10)

with st.container():
    st.header("Technical Skills")
    content = """
            * Languages: Python, C++, Java, Javascript 
            * Frameworks: Flask, Django, React
            * Operating Systems: Windows, Linux 
            * Other: SQLite, Firebase, Splunk
    """
    st.info(content)

st.write('-'*10)

with st.container():
    st.header("Relevant Coursework")
    content = """
            * Computer Science I & II 
            * C++ in UNIX Environment
            * Discrete Mathematics 
            * Electricity and Magnetism
            * Digital Logic and Computer Design      
    """
    st.info(content)

st.write('-'*10)
