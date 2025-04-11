import streamlit as st
import smtplib
from email.message import EmailMessage
import psycopg2
from pytz import timezone
#import sqlite3
import random
import datetime
from io import BytesIO
from streamlit_option_menu import option_menu
import pandas as pd
import boto3
from io import StringIO
import os
st.set_page_config(layout="wide")
#st.image("aboutaec.jpg",use_container_width=True)
if 'otp' not in st.session_state:
    st.session_state.otp = None
if 'otp_verified' not in st.session_state:
    st.session_state.otp_verified=False
if "otp_entered" not in st.session_state:
    st.session_state.otp_entered=""
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
def load_csv_from_s3(file_key):
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        response = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)
        csv_data = response["Body"].read().decode("utf-8")
        df = pd.read_csv(StringIO(csv_data))
        return df
    except Exception as e:
        st.error(f"⚠️ Error loading `{file_key}`: {e}")
        return pd.DataFrame()
# Function to generate a new OTP
def generate_otp():
    otp = ''.join(str(random.randint(0, 9)) for _ in range(6))  # Generate 6-digit OTP
    st.session_state.otp = otp  # Store the OTP in session state


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

#conn=psycopg2.connect('pulserhythm','pulserhythm_user','MGnD0tV8J7ll7AXgOGRW0zAJ7lDPWnve','dpg-cvrrmvali9vc739mtoh0-a','5432')
#conn=sqlite3.connect('form.db',check_same_thread=False)
conn = psycopg2.connect(
    dbname='pulserhythm',
    user='pulserhythm_user',
    password='MGnD0tV8J7ll7AXgOGRW0zAJ7lDPWnve',
    host='dpg-cvrrmvali9vc739mtoh0-a.oregon-postgres.render.com',
    port='5432'
)
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
        c1.title("Pulse Rhythm :Real-Time ECG Monitoring and Arrhythmia Prediction")
        sel1=option_menu(menu_title=None,options=['about Project','Project Members'],orientation='horizontal')
        if sel1=="about Project":
            c1.subheader("Project Title")
            c1.write("Deep Learning-Based ECG Analysis for Real-Time Arrhythmia Classification.")
            c1.subheader("Project Description/Abstract")
            c1.write("This project focuses on real-time ECG signal acquisition and arrhythmia detection using an AD8232 sensor, MCP3208 ADC, and Raspberry Pi 4B. A MAX30102 sensor is also integrated for heart rate and SpO₂ measurement. The acquired signals are processed using a Convolutional Neural Network (CNN) trained on the MIT-BIH Arrhythmia dataset, enabling accurate classification of normal and abnormal heart rhythms. An OLED display provides real-time feedback for easy monitoring.")
            c1.write("To enhance accessibility, a user-friendly interface is developed using Streamlit for real-time ECG visualization and arrhythmia prediction. By combining hardware-based signal acquisition, AI-driven classification, and an intuitive UI, this project offers an efficient and interactive cardiac monitoring solution.")
            c1.subheader("Project Objectives")
            c1.write("To develop an IoT-based system for real-time ECG monitoring and arrhythmia prediction.")
            c1.write("To integrate MAX30102 and AD8232 sensors for heart pulse and ECG signal measurement.")
            c1.write("To design a deep learning model for ECG analysis and arrhythmia classification.")
            c1.write("To implement a real-time alert system for healthcare providers and patients.")
            c1.write("To deploy a cloud-based data management system for secure storage and access.")
            c1.subheader("Project Scope")
            c1.write("The project aims to develop an IoT-based system for real-time ECG monitoring and arrhythmia prediction, leveraging deep learning algorithms for accurate diagnosis and timely intervention. The system will integrate MAX30102 and AD8232 sensors to measure heart pulse and ECG signals, storing data securely on cloud platforms for remote access. Deep neural networks (DNNs) will analyze ECG patterns to detect and predict arrhythmias, enhancing early diagnosis and intervention. A real-time alert system will send alerts to healthcare providers and patients, enabling timely medical intervention and reducing mortality rates. The cloud-based data management system will securely store and manage patient data, ensuring data privacy and accessibility for healthcare providers.")
            c1.subheader("Block Diagram")
            c1.image("block_diagram.png",use_container_width=True)
            c1.subheader("Schematic Diagram")
            c1.image("schematic.jpg",width=800)
            
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
            c3.image("Figure_1.png",use_container_width=True)
            c4.image("Figure_3.png",use_container_width=True)
            c1.image("hroutput.png",use_container_width=True)
            
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
            c1.write("1. [Project PPT I](https://docs.google.com/presentation/d/1ImBgtVzBopKCQkcvONHsnJjuoaG_T9lm/edit?usp=sharing&ouid=114552480234223904802&rtpof=true&sd=true)")
            c1.write("1. [Project PPT II](https://docs.google.com/presentation/d/1xzYX5-VTLjPygr2XH5yaBr4Hm_pTRape/edit?usp=sharing&ouid=114552480234223904802&rtpof=true&sd=true)")    
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
            
            kolkata=timezone("Asia/Kolkata")
            date = datetime.datetime.now(tz=kolkata)
            #date=datetime.datetime.now()
            #with open(photo, "rb") as file:
                #binary_data = file.read()
            cur.execute(
                        """
            CREATE TABLE IF NOT EXISTS userdata(USERNAME VARCHAR(50),ROLLNUMBER VARCHAR(50),PASSWORD VARCHAR(50),DATEOFBIRTH VARCHAR(50),MAIL VARCHAR(50),MOBILE VARCHAR(50),DATE VARCHAR(50),IMAGE_DATA BYTEA)
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
                binary_data = photo.read()
                        #image_bytes = photo.getvalue()
                cur.execute(
                            """
                            INSERT INTO userdata VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (username, rollnumber, password, dob, mail, mobile, date, binary_data),
                        )
                conn.commit()
                conn.close()
                st.success("Registration successful")
                st.balloons()
                
                    
        elif select=="Login":
            username=c2.text_input("enter your registered username")
            password=c2.text_input("enter your password",type="password")
            submit_button=c2.button("submit")
            if submit_button:
                query=("SELECT * FROM userdata WHERE USERNAME = %s")
                value=(username,)
                cur.execute(query,value)
                rows=cur.fetchall()
                if submit_button:
                    if not rows:
                        st.error("user is not registered")
                    else:
                        db_password, db_photo=rows[0][2],rows[0][-1]
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
    st.title("🩺 Real-Time Health Monitoring Dashboard")

    # Choose which data to view
    view = st.radio("Select Data to View", ["📈 ECG Classification", "❤️ Heart Rate + SpO₂"])

    # ------------------- ECG Section ------------------- #
    if view == "📈 ECG Classification":
        st.subheader("📊 ECG Prediction History")
        ecg_df = load_csv_from_s3("ecg.csv")
        if not ecg_df.empty:
            st.dataframe(ecg_df, use_container_width=True)
            st.bar_chart(ecg_df["ecg"].value_counts())
        else:
            st.info("No ECG data available yet.")

    # ------------------- Heart Rate Section ------------------- #
    elif view == "❤️ Heart Rate + SpO₂":
        st.subheader("💓 Heart Rate and SpO₂ Readings")
        hr_df = load_csv_from_s3("heart.csv")
        if not hr_df.empty:
            st.dataframe(hr_df, use_container_width=True)
            try:
                st.line_chart(hr_df[["heart Rate", "spo2"]])
            except:
                st.warning("Plot skipped: Check if 'Heart Rate' and 'SpO2' columns exist.")
        else:
            st.info("No Heart Rate or SpO₂ data found.")