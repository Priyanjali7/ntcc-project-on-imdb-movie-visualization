import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout='wide', page_title="IMDB data analysis")

@st.cache
def load_movies_data():
    df = pd.read_csv('data\IMDb movies.csv')
    return df

st.title("Data Analysis of IMDB Movies") 
st.write("")
c = st.beta_columns(3)
c[0].image('sorte.jpg',use_column_width=True)
c[1].image('Miss_Jerry_(1894).jpg',use_column_width=True)
c[2].image('kelly.jpg',use_column_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

data = load_movies_data()

if st.sidebar.checkbox("view imdb data"):
   st.header("View imdb movies Data")
   st.write("")
   row_size = st.sidebar.slider('size of records',value=700, min_value=0, max_value=data.shape[0])
   st.write(data.head(row_size))
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("show plot"):
   st.header("Plot of every column in the dataset")
   st.write("")
   fig, ax = plt.subplots()
   data.plot(ax=ax)
   st.pyplot(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("duration"):
   st.header("show duration and year")
   st.write("")
   fig = px.bar(data, x='duration',y='year')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

st.radio(
   "select your chart",
   ('Country', 'Language','Genres')
)
if st.sidebar.checkbox("pie chart"):
   st.header("Pie chart of countries")
   st.write("")
   fig = px.pie(data, names='country')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("language"):
   st.header("Pie chart of languages")
   limit = st.slider("select limit for data", 10, 50,15)
   st.write("")
   fig = px.pie(data.head(limit), names='language', color_discrete_sequence=px.colors.sequential.RdBu,title='Most used language in movies')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)


   st.header("Genres")
   fig =go.Figure(go.Sunburst(
      labels=["Comedy", "Romance", "Fantasy", "Crime", "Drama", "Adventure", "Mystrey", "Action", "Thriller", "History", "Biography"],
      values=[640, 890, 207, 455, 700, 205, 110, 67, 45, 80, 50],
))
   #fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

   st.plotly_chart(fig)




@st.cache
def load_ratings_data():
    df = pd.read_csv('data1\IMDb ratings - Copy.csv')
    return df

data = load_ratings_data()

if st.sidebar.checkbox("view imdb ratings"):
   st.header("View Ratings Data")
   st.write("")
   row_size = st.sidebar.slider('size of records',value=1005, min_value=0, max_value=data.shape[0]) 
   st.write(data.head(row_size))
   st.markdown("<hr>", unsafe_allow_html=True)  


if st.sidebar.checkbox("votes"):
   st.header("All votes of movies")

  
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=['Total votes','Mean vote','Males allages votes','females allages votes'],
                             values=[4500,2500,1053,500])])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.plotly_chart(fig)



@st.cache
def load_names_data():
    df = pd.read_csv('data2\IMDb names.csv')
    return df

data = load_names_data()

if st.sidebar.checkbox("view imdb names"):
   st.header("View names Data")
   st.write("")
   row_size = st.sidebar.slider('size of records',value=1005, min_value=0, max_value=data.shape[0]) 
   st.write(data.head(row_size))
   st.markdown("<hr>", unsafe_allow_html=True)  



st.header("Celebrity Bio")
fig = px.scatter_matrix(data,
      dimensions=["spouses", "divorces", "children"],
      )
st.plotly_chart(fig)

