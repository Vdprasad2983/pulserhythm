import streamlit as st
import smtplib
from email.message import EmailMessage
import sqlite3
import random
import datetime
from io import BytesIO
from streamlit_option_menu import option_menu
import csv
import pandas as pd

st.set_page_config(layout="wide")
#st.image("aboutaec.jpg",use_column_width=True)
if 'otp' not in st.session_state:
    st.session_state.otp = None
if 'otp_verified' not in st.session_state:
    st.session_state.otp_verified=False
if "otp_entered" not in st.session_state:
    st.session_state.otp_entered=""

# Function to generate a new OTP
def generate_otp():
    otp = ''.join(str(random.randint(0, 9)) for _ in range(6))  # Generate 6-digit OTP
    st.session_state.otp = otp  # Store the OTP in session state
'''
# Aditya College of Engineering and Technology (ACET)
'''

def sendmail(subject,to_mail,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    from_mail='veduruparthydurgaprasad@gmail.com'
    server.login(from_mail,'zzsb qqto bvey gvrf')
    msg=EmailMessage()
    msg['Subject']=subject
    msg['From']=from_mail
    msg['To']=to_mail
    msg.set_content(content)
    server.send_message(msg)


conn=sqlite3.connect('form.db',check_same_thread=False)
cur=conn.cursor()
if 'auth' not in st.session_state:
    st.session_state.auth = 0
if 'username' not in st.session_state:
    st.session_state.username = None
if 'photo' not in st.session_state:
    st.session_state.photo = None 
if st.session_state.auth == 0:
    
    c1,c2=st.columns([3,1])
    
    with c1:
        sel1=option_menu(menu_title=None,options=['about Project','Project Members'],orientation='horizontal')
        if sel1=="about Project":
            c1.subheader("Project Title")
            c1.write("Deep Learning-Based ECG Analysis for Real-Time Arrhythmia Classification.")
            c1.subheader("Project Description/Abstract")
            c1.write("IoT-Based Real-Time Monitoring – The system integrates MAX30102 and AD8232 sensors to measure heart pulse and ECG signals, storing data securely on cloud platforms for remote access.")
            c1.write("AI-Driven Arrhythmia Prediction – Deep neural networks (DNNs) analyze ECG patterns to detect and predict arrhythmias, enhancing early diagnosis and intervention.")
            c1.write("Real-Time Alert System – The system sends alerts to healthcare providers and patients in real-time, enabling timely medical intervention and reducing mortality rates.")
            c1.write("Cloud-Based Data Management – The system securely stores and manages patient data on cloud platforms, ensuring data privacy and accessibility for healthcare providers.")
            c1.subheader("Project Objectives")
            c1.write("To develop an IoT-based system for real-time ECG monitoring and arrhythmia prediction.")
            c1.write("To integrate MAX30102 and AD8232 sensors for heart pulse and ECG signal measurement.")
            c1.write("To design a deep learning model for ECG analysis and arrhythmia classification.")
            c1.write("To implement a real-time alert system for healthcare providers and patients.")
            c1.write("To deploy a cloud-based data management system for secure storage and access.")
            c1.subheader("Project Scope")
            c1.write("The project aims to develop an IoT-based system for real-time ECG monitoring and arrhythmia prediction, leveraging deep learning algorithms for accurate diagnosis and timely intervention. The system will integrate MAX30102 and AD8232 sensors to measure heart pulse and ECG signals, storing data securely on cloud platforms for remote access. Deep neural networks (DNNs) will analyze ECG patterns to detect and predict arrhythmias, enhancing early diagnosis and intervention. A real-time alert system will send alerts to healthcare providers and patients, enabling timely medical intervention and reducing mortality rates. The cloud-based data management system will securely store and manage patient data, ensuring data privacy and accessibility for healthcare providers.")
            c1.subheader("Block Diagram")
            c1.image("block_diagram.png",use_column_width=True)
            
            c3,c4=st.columns([1,1])
            c3.subheader("Components used")
            c3.write("1. MAX30102 Sensor")
            c3.write("2. AD8232 Sensor")
            c3.write("3. Raspberry Pi 4")
            c3.write("4. Oled Display")
            c3.write("5. CNN Model")
            c3.write("6. gsm sim 900A")
            c3.write("7. ADC mcp 3208")
            c3.write("8. Bread Board & jumper wires")
            c3.write("9. Power Supply")
            c3.write("10. Cloud Platform")
            c4.subheader("Applications")
            c4.write("1. Healthcare Industry")
            c4.write("2. Remote Patient Monitoring")
            c4.write("3. Wearable Health Devices")
            c4.write("4. Medical Research")
            c4.write("5. Health Data Analytics")
            c4.write("6. Telemedicine")
            c4.write("7. Health Informatics")
            c4.write("8. IoT-Based Healthcare Solutions")
            c4.write("9. Real-Time Health Monitoring")
            c4.write("10. AI-Driven Healthcare Systems")
            
            c1.subheader("Connections")
            c1.image("Connections.jpg",width=800)
            c1.image("Connections_1.jpg",width=500)    
            c1.subheader("Present output")   
            c3,c4=st.columns([1,1])
            c3.image("Figure_1.png",use_column_width=True)
            c4.image("Figure_3.png",use_column_width=True)
            c1.image("hroutput.png",use_column_width=True)
            
            c1.subheader("Conclusion")
            c1.write("The proposed system offers a novel approach to real-time ECG monitoring and arrhythmia prediction, leveraging IoT and AI technologies for enhanced healthcare services. By integrating MAX30102 and AD8232 sensors, the system can measure heart pulse and ECG signals, storing data securely on cloud platforms for remote access. Deep learning algorithms analyze ECG patterns to detect and predict arrhythmias, enabling early diagnosis and intervention. The real-time alert system sends alerts to healthcare providers and patients, facilitating timely medical intervention and reducing mortality rates. The cloud-based data management system ensures secure storage and access to patient data, enhancing healthcare services and patient outcomes.")
            c1.subheader("References")
            c1.write("1. Web-Based Medical System for Remote Heart Rate Monitoring with Cloud Integration")
            c1.write("2. Smart Health Care Monitoring System based on Internet of Things (IoT)")
            c1.write("3. Remote Patient Monitoring: A Systematic Review")
            c1.write("4. Automated ECG Classification Using Deep Neural Networks")

        if sel1=="Project Members":
            c1.subheader("Supervisor")
            c1.write("K. Jayaram Kumar M.Tech, (P.hD)")
            c1.write("Assistant Professor")
            c1.write("Department of Electronics and Communication Engineering")
            c1.write("Aditya College of Engineering and Technology")
            
            
            c1.subheader("Project Members")
            c1.write("1. K. Rajeswari     - 21P31A04L7")
            c1.write("2. P. Harika        - 21P31A04O0")
            c1.write("3. V. Durga Prasad  - 21P31A04P8")
            c1.write("4. T. Pravallika    - 21P31A04P2")
            c1.write("5. S. Sri Vaishnavi - 21P31A04O8") 
            
            c1.subheader("View or Download files")
            c1.write("1. [Project PPT](https://docs.google.com/presentation/d/1ImBgtVzBopKCQkcvONHsnJjuoaG_T9lm/edit?usp=sharing&ouid=114552480234223904802&rtpof=true&sd=true)")    
            c1.write("2. [Project Report](https://docs.google.com/document/d/1z9ufHiOSpmEYsMnTa2ZAov1kkca2UgHR/edit?usp=sharing&ouid=114552480234223904802&rtpof=true&sd=true)")    
            
            
            
    with c2:
        select=option_menu(menu_title=None,options=['Register','Login'],orientation="horizontal",)
        if select=="Register":
            username=c2.text_input("enter your username")
            rollnumber=c2.text_input("enter your Roll Number")
            password=c2.text_input("enter your password",type='password',help="should contain atleast 8 characters and atleast one number and special character")
            password1=c2.text_input("re-enter your password",type='password',help="should contain atleast 8 characters and atleast one number and special character")
            dob=c2.date_input("Enter your date of birth",min_value=datetime.date(1900, 1, 1))
            mail=c2.text_input("enter your email address")
            mobile=c2.text_input("enter your mobile number",max_chars=10)
            with c2.expander("Toggle Menu"):
                page = c2.radio("Choose a section", ["upload photo", "Live photo"])
            if page=="Live photo":
                photo=c2.camera_input("capture you live image")
            if page=="upload photo":
                photo=c2.file_uploader("upload the photo",type=['png','jpg','jpeg'])
            submit_button=c2.button("submit")
            
            date=datetime.datetime.now()
            cur.execute(
                        """
            CREATE TABLE IF NOT EXISTS userdata(USERNAME TEXT(50),ROLLNUMBER TEXT(50),PASSWORD TEXT(50),DATEOFBIRTH TEXT(50),MAIL TEXT(50),MOBILE TEXT(50),DATE TEXT(50),IMAGE_DATA BLOB)
            """
                    )
            cur.execute('select USERNAME,PASSWORD from userdata')
            rows = cur.fetchall()
            if submit_button:
                if not username or not password or not photo:
                    st.warning("please enter the mandatory fields")
                    st.stop()
                if password!=password1:
                    st.warning("Your password is not matching")
                    st.stop()
                if len(password)<8 or sum(i.isnumeric() for i in password)<1 or sum(i.isupper() for i in password)<1 or sum(not(i.isalnum()) for i in password)<1:
                    st.warning("your password doesnt meet the critereia")
                    st.stop()
                for row in rows:
                    if username == row[0]:
                        st.warning("user name already exists")
                        st.stop()
                
                generate_otp()
                sendmail("OTP VERIFICATION",mail,f"you otp for the registration in the adityaece.onrender.com is {st.session_state.otp}")
                st.success("otp sent to you email id")
            if st.session_state.otp is not None and not st.session_state.otp_verified:
                st.session_state.otp_entered = st.text_input("Enter the OTP sent to your email address", value=st.session_state.otp_entered, max_chars=6)
                if st.button("Verify OTP"):
                    if st.session_state.otp_entered == st.session_state.otp:
                        st.session_state.otp_verified = True
                        image_bytes = photo.getvalue()
                        cur.execute(
                            """
                            INSERT INTO userdata VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (username, rollnumber, password, dob, mail, mobile, date, image_bytes),
                        )
                        conn.commit()
                        conn.close()
                        sendmail("REGISTERED SUCCESSFULLY", mail, f"Welcome to our website {username}. Thank you for registering 🤝")
                        st.success("OTP verified and registered successfully !")
                    else:
                        st.error("Invalid OTP. Please try again.")    
                    
        elif select=="Login":
            username=c2.text_input("enter your registered username")
            password=c2.text_input("enter your password",type="password")
            submit_button=c2.button("submit")
            if submit_button:
                query=("SELECT * FROM userdata WHERE USERNAME = ?")
                value=(username,)
                cur.execute(query,value)
                rows=cur.fetchall()
                if submit_button:
                    if not rows:
                        st.error("user is not registered")
                    else:
                        db_password, db_photo=rows[0][1],rows[0][-1]
                        if db_password==password:
                            st.session_state.auth = 1
                            st.session_state.username=username
                            st.session_state.photo=db_photo
                            st.rerun()
                            #st.success(f"Welcome to our website {username}")
                        else:
                            st.warning("you have entered wrong password plese check")
            
else:  # If authenticated
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    if st.session_state.photo:
        st.sidebar.image(BytesIO(st.session_state.photo),caption="your profile photo")
with st.sidebar:
    if st.session_state.auth==1:
        if st.button("Logout"):
            st.session_state.username=None
            st.session_state.photo=None
            st.session_state.auth = 0  # Reset auth to 0 on logout
            st.rerun()
if st.session_state.auth==1:
    st.write("welcome")
