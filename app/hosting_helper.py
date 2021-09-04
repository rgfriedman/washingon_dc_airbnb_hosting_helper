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

    neighborhood_list = pickle.load(open('../models/neighborhood_list.pkl','rb'))

    neighbourhood_cleansed = st.selectbox('Select the neighborhood where your listing is located:',
        sorted(neighborhood_list))

    room_type_list = pickle.load(open('../models/room_type_list.pkl','rb'))

    room_type = st.selectbox('Select the type of listing:',
        sorted(room_type_list))

    accommodates = st.number_input(
        'How many people does the property accomodate?',
        min_value = 0,
        step= 1)

    bedrooms = st.number_input(
        'How many bedrooms does the listing have?',
        min_value = 0.0,
        max_value = 40.0,
        step= 0.5)

    beds = st.number_input(
        'How many beds does the listing have?',
        min_value = 0,
        max_value = 40,
        step= 1)

    bathrooms = st.number_input(
        'How many bathrooms does the listing have?',
        min_value = 0.0,
        max_value = 20.0,
        step= 0.5)

    price = st.number_input(
        'What is the current daily price?',
        min_value = 0.0,
        max_value = 10_000.0,
        step= 0.01)


    st.write('Calendar information')

    minimum_nights = st.number_input(
        "What's the current minimum number of nights required to stay at this listing?",
        min_value = 0,
        step= 1)

    maximum_nights	= st.number_input(
        "What's the current maximum number of nights required to stay at this listing?",
        min_value = 0,
        step= 1)

    minimum_nights_avg_ntm = st.number_input(
        "What's the average minimum number of nights required to stay at this listing looking 365 nights into the future? (full calendar rules may differ)",
        min_value = 0,
        step= 1)

    maximum_nights_avg_ntm = st.number_input(
        "What's the average maximum number of nights required to stay at this listing looking 365 nights into the future? (full calendar rules may differ)",
        min_value = 0,
        step= 1)

    availability_30	= st.number_input(
        "How many days is this listing currently available to book in the next 30 days?",
        min_value = 0,
        max_value = 30,
        step= 1)

    availability_60	= st.number_input(
        "How many days is this listing currently available to book in the next 60 days?",
        min_value = 0,
        max_value = 60,
        step= 1)

    availability_90	= st.number_input(
        "How many days is this listing currently available to book in the next 90 days?",
        min_value = 0,
        max_value = 90,
        step= 1)

    availability_365 = st.number_input(
        "How many days is this listing currently available to book in the next 365 days?",
        min_value = 0,
        max_value = 365,
        step= 1)

    instant_bookable = st.radio('Is the listing instantly bookable?',
    ['Yes', 'No'])

    days_since_first_review =st.number_input(
        "How many days has it been since the listing received its first review?",
        min_value = 0,
        step= 1)

    days_since_last_review =st.number_input(
        "How many days has it been since the listing received its most recent review?",
        min_value = 0,
        step= 1)
