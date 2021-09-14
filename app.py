import streamlit as st
from multiapp import  MultiApp

from home import main #home, data_stats # import your app modules here
from EDA import EDA
from prediction import prediction


app = MultiApp()

# Add all your application here
app.add_app("Home", main)
app.add_app("EDA", EDA)
app.add_app('Use Model', prediction)


# # set page layout
# st.set_page_config(
#     page_title="Stop & Search UK",
#     page_icon="",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )	

# The main app
app.run()