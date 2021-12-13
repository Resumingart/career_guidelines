from pkg_resources import run_script
import streamlit as st
import functions
from database import Login, Career
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import hashlib
import pickle
import os

# file to store setting
st.sidebar.image('path.jpg',use_column_width=True)
st.sidebar.title("welcome to career guidelines")

def script_runner(code):
    a=os.path.dirname(st.__file__)+'/static/index.html'
    with open(a, 'r') as f:
        data=f.read()
        if len(re.findall('UA-', data))==0:
            with open(a, 'w') as ff:
                newdata=re.sub('<head>','<head>'+code,data)
                ff.write(newdata)

def store_setting(dict):
    pickle.dump(dict, open("setting.pkl", "wb"))

# def load_setting():
#     try:
#         return pickle.load(open("setting.pkl", "rb"))
#     except Exception as e:
#         return {
#             "login_status": False,
#             "career": None,
#             "email":None,
#             'page':1,
#         }

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
        print("here")  
        if btn  and len(new_user)>0: 
            db = open_db()
            if new_passwd == new_passwd2:
                try:
                    l = Login(email = new_user, password = new_passwd)
                    db.add(l)
                    db.commit()
                    settings['email']=new_user
                    settings['page'] = 2
                    store_setting(settings)
                    msg.success("Account created successfully")
                    return True
                except Exception as e:
                    print(e)
                    msg.error("Could not create account")
            else:
                msg.error("password isn't matching !")
            db.close()
        else:  
            msg.error("signup to continue")    
        return False

def login(box):
    with st.form('f1'):
        user = st.text_input('Email here')
        passwd = st.text_input('Password here',type='password')
        btn = st.form_submit_button("login")
        if btn:
            db = open_db()
            hashed_pswd = make_hashes(passwd)
            result = db.query(Login).filter(Login.email == user).filter(Login.password==passwd)
            print(result.count())
            if result.count()==1:
                settings['login_status']= True
                settings['page']=3
                settings['email']=result[0].email
                store_setting(settings)
                st.markdown('''
                <script>
                location.reload();
                </script>
                ''',unsafe_allow_html=True)
            
        return False

def about(box):
    box.markdown('''
    this web_App is to help you to choose best career option

    BEST OF LUCK👍👍
    ''')

def career_form():
    career = settings['career']
    if career:
        nm = career.get('name','')
        clg = career.get('college','')
    else:
        nm = ''
        clg = ''
    with st.form("f3"):
        name = st.text_input("Enter your Name:",value=nm)
        college = st.text_input("Enter your college name:",value=clg)
        edn = st.selectbox('Education Level:',['select one','12th','Graduate','Masters','Diploma'])
        strm = st.selectbox("What is your Stream:",['select',"Science","Commerce","Arts"])
        category = st.selectbox('select',('select','PCM','PCB','No Category'))
        submit_btn = st.form_submit_button("submit form")
    if submit_btn and len(name)>1 and strm =='Science' and (edn=='12th' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):        
        db = open_db()
        career= Career(name=name,college=college,education_lvl=edn,stream=strm,email=settings['email'],career=category)
        db.add(career)
        db.commit()
        db.close()
        settings['career']= {
            'name':name,
            'college':college,
            'education_lvl':edn,
            'stream':strm,
            'category':category,
        }
        store_setting(settings)
        msg.success("data submitted successfully")
    if 'stream' in settings.get('career'):
        car = settings['career']
        if car['stream'] == 'Science' and car['category']=='PCM':
            functions.PCM()
        if car['stream'] == 'Science' and car['category']=='PCB':
            functions.PCB()
        elif car['stream']=='Commerce' and ( car['edn']=='12th' or car['edn']=='Graduate' or car['edn']=='Masters' or car['edn']=='Diploma'):
            functions.commerce()
        elif car['stream'] =='Arts' and ( car['edn']=='12th' or car['edn']=='Graduate' or car['edn']=='Masters' or car['edn']=='Diploma'):
            functions.Arts()
        else:
            st.error("Please fill the form to get some guidance")

settings = load_setting()
c = st.columns(8)
b1 = c[0].button("About")
if settings['login_status'] == True:
    b2  = c[1].button("Logout")
else:
    b2 = c[1].button("Login")
    b3 = c[2].button("Signup")
box = st.empty()
msg = st.empty()
st.sidebar.write(settings)
if settings['page']==1:
    status = signup(box)
    if status:
        settings['page']=2
        store_setting(settings)
        msg.success("Account created successfully")
elif settings['page']==2:
    status = login(box)
    if status:
        msg.info(f"you are logged in as {settings['email']}")
    else:
        msg.error("please login to continue")
elif settings['page']==3 and settings['login_status']:
    career_form()
if b1 :
    about(box)

if b2 :
    settings['page']=2
    settings['email'] = None
    settings['login_status']=False
    store_setting(settings)
try:
    if b3:
        settings['page']=1
        settings['email'] = None
        settings['login_status']=False
        store_setting(settings)
except Exception as e:
    pass