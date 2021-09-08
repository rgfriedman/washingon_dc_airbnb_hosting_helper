import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from nltk.corpus import stopwords
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer

#title and info for whole app
st.title('Washington DC Airbnb Hosting Helper')
st.write('Use this app to predict if your Airbnb listing will be one of the most popular listings in the current Washington DC market and get recommendations on how to increase its popularity.')

st.image('./app/dc.jpg', caption='Photo by Andy He on Unsplash')

#set app pages
page = st.sidebar.selectbox(
    'Select a page:',
    ('Prediction and Recommendations', 'About', 'Explore DC Airbnb Data'))

if page == 'Prediction and Recommendations':
    st.write('Input information below about your current listing to generate a prediction and recommendations. Please fill out as many fields as possible.')

    st.write('Listing overview')

    name = st.text_input('Listing name:',
        value=' ')

    description = st.text_input('Listing description:',
        value=' ')

    neighborhood_overview = st.text_input('Neighborhood overview in listing:',
        value=' ')

    st.write('Host Information')

    host_about = st.text_input('About the host in listing:',
        value=' ')

    #process text entry

    tokenizer = RegexpTokenizer(r'\w+')

    sentiment = SentimentIntensityAnalyzer()

    #name text
    name = name.lower()
    name = ' '.join(tokenizer.tokenize(name))
    name_word_count = len(list(name.split(' ')))
    name_neutral_sentiment = sentiment.polarity_scores(name)['neu']
    name_negative_sentiment = sentiment.polarity_scores(name)['neg']
    name_positive_sentiment = sentiment.polarity_scores(name)['pos']
    name_compound_sentiment = sentiment.polarity_scores(name)['compound']

    #description text
    description = description.lower()
    description = ' '.join(tokenizer.tokenize(description))
    description_word_count = len(list(description.split(' ')))
    description_neutral_sentiment = sentiment.polarity_scores(description)['neu']
    description_negative_sentiment = sentiment.polarity_scores(description)['neg']
    description_positive_sentiment = sentiment.polarity_scores(description)['pos']
    description_compound_sentiment = sentiment.polarity_scores(description)['compound']

    #neighborhood_overview text
    neighborhood_overview = neighborhood_overview.lower()
    neighborhood_overview = ' '.join(tokenizer.tokenize(neighborhood_overview))
    neighborhood_overview_word_count = len(list(neighborhood_overview.split(' ')))
    neighborhood_overview_neutral_sentiment = sentiment.polarity_scores(neighborhood_overview)['neu']
    neighborhood_overview_negative_sentiment = sentiment.polarity_scores(neighborhood_overview)['neg']
    neighborhood_overview_positive_sentiment = sentiment.polarity_scores(neighborhood_overview)['pos']
    neighborhood_overview_compound_sentiment = sentiment.polarity_scores(neighborhood_overview)['compound']

    #host text
    host_about = host_about.lower()
    host_about = ' '.join(tokenizer.tokenize(host_about))
    host_about_word_count = len(list(host_about.split(' ')))
    host_about_neutral_sentiment = sentiment.polarity_scores(host_about)['neu']
    host_about_negative_sentiment = sentiment.polarity_scores(host_about)['neg']
    host_about_positive_sentiment = sentiment.polarity_scores(host_about)['pos']
    host_about_compound_sentiment = sentiment.polarity_scores(host_about)['compound']

    #mapping values for yes no quesitons
    yes_no_map = {'Yes':1, 'No':0}

    host_is_superhost = st.radio('Are you a super host?',
    ['Yes', 'No'])
    host_is_superhost = yes_no_map[host_is_superhost]

    host_has_profile_pic = st.radio('Do you have a profile picture?',
    ['Yes', 'No'])
    host_has_profile_pic = yes_no_map[host_has_profile_pic]

    host_identity_verified = st.radio('Is your identity is verified?',
    ['Yes', 'No'])
    host_identity_verified = yes_no_map[host_identity_verified]

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


    response_time_list = pickle.load(open('./models/response_time_list.pkl','rb'))

    host_response_time= st.selectbox('What is your response time?',
    sorted(response_time_list))

    st.write('Listing details')

    neighborhood_list = pickle.load(open('./models/neighborhood_list.pkl','rb'))

    neighbourhood_cleansed = st.selectbox('Select the neighborhood where your listing is located:',
        sorted(neighborhood_list))

    room_type_list = pickle.load(open('./models/room_type_list.pkl','rb'))

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

    st.write('Please select all emenities that your listing offers:')

    #set up amenities offered, change input into int
    wifi = st.checkbox('wifi')
    wifi= int(wifi)
    smoke_alarm	= st.checkbox('smoke alarm')
    smoke_alarm= int(smoke_alarm)
    essentials	= st.checkbox('essentials')
    essentials = int(essentials)
    heating	= st.checkbox('heating')
    heating = int(heating)
    air_conditioning	= st.checkbox('air conditioning')
    air_conditioning = int(air_conditioning)
    hangers	= st.checkbox('hangers')
    hangers = int(hangers)
    iron	= st.checkbox('iron')
    iron = int(iron)
    kitchen	=  st.checkbox('kitchen')
    kitchen = int(kitchen)
    long_term_stays_allowed	= st.checkbox('long term stays allowed')
    long_term_stays_allowed = int(long_term_stays_allowed)
    hair_dryer	= st.checkbox('hair dryer')
    hair_dryer = int(hair_dryer)
    carbon_monoxide_alarm	= st.checkbox('carbon monoxide alarm')
    carbon_monoxide_alarm = int(carbon_monoxide_alarm)
    hot_water	= st.checkbox('hot water')
    hot_water = int(hot_water)
    shampoo	= st.checkbox('shampoo')
    shampoo = int(shampoo)
    dedicated_workspace	= st.checkbox('dedicated workspace')
    dedicated_workspace = int(dedicated_workspace)
    dishes_and_silverware	= st.checkbox('dishes and silverware')
    dishes_and_silverware = int(dishes_and_silverware)
    microwave	= st.checkbox('microwave')
    microwave = int(microwave)
    washer	= st.checkbox('washer')
    washer = int(washer)
    dryer	= st.checkbox('dryer')
    dryer = int(dryer)
    fire_extinguisher	= st.checkbox('fire extinguisher')
    fire_extinguisher = int(fire_extinguisher)
    refrigerator	= st.checkbox('refrigerator')
    refrigerator = int(refrigerator)
    coffee_maker	= st.checkbox('coffee maker')
    coffee_maker = int(coffee_maker)
    cooking_basics	= st.checkbox('cooking basics')
    cooking_basics = int(cooking_basics)
    private_entrance	= st.checkbox('private entrance')
    private_entrance = int(private_entrance)
    bed_linens	= st.checkbox('bed linens')
    bed_linens = int(bed_linens)
    stove	= st.checkbox('stove')
    stove = int(stove)
    oven	= st.checkbox('oven')
    oven = int(oven)
    free_street_parking	= st.checkbox('free street parking')
    free_street_parking = int(free_street_parking)
    dishwasher	= st.checkbox('dishwasher')
    dishwasher = int(dishwasher)
    first_aid_kit	= st.checkbox('first aid kit')
    first_aid_kit = int(first_aid_kit)
    extra_pillows_and_blankets	= st.checkbox('extra pillows and blankets')
    extra_pillows_and_blankets = int(extra_pillows_and_blankets)
    tv	= st.checkbox('tv')
    tv = int(tv)
    patio_or_balcony= st.checkbox('patio or balcony')
    patio_or_balcony= int(patio_or_balcony)

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
        min_value = 0.0,
        step= 0.1)

    maximum_nights_avg_ntm = st.number_input(
        "What's the average maximum number of nights required to stay at this listing looking 365 nights into the future? (full calendar rules may differ)",
        min_value = 0.0,
        step= 0.1)

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

    instant_bookable = st.radio('Is the listing is instantly bookable?',
    ['Yes', 'No'])
    instant_bookable = yes_no_map[instant_bookable]

    instant_bookable = int(instant_bookable)

    days_since_first_review =st.number_input(
        "How many days has it been since the listing received its first review?",
        min_value = 0,
        step= 1)

    days_since_last_review =st.number_input(
        "How many days has it been since the listing received its most recent review?",
        min_value = 0,
        step= 1)

    #venue Information

    neighborhood_venues = pickle.load(open('./models/neighborhood_venues.pkl','rb'))

    historic_site = neighborhood_venues.get('historic site',{}).get(neighbourhood_cleansed)
    museum = neighborhood_venues.get('museum',{}).get(neighbourhood_cleansed)
    metro = neighborhood_venues.get('metro',{}).get(neighbourhood_cleansed)
    music_venue	= neighborhood_venues.get('music venue',{}).get(neighbourhood_cleansed)
    perfomring_arts_venue = neighborhood_venues.get('perfomring arts venue',{}).get(neighbourhood_cleansed)
    college_and_university	= neighborhood_venues.get('college and university',{}).get(neighbourhood_cleansed)
    food = neighborhood_venues.get('food',{}).get(neighbourhood_cleansed)
    nightlife_spot	= neighborhood_venues.get('nightlife spot',{}).get(neighbourhood_cleansed)
    outdoors_and_recreation	= neighborhood_venues.get('outdoors and recreation',{}).get(neighbourhood_cleansed)
    government_building	= neighborhood_venues.get('government building',{}).get(neighbourhood_cleansed)
    clothing_store = neighborhood_venues.get('clothing store',{}).get(neighbourhood_cleansed)

    #sanitize user inputs

    #load one hot encoder
    enc = pickle.load(open('./models/enc.pkl','rb'))

    normal_input = np.array([host_response_rate, host_acceptance_rate,	host_is_superhost,	host_has_profile_pic,
    	host_identity_verified, accommodates, bathrooms, bedrooms,	beds,	price,	minimum_nights,	maximum_nights,
        minimum_nights_avg_ntm,	maximum_nights_avg_ntm,	availability_30, availability_60,
        availability_90, availability_365, instant_bookable, calculated_host_listings_count, historic_site,	museum,
        metro,	music_venue, perfomring_arts_venue,	college_and_university,	food, nightlife_spot,
        outdoors_and_recreation, government_building,	clothing_store,	days_being_host, days_since_first_review,
        days_since_last_review,	name_word_count,	name_neutral_sentiment,	name_negative_sentiment,
        name_positive_sentiment, name_compound_sentiment,	description_word_count,	description_neutral_sentiment,
        description_negative_sentiment,	description_positive_sentiment,	description_compound_sentiment,	neighborhood_overview_word_count,
        neighborhood_overview_neutral_sentiment,	neighborhood_overview_negative_sentiment,	neighborhood_overview_positive_sentiment,
        neighborhood_overview_compound_sentiment,	host_about_word_count,	host_about_neutral_sentiment,	host_about_negative_sentiment,
        host_about_positive_sentiment, host_about_compound_sentiment,	wifi,	smoke_alarm, essentials, heating, air_conditioning,
        hangers, iron,	kitchen, long_term_stays_allowed,	hair_dryer,	carbon_monoxide_alarm,	hot_water,	shampoo,
        dedicated_workspace,	dishes_and_silverware,	microwave,	washer,	dryer,	fire_extinguisher,	refrigerator,
        coffee_maker,	cooking_basics,	private_entrance,	bed_linens,	stove,	oven,	free_street_parking,	dishwasher,
        first_aid_kit,	extra_pillows_and_blankets,	tv,	patio_or_balcony])

    #use one hot encoder on categorical varialbes
    ohe_cats = np.array([host_response_time, neighbourhood_cleansed, room_type]).reshape(1,-1)[0]
    ohe_cats = enc.transform(ohe_cats.reshape(1,-1))[0]

    #combine user input into one
    user_input = np.hstack([normal_input, ohe_cats])

    #load model
    et = pickle.load(open('./models/et.pkl','rb'))

    #Make a Prediction
    pred = []

    pred = et.predict(user_input.reshape(1,-1))

    #click button to generate prediction and recommendations
    if st.button('Make popularity prediction'):
        if pred == [1]:
            st.write('Great work! This lisitng is predicted to be popular on the Washington DC Airbnb market.')
            st.write('Here are some recommendations to add to your listing that will help it stay popular:')

            if instant_bookable==0:
                st.write('- Make listing instantly bookable')

            if host_is_superhost ==0:
                st.write('- Become a super host')

            if host_has_profile_pic==0:
                st.write('- Add a profile picture')

            if host_identity_verified==0:
                st.write('- Verify your identity on Airbnb')

            if host_acceptance_rate<.7:
                st.write('- Increase your acceptance rate for guests')

            if host_about_word_count<2:
                st.write('- Add a host about section')

            if (host_about_word_count >1) & (host_about_positive_sentiment< 0.03):
                st.write('- Add more positive language to your about the host section')

            if (host_about_word_count>1) & (host_about_neutral_sentiment<.4):
                st.write('- Add more neutral language to your about the host section')

            if description_word_count<2:
                st.write('- Add a listing description')

            if (description_word_count>1) & (description_neutral_sentiment<.4):
                st.write('- Add more neutral language to your listing description')

            if (description_word_count>1) & (description_positive_sentiment<0.03):
                st.write('- Add more positive language to your listing description')

            if neighborhood_overview_word_count<2:
                st.write('- Add a neighborhood overview section')

            if (neighborhood_overview_word_count>1) & (neighborhood_overview_positive_sentiment<0.03):
                st.write('- Add more positive language to your neighborhood overview section')

            if name_word_count<2:
                st.write('- Add a listing name')

            if (name_word_count>1) & ( name_positive_sentiment<0.03):
                st.write('- Add more positive language to your listing name')

            if dishes_and_silverware==0:
                st.write('- Add dishses and silverware as an amenity')

            if smoke_alarm==0:
                st.write('- Add a smoke alarm as an amenity')

            if hair_dryer==0:
                st.write('- Add a hair dryer as an amenity')

            if carbon_monoxide_alarm==0:
                st.write('- Add a carbon monoxide alarm as an amenity')

            if iron ==0:
                st.write('- Add an iron as an amenity')

            if hangers == 0:
                st.write('- Add hangers as an amenity')

            if first_aid_kit==0:
                st.write('- Add a first aid kit as an amenity')

            if stove==0:
                st.write('- Add a stove as an amenity')

            if hot_water==0:
                st.write('- Add hot water as an amenity')

            if dedicated_workspace==0:
                st.write('- Add a dedicated workspace as an amenity')

            if bed_linens==0:
                st.write('- Add bed linens as an amenity')

            if refrigerator==0:
                st.write('- Add a refrigerator as an amenity')

            if shampoo==0:
                st.write('- Add a shampoo as an amenity')

            if coffee_maker==0:
                st.write('- Add a coffee maker as an amenity')

            if free_street_parking==0:
                st.write('- Add a free parking as an amenity')

            if dishwasher==0:
                st.write('- Add a dishwasher  as an amenity')

            if wifi==0:
                st.write('- Add a wifi as an amenity')


        elif pred == [0]:
            st.write('This lisitng is not predicted to be one of the most popular on the Washington DC Airbnb market.')
            st.write('Here are some recommendations to add to your listing to increase its chance of being popular:')

            if instant_bookable==0:
                st.write('- Make listing instantly bookable')

            if host_is_superhost ==0:
                st.write('- Become a super host')

            if host_has_profile_pic==0:
                st.write('- Add a profile picture')

            if host_identity_verified==0:
                st.write('- Verify your identity on Airbnb')

            if host_acceptance_rate<.7:
                st.write('- Increase your acceptance rate for guests')

            if host_about_word_count<2:
                st.write('- Add a host about section')

            if (host_about_word_count >1) & (host_about_positive_sentiment< 0.03):
                st.write('- Add more positive language to your about the host section')

            if (host_about_word_count>1) & (host_about_neutral_sentiment<.4):
                st.write('- Add more neutral language to your about the host section')

            if description_word_count<2:
                st.write('- Add a listing description')

            if (description_word_count>1) & (description_neutral_sentiment<.4):
                st.write('- Add more neutral language to your listing description')

            if (description_word_count>1) & (description_positive_sentiment<0.03):
                st.write('- Add more positive language to your listing description')

            if neighborhood_overview_word_count<2:
                st.write('- Add a neighborhood overview section')

            if (neighborhood_overview_word_count>1) & (neighborhood_overview_positive_sentiment<0.03):
                st.write('- Add more positive language to your neighborhood overview section')

            if name_word_count<2:
                st.write('- Add a listing name')

            if (name_word_count>1) & ( name_positive_sentiment<0.03):
                st.write('- Add more positive language to your listing name')

            if dishes_and_silverware==0:
                st.write('- Add dishses and silverware as an amenity')

            if smoke_alarm==0:
                st.write('- Add a smoke alarm as an amenity')

            if hair_dryer==0:
                st.write('- Add a hair dryer as an amenity')

            if carbon_monoxide_alarm==0:
                st.write('- Add a carbon monoxide alarm as an amenity')

            if iron ==0:
                st.write('- Add an iron as an amenity')

            if hangers == 0:
                st.write('- Add hangers as an amenity')

            if first_aid_kit==0:
                st.write('- Add a first aid kit as an amenity')

            if stove==0:
                st.write('- Add a stove as an amenity')

            if hot_water==0:
                st.write('- Add hot water as an amenity')

            if dedicated_workspace==0:
                st.write('- Add a dedicated workspace as an amenity')

            if bed_linens==0:
                st.write('- Add bed linens as an amenity')

            if refrigerator==0:
                st.write('- Add a refrigerator as an amenity')

            if shampoo==0:
                st.write('- Add a shampoo as an amenity')

            if coffee_maker==0:
                st.write('- Add a coffee maker as an amenity')

            if free_street_parking==0:
                st.write('- Add a free parking as an amenity')

            if dishwasher==0:
                st.write('- Add a dishwasher  as an amenity')

            if wifi==0:
                st.write('- Add a wifi as an amenity')

            st.write('Also keep in mind that more bookings and reviews over time will help the listing to become popular. ')

if page == 'About':

    st.subheader('Background')
    st.write("Airbnb was started in 2007 and has been disrupting the hospitality industry ever since. Hosts on Airbnb offer unique stays and local experiences for travelers that can't be replicated by a stay in a hotel. According to a recent study by [SmartAsset](https://smartasset.com/mortgage/where-do-airbnb-hosts-make-the-most-money), hosts in major US cities can expect an annual profit of around $20,000 for renting out a two-bedroom apartment after expenses or can expect to pay about 80% of their rent on average from renting out one room in a two-bedroom place. As the popularity of Airbnb continues, it's clear that renting out an entire place or room can be a profitable venture.")
    st.write("There are a lot of apps out there to help hosts price their listing, but not a lot that look at what helps to make a listing popular in the first place. The goal of this project is to help hosts understand what makes and Airbnb listing the most popular on the DC market and what to focus on to make their listing more competitive and increase their profits.")

    st.subheader('App Overview')
    st.write("My name is Rachael Friedman and I am a data scientist that has created an app for hosts in DC to use to make their listing as strong as possible. Hosts can use this application to generate a prediction on whether their listing will be considered popular on the DC Airbnb market given its features and get suggestions on what to add to the listing to increase popularity.")
    st.write('Popularity in this project is defined as a listing having over a 4.8 overall rating and 60 or more reviews. The data used for this project is collected from [Inside Airbnb](http://insideairbnb.com/index.html) and overlayed with DC venue information from the [Foursquare API](https://developer.foursquare.com/).')

    st.subheader('More Information')
    st.write('Check out the project GitHub repo for more information at [DC Hosting Helper](https://github.com/rgfriedman/Airbnb_listings_capstone).')
    st.write('You can also get in touch with me at [my page](https://rgfriedman.github.io/).')
