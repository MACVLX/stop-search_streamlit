import streamlit as st 

import pandas as pd 
import numpy as np 
import base64 as base64

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



# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# bin_str = get_base64_of_bin_file('images/stopsearch.png')

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     color: white;
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     background-color: white;
#     -webkit-tap-highlight-color: red;
#     -webkit-highlight-color: red;

#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return



# set_png_as_page_bg('images/stopsearch.png')

def main():
	
	
	st.markdown(html_temp.format('Stop & Search UK app'),unsafe_allow_html=True)
	st.sidebar.markdown(footer,unsafe_allow_html=True)
	st.write('')
	st.write('')

	with st.expander('Project Summary'):
		# st.write('#### Summary')
		st.markdown('''Stop and Search operations are an important and controversial component of daily policing strategies in the United Kingdom (UK) recently receiving a fair amount of public criticism. Together with the help of the IT police Department, this project will address these concerns by investigating any evidence of wrongdoing, abuses or discrimination of minority or social sensitive groups by the authorities and will attempt to propose a decision-making model designed to aid police officers in selecting to search only when there is a high likelihood of success. In summary, the two major tasks this enterprise aims to deliver can be summarized in:''')

		
		st.write('''* analysis of a dataset with records from a broad spectrum of police stations across the UK looking for potential evidence of discrimination towards minority groups, gender-related or age-related. Furthermore, we intend to address the highly concerning issue of police officers asking for the removal of more than outer clothing to certain groups, namely if these practices are more frequently applied to women of certain age brackets;''')
		st.write('''* develop a model that can be easily translated into a ‘search vs no search’ advice service regarding potential stops and searches of individuals. The proposed model should be comprehensive and general enough to be applicable to all stations nationwide without significant differences in discovery rates between minority groups.''')
	
	with st.expander('Requirements clarifications'):
		st.write('''The main goal of this project is to yield a model capable of uniformizing the decision to perform searches whilst trying to minimize any bias towards the different ethnic, gender and age groups within a certain police station. 
Although many possible types of offences might be incurred in this project we will frame the task as a  binary classification problem where observations in the training data are considered successful if the outcome is positive, i.e, observations where the model should predict infractions of law are likely to be occurring,  and this outcome is related to the search.
 We are asked to reduce the number of cases where a search does not result in a successful outcome, which, in other words, means that for the same number of people stopped the model should give a higher frequency of positive results. A general measure like accuracy is not suitable for this problem as we are dealing with an imbalanced dataset but this requirement can be translated into an analytic measure such as precision in increasing the discovery rate. However, by maximizing this it is only natural that the ability to dismiss potential offences is increased as well. This should be measured by the sensitivity/recall of the constructed model and a reasonable balance between them must be proposed. These metrics will be used to identify how many stations comply with a tolerance level of discrepancies within each group and each police station and achieve a balance between a unified policy and local possible differences. Ideally, we would seek to get the majority of stations with no more than 5-10% difference of successful discoveries within groups and between stations. 
''')
	with st.expander('Data Analysis'):
		st.write('''For the task at hand, the IT Department has made available a dataset comprising 660 661 stop and search events spread throughout the country.''')
		st.write('##### Please use the "EDA" button on the sidebar on the left to navigate through a comprehensive analysis of the data')






# if __name__ == '__main__':
# 	main()