import streamlit as st 

import pandas as pd 
import numpy as np 
import base64 

# Utils
import os
import joblib 
import json
import pickle
import datetime

from custom_transformers_3.transformer import * 
from utils import *
from templates import *
from Exploratory import ExploratoryAnalysis

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')





@st.cache(allow_output_mutation=True)
def img_to_bytes(img_path):
    with open(img_path, 'rb') as f:
        img_bytes = f.read()
    # img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

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
		st.write('##### Please use the "EDA" button on the sidebar to navigate through a comprehensive analysis of the data')

	with st.expander('Business Questions analysis'):
		
		st.write('The main question this report seeks to investigate is potential discrimination towards age, gender or ethnic groups across the stations and nationwide. To do this we looked at the current distribution of discovery rate of offences in these subgroups and across stations (excluding the ones where the target label couldn’t be attributed). The global discovery rate is at 20% as discussed but it varies greatly across the country.')
		st.image('images/Distribution of discovery rate per station.png','Distribution of discovery rate per station.')
		
		st.write('#### Gender')
		st.write('''In general,  although men are stopped a lot more than women the discovery rate is usually around the same for both groups, i.e, from the stopped people, the same proportion of men and women have been caught committing offences. Nationwide, the percentage of men and women stopped who are actually found to be practising some offence is around 20%.''')
		st.image('images/Global Discovery rate per gender.png','Global Discovery rate per gender.')
		st.write(''' Some stations have higher discovery rates for men like city-of-london, Durham or surrey where the difference for women is around 7-9%.  Other stations report a slightly higher number of discoveries for women like Northumbria or the transport police but the difference is only about 2% compared to men.''')

		st.write('#### Ethnicity')
		st.write('''According to the UK census data from 2011 the frequency of white people in the UK is around 87%, black people around 3% and asians 5%. This is even more evident in Whales, Scotland and Northern Ireland where the representativity of white people surpasses the 95% mark. If we consider all the data it is very clear that black and Asian minorities are overrepresented when compared to census data - 26% for black and 13% for asian. However, when we exclude the metropolitan station get a lot closer to census with 10% for black and 8% for asians only. When analysing the discovery rate, excluding the metropolitan station, we see that the proportion of offences is very similar in all ethnic groups.''')
		st.image('images/Officer defined ethnic groups success rates and other offences rates.png','Officer defined ethnic groups success rates and other offences rates',width=500)
		st.write('''We couldn’t find any obvious evidence in regards to what constitutes our positive class. Within stations we find some the maximum discovery rate discrepancy between ethnic groups to be 22% but the average difference nationwide is 7%.''')
		st.image('images/Nationwide  maximum and average differences per sub groups..png','Nationwide maximum and average differences per sub groups.',width=300)

		st.write('#### Age Range')
		st.write('''People in the age range are stopped at a higher rate and also seem to have a higher discovery rate than the other age groups. However the difference between these 2 metrics perhaps implies that there might be a discrimination issue with this age range.We also noticed that people over 34 have been issued penalties a lot more frequently than the other groups that are more likely to get issued mere caution notices. When looking at the distribution of offences per station it seems that there aren’t significant differences  on all stations.''')
		st.image('images/Age range groups success rate and several other offences rates.png','Age range groups success rate and several other offences rates',width=500)

		st.write('''#### Removal of more than outer clothes''')
		st.write('''It is very infrequent for removal of outer clothing to be done. It is slightly more likely to happen to women than men - 4.1% vs 3,4%. It was interesting to verify that to the people asked to remove more than outer clothing, the discovery rate actually increases to 30%. Addressing the specific question of this being asked to certain females' age groups rather than others, we verify that indeed it is a lot more frequent for women in the range over 34 to be asked to remove outer clothing.''')
		st.image('images/% removal of outer clothing asked to women per age range.png','% removal of outer clothing asked to women per age range.', width=200)

		# outer_cloth=img_to_bytes('images/% removal of outer clothing asked to women per age range.png')
		# st.write(img_html.format({outer_cloth},{'% removal of outer clothing asked to women per age range.png'}),unsafe_allow_html=True)
		# st.markdown('''<figure>
		# 		<img src=data:image/png;base64,{} style= width:40% float: right class='img-fluid'>
		# 		<figcaption style=font-size:11 display: block>% removal of outer clothing asked to women per age range.</figcaption>
		# 	</figure>'''.format(outer_cloth),unsafe_allow_html=True)
	with st.expander('Modeling'):
		st.write('''
		
		The model developed and improved over time will attempt to minimize the discrepancies in discovery rate across the ethnicity, age and gender subgroups. In the data that was made available, we couldn’t identify any major differences in said groups albeit in some particular stations. But evidently, we also do not know which individuals were left unsearched that potentially were breaking the law in some way. With this data, it has been very challenging to unify all stations in a single policy model whilst keeping the identified potentially problematic groups with no discrimination. We would thrive to achieve an overall discovery rate higher than the original data (20%) which would translate into an approximate global 28% success rate. It has been challenging to unify the rates within groups. At the moment our model will yield some significant differences in discovery rate across different stations. The global discovery rate of people that are stopped is expected to be around 26%. We believe that an acceptable difference rate within stations should not exceed 10% within any subgroup but this is proving very difficult to achieve perhaps because the available features are not that representative of particular culprit idiosyncrasies of offenders.  In some cases, we think that we actually have not improved upon the existing stopping criteria, for example in regards to the gender subgroup, but maybe we should, in the future, look to refine the models per station. We tested the best threshold for search and concluded that a good balance is that a person will only be searched if the model yields a 50% likelihood of success. We will be monitoring variables such as maximum and average differences in subgroups nationwide and will attempt to level these metrics with future refinements to the model. In regards to people that should be stopped, i.e., of the people that are actually ‘offending’ it is expectable that we get a high rate of stops around the 0.74 mark. This metric should also vary significantly across the stations. ''')

		st.write("#### Use the 'Modeling' Button on the sidebar to navigate through a detailed perusal of the model achieved")


	






# if __name__ == '__main__':
# 	main()