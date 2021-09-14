import streamlit as st



html_temp = """
		<div style="background-color:#FFCE54;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Stop & Search UK app</h1>
		</div>
		"""
# html_temp = """
# 		<div style="background-image:url("data:image/png;base64,{}");padding:10px;border-radius:10px">
# 		<h1 style="color:white;text-align:center;">Stop & Search UK app</h1>
# 		</div>
# 		"""


result_true ="""
	<div style="background-color:green;padding:10px;border-radius:10px;margin:10px;width:200px;">
	<h4 style="color:black;text-align:center;">SEARCH</h4>
	</div>
	"""

result_false ="""
	<div style="background-color:red;padding:10px;border-radius:10px;margin:10px;width:200px;">
	<h4 style="color:white;text-align:center;">NO SEARCH</h4>
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

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
font-size: x-small;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
font-size: x-small;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
font-size: xx-small;

}
</style>
<div class="footer"; >
<a style='display: block; text-align: center;' 
 target="_blank">Developed by Miguel Vieira</a>
<a>with contributions from:</a>
<a style='display: block; text-align: center;' target="_blank", href='https://github.com/rafaelloni/EAT_app'>https://github.com/rafaelloni/EAT_app</a>
<a style='display: block; text-align: center;' target="_blank", href='https://github.com/upraneelnihar/streamlit-multiapps'>https://github.com/upraneelnihar/streamlit-multiapps</a>
</div>
"""
# <p> </p>
