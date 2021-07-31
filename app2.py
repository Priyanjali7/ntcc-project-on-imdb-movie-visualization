import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import os

st.set_page_config(layout='wide', page_title="IMDB data analysis")

audio_file = open('audiotreatyoubetter.mpeg','rb')
audio_bytes = audio_file.read()
st.sidebar.audio(audio_bytes, format='audio/mpeg') 

@st.cache
def load_data(name):
    return pd.read_csv('data/'+name)

files = os.listdir('data')
data0 = load_data(files[0])
data1 = load_data(files[1])

def home(title):
    st.title("IMDB Movie Data Analysis")
    st.write("")
    c = st.beta_columns(3)
    c[0].image('sorte.jpg',use_column_width=True)
    c[1].image('Miss_Jerry_(1894).jpg',use_column_width=True)
    c[2].image('kelly.jpg',use_column_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def page1(title):
    st.title(title)
    df = data0
    st.write("")
    x = st.sidebar.slider('size of records',value=10, min_value=0, max_value=df.shape[0])
    st.write(df.head(x))
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Dataset Summary")
    st.write(df.describe())
    st.markdown("<hr>", unsafe_allow_html=True)

def page2(title):
    st.title(title)
    df = data0
    ## show plot
    st.header("Plot of every column in the dataset")
    st.write("")
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    st.pyplot(fig)
    st.markdown("<hr>", unsafe_allow_html=True)
    ## duration
    st.header("show duration and year")
    st.write("")
    st.plotly_chart(px.bar(df, x='duration',y='year'))
    st.markdown("<hr>", unsafe_allow_html=True)
    ## country, language, genres pie chart
    col = st.beta_columns((1,3))
    choices = ('Country', 'Language', 'Genres')
    choice = col[0].radio('Select your chart', choices)
    if choice ==  choices[0]:
        col[1].header("Pie chart of countries")
        data = df.groupby('country', as_index=False).count()
        names, values = data.country[:10], data.imdb_title_id[:10]
        fig = px.pie(names=names, values=values)
        col[1].plotly_chart(fig)

    if choice ==  choices[1]:
        col[1].header("Pie chart of Languages")
        data = df.groupby('language', as_index=False).count()
        fig = px.bar(x=data.language, y=data.title)
        col[1].plotly_chart(fig)

    if choice ==  choices[2]:
        col[1].header("Pie chart of Genres")
        fig = px.pie(
            names = ["Comedy", "Romance", "Fantasy", "Crime", "Drama", "Adventure", "Mystrey", "Action", "Thriller", "History", "Biography"],
            values = [640, 890, 207, 455, 700, 205, 110, 67, 45, 80, 50]
        )
        col[1].plotly_chart(fig)

def page3(title):
    st.title(title)
    df = data1
    if st.sidebar.checkbox("Show Raw Data"):
        st.write("")
        row_size = st.sidebar.slider('size of records',value=10, min_value=0, max_value=df.shape[0])
        st.write(df.head(row_size))
        st.markdown("<hr>", unsafe_allow_html=True)

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig = go.Figure(data=[go.Pie(labels=['Total votes','Mean vote','Males allages votes','females allages votes'],
                                 values=[4500,2500,1053,500])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)
    st.header("Pie chart of gender of voters")
    st.plotly_chart(px.pie(names=['Total Male Votes', 'Total Female Votes'], values=[df.males_allages_votes.sum(), df.females_allages_votes.sum()]))
    st.header("Pie chart of ages of voters")
    votes = df.sum()
    voters_age = [
        votes.males_0age_votes + votes.females_0age_votes,
        votes.males_18age_votes + votes.females_18age_votes,
        votes.males_30age_votes + votes.females_30age_votes,
        votes.males_45age_votes + votes.females_45age_votes,
        ]
    st.plotly_chart(px.pie(names=['0-18','18-30','30-45','45+'], values=voters_age))
    st.header("voter's nationality")
    st.plotly_chart(px.pie(names=['US voters','Non-US voters'], values=[votes.us_voters_votes, votes.non_us_voters_votes]))

def page4(title):
    st.title(title)
    st.header("Priyanjali Singh ")


pages = {
    'Introduction': home,
    'Raw Data Analysis': page1,
    'Movie Data Visualization': page2,
    'Movie Rating Visualization': page3,
    'About us': page4
    }
page = st.sidebar.radio("Navigate through pages",list(pages.keys()))
pages[page](page)

# depracated
def page4(title):
    st.header("Celebrity Bio")
    fig = px.scatter_matrix(data,
          dimensions=["spouses", "divorces", "children"],
          )
    st.plotly_chart(fig)
