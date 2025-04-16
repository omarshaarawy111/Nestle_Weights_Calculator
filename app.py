import streamlit as st
import numpy as np
import statistics as sta
import warnings
warnings.filterwarnings('ignore')

valid_Db = {
    "web":"1234",  
}

def authenticate_user(email, password):
    return valid_Db.get(email) == password

if __name__ == "__main__" :
    st.set_page_config(
        layout="wide", 
        page_icon='⚖️', 
        page_title='Weights Calculator'
    )
    is_logged_in = st.session_state.get('is_logged_in', False)
    if not is_logged_in:
        st.markdown(
        '''
        <div style="text-align: center;">
            <img src="https://www.nestle.com/themes/custom/da_vinci_code/logo.svg" alt="Logo" style="width: 600px; height: auto;">
        </div>
        ''',
        unsafe_allow_html=True)
        
        st.markdown('<h1 style="text-align: center;  font-size:28px;">Weights Calculator</h1>', unsafe_allow_html=True)
        
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
    
        if login_button:
            if authenticate_user(email, password):
                st.session_state.is_logged_in = True
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Wrong Email or Password.")
    else:
        st.empty()
        st.markdown("<h2 style='text-align: center;'>Welcome to Weights tool</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Choose factors values of your task 😎 😎 😎</h2>", unsafe_allow_html=True)

        col1, col_space_1, col2, col_space_2, col3, col_space_3, = st.columns([1,0.5,1,0.5,1,0.5])
        
        with col1:
            st.markdown("<h3 style='text-align: center;'>Time</h3>", unsafe_allow_html=True)
            time_factor = st.selectbox("Time", list(range(1, 6)), key='time', label_visibility="collapsed")
        
        with col2:
            st.markdown("<h3 style='text-align: center;'>Uncertainty</h3>", unsafe_allow_html=True)
            uncertainty_factor = st.selectbox("Uncertainty", list(range(1, 6)), key='cert', label_visibility="collapsed")
        
        with col3:
            st.markdown("<h3 style='text-align: center;'>Complexity</h3>", unsafe_allow_html=True)
            complexity_factor = st.selectbox("Complexity", list(range(1, 6)), key='comp', label_visibility="collapsed")  

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            calc_button = st.button("Calculate", use_container_width=True) 
        if calc_button:
            factors = []
            lst = [time_factor, uncertainty_factor, complexity_factor]
            for i in lst:
                factors.append(i)
            median_value = sta.median(factors)
            st.markdown(f"<h4 style='text-align: center;font-size:25px'>Weight : {median_value}</h4>", unsafe_allow_html=True)
        
        st.markdown(f"<h4 style='text-align: center;font-size:22px'>Made with ❤️ by Web and Search team (NBS Cairo)</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;font-size:16px'>Authority : Omar Shaarawy - Moody Adel</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;font-size:16px'>Version 1.0.0 Beta</h4>", unsafe_allow_html=True)

    
