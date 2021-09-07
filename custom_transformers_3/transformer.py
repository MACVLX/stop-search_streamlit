import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

#Custom Transformer that extracts columns passed as argument to its constructor 
class FeatureTransform(BaseEstimator, TransformerMixin):
    #Class Constructor 
#     def __init__( self, feature_names):
#         self._feature_names = feature_names 
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self
    
    #Method that describes what we need this transformer to do
    def transform( self, X, y = None):
        df_= X.copy()

        # put all in lower case
    #     df_=df_.apply(lambda x: x.astype(str).str.lower())
        def legislation(x):
            if x is None:
                return x
            x = x.lower()
            if 'drugs' in x:
                return 'drugs related'
            elif 'criminal' in x:
                return 'criminal offence'
            elif 'firearms' in x:
                return 'firearms'
            else:
                return 'other'

        df_['Legislation_simple']=df_['Legislation'].apply(legislation)
        
        df_=df_.drop(columns='Legislation')
        
        def objects(x):
            if x is None:
                return x
            x = x.lower()
            if 'drugs' in x:
                return 'drugs related'
            elif 'weapons' in x:
                return 'weapons'
            elif 'firearms' in x:
                return 'firearms'
            elif 'article' in x:
                return 'article for crimes'
            else:
                return 'other'

        df_['object_simple']=df_['Object of search'].apply(objects)
        
        df_=df_.drop(columns='Object of search')
        
        df_ = df_.drop(columns=['Latitude','Longitude','Self-defined ethnicity'])
        # date add features from date
        df_['DateTime'] = pd.to_datetime(df_['Date'])
        df_.drop(columns='Date',inplace=True)
        # get the hour and day of the week, maybe they will be useful 
        df_['hour'] = df_['DateTime'].dt.hour
        df_['month'] = df_['DateTime'].dt.month.astype(str)
        df_['day_of_week'] = df_['DateTime'].dt.day_name()
        df_['time_day']=df_['hour'].apply(lambda x: 'morning' if (x >7 and x <13) else 'afternoon' if (x>=13 and x<20) else 'night')
        df_.drop(columns='DateTime',inplace=True)
        df_.hour=df_.hour.astype(str)
        df_['Part of a policing operation'].fillna(False,inplace=True)

        return df_  