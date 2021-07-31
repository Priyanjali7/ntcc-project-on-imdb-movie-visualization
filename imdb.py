import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px

st.set_page_config(layout='wide')
@st.cache
def load_movies_data():
    df = pd.read_csv('data\IMDb movies.csv')
    return df

c = st.beta_columns(3)

c[0].image('sorte.jpg',use_column_width=True)
c[1].image('Miss_Jerry_(1894).jpg',use_column_width=True)
c[2].image('kelly.jpg',use_column_width=True)


st.title("Data Analysis of IMDB Movies") 
data = load_movies_data()
if st.sidebar.checkbox("viwe data"):
    row_size = st.sidebar.slider('size of records',value=40)
    st.write(data.head(row_size))

if st.sidebar.checkbox("show plot"):
    fig,ax = plt.subplots()
    data.plot(ax=ax)
    st.pyplot(fig)

st.title("show duration and year")
if st.sidebar.checkbox("duration"):
   fig = px.bar(data, x='duration',y='year')
   st.plotly_chart(fig)


if st.sidebar.checkbox("pie chart"):
    df = px.data.tips()
    fig = px.pie(data, names='country')
    fig.show()

if st.sidebar.checkbox("language"):
   df = px.data.tips()
   fig = px.pie(data, names='language', color_discrete_sequence=px.colors.sequential.RdBu,title='Most used language in movies')
   fig.show()

