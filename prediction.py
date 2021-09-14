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

@st.cache(allow_output_mutation=True)
def load_model():
	with open('columns_RF_opt_2.json') as fh:
		columns = json.load(fh)

	with open('pipeline_RF_opt_2.pickle', 'rb') as fh:
		pipeline = joblib.load(fh)

	with open('dtypes_RF_opt_2.pickle', 'rb') as fh:
		dtypes = pickle.load(fh)

	return columns, pipeline, dtypes



def prediction():
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.subheader("Predictive Analytics")
    with st.form("my_form"):
        id = st.text_input("observation id")
        
        type = st.selectbox("Type",valid_category_map.get('Type'))
        today = datetime.date.today()
        try:
            date = st.date_input("Date",today)
            date = date.strftime("%m/%d/%Y")
        except:
            st.error('Incorrect or missing date.')
        
        Part_policing_operation=st.selectbox('Part of a policing operation',valid_category_map.get('Part of a policing operation'))
        
        latitude = st.number_input("Latitude",format='%8.6f')
        if latitude == 0.0000:
            latitude = None
        
        longitude = st.number_input("Longitude",format='%8.6f')
        if longitude == 0.0000:
            longitude = None
        
        Gender = st.selectbox('Gender',valid_category_map.get('Gender'))
        Age_range = st.selectbox('Age range',valid_category_map.get('Age range'))
        Officer_defined_ethnicity=st.selectbox('Officer-defined ethnicity',valid_category_map.get('Officer-defined ethnicity'))
        Legislation=st.selectbox('Legislation',valid_category_map.get('Legislation'))
        Object_search=st.selectbox('Object of search',valid_category_map.get('Object of search'))
        station=st.selectbox('station',valid_category_map.get('station'))

        # Every form must have a submit button.
        submitted = st.form_submit_button("Advice")
        if submitted:
            columns, pipeline, dtypes = load_model()
            observation = {
                'Type': type,
                'Date': date,
                'Part_policing_operation': Part_policing_operation,
                'Latitude' : latitude,
                'Longitude' : longitude,
                'Gender' : Gender,
                'Age range' : Age_range,
                'Officer-defined ethnicity' : Officer_defined_ethnicity,
                'Legislation' : Legislation,
                'Object of search' : Object_search,
                'station' : station
            }


            obs = pd.DataFrame([observation], columns=columns).astype(dtypes)
            proba = pipeline.predict_proba(obs)[0, 1]

            proba
            prediction = pipeline.predict(obs)[0]
            if prediction == True:
                st.markdown(result_true,unsafe_allow_html=True)
            else:
                st.markdown(result_false,unsafe_allow_html=True) 