import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use('Agg')

#set seaborn as style
sns.set_style('darkgrid')

#import streamlit
import streamlit as st
#ignore warning 
# st.set_option('deprecation.showPyplotGlobalUse', False) 

#import necessary NLP libraries
import nltk
import textblob
from textblob import TextBlob
#setting background image from local host  
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#restyling the CSS and HTML tags.  
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
    .st-ci {
    color: blue;
    
    }
    .st-br {
    background-color:#C0C0C0;  
       }
    .st-cd {
    color: black;
	}
    .st-dd {
    color: white;
    }
    .st-de {
    color: white;
	}
    .css-145kmo2 {
    color: white;
    }
    .css-3xqji8 {
    color: white;
    }
    #head {
	 -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
 	 border-radius: 10px;
 	 -webkit-box-shadow: 0px 0px 100px #0000A0;
	  -moz-box-shadow: 0px 0px 100px #0000A0;
 	 box-shadow: 0px 0px 100px #0000A0;
	}
	#para {
    font-family: "IBM Plex Sans", sans-serif;
	}
	#Mname {
    font-family: "IBM Plex Sans", sans-serif;
     
     color:#C0C0C0;    
	}
	.css-2trqyj {
    color: red;
    }
	.css-1v4eu6x a {
	color: #013220;
	text-decoration: none;
	-webkit-border-radius: 10px;
    -moz-border-radius: 10px;
 	 border-radius: 10px;
 	padding:5px;
 	 
	} 
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

#file name
set_png_as_page_bg('ai_bkgrd.jpg')


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

st.subheader("""
	Start NLProcessing Here...
	""")

#The main script body
def main():
	word = st.text_area('Enter text ', height = 120)
	text  = TextBlob(word)
	