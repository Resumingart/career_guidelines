import streamlit as st
import functions
from database import Login, Career
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import hashlib

# global 
login_state= False
email = None

c = st.columns(8)
b1 = c[0].button("About")
b2  = c[1].button("Login")
b3  = c[2].button("Signup")

form =st.empty()
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def open_db():
    engine = create_engine("sqlite:///db.sqlite3")
    Session = sessionmaker(bind=engine)
    return Session()

def signup(box):
    with st.form('f2'):
        box.subheader("Create an Account")
        new_user = st.text_input('Email address')
        new_passwd = st.text_input('New Password', type='password')
        new_passwd2 = st.text_input('New Password again', type='password')
        btn = st.form_submit_button("Sign Up")   
        if btn  and len(new_user)>0: #
            db = open_db()
            if new_passwd == new_passwd2:#
                db.add(Login(email = new_user, password = new_passwd))
            else:#
                st.error("password isn't matching !")#
            db.commit()
            db.close()
            box.success("You have successfully created an account!")

        else:  #
            st.error("something went wrong....")    #

def login(box):
    with st.form('f1'):
        user = st.text_input('Email here')
        passwd = st.text_input('Password here',type='password')
        btn = st.form_submit_button("submit")
        if btn:
            db = open_db()
            hashed_pswd = make_hashes(passwd)
            result = None
            try:
                result = db.query(Login).filter(Login.email == user).filter(Login.password==passwd)
            except:
                box.error("Could not log you in! wrong credentials")
            else:
                if result:
                    box.success("Logged In as {result.email}".format(user))
                    return result

def about(box):
    box.markdown('''
    this web_App is to help you to choose best career option

    BEST OF LUCK👍👍
    ''')
                

st.image('path.jpg')

st.title("welcome to career guidelines")

box = st.empty()
if b1 :
    about(box)

if b2 :
    email = login(box)

if b3:
    signup(box)

if email and len(email) > 10:
    login.text("You are logged in.")

if login or signup:
    with st.form("f3"):
        name = st.text_input("Enter your Name:")
        college = st.text_input("Enter your college name:")
        edn = st.selectbox('Education Level:',['select one','12th','Graduate','Masters','Diploma'])
        strm = st.selectbox("What is your Stream:",['select',"Science","Commerce","Arts"])
        submit_btn = st.form_submit_button("submit form")

    if len(name)>1 and strm =='Science' and (edn=='12th' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):        
        category = st.selectbox('select',('select','PCM','PCB'))
        if strm=='Science' and category=='PCM':
            functions.PCM()
        elif strm=='Science' and category=='PCB':
            functions.PCB()
        else:
            st.info("please select a right option")
    elif len(name)>1 and strm=='Commerce' and ( edn=='12th' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):
            functions.commerce()

    elif len(name)>1 and strm =='Arts' and ( edn=='12th' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):
        functions.Arts()
    else:
        st.error("form incomplete")



if email and len(email)>10:
    with st.expander("Starting Form",True):
        pass
