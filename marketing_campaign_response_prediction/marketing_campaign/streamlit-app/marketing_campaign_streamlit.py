import streamlit as st
import pickle
import pandas as pd
def achieved(url): 
    st.markdown(f'<p style="color:#32CD32;font-size:35px;"><strong>{url}</strong></p>', unsafe_allow_html=True)
    
def non_achieved(url): 
    st.markdown(f'<p style="color:#ff0000;font-size:35px;"><strong>{url}</strong></p>', unsafe_allow_html=True)
def svc_predict():
    col1, col2 = st.columns([1,1])

    with col1:
         st.image("woxsen_logo.png")


    with col2:
        st.image("appstek_logo.jpg")

    st.header("Market Campaign Prediction")
    output_list = []
 
    
    col1, col2 = st.columns([1,1])
    with col1:
        age=st.text_input('age',12)
        output_list.append(int(age))
        

    with col2:
        job_list = ['blue-collar', 'technician', 'management', 'services','retired', 'admin.', 'housemaid', 'unemployed', 'entrepreneur', 'self-employed', 'unknown', 'student']
        job_type = st.selectbox("Select the job type:",job_list)
        job_dict = {'blue-collar':0, 'technician':1, 'management':2, 'services':3,'retired':4, 'admin.':5, 'housemaid':6, 'unemployed':7, 'entrepreneur':8, 'self-employed':9, 'unknown':10, 'student':11}
        output_list.append( job_dict[job_type])
        
      


    col1 , col2 = st.columns([1,1])
    with col1:
        marital_list=['married', 'single', 'divorced', 'unknown']
        marital=st.selectbox("Select the marital :",marital_list)
        marital_dict = {'married':0, 'single':1, 'divorced':2, 'unknown':3}
        output_list.append(marital_dict[marital])
        
      
       

    with col2:
        education_list=['basic.4y', 'unknown', 'university.degree', 'high.school', 'basic.9y','professional.course', 'basic.6y', 'illiterate']
        education=st.selectbox("Select the education :",education_list)
        education_dict = {'basic.4y':0, 'unknown':1, 'university.degree':2, 'high.school':3, 'basic.9y':4,'professional.course':5, 'basic.6y':6, 'illiterate':7}
        output_list.append(education_dict[education])
        
        



    col1 , col2 = st.columns([1,1])
    with col1:
        default_list=['unknown', 'no', 'yes']
        default=st.selectbox("Select the default :",default_list)
        default_dict={'unknown':0, 'no':1, 'yes':2}
        output_list.append( default_dict[ default])
        

    with col2:
        housing_list=['unknown', 'no', 'yes']
        housing=st.selectbox("Select the housing :",housing_list)
        housing_dict={'unknown':0, 'no':1, 'yes':2}
        output_list.append( housing_dict[ housing])
        


        
    col1 , col2 = st.columns([1,1])
    with col1:
        loan_satus_list=['unknown', 'no', 'yes']
        loan_satus=st.selectbox("Select the loan_satus :",loan_satus_list)
        loan_dict={'unknown':0, 'no':1, 'yes':2}
        output_list.append( loan_dict[ loan_satus])
        




    
    with col2:
        contact_list=['cellular', 'telephone']
        contact =st.selectbox("Select the contact :",contact_list)
        contact_dict={'cellular':0, 'telephone':1}
        output_list.append(  contact_dict[ contact])

    col1 , col2 = st.columns([1,1])   
    with col1:
        month_list=['aug', 'nov', 'jun', 'apr', 'jul', 'may', 'oct', 'mar', 'sep', 'dec','feb','jan']
        month=st.selectbox("Select the month :",month_list)
        month_dict={'aug':0, 'nov':1, 'jun':2, 'apr':3, 'jul':4, 'may':5, 'oct':6, 'mar':7, 'sep':8,
       'dec':9,'feb':10,'apr':11}
        output_list.append( month_dict[ month])
        
        




    
    with col2:
        day_list=['thu', 'fri','sat', 'sun', 'tue', 'mon', 'wed']
        day =st.selectbox("Select the  day :", day_list)
        day_dict={'thu':3, 'fri':4,'sat':5, 'sun':6, 'tue':1, 'mon':0, 'wed':2}
        output_list.append( day_dict[ day])


    col1 , col2 = st.columns([1,1])
    with col1:
        Campaign=st.text_input('Campaign:',0)
        output_list.append(int(Campaign))
    with col2:
        Pdays=st.text_input('Pdays:',0)
        output_list.append(int(Pdays))


    col1 , col2 = st.columns([1,1])   
    with col1:
        Previous=st.text_input('Previous',0)
        output_list.append(int(Previous))
                  
    with col2:
        poutcome_list=['nonexistent', 'success', 'failure']
        poutcome=st.selectbox("Select the  poutcome:", poutcome_list)
        poutcome_dict={'nonexistent':0, 'success':1, 'failure':2}
        output_list.append( poutcome_dict[ poutcome])



    col1 , col2 = st.columns([1,1])
    with col1:
        emp_var_rate=st.text_input('emp_var_rate:',2)
        output_list.append(int(emp_var_rate))
        

    with col2:
        Duration=st.text_input('Duration:',2)
        output_list.append(int(Duration))
        
    col1 , col2 = st.columns([1,1])  
    with col1:
        Cons_price_idx=st.text_input('Cons_price_idx:',2)
        output_list.append(int(Cons_price_idx))
        
    with col2:
        Cons_conf_idx=st.text_input('Cons_conf_idx:',2)
        output_list.append(int( Cons_conf_idx))
        
    col1 , col2 = st.columns([1,1])    
    with col1:
        Euriborem =st.text_input('Euriborem :',2)
        output_list.append(int( Euriborem))
        

    with col2:
        nr_employed =st.text_input('nr_employed :',2)
        output_list.append(int( nr_employed))
        
        
    

    if st.button("Predict"):

        df = pd.DataFrame(columns=['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
       'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
       'previous', 'poutcome', 'emp_var_rate', 'cons_price_idx',
       'cons_conf_idx', 'euribor3m', 'nr_employed'])
        df.loc[0,:] = output_list
        
        #x_test = scaler.fit_transform(df)
        
        with open('Marketing_campaign.pkl', 'rb') as f:
            loaded_svc_linear = pickle.load(f)

        output=loaded_svc_linear.predict(df)

        
        if output[0] == 1:
            with col3:
                 achieved("The Markerting campaign will be successful")
            
        else:
            non_achieved("The Markerting campaign won't successful")


if __name__ == "__main__":
    svc_predict()
