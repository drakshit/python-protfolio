import streamlit as st
from streamlit import button
from utils.send_mail import send_email

st.header("Contact US")

with st.form(key="contact_form"):
    email = st.text_input(label="Your email address")
    message_body = st.text_area(key="message", label="Your message")
    message = f"""\
Subject: New email from {email}

From: {email}
{message_body}
"""
    submit = st.form_submit_button(label="Send")
    if submit:
        send_email(message)
        st.info("Your email sent successfully!")