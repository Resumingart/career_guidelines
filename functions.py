import streamlit as st



def PCM():
    
    job_options = ['select','Architecture','Industrial Design','Data Analyst','Defense','Forensic Science','Ethical Hacking','Physicist','Pharmacy']
    job_fields =st.selectbox("select a field",job_options)
    if job_fields==job_options[1]:
        print(st.markdown('''
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
        '''))
    elif job_fields==job_options[2]:
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

    elif job_fields==job_options[3]:
        st.markdown('''
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
        - Other Data Analysis Certifications''')
    elif job_fields==job_options[4]:
        st.markdown('''
        ### you can go through various ways
        - Indian Army
        - Indian Airforce
        - Indian Navy
        go through the link-https://www.4ono.com/how-join-indian-armed-forces/
            ''')
    elif job_fields==job_options[5]:
        st.markdown('''
        go through the link- https://www.shiksha.com/science/forensic-science-chp
        ''')

    elif job_fields==job_options[6]:
        st.markdown(''' go through the link-https://cybersecurityguide.org/resources/ethical-hacker/''')

    elif job_fields==job_options[7]:
        st.markdown('Go through the link-https://www.indeed.com/career-advice/career-development/how-to-become-a-physicist')

    elif job_fields==job_options[8]:
        st.markdown('Go through the link-https://www.mindler.com/blog/pharmacy-career-india-guide/')

    else:
        pass


def PCB():
    job_options = ['select','Clinical Research','Genetics','Bio-Technology','Bio-Informatics','Food Science','Public Health Adminstration','Bio-Medical Science','Environmental Science','Agriculture','Hydrology']
    job_fields = st.selectbox("select a field",job_options)
    
    if job_fields == job_options[1]:
        st.markdown('Go Through the link-https://bestaccreditedcolleges.org/articles/how-to-become-a-clinical-research-scientist-career-roadmap.html')

    elif job_fields == job_options[2]:
        st.markdown('Go Through the link-TBA')

    elif job_fields == job_options[3]:
        st.markdown('Go Through the link-https://collegedunia.com/courses/bachelor-of-engineering-be-biotechnology')

    elif job_fields == job_options[4]:
        st.markdown('Go Through the link-https://bitesizebio.com/38236/how-to-become-a-bioinformatician/')
    elif job_fields == job_options[5]:
        st.markdown('Go Through the link-https://manavrachna.edu.in/blog/career-guide-to-become-food-scientist/')
    elif job_fields == job_options[6]:
        st.markdown('Go Through the link-https://www.healthcareadministrationedu.org/public-health-administration/')
    elif job_fields == job_options[7]:
        st.markdown('Go Through the link-https://www.indiaeducation.net/careercenter/science/biomedical-science/')
    elif job_fields == job_options[8]:
        st.markdown('Go Through the link-https://www.bls.gov/ooh/life-physical-and-social-science/environmental-scientists-and-specialists.htm')
    elif job_fields == job_options[9]:
        st.markdown('Go Through the link-https://www.shiksha.com/science/agriculture-chp')
    elif job_fields == job_options[10]:
        st.markdown('Go Through the link-https://www.indeed.com/career-advice/career-development/how-to-be-hydrologist')
    else:
        pass

def commerce():
    job_options =['select','Research Analyst','Sales Manager','Budget Analyst','Auditor','Chief Financial Officer','Business Consultant','Stock Broker','Investment Banker','Taxation','Company secretary','Finance Advisor']
    job_fields =st.selectbox("select a field",job_options)
    if job_fields == job_options[1]:
        st.markdown('Go Through the link-https://corporatefinanceinstitute.com/resources/careers/jobs/research-analyst/')
    elif job_fields == job_options[2]:
        st.markdown('Go Through the link-https://www.collegedekho.com/careers/sales-manager')
    elif job_fields == job_options[3]:
        st.markdown('Go Through the link-https://www.collegedekho.com/careers/budget-analyst')
    elif job_fields == job_options[4]:
        st.markdown('Go Through the link-https://www.collegedekho.com/careers/auditor')
    elif job_fields == job_options[5]:
        st.markdown('Go Through the link-https://www.seek.com.au/career-advice/role/chief-financial-officer')
    elif job_fields == job_options[6]:
        st.markdown('Go Through the link-https://www.indeed.com/career-advice/careers/what-does-a-business-consultant-do')
    elif job_fields == job_options[7]:
        st.markdown('Go Through the link-https://www.indiaeducation.net/careercenter/commerce/career-in-stock-broking/')
    elif job_fields == job_options[8]:
        st.markdown('Go Through the link-https://www.upgrad.com/blog/investment-banker-salary-beginner-experienced/')
    elif job_fields == job_options[9]:
        st.markdown('Go Through the link-http://employmentnews.gov.in/newemp/MoreContentNew.aspx?n=InDepthJobs&k=64')
    elif job_fields == job_options[10]:
        st.markdown('Go Through the link-https://www.collegedekho.com/careers/company-secretary-cs')
    elif job_fields == job_options[11]:
        st.markdown('Go Through the link-https://www.careerindia.com/features/how-to-become-a-financial-advisor-in-india-023404.html')
    else:
        pass

def Arts():
    job_options=['select','Designer','Filmaker','Journalist','Photographer','Philosophy','Criminology','Fine Arts']
    job_fields =st.selectbox("select a field",job_options)
    if job_fields == job_options[1]:
        st.markdown('Go Through the link-https://www.themuse.com/advice/how-to-become-a-designer-at-any-stage-of-your-career')
    elif job_fields == job_options[2]:
        st.markdown('Go Through the link-https://www.wikihow.com/Be-a-Filmmaker')
    elif job_fields == job_options[3]:
        st.markdown('Go Through the link-https://collegedunia.com/courses/bachelor-of-arts-ba-journalism/how-to-become-a-journalist')
    elif job_fields == job_options[4]:
        st.markdown('Go Through the link-https://www.indiatoday.in/education-today/jobs-and-careers/story/how-to-become-a-photographer-1735030-2020-10-26')
    elif job_fields == job_options[5]:
        st.markdown('Go Through the link-https://www.gmercyu.edu/academics/learn/philosophy-major-jobs')
    elif job_fields == job_options[6]:
        st.markdown('Go Through the link-https://www.mindler.com/blog/criminology-career-india/')
    elif job_fields == job_options[7]:
        st.markdown('Go Through the link-https://www.sarvgyan.com/courses/arts/fine-arts')
    else:
        pass
