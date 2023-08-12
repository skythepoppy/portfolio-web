import streamlit as st
from send_email import send_email


st.header("📧 Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Email Address")
    raw_message = st.text_area("Message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully! I'll respond as soon as I can!")

