import pandas as pd 
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt


from PIL import Image

dataset=pd.read_csv('covid_worldwide.csv')
st.set_page_config(page_title="Statistics Covid 19",layout="wide",page_icon="virus.png")

st.sidebar.header("Filter By :")
Country=st.sidebar.multiselect("Filter By Country:",
                               options=dataset["Country"].unique(),
                               default=dataset["Country"].unique())
selection_query=dataset.query(
    "Country==@Country"
)
st.dataframe(selection_query)

st.title("Statistics :red[Covid 19] ")
st.caption('_It was found that a new virus called SARS-CoV-2 was the cause of an outbreak of a disease that began to appear in China in 2019. The resulting disease is called: Coronavirus Disease 2019 (COVID-19). In March 2020, the World Health Organization declared COVID-19 a global pandemic. Public health groups, including the US Centers for Disease Control and Prevention and the World Health Organization, are monitoring the pandemic and posting updates on their websites. These groups issue recommendations to prevent the spread of this virus that causes Covid 19 disease._')


# labels = 'USA', 'India', 'France', 'Brazil'
# sizes = [15, 30, 45, 10]

# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)

data={ "Country": ["USA", "France","Brazil","India"],
      "Total Cases": ["USA", "France","Brazil","India"]}
dataset=pd.DataFrame(data)
colors=['#424bff','#2dab90','#b7d638','#2d90ab']
st.write(px.bar(dataset,x="Country",y="Total Cases",color="Country",color_discrete_sequence=colors))
      
















