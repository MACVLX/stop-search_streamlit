Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@MACVLX 
Jcharis
/
data-science-projects
2
1941
Code
Issues
Pull requests
Actions
Projects
1
Wiki
Security
Insights
data-science-projects/Dsc-Project-Hepatitis_Mortality_Prediction/ml_web_apps_flask_n_streamlit/ML_App_Hepatitis_mortality_predictor-Streamlit/managed_db.py /
@Jcharis
Jcharis Added ML Web apps for HepB Mortality Prediction
Latest commit d7c7a1c on 26 Jun 2020
 History
 1 contributor
26 lines (18 sloc)  600 Bytes
  
# DB
import sqlite3
conn = sqlite3.connect('usersdata.db')
c = conn.cursor()

# Functions

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data



def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

