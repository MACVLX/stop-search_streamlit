import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
sns.set_style('darkgrid')

# import nltk
import textblob
from textblob import TextBlob
# from nltk import ngrams 
# from nltk.corpus import stopwords
# from nltk.sentiment import SentimentIntensityAnalyzer
# from gensim.summarization import summarize
# from summa.summarizer import summarize

import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    color: white;
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-color: white;
    -webkit-tap-highlight-color: red;
    -webkit-highlight-color: red;

    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# paste the image file name to reset your background image
set_png_as_page_bg('stopsearch.png')


html_temp = """
<div style="background-color:{};height:{};width:{};">
</div>
<div id="head" style="background-color:{};padding:10px;">
<h1 style="color:{};text-align:center;">Natural Language Processing WebApp </h1>
</div>
"""
st.markdown(html_temp.format('red','5px', '100%','#cccccc','#0000A0'),unsafe_allow_html=True)


html_temp2 = """
<hr>

<p id="para" style="font-size:{};color:{};text-align:left;">
<b> Description </b> <br/>
This is a mini Natural Language Processing (NLP) web-app built with streamlit. It performs 
various NLP activities like tokenization, sentiment-analysis, translation and summarization. \
It uses packages like textblob, nltk, gensim, goslate, pandas and seaborn.<br/>
More features like NER will be added later.
 </p>
"""

st.markdown(html_temp2.format('17px', '#ffffff' ),unsafe_allow_html=True)

def main():
    word = st.text_area('Enter text ', height = 120)
    text  = TextBlob(word)

if __name__ == '__main__':
    main()