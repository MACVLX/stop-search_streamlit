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



def modeling():
    
    st.markdown(html_temp.format('Creating the Model'),unsafe_allow_html=True)
    
    features=st.sidebar.radio("Creating the Model",['Model Specs', 'Analysis of outcomes',
     'Alternatives considered', 
    'Knwon issues and risks'])

    if features == 'Model Specs':
        st.write('\n')
        st.write('''
        The proposed model will make use of some features as they are, discard some and use others to perform feature engineering by creating new features. They are all categorical features. The non-categorical features are Latitude and Longitude which correspond to geolocation coordinates. These are not used in the model. Features used: 'Type', 'Date', 'Part of a policing operation', 'Gender',  'Age range', 'station', ‘Legislation’, ‘Object of search’
Features not used: ‘Latitude’, ‘Longitude’, 'Self-defined ethnicity',
Feature Engineering: 
        \n''')
        st.write('\n')
        st.image('images/feature_engineering.png',width=700)
        st.write('''* Consequently, eliminate original features  ‘Date’, ‘Legislation’ and Object of search’
* If ‘fitting’ the model with new training data exclude the samples with value ‘Other’ at feature ‘Gender’ 
 ''')
        st.write('''The prediction of the model is a binary output of true or false for the stop and search to be conducted. To ‘fit’ or train a replication of this model the target feature has to be created. The ‘True’ label occurs when both ‘ Outcome’  and ‘Outcome linked to ‘object of search’ are positive. The model must be able to deal with missing values and categories that were not previously seen by the model on the training set.
Coding of all features categorical values using a one-hot encoding strategy.

The algorithm used is a binary classification, non-linear model  Random Forest with the following general specifications 
''')
        st.write()
        st.write('''* maximum number of branches = 15 
        * number of trees = 100 
        * maximum leaf nodes =10
        * class weight = balanced''')
        st.write('The probability threshold used for predictions is above or equal to 0.5.')

    elif features == 'Analysis of outcomes':
        st.write('\n')
        st.write('''A balance between global discovery rates and global recall has been difficult. With a tolerance of 10% difference between groups, we hope to achieve a global precision of 26% with the current model and a specificity or overhaul recall of about 75%.
 Within the above-mentioned tolerance, we expect the current model to have ¾ of stations being compliant in regards to ethnicity with a maximum difference being 29% but the average below 10%. This difference was observed in the station Cambridgeshire where the number of observations is very small accounting for only 876 samples of the total set. The gender subgroup should also perform relatively well with 32 police stations within the tolerance for discovery rate and a maximum of 18%. The sample size per police station does not seem to have had any impact when considering this group. There is a relatively narrow range of difference 10.5 to 18% when it comes to gender and it does not seem to correlate with the specific sample sizes.
The biggest problem will be the Age group where 32 stations do not comply with the tolerance. Most likely because indeed the 18-34 group is overwhelmingly searched and has a higher discovery rate and the under-10 group is under-represented. However, the global average difference is only 14%. \n
Based on this training set and experiments with the randomized search for hyperparameter tuning we believe it will be very difficult to fulfil all the requirements namely to reduce sub groups potential for bias and achieve a nationwide effective protocol. Maybe a more targeted local approach instead of a unified policy would yield better results but at least the officers would be guided by an auditable model that can be improved over time. 
''')

    elif features == 'Alternatives considered': 
    
        st.write('\n')
        st.write('''Several iterations were tested with different ideas for feature engineering as well as different approaches to model selection and hyperparameter tuning. The optimization process was very focused on a balance between precision and recall both on the type of algorithm as well as on the corresponding parameters. The metric of choice for optimization was AUROC done with a strategy of randomized search. Only then one would test these parameters upon evaluation of our chosen business requirements metrics considering the balance tolerance between false positives and false negatives. We did investigate different decision-making thresholds but in the end, settled for 0.5 probability. 
In regards to the algorithms studied, we tested linear (logistic regression) and non-linear algorithms (Random Forest and Decision Trees) and decided on the Random Forest option although the differences were very subtle. On the feature engineering front, we decided not to use the geo-location data because it was most likely related to the station's location so it would be redundant. We tested without using any feature building from the ‘Date’ feature but the results were not promising. We also attempted cost-sensitive learning on the sci-kit learn library as it is available and had much better results by opting for a balanced class_weight. We did not investigate oversampling of the target data but did try random under-sampling of the majority target class however the results were not better in reducing overhaul discrimination in a number of police stations. Also, the stratification of subgroups was attempted but seemed to impact substantially the occurrence of discrimination on other groups, again in terms of the number of police stations not complying with the 10% tolerance in the difference within groups.''')

    elif features == 'Knwon issues and risks':
            st.write('\n')
            st.write('''We do not expect that the overall precision and recall nationwide to be far from our results in the out-of-sample tests. However, we do see the potential for specific stations to broaden their already established biases. For example, we opted to remove the value ‘other’ in Gender from the training dataset so this could have an impact on the Gender subgroup. On our initial analysis, despite the massive difference in men being stopped, the discovery rate was pretty much the same for both groups. With this model, this might change in some stations.
 The number of features made available does not seem to be giving any particular signals that would be useful to improve on meeting the requirements. Also, the absence of the metropolitan station from the dataset given its data entry issues will probably have a tremendous impact on our modelling as 50% of data in this dataset was not used for modelling. Also, the local demographic, economic and social data specific to different locations is absent from these data and will, most likely, have an impact on our results. It is my understanding that if a unified nationwide approach is required then more granular data both from the individual as well as from the location characteristics is desirable.
In addition, it is important to note that the majority of reasons and the majority of issues identified in these stops and searches are related to a handful of factors of which the biggest problem being drugs issues. If, for some reason, the paradigm or distribution of offences changes, the model might not perform well. For example in the context of the current pandemic lockdowns and restrictions people might be prohibited from even walking on the street or gathering in large groups or maybe stopped and fined for not wearing a mask. The current model does account for unknown, unseen potential offences so one would not expect a total lack of performance but these types of unforeseen unlawful events would probably impair the model’s ability to yield good results if the change in the features becomes permanent for the long term. This would obviously require revisiting the modelling process and adaptation to the new paradigm. 
''')