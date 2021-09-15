import streamlit as st




html_temp = """
		<div style="background-color:#3FB8AF;padding:10px;border-radius:10px">
		<h1 style="color:black;text-align:center;">{}</h1>
		</div>
		"""
# html_temp = """
# 		<div style="background-image:url("data:image/png;base64,{}");padding:10px;border-radius:10px">
# 		<h1 style="color:white;text-align:center;">Stop & Search UK app</h1>
# 		</div>
# 		"""


result_true ="""
	<div style="background-color:green;padding:10px;border-radius:10px;margin:10px;width:auto;">
	<h4 style="color:black;text-align:center;">SEARCH</h4>
	</div>
	"""

result_false ="""
	<div style="background-color:red;padding:10px;border-radius:10px;margin:10px;width:auto;">
	<h4 style="color:white;text-align:center;">DON'T SEARCH</h4>
	</div>
	"""

img_html = '''<figure>
				<img src='data:image/png;base64,{}' class='img-fluid' style="width:100%">
				<figcaption>{}}</figcaption>
			</figure>>'''

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
background-color: #f0f0f0;
color: black;
text-align: center;
font-size: xx-small;

}
</style>
<div class="footer"; >
<a style='display: block; text-align: center;' 
 target="_blank">Developed by Miguel Vieira with contributions from:</a>
<a style='display: block; text-align: center;' target="_blank", href='https://github.com/rafaelloni/EAT_app'>https://github.com/rafaelloni/EAT_app</a>
<a style='display: block; text-align: center;' target="_blank", href='https://github.com/upraneelnihar/streamlit-multiapps'>https://github.com/upraneelnihar/streamlit-multiapps</a>
</div>
"""
# <p> </p>

