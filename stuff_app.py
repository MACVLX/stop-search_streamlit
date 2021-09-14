import pandas as pd
import streamlit as st
import datetime



from PIL import Image

img = Image.open("images/stopsearch.png")

# Reduce to thumbnail in place
# img.thumbnail((300,300), Image.ANTIALIAS)
# newImg1 = Image.new('RGB', (512,512))
resized_img = img.resize((250, 250))
resized_img.save("images/stopsearch2.png")



# st.cache(suppress_st_warning=True)
# def load_df():
#     df=pd.read_csv('https://storage.googleapis.com/capstone4ldsaa/train.csv')
#     return df

# def main():
#     train = load_df()
#     df=train.rename(columns={'Latitude':'lat','Longitude':'lon'})
#     df_coord=df[(~df.lat.isna()) & (~df.lon.isna())]
#     df_coord.info()
    

#     # # Calculate the timerange for the slider
#     # df_coord['DateTime'] = pd.to_datetime(df_coord['Date'])
#     # min_ts = min(df_coord['DateTime'])
#     # max_ts = max(df_coord['DateTime'])

#     # st.subheader("Inputs")
#     # min_selection, max_selection = st.slider(
#     #     "Timeline", min_value=min_ts, max_value=max_ts, value=[min_ts, max_ts])
#     # # Filter Data based on selection
#     # st.write(f"Filtering between {min_selection.date()} & {max_selection.date()}")
#     # time_data = df_coord[
#     #     (df_coord["DateTime"] >= min_selection) & (df_coord["DateTime"] <= max_selection)
#     # ]
#     # time_data.head()
#     # st.map(time_data)

# if __name__ == '__main__':
# 	main()
