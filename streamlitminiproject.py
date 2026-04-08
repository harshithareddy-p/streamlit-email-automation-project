import streamlit as st
import smtplib

# Function to send email
def send_email(subject, message, to_email):
    sender_email = st.secrets["EMAIL"]
    sender_password = st.secrets["PASSWORD"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, f"Subject: {subject}\n\n{message}")
    server.quit()


st.title("JOB APPLICATION FORM")

name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
password = st.text_input("Enter your password:", type="password")

gender = st.radio("Select your gender:", ["Male", "Female", "Other"])

message = st.text_area("Enter your message:")

position = st.selectbox(
    "Select your position:",
    ["Software Engineer", "Data Scientist", "Product Manager"]
)

country_code = st.selectbox(
    "Select your country code:",
    ["+91", "+92", "+93", "+94", "+95"]
)

skills = st.multiselect(
    "Select your skills:",
    ["Python", "JavaScript", "SQL", "Machine Learning", "Cloud Computing"]
)

agree = st.checkbox("I agree to the terms and conditions")

app = st.button("Submit")

if app:
    if name and email and password and message and agree:
        send_email(
            "New Job Application Submitted Successfully!",
            f"""
Name: {name}
Email: {email}
Gender: {gender}
Position: {position}
Skills: {', '.join(skills)}
Message: {message}
            """,
            email
        )
        st.success("Your application has been submitted successfully!")
    else:
        st.error("Please fill all fields and accept terms.")
