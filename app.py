import streamlit as st

st.title("welcome to career guidelines")
login = st.empty()
email = login.text_input("what's your email")
if email and len(email) > 10:
    login.text("Continue")

abt = st.sidebar.write("about")
st.sidebar.markdown('''
this web_App is to help you to choose best career option..


BEST OF LUCK👍👍
''')


if email and len(email)>10:
    with st.form("add_form"):
        name = st.text_input("Enter your Name:")
        edn = st.selectbox('Education Level:',['12th','Graduate','Masters','Diploma'])
        strm = st.selectbox("What is your Stream:",["Science","Commerce","Arts"])
        job_category =['Analyst','Manager','Architecture','Industrial Design','Defense','Accountant','Investment Banker','Company Secretary',
        'Finance Advisior','CEO','Actuary','Taxation','CO','Auditor','Finance Officer',
        'Stock Broker','Business Consultant','Designer','Air hostess',
        'Social worker','Lawyer','Teacher','Philosophy','Psychology','International Relations',
        'Criminology','Chef','Archeology','software developer','Engineer','Physicist','Forensic','Pharmacy','Aviation','Hacking',
        "Clinical Research",'Genetics','Bio-Informatics',
        'Bio-Technology','Food Science','Public Health Adminstration','Environmental Science',
        'Pharmacy Agriculture','Hydrology','Physiology']
        jb=st.selectbox("select the field you want to work:",job_category)
        submit_btn = st.form_submit_button("submit form")


    if name and submit_btn and jb==job_category[0] and strm =='Science' and edn =='12th':
        st.info("You have selected")
        st.write(job_category[0],"Science","12th")
        st.markdown(f'''
        ### {name}, you can go through various ways
        - Research Analyst 
        - Data Analyst
        - Business Analyst

        
        ### To Be Data Analyst  
        ##### skills you must have to be data analyst 
        - Structured Query Language (SQL)
        - Microsoft Excel
        - Machine learning algorithms
        - Data visualization/Tableau
        - Python and other programming languages
        - Decision making
        - Building data sets
        - Machine learning models
        - Predictive modeling
        - Statistical analysis
        - Data engineering
        - Regression analysis
        - Data optimization

        #### Course you need
        - To be Data Analyst it is not essential you must be from technical background you just need skills.
        #### Certification
        - CompTIA Data+
        - Cloudera Certified Associate Data Analyst
        - Microsoft Certified: Data Analyst Associate
        - Other Data Analysis Certifications

        ''')
        st.subheader("Trend")
        st.image('data analyst.png')


        st.markdown('''### To be business analyst
        #### Skills Needed by Business Analyst
        Employers may require the following skills for business analysts:

        - Communication skills to guide conversations with management and clients
        - Analytical skills to find issues from varying information sources
        - Creativity with project planning and problem solving
        - Persuasion skills when explaining proposed solutions
        - Self-management skills to complete tasks without frequent intervention

        #### Job Titles Related to Business Analyst
        - Management Consultant
        - Management Analyst
        - Technology Consultant
        ''')

        st.markdown(''' ### Research Analyst
        A research analyst researches and analyses data related to the market, finance, accounting, customers, etc., and presents it to their organization. 

        #### skills
        - Numerical skills
        - Attention to detail
        - Analytical skills
        - Organizational skills
        - Critical thinking ability
        - Logical reasoning ability
        - Communication skills
        - Presentation skills

        #### TYPE OF COMPANIES THAT HIRE A RESEARCH ANALYST    jigsawaacademy.com
        - Traditional & digital banks
        - Insurance companies
        - Government agencies
        - Medical organizations
        - Pharmaceutical firms
        - Advertising/marketing companies
        - Manufacturing outlets
        - IT firms

        ### TYPES OF RESEARCH ANALYST
        - Market research analyst 
        - Operations research analyst 
        - Financial analyst
        - Economic research analyst
        - Equity research analyst
        ''')


        

    elif name and submit_btn and jb==job_category[1] and strm =='Commerce' and edn =='12th':
        st.info("You have selected")
        st.write(job_category[1],"Science","12th")
        st.markdown(f'''
        ### {name}, you can go through various ways 
        - Accountant Manager
        - Production Manager
        - Finance Manager
        - Marketing Manager
        - Human Resource Manager
        - Sales Manager
        
        ### Skills managers need
        - Managers take responsibility for the team, project or budget they are managing. They need to:
        - understand what goals need to be met
        - help plan how to achieve these goals
        - check that everyone involved understands what is needed monitor progress
        - take action if problems occur.

        ### Top Five Certifications To Advance Your Management Career
        - PMP® Project Management Professional. ...
        - Certified ScrumMaster® (CSM) ...
        - CBPA® Certified Business Process Associate, Professional, or Leader. ...
        - AIPMM Certified Brand Manager. ...
        - AMA® Certificate in Analytical Skills.


        ### courses
        - Master of Business Administration (MBA) 
        - Project Management Professional (PMP) 
        - Chartered Management Institute (CMI) 
        - Institute of Leadership and Management (ILM) 
        - Certified Management Consultant (CMC) 
        - Master in Management (MIM)
        ''')

    if name and submit_btn and jb==job_category[0] and strm =='Science' and edn =='12th':
        st.info("You have selected")
        st.write(job_category[2],"Science","12th")
        st.markdown('''
        ### B.Arch Eligibility criteria
        - To study a full-time B.Architecture programme, students must fulfill the eligibility requirements given below:

        - Aspirants must have passed their 10+2 examination or equivalent with Mathematics as one of the subjects.
        - They must have secured a minimum of 50 per cent marks (45 per cent marks for reserved category) in 10+2 or
        Should have passed 10+3 Diploma (any stream) recognised by Central/state governments with 50 per cent  aggregate marks or

        - Should have completed their International Baccalaureate Diploma, after 10 years of schooling, 
        with not less than 50 per cent marks in aggregate and with Mathematics as compulsory subject of examination.

        ### Top Entrance Exams

        - The National Aptitude Test in Architecture (NATA) and the Architecture Aptitude Test (AAT) are two of the most popular B.Arch entrance exams. 
        The former is widely accepted by colleges offering this programmes.
        The AAT is an entrance exam for admissions to architecture programmes offered by the Indian Institutes of Technology (IITs). 
        
        ### UnderGraduate Course
        - B.Architecture
        ''')

    if name and submit_btn and jb==job_category[0] and strm =='Science' and edn =='12th':
        st.info("You have selected")
        st.write(job_category[3],"Science","12th")
        st.markdown('''
        ### skills
        - Creativity
        - Artistic abilities
        - Team worker
        - Good visual imagination
        - Problem-solving ability
        - Business savvy
        - Open to feedback
        - Ability to sketch

        ### eligibility criteria
        -  candidates need to have cleared their 10+2 from a recognised board with minimum 50% aggregate marks
        -  to be eligible for admission in postgraduate level programmes in Industrial Design,
           aspirants should possess bachelor’s degree in Engineering/Architecture Design/Interior Design, or equivalent. 
        ### Industrial Design Job Profiles 
        
        - Industrial Designer
        - Product Designer
        - Industrial Design Researcher
        - Art Director
        - Desktop Publisher
        - Industrial Engineer 

        ### Industrial Design Top Recruiters
        - Industrial Designers are hired by Advertising Companies, 
        - online Retailing Companies, 
        - Colleges/Universities,
        - start-ups,
        - Multinational corporations,
        - government agencies and the likes. 

        ### UG COURSE
        - UG Diploma

        ### PG COURSES
        - M.Arch
        - M.Des
        ''')

    if name and submit_btn and jb==job_category[0] and strm =='Science' and edn =='12th':
        st.info("You have selected")
        st.write(job_category[4],"Science","12th")
        st.markdown('''
        ### you can go through various ways
        - Indian Army
        - Indian Airforce
        - Indian Navy

        ### for Indian Army 
        #### Exams to join Indian Army
        - NDA
        - CDS

        ### Indian Airforce
        ### Eligibility Criteria
        - Aspirants must have passed their 10+2 examination or equivalent with Mathematics,Physics and Chemistry as of compulsary subjects.
        - They must have secured a minimum of 60% marks in 10+2 in eachh of Physics,Chemistry and Mathematics 
        ''')

    else:
        st.warning("Something went wrong...😥😥😥")
            

            