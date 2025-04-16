import streamlit as st
import numpy as np
import statistics as sta
import warnings
warnings.filterwarnings('ignore')

# Authentication data
valid_Db = {
    "web": "1234",
}

# Task weights
points_weights = {
    "Epic Task": 5,
    "Campaign page creation": 4,
    "New page with built-in Drupal components": 4,
    "Syncing on Smart Recipe Hub": 4,
    "Qualifio - ID integration on page level": 4,
    "Issue fixing at CMS level (Dev team)": 3,
    "New page from a template (pre-defined layout with set of components)": 3,
    "Page layout update (adding/modifying/removing page sections)": 3,
    "Coordination of rollouts of new content with the markets": 3,
    "Products and brand products updates": 3,
    "Terms and Condition/Privacy Policy/Copyright page creations/updates for the websites": 3,
    "Recipe sync": 3,
    "Image optimization at CMS level": 3,
    "Navigation menu updates (add/remove/re-order sections, updating links)": 3,
    "Existing categories, filters updates (add/remove/re-order)": 3,
    "Adimo ID updates for products": 3,
    "Update/ upload of new content using existing Drupal components": 2,
    "Page content update (copy, images)": 2,
    "Archive/remove a page": 2,
    "Press Release content upload": 2,
    "Upload, remove images from a page": 2,
    "Simple resizing, compressing, light Photoshop adjustments (brightness/contrast level)": 2,
    "“Buy now” solution on-page setup (Adimo, Fusepump)": 1,
    "Update image details (title, alt text)": 1,
    "Light Photoshop adjustments": 1
}

# Authentication check
def authenticate_user(email, password):
    return valid_Db.get(email) == password

# Get task complexity value
def complexity_value(key):
    return points_weights.get(key)

# Custom factor selector using st.radio with disabled "5"
def factor_selector(label, key, disable_five=True):
    options = ["1", "2", "3", "4", "5"]
    disabled_options = ["5"] if disable_five else []
    return int(st.radio(
        label,
        options=options,
        index=0,
        key=key,
        disabled=disabled_options,
        label_visibility="collapsed",
        horizontal=True
    ))

# Main Streamlit app
if __name__ == "__main__":
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

        st.markdown('<h1 style="text-align: center; font-size:28px;">Weights Calculator</h1>', unsafe_allow_html=True)

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

        col1, col_space_1, col2, col_space_2, col3, col_space_3, col4, col_space_4 = st.columns([1, 0.5, 1, 0.5, 1, 0.5, 1, 0.5])

        with col1:
            st.markdown("<h3 style='text-align: center;'>Task type</h3>", unsafe_allow_html=True)
            complexity_factor = st.selectbox("Complexity", points_weights.keys(), key='tsk', label_visibility="collapsed")

        # Determine if Epic Task is selected
        epic_selected = complexity_factor == "Epic Task"

        with col2:
            st.markdown("<h3 style='text-align: center;'>Complexity</h3>", unsafe_allow_html=True)
            task_factor = factor_selector("Task", key='comp', disable_five=True)

        with col3:
            st.markdown("<h3 style='text-align: center;'>Time</h3>", unsafe_allow_html=True)
            time_factor = factor_selector("Time", key='time', disable_five=True)

        with col4:
            st.markdown("<h3 style='text-align: center;'>Uncertainty</h3>", unsafe_allow_html=True)
            uncertainty_factor = factor_selector("Uncertainty", key='cert', disable_five=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            calc_button = st.button("Calculate", use_container_width=True)

        if calc_button:
            factors = [
                complexity_value(complexity_factor),
                task_factor,
                time_factor,
                uncertainty_factor
            ]
            median_value = sta.median(factors)
            if isinstance(median_value, float):
                median_value = int(np.ceil(median_value))
            st.markdown(f"<h4 style='text-align: center;font-size:25px'>Weight : {median_value}</h4>", unsafe_allow_html=True)

        st.markdown(f"<h4 style='text-align: center;font-size:22px'>Made with ❤️ by Web and Search team (NBS Cairo)</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;font-size:16px'>Authority : Omar Shaarawy - Moody Adel</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;font-size:16px'>Version 1.0.0 Beta</h4>", unsafe_allow_html=True)
