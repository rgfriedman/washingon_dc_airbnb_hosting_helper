# Washington D.C. Airbnb Hosting Helper

### Author

Rachael Friedman

---

### Executive Summary

Airbnb was started in 2007 and has been disrupting the hospitality industry ever since. Hosts on Airbnb offer unique stays and local experiences for travelers that can't be replicated by a stay in a hotel. According to [their site,](https://news.airbnb.com/about-us/) Airbnb has helped over 4 million hosts welcome over 900 million guests in almost every country around the world. 

According to [SmartAsset's](https://smartasset.com/mortgage/where-do-airbnb-hosts-make-the-most-money) 2020 study on the profit potential of rentals in 15 of the largest Airbnb markets in the US, renting out an entire place or room can be a profitable venture. The average expected annual profit of Airbnb hosts renting out a full two bedroom apartment or house after expenses is $20,619 in the cities studied. For hosts renting out a one room in a two-bedroom home on Airbnb in these cities, they could expect to pay about 81% of their rent from renting on average. 

There is a robust amount of Airbnb information in every major city around the world and I want to use this to help hosts maximize their revenue potential. In this project, I will use my data science skill set to explore and model Airbnb listing data for Washington DC. The goal of this project is to help hosts understand what makes and Airbnb listing the most popular on the DC market and what they could focus on to make their listing more competitive and increase their profits. I will be using listing data from [Inside Airbnb](http://insideairbnb.com/index.html), an independent, non-commercial website that scrapes publicly available listing and review data from Airbnb every month. I will also use the [Foursquare API](https://developer.foursquare.com/) to gather information on type of venues in each neighborhood to get a better idea of the city from a tourist's point of view and see if this impacts the Airbnb listing popularity.

I will create the best binary classification model to predict whether an Airbnb listing in DC will be considered popular or not compared to the current listing competition. In addition to the best predictive model, I will create a highly interpretive model to help hosts understand what features they could improve on their listing to increase popularity. These models will be deployed together an app that hosts can use to make their listings as strong as possible.

---

### Folder Directory

The folder directory is descirbed below. 

Folder|Description|
|---|---|
|app|all things related to the final Streamlit app|
|code|this includes notebooks for all steps in the modeling process, starting with data cleaning and ends with final models|
|data|includes the data used for this project, starting with initial versions and iterating through to final versions|
|models|this is where all pickled information needed for modeling in the Streamlit app is stored|
|presentation.pdf|a PDF version of the slide presentation for this project|

---

### Datasets

The datasets included in the [`data`](./data) folder were used for this project and described below. 

* [`cleaned_numerical_df.csv`](./data/cleaned_numerical_df.csv): cleaned numerical data as a step in the data cleaning process
* [`final_df.csv`](./data/final_df.csv): the final version of cleaned data used in modeling
* [`listings.csv.gz`](./data/listings.csv.gz): the original Airbnb listing data 
* [`neighborhood_venues.csv`](./data/neighborhood_venues.csv): data on number and types of venues in each DC neighborhood pulled from the Foursquare API

---

### Data Dictionary (Full Dataset)

This is the data dictionary for the final data (final_df.csv) used in modeling.

|Feature|Type|Description|
|---|---|---|
|id|int|listing id| 
|name|string|name of listing| 
|description|string|listing description| 
|neighborhood_overview|string|neighborhood description on listing|
|host_id|int|host id| 
|host_about|string|about the host text on listing|
|host_response_time|string|how long it takes the host to respond| 
|host_response_rate|float|the rate at which the host responds|
|host_acceptance_rate|float|the rate at which the host accepts booking requests| 
|host_is_superhost|int|whether or not the host is a super host|
|host_has_profile_pic|int|whether or not the host has a profile picture| 
|host_identity_verified|int|whether or not the host's identity has been verified|
|neighbourhood_cleansed|string|the Washington DC neighborhood where the listing is located| 
|latitude_x|float|latitude coordinate for listing location|
|longitude_x|float|longitude coordinate for listing location|
|room type|string|the listing's room type|
|accommodates|int|how many people the listing accommodates|
|bathrooms|float|number of bathrooms in the listing|
|bedrooms|float|number of bedrooms in the listing|
|beds|float|number of beds in the listing|
|amenities|list|list of all amenities included for listing|
|price|float|current daily price of listing|
|minimum nights|int|current minimum night stays for the listing|
|maximum_nights|int|current maximum night statys for the listing|
|minimum_nights_avg_ntm|float|the average minimum_nights value from the calendar (looking 365 nights in the future)|
|maximum_nights_avg_ntm|float|the average maximum_nights value from the calendar (looking 365 nights in the future)|
|availability_30|int|availability of the listing 30 days in the future|
|availability_60|int|availability of the listing 60 days in the future|
|availability_90|int|availability of the listing 90 days in the future|
|availability_365|int|availability of the listing 365 days in the future|
|instant_bookable|int|whether or not the listing is instantly bookable|
|calculated_host_listings_count|int|number of total listings the host has|
|historic site|int|number of historic sites in the DC neighborhood|
|museum|int|number of museums in the neighborhood|
|metro|int|number of metro stations in the neighborhood|
|music venue|int|number of music venues in the neighborhood|
|perfomring arts venue|int|number of perfomring arts venues in the neighborhood|
|college and university|int|number of college and university buildings in the neighborhood|
|food|int|number of places to get food in the neighborhood|
|nightlife spot|int|number of nightlife spots in the neighborhood|
|outdoors and recreation|int|number of outdoors and recreation spots in the neighborhood|
|government building|int|number of government buildings in the neighborhood|
|clothing store|int|number of clothing stores in the neighborhood|
|popular|int|the target variable, whether or not the listing is popular|
|days_being_host|int|number of days the host has been in business|
|days_since_first_review|int|number of days since the first review of the listing|
|days_since_last_review|int|number of days since the last review of the listing|
|name_word_count|int|how many words the listing name contains|
|name_neutral_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the name text that are neutral in sentiment|
|name_negative_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the name text that are negative in sentiment|
|name_positive_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the name text that are positive in sentiment|
|name_compound_sentiment|float|VADER sentiment analysis score, the normalized and weighted composite score for sentiment|
|description_word_count|int|how many words the listing description contains|
|description_neutral_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the description text that are neutral in sentiment|
|description_negative_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the description text that are negative in sentiment|
|description_positive_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the description text that are positive in sentiment|
|description_compound_sentiment|float|VADER sentiment analysis score, the normalized and weighted composite score for sentiment|
|neighborhood_overview_word_count|int|how many words the listing neighborhood overview contains|
|neighborhood_overview_neutral_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the neighborhood overview text that are neutral in sentiment|
|neighborhood_overview_negative_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the neighborhood overview text that are negative in sentiment|
|neighborhood_overview_positive_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the neighborhood overview text that are positive in sentiment|
|neighborhood_overview_compound_sentiment|float|VADER sentiment analysis score, the normalized and weighted composite score for sentiment|
|host_about_word_count|int|how many words the listing host about text contains|
|host_about_neutral_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the host about text that are neutral in sentiment|
|host_about_negative_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the host about text that are negative in sentiment|
|host_about_positive_sentiment|float|VADER sentiment analysis score, the ratio for proportions of the host about text that are positive in sentiment|
|host_about_compound_sentiment|float|VADER sentiment analysis score, the normalized and weighted composite score for sentiment|
|wifi|int|whether or not the listing has wifi as an amenity|
|smoke alarm|int|whether or not the listing has a smoke alarm as an amenity|
|essentials|int|whether or not the listing has essentials as an amenity|
|heating|int|whether or not the listing has heating as an amenity|
|air conditioning|int|whether or not the listing has air conditioning as an amenity|
|hangers|int|whether or not the listing has hangers as an amenity|
|iron|int|whether or not the listing has an iron as an amenity|
|kitchen|int|whether or not the listing has a kitchen as an amenity|
|long term stays allowed|int|whether or not the listing has long term stays allowed as an amenity|
|hair dryer|int|whether or not the listing has a hair dryer as an amenity|
|carbon monoxide alarm|int|whether or not the listing has a carbon monoxide alarm as an amenity|
|hot water|int|whether or not the listing has hot water as an amenity|
|shampoo|int|whether or not the listing has shampoo as an amenity|
|dedicated workspace|int|whether or not the listing has a dedicated workspace as an amenity|
|dishes and silverware|int|whether or not the listing has dishes and silverware as an amenity|
|microwave|int|whether or not the listing has a microwave as an amenity|
|washer|int|whether or not the listing has a washer as an amenity|
|dryer|int|whether or not the listing has a dryer as an amenity|
|fire extinguisher|int|whether or not the listing has a fire extinguisher as an amenity|
|refrigerator|int|whether or not the listing has a refrigerator as an amenity|
|coffee maker |int|whether or not the listing has a coffee maker as an amenity|
|cooking basics|int|whether or not the listing has cooking basics as an amenity|
|private entrance|int|whether or not the listing has a private entrance as an amenity|
|bed linens|int|whether or not the listing has bed linens as an amenity|
|stove|int|whether or not the listing has a stove as an amenity|
|oven|int|whether or not the listing has an oven as an amenity|
|free street parking|int|whether or not the listing has free street parking as an amenity|
|dishwasher|int|whether or not the listing has a dishwasher as an amenity|
|first aid kit|int|whether or not the listing has a first aid kit as an amenity|
|extra pillows and blankets|int|whether or not the listing has extra pillows and blankets as an amenity|
|tv|int|whether or not the listing has a tv as an amenity|
|patio or balcony|int|whether or not the listing has a patio or balcony as an amenity|

---

### Methodology 

I used the Washington D.C. listing data dump from [Inside Airbnb](http://insideairbnb.com/index.html) and collected neighborhood venu information through [Foursquare's API](https://developer.foursquare.com/). The raw listing data had about 8,000 entries with 74 features and this was combined with venue information for the 39 D.C. neighborhoods in the dataset. 

Once the neighborhood venue and listing datasets were combined, I started on data cleaning. The first thing I did was filter the dataset to only contain recent listings. This is defined as a listing having a review in the past 12 months. Although this cut the datset in half to 3,666 listings, this decision was made to gather the most accurate information on the DC Airbnb market right now. As I am looking to predict the most popular listings on the current market, listings on the site that are not acctive could confuse the predictions and make it less accurate. This is also in line with the way Airbnb shows listings on their site, they prioritize listings with the current reviews from the past year.

The next did was to explore the ratings and number of reviews below to come up with criteria for the popular target variable below. When looking at the distributions of ratings, it is clear that DC airbnbs are all pretty high quality. For example, 3,508 airbnbs (96%) in the data have an overall rating above a 4. I will look into different percentiles to see which should be used as a threshhold to help indicate popularity. I needed to find a threshhold to indicate the most popular listings. In this case, I decided that to be considered popular in DC, it seems an overall rating close to 4.85 (the 50th percentile) is reasonable, whereas the 4.9 rating may be too high. I will be using a rating of 4.8 as part of the metric to calculate popularity. 

For the other part of the popularity metric, I chose criteria for number of reviews needed to be considered a popular listing based off of the percentile information in my data exploration. In this case the 70th percentile for number of reviews is 70, so I stayed around this number and selected 60 reviews which sound reasonable to considered one of the most popular listings. Now, I had my popularity criteria for the DC market set in place. There are 815 listings that have a rating of at least 4.8 and 60 or more reviews which are considered to be the most popular listings in the dataset. I added my target variable, popular, to the dataset and labeled the listings accordingly based on this criteria. I then removed the number of ratings and rating scores from the data set to ensure there is no data leakage that will affect the predictions. 

For the rest of the data cleaning, I went through all variables in the dataset. Besides the text fields, I made sure there were no nulls and filled them with 0, the mean, or unknown when appropriate. I removed all outliers and transformed data when needed. I also did exploratory data analysis on all variables in another notebook. For the text fields, I ran a sentiment analysis and count of words for each field to act as features in the dataset.

For my modeling process, I built the best predictive model possible using an Extra Trees Classifier and a best model for interpretation using Logistic Regression. The best predictive model was used to predict the most accurate result for the listing and used an Extra Trees Classifier and oversampling the minority class (popular). The interpretative model gave me coefficient values from Logistic Regression that I used to make reccomendations and understand which features are most important for listing popularity (most reviews and highest ratings). I tested many other types of classification models to ensure I was choosing the best one. 

The metrics I focused on to select both of these final models were the accuracy and precision scores. To choose the best model, I was looking for the accuracy scores for both training and testing data to be consistent and high to explain as much variance as possible. I also chose to optimize the precision score (true positives over all predicted positives), because in this specific case it is worse to tell a host that their listing will be popular if it is actually not.

---

### Conculsions and Recommendations

After reflecting on my model, I was curious why the model including the most variables (kitchen sink model) is the best model for my data. The majority of these features are dummy variables (whether or not a listing has an amenity or is in a certain neighborhood) and do not have a lot of correlation with each other. The Extra Trees Classifier does very well with sorting through this type of informaiton and deciding what is noise and what effects the prediction. It could be that all of these binary features together were needed for the extra trees model to be more informative so the model features did not need to be paired down.

My best predictive model is the Extra Trees Classifier with the default paramter combined with oversampling the minority class. The model's accuracy score on testing data is 85%, showing that the model explains 85% of the variance of the data. Also, the precision score is 81% which is the highest we have seen in all the models. My best interpretative is Logistic Regression with default parameters and using Standard Scaler on the data before modeling. This models' accuracy score is 84%, meaning it accounts for 84% of the variance in the data, and the precision score is 69%. The coefficients from this model were used to make reccomendations to users on what features would increase their odds of having a popular listing. For example, the 5 largest coefficients for this model are days since first review, being a super host, how many guests the listing accommodates, the neutral sentiment of the listing description, and dishes and silverware as an amenity. Some of these a host may not be able to change such as days since first review or how many guests the listing accommodates, however it is nice to still know that an increase in these features can increase the odds of the listing being popular. As for the other coefficients, I can recommend to hosts to become a super host, include a listing description with neutral sentiment, and have dishes and silverware as an amenity if they are not already doing so and this will increase their odds of having a popular listing. 

Overall, these model scores improve upon the baseline and I am happy with this as the final model for production and think it will be useful for hosts. However, I was curious why the metrics were hovering in the low to mid 80s and I could not improve on the baseline more and realized it may be due to the data itself. The characteristics in listings that are not popular and popular may not have that distinct of differences in their features and so the models can only do so much with this situaion. In the exploratory data analysis phase of this project, we learned that most airbnb listings are all rated pretty highly so this may be the case. This is an important finding to keep in mind to understand the results. 

There are a couple of limitations for these models. The first is addressed above, that there may not be enough differentiatio between the two classes to improve upon the baseline score with unbalanced classes too much. Second, the popularity metric is not a perfect metric because longer stays will have fewer reviews which is a limitation. However, according to [IPropertyManagement](https://ipropertymanagement.com/research/airbnb-statistics), a site that has conducted research on Airbnb listings worldwide, the average stay in an Airbnb is 4.3 nights. With this information, I can say that popularity metric should be representative of the average stay in DC but we should keep in mind the limitation. Lastly, it would have been nice to have more data to analyze if so many of the listings in the data were not outdated (not used in the past 12 months) and had to be removed. If there were more time, I would recommend gathering more data to evaulauate. It would be interesting to test models using different threshholds to calculate the popularity of listings and seeing if these yielded any better results. Also, I would have liked to explore the possibility of predicting popularity rankings and not just a binary class. 

My recommendations for hosts is that this application can be used as a helpful tool to evaluate your listing. There are a lot of apps out there to help hosts predict the price for their listing, but not a lot that are looking at what helps to make a listing popular in the first place. This application will return any features in your listing that you can add to increase the odds of the listing being popular. This app will help hosts improve their listing to be more popular on the market which should increase their profits. 