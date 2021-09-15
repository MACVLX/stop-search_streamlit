import streamlit as st 

import pandas as pd 
import numpy as np 


# Utils
import os
import joblib 
import json
import pickle
import datetime

from custom_transformers_3.transformer import * 
from utils import *
from Exploratory import ExploratoryAnalysis

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

from templates import *

@st.cache
def load_train_df():
	URL = 'https://storage.googleapis.com/capstone4ldsaa/train.csv'
	df = pd.read_csv(URL)
	
	return df



def EDA():
    st.markdown(html_temp.format('Exploratory Analysis'),unsafe_allow_html=True)
      
    try:
        with st.spinner('Loading data....'):
            df = load_train_df()				
    except:
        st.error('csv file upload error')
    else:
        EA = ExploratoryAnalysis(df)
        st.sidebar.markdown('#### Exploratory analysis')
        features=st.sidebar.radio("",['Overview','Data entry issues','Unique values and frequency',  'Gender, Ethnicity and Age', 'Lat & Long'])

        if features == 'Overview':
            st.subheader('Dataframe first rows:')
            st.write(df.head(20))
            st.markdown("For the task at hand, the IT Department has made available a dataset comprising 660 661 stop and search events spread throughout the country. This dataset is composed of features that can be used for modelling -  'Type', 'Date', 'Part of a policing operation', 'Latitude', 'Longitude', 'Gender', 'Age range', 'Self-defined ethnicity', 'Officer-defined ethnicity', 'Legislation','Object of search', 'station' - by features which will be used to build a classification target given there isn’t a specific ‘target’ or ‘ label’ feature - 'Outcome', 'Outcome linked to object of search' - and by the feature  'Removal of more than just outer clothing',  to be used in the analysis only. As previously mentioned a search is considered successful if the outcome is positive and is related to the search. Except for ‘Latitude’ and ‘Longitude’, all the others are categorical variables.")
        
            st.subheader('Dataframe informations:')
            st.text(EA.info())

        elif features == 'Unique values and frequency':
            col = st.selectbox('Choose a column for see unique values',EA.columns)
            st.subheader('Unique values and frequency')
            st.write(EA.info2(col))

        elif features == 'Data entry issues':
            st.write('Data entry issues')
            st.image('images/overhaul_nulls.png')
            st.markdown('There seems to be some issues regarding data entries although in general most of the dataset is quite well populated. Maybe not surprisingly, the London metropolitan station accounts for more than 50% of all the data points in this dataset.')
            st.markdown('In regards to missing data across all stations, the columns ‘Outcome linked to object of search’ and ‘Removal of more than just outer clothing’ are the most affected')
            st.image('images/%_nulls.png')
            st.markdown("A more granular analysis by police station allows for in depth appraisal of the reality of record keeping per  station (Annex 3). Some stations are top exemplar  - essex, suffolk, sussex, northamptonshire, norfolk and gloucester - with near 0% of data missing whereas other stations like thames-valley, lancashire and dyfed-powys have severe data keeping records with more than 30% of data missing, particularly in respect to geolocation, information if it was part of police operation and the two above mentioned categories. The most severe issue pertaining to missing data is related to the feature ‘Outcome linked to object of search’ in the metropolitan station. There is no data at all, which will disallow these data points to be included in any modelling attempt and impair any statistical analysis related to outcome in this important area of the country. The station gwent and humberside also have no data in this feature. Another worrying fact related to this project is the almost entire lack of report regarding the removal of outer clothing. Some stations like gwent, cleveland, north-yorkshire, metropolitan and surrey do not report this information  at all and many others have less than 50% reporting in this category. For some columns it makes sense to infer the missing data, for example in ‘Outcome linked to object of search’ any missing values are most likely to be False since officers tend to forget to go back to the application.There seems to be a substantial amount of records where ‘Outcome’ is negative but the column ‘Outcome linked to the object of search is True. This indicates potential compromise when training any model as these data points may be of no use. In figure 3 we can clearly see that some stations (warwickshire,btp,west-yorkshire and derbyshire) have more than 50% of observations with this mismatch. As mentioned the features ‘Outcome’ and 'Outcome linked to object of search' will be used to build our target labels for binary classification. The latter is a boolean feature with True or False values. The Outcome feature is a wide range of consequences from arrestas to penalties or mere caution but the vast majority is that no action was taken.  After constructing the target feature we achieve an imbalanced dataset where the positive outcome accounts for approximately 20% of the observations. By removing the stations where the target is not possible to be constructed (metropolitan, gwent and humberside) the  final data set is only 46% of the original data.")

        elif features == 'Gender, Ethnicity and Age':
            st.write("Gender, Ethnicity and Age groups distribution of stops can be seen in the chart below. The Gender feature has 3 categories: Female, Male and Other. Given that the representativity of ‘other’ is extremely low in the dataset (less than 0.001%) we will exclude this from our analysis and modelling. There is an over representativity of Male compared to Female. Females account for little more than 8% but if the metropolitan station is removed then it increases slightly to more than 10%. In regards to Ethnic groups we have 2 different features: Officer defined and self-defined. For modelling purposes it only makes sense to use the Officer-defined feature as this is the only information present prior to any decision making. By far the majority is composed of ‘white’ subgroups making white man the most stopped.The age brackets recorded show a majority of young adults between 18 and 34 years old. Possibly of concern is the fact that there are 384 occurrences of children aged less than 10 years old.")
            st.image('images/stops_per_group.png')
            st.write("In regards to ethnicity we also investigated if there was any significant discrepancy between Officer-defined  and self-defined reported values.  Although not significant, it seems that officers tend to dismiss the categories 'Mixed' and 'Other' , distributing them more across 'White' and 'Black' categories")
            st.image('images/Match between self-defined and police-defined ethnicity.png')
        elif features == 'Lat & Long':
            st.subheader('Coordinates of operations')
            # Calculate the timerange for the slider
            
            df=df.rename(columns={'Latitude':'lat','Longitude':'lon'})
            df_coord=df[(~df.lat.isna()) & (~df.lon.isna())]
            # # Calculate the timerange for the slider
            
            df_coord['Date'] = pd.to_datetime(df_coord['Date']).dt.date
            

            min_ts = df_coord['Date'].min()#.date()
            max_ts = df_coord['Date'].max()#.date()
            

            # st.subheader("Inputs")
            min_selection, max_selection = st.slider(
                "Timeline", min_value=min_ts, max_value=max_ts, value=[min_ts, max_ts])
            # # Filter Data based on selection
            st.write(f"Filtering between {min_ts} & {max_ts}")
            time_data = df_coord[
                (df_coord["Date"] >= min_selection) & (df_coord["Date"] <= max_selection)
            ]
            
            st.map(time_data)