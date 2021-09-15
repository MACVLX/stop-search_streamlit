import streamlit as st
from multiapp import  MultiApp

from home import main 
from EDA import EDA
from prediction import prediction
from modeling import modeling

## set page layout
# st.set_page_config(
#     page_title="Stop & Search UK",
#     page_icon="",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )	


app = MultiApp()

# Add all your application here
app.add_app("Home", main)
app.add_app("EDA", EDA)
app.add_app('Modeling', modeling)
app.add_app('Use Model', prediction)





# The main app
app.run()