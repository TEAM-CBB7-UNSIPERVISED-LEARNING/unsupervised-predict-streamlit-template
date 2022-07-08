"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import select
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","Team","Data analysis", "contuct us@"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
        st.write("we build this app look for movies using filtering and contend basesd algorythms")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    # Building Team Page
    if page_selection == "Team":
        #Team name
        st.title("Team CB7")
        #team mates names
        st.write("Thembani maswengani - Team Learder")
        st.write("Katlego Maponya -Team Coordinator")
        st.write("Keabetswe sebanyoni")
        st.write("Charmain Nhlapho")
        st.write("Sydney Abrahams")
        st.write("MR easy gym")
        st.image("http://images.clipartpanda.com/working-together-as-a-team-TeamEvent.jpg")
    #EDA
    if page_selection == "Data analysis":
        st.write("EXPLONATORY DATA ANALYSIS")
        st.image("https://st3.depositphotos.com/3116407/15347/i/950/depositphotos_153476170-stock-photo-data-analysis-concept-on-a.jpg")

    page_bg_img = '''
<style>
body {
background-image: url("https://www.bing.com/images/search?view=detailv2&form=SBIHVR&iss=sbi&q=imgurl:https%3A%2F%2Ftechcrunch.com%2Fwp-content%2Fuploads%2F2021%2F10%2FGettyImages-1165220714.jpg%3Fw%3D711&pageurl=https%3A%2F%2Ftechcrunch.com%2F2021%2F10%2F05%2Fstreamlit-reaches-1-0-milestone-for-open-source-data-app-building-tool%2F&pagetl=Streamlit+reaches+1.0+milestone+for+open+source+data+app+building+tool+%E2%80%93+TechCrunch&imgsz=712x400&selectedindex=7&id=https%3A%2F%2Fak8.picdn.net%2Fshutterstock%2Fvideos%2F2996629%2Fthumb%2F1.jpg&ccid=qnV7bBZ6&mediaurl=https%3A%2F%2Fak8.picdn.net%2Fshutterstock%2Fvideos%2F2996629%2Fthumb%2F1.jpg&exph=480&expw=852&vt=2&simid=608055988107092185&ck=3EFB9FE1B1D0E41FCEA90AA0A5430ED0&thid=OIP.qnV7bBZ6PIe1RtDKAEVb4QHaEL&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.aa757b6c167a3c87b546d0ca00455be1%3Frik%3DOzKI7fsBKlutCA%26pid%3DImgRaw%26r%3D0&sim=15,16");
background-size: cover;
}
</style>
'''
if __name__ == '__main__':
    main()
