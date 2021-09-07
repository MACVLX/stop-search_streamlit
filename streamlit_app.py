# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Utils
import os
import joblib 
import json
import pickle

from custom_transformers_3.transformer import * 


# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

# DB
# from managed_db import *


# Load ML Models
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


# ML Interpretation
import lime
import lime.lime_tabular


html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Stop & Search UK app</h1>
		
		</div>
		"""

# Avatar Image using a url
avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"

result_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

result_temp2 ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/{}" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

prescriptive_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Recommended Life style modification</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Get Plenty of Rest</li>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Avoid Alchol</li>
		<li style="text-align:justify;color:black;padding:10px">Proper diet</li>
		<ul>
		<h3 style="text-align:justify;color:black;padding:10px">Medical Mgmt</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Consult your doctor</li>
		<li style="text-align:justify;color:black;padding:10px">Take your interferons</li>
		<li style="text-align:justify;color:black;padding:10px">Go for checkups</li>
		<ul>
	</div>
	"""





# @st.cache
def load_model():
	with open('../columns_RF_opt_2.json') as fh:
		columns = json.load(fh)

	with open('../pipeline_RF_opt_2.pickle', 'rb') as fh:
		pipeline = joblib.load(fh)

	with open('../dtypes_RF_opt_2.pickle', 'rb') as fh:
		dtypes = pickle.load(fh)

	return columns, pipeline, dtypes

@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im
	

def change_avatar(sex):
	if sex == "male":
		avatar_img = 'img_avatar.png'
	else:
		avatar_img = 'img_avatar2.png'
	return avatar_img

valid_category_map = {
        "Type": [None,'Person search', 'Person and Vehicle search', 'Vehicle search'],
        'Part of a policing operation':[None, True, False],
        'Gender':[None,'Male','Female','Other'],
        'Age range':[None,'18-24', '25-34', 'over 34', '10-17', 'under 10'],
        'Officer-defined ethnicity':[None,'Asian', 'White', 'Black', 'Other', 'Mixed'],  
    'Legislation':[None,'Misuse of Drugs Act 1971 (section 23)', 
                   'Police and Criminal Evidence Act 1984 (section 1)',
                   'Psychoactive Substances Act 2016 (s36(2))',
                   'Criminal Justice Act 1988 (section 139B)',
                   'Firearms Act 1968 (section 47)',
                   'Poaching Prevention Act 1862 (section 2)',
                   'Criminal Justice and Public Order Act 1994 (section 60)',
                   'Police and Criminal Evidence Act 1984 (section 6)',
                   'Wildlife and Countryside Act 1981 (section 19)',
                   'Psychoactive Substances Act 2016 (s37(2))',
                   'Aviation Security Act 1982 (section 27(1))',
                   'Protection of Badgers Act 1992 (section 11)',
                   'Crossbows Act 1987 (section 4)',
                   'Public Stores Act 1875 (section 6)',
                   'Customs and Excise Management Act 1979 (section 163)',
                   'Deer Act 1991 (section 12)',
                   'Conservation of Seals Act 1970 (section 4)'], 
    'Object of search':[None,'Controlled drugs',
                        'Offensive weapons',
                        'Stolen goods',
                        'Article for use in theft',
                        'Articles for use in criminal damage',
                        'Firearms',
                        'Anything to threaten or harm anyone',
                        'Crossbows',
                        'Evidence of offences under the Act',
                        'Fireworks',
                        'Psychoactive substances',
                        'Game or poaching equipment',
                        'Evidence of wildlife offences',
                        'Detailed object of search unavailable',
                        'Goods on which duty has not been paid etc.',
                        'Seals or hunting equipment'],
'station':[None,'devon-and-cornwall', 'dyfed-powys', 'derbyshire', 'bedfordshire', 'avon-and-somerset', 'cheshire', 'sussex', 'north-yorkshire', 'cleveland', 'merseyside', 'north-wales', 'wiltshire', 'norfolk', 'suffolk', 'thames-valley', 'durham', 'warwickshire', 'leicestershire', 'hertfordshire', 'cumbria', 'metropolitan', 'essex', 'south-yorkshire', 'surrey', 'staffordshire', 'northamptonshire', 'northumbria', 'city-of-london', 'nottinghamshire', 'gloucestershire', 'cambridgeshire', 'lincolnshire', 'btp', 'west-yorkshire', 'dorset', 'west-mercia', 'kent', 'hampshire', 'humberside', 'lancashire', 'greater-manchester', 'gwent']
}


def main():
	"""Hep Mortality Prediction App"""
	
	st.markdown(html_temp.format('royalblue'),unsafe_allow_html=True)

	menu = ['Home',"Plot","Prediction","Metrics"]

	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home")
		
		st.markdown("""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Project overview</h3>
		<p>A summary of the project premisses, objectives and requirements.</p>
	</div>
	""",unsafe_allow_html=True)

		st.checkbox('open overview')
	
		# st.image(load_image('images/hepimage.jpeg'))


	elif choice == "Plot":

			# create_usertable()
		st.subheader("Data Vis Plot")
		# df = load_dataset("train.csv")
		# st.dataframe(df)

		# df['Outcome'].value_counts().plot(kind='bar')
		# st.pyplot()	

	# 				# Freq Dist Plot
	# 				freq_df = pd.read_csv("data/freq_df_hepatitis_dataset.csv")
	# 				st.bar_chart(freq_df['count'])


	# 				if st.checkbox("Area Chart"):
	# 					all_columns = df.columns.to_list()
	# 					feat_choices = st.multiselect("Choose a Feature",all_columns)
	# 					new_df = df[feat_choices]
	# 					st.area_chart(new_df)
						


	elif choice== "Prediction":


		st.subheader("Predictive Analytics")
		with st.form("my_form"):
			id = st.text_input("observation id")
			
			type = st.selectbox("Type",valid_category_map.get('Type'))
			
			import datetime
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
				prediction
				# prediction=bool(prediction)


	# 					# st.write(prediction)
	# 					# prediction_label = {"Die":1,"Live":2}
	# 					# final_result = get_key(prediction,prediction_label)
	# 					if prediction == 1:
	# 						st.warning("Patient Dies")
	# 						pred_probability_score = {"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}
	# 						st.subheader("Prediction Probability Score using {}".format(model_choice))
	# 						st.json(pred_probability_score)
	# 						st.subheader("Prescriptive Analytics")
	# 						st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
							
	# 					else:
	# 						st.success("Patient Lives")
	# 						pred_probability_score = {"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}
	# 						st.subheader("Prediction Probability Score using {}".format(model_choice))
	# 						st.json(pred_probability_score)
							
	# 				if st.checkbox("Interpret"):
	# 					if model_choice == "KNN":
	# 						loaded_model = load_model("models/knn_hepB_model.pkl")
							
	# 					elif model_choice == "DecisionTree":
	# 						loaded_model = load_model("models/decision_tree_clf_hepB_model.pkl")
							
	# 					else:
	# 						loaded_model = load_model("models/logistic_regression_hepB_model.pkl")
							

	# 						# loaded_model = load_model("models/logistic_regression_model.pkl")							
	# 						# 1 Die and 2 Live
	# 						df = pd.read_csv("data/clean_hepatitis_dataset.csv")
	# 						x = df[['age', 'sex', 'steroid', 'antivirals','fatigue','spiders', 'ascites','varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime','histology']]
	# 						feature_names = ['age', 'sex', 'steroid', 'antivirals','fatigue','spiders', 'ascites','varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime','histology']
	# 						class_names = ['Die(1)','Live(2)']
	# 						explainer = lime.lime_tabular.LimeTabularExplainer(x.values,feature_names=feature_names, class_names=class_names,discretize_continuous=True)
	# 						# The Explainer Instance
	# 						exp = explainer.explain_instance(np.array(feature_list), loaded_model.predict_proba,num_features=13, top_labels=1)
	# 						exp.show_in_notebook(show_table=True, show_all=False)
	# 						# exp.save_to_file('lime_oi.html')
	# 						st.write(exp.as_list())
	# 						new_exp = exp.as_list()
	# 						label_limits = [i[0] for i in new_exp]
	# 						# st.write(label_limits)
	# 						label_scores = [i[1] for i in new_exp]
	# 						plt.barh(label_limits,label_scores)
	# 						st.pyplot()
	# 						plt.figure(figsize=(20,10))
	# 						fig = exp.as_pyplot_figure()
	# 						st.pyplot()



					


	# 		else:
	# 			st.warning("Incorrect Username/Password")


	# elif choice == "SignUp":
	# 	new_username = st.text_input("User name")
	# 	new_password = st.text_input("Password", type='password')

	# 	confirm_password = st.text_input("Confirm Password",type='password')
	# 	if new_password == confirm_password:
	# 		st.success("Password Confirmed")
	# 	else:
	# 		st.warning("Passwords not the same")

	# 	if st.button("Submit"):
	# 		create_usertable()
	# 		hashed_new_password = generate_hashes(new_password)
	# 		add_userdata(new_username,hashed_new_password)
	# 		st.success("You have successfully created a new account")
	# 		st.info("Login to Get Started")







if __name__ == '__main__':
	main()