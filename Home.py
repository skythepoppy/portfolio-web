import base64
import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)



ex4, ex5, ex6, ex7,ex8= st.columns([1.5,1,0.5,0.5,1.5])
with ex5:
    st.header("Raphael Evangelista")
    st.markdown("*(Computer Science Major/Aspiring Software Developer)*")



filler1, col1, col2, filler3 = st.columns([1.5,1,1,1.5])  # returns 2 column objects for webpage
with col1:
    content = """I am currently a UT Dallas Computer Science Major. As an aspiring Software Engineer/Full-Stack Dev, It is my fundamental belief that as one pursues their academic endeavors, one is not just a student then, but for life. 
       I strive to seek knowledge and to constantly learn in hopes that through my passion for technological innovation, 
       I am not only able to improve my skillset but also create a lasting impact in software development."""
    st.info(content)
with col2:
    st.image("images/me.JPEG", width=300)



line1,line2,line3 = st.columns([1.5,2,1.5])
with line2:
    st.write('-'*10)


c1,c2,c3,c4 = st.columns([1.5,1.5,0.5,1.5])
with c2:
    st.subheader(" 🖥️ I'm interested in...")

m1,m2,m3 = st.columns([1.5,2,1.5])
with m2:
    st.info("These are some aspects of computer programming that I am most interested in!"
            "I have either worked with or am currently learning these interests of mine!")
    st.write("""
                **Programming Languages**  : *Python* , *C++*, *Java* , *Javascript* , *Typescript* 

                **Web Dev**: *Flask* , *Django* , *React* , *Tailwind CSS* , *Redux* , *Node*

                **Databases** : *sqlite* , *firebase* , *mysql* , *oracle* 

                **Other**: *Splunk* , *Better Stack*
        """)

line4,line5,line6 = st.columns([1.5,2,1.5])
with line5:
    st.write('-'*5)

c4,c5,c6,c7 = st.columns([1.5,1.5,0.6,1.5])
with c5:
    st.subheader(" 😄 My favorite memories!")
c8,c9,c10,c11 = st.columns([1.5,1.0,1.0,1.5])
with c9:
    st.image("images/VAIP2.jpg")
    st.caption("Had a great time at the largest hackathon in North Texas; the 48 hour HACKUTD! As a team, we were able "
               "to complete our project 'Vehicular AI Presets' and present it to companies such as Toyota and Statefarm!"
               "")
with c10:
    st.image("images/EE.JPG")
    st.caption("My first hackathon was during my sophomore year "
               "at the 48 hour A&M Engineering Entrepreneurship Hackathon! The theme that year was SOCOM, "
               "geared towards the Army and Special Operations. As a group we developed a prototype reconnaissance "
               "drone fitted with 4 dc motors, a single motion sensor, and an imaging sensor! ")


line7,line8,line9 = st.columns([1.5,2,1.5])
with line8:
    st.write('-'*5)


c12,c13,c14,c15 = st.columns([1.5,1.5,0.5,1.5])
with c13:
    st.subheader(" 🤝 Let's Connect!")

c15, c16, c17, c18, c19 = st.columns([1.5, 0.6, 0.6, 0.6, 1.5])
with c16:
    email_me = st.button("Send me an email! 📨", on_click=open_page, args=('https://www.linkedin.com/in/raphaelevangelista58/',),
              key='email')
    if email_me:
        switch_page("Contact Me")
with c17:
    st.button("Add me on LinkedIn! 🧠", on_click=open_page, args=('https://www.linkedin.com/in/raphaelevangelista58/',),
              key='linkedin')
with c18:
    st.button("Checkout my Github! 💡", on_click=open_page, args=('https://github.com/skythepoppy',),
              key='github')



