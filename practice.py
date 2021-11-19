import streamlit as st
import functions
st.image('header.png')

st.title("welcome to career guidelines")
login = st.empty()
email = login.text_input("what's your email")
if email and len(email) > 10:
    login.text("You are logged in.")

abt = st.sidebar.write("about")
st.sidebar.markdown('''
this web_App is to help you to choose best career option..

BEST OF LUCK👍👍
''')



if email and len(email)>10:
    with st.expander("Starting Form",True):
        with st.form("add_form"):
            name = st.text_input("Enter your Name:")
            edn = st.selectbox('Education Level:',['select one','12th','Graduate','Masters','Diploma'])
            strm = st.selectbox("What is your Stream:",['select',"Science","Commerce","Arts"])
            submit_btn = st.form_submit_button("submit form")
    
    
    if len(name)>3 and strm =='Science' and (edn=='12' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):        
        category = st.selectbox('select',('select','PCM','PCB'))
        if strm=='Science' and category=='PCM':
            functions.PCM(edn)
        elif strm=='Science' and category=='PCB':
            functions.PCB(edn)
        else:
            pass
    elif len(name)>0 and strm=='Commerce' and (edn=='12' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):
        functions.commerce()

    elif len(name)>0 and strm =='Arts' and (edn=='12' or edn=='Graduate' or edn=='Masters' or edn=='Diploma'):
        functions.Arts()
    else:
        st.error("form incomplete")


