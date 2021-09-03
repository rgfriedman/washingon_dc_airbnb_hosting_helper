import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier

st.title('Washington D.C. Airbnb Hositing Helper')
st.write('Use this app to predict if your Airbnb listing will be one of the most popular listings in the current Washington D.C. market and get recommendations on how to increase its popularity.')

st.image('./dc.jpg', caption='Photo by Andy He on Unsplash')

page = st.sidebar.selectbox(
    'Select a page:',
    ('About', 'Prediction and Recommendations', 'Explore D.C. Airbnb Data'))

if page == 'About':

    st.write('Summary of project and model')
    st.write('get in touch with me at:')

if page == 'Prediction and Recommendations':
    st.write('Input information below about your current listing to generate a prediction and recommendations.')

    st.write('Listing overview')

    name = st.text_input('Listing name:',
        value='')

    description = st.text_input('Listing description:',
        value='')

    neighborhood_overview = st.text_input('Neighborhood overview in listing:',
        value='')

    st.write('Host Information')

    host_about = st.text_input('About the host in listing:',
        value='')

    host_is_superhost = st.radio('Are you a super host?',
    ['Yes', 'No'])

    host_has_profile_pic = st.radio('Do you have a profile picture?',
    ['Yes', 'No'])

    host_identity_verified = st.radio('Is your identity verified?',
    ['Yes', 'No'])

    days_being_host = st.number_input(
        'How many days have you been a host?',
        min_value = 0,
        step= 1)

    calculated_host_listings_count = st.number_input(
        'How many total listings do you have?',
        min_value = 0,
        step= 1)

    host_response_rate = st.number_input(
        'What is your response rate?',
        min_value = 0.0,
        max_value = 1.0,
        step= 0.1)

    host_acceptance_rate = st.number_input(
        'What is your acceptance rate?',
        min_value = 0.00,
        max_value = 1.00)

    host_response_time= st.radio('What is your response time?',
    ['within an hour', 'within a few hours', 'within a day', 'unknown'])

    st.write('Listing details')
