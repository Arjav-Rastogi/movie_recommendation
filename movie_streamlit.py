import numpy as np
import pandas as pd
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    import requests

    url = "https://api.themoviedb.org/3/movie/{}/images".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YjU2NGRiZGQ2NWU5ZTQyY2MwMjgyZDY2MWI2NDQzOCIsIm5iZiI6MTczNDEyMDg1NC44OTUsInN1YiI6IjY3NWM5NTk2ODUzNGExYzhlMjJiNGYyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pr396MMpabWwIzPmxa_ULGs9QX9qCiuw87iWjEXIqr4"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    path = "http://image.tmdb.org/t/p/w500"+data['posters'][0]['file_path']
    return path

def recommend(movie):
    movie_index = np.where(movies_list == movie)
    distances = similarity[movie_index[0][0]]
    recommended_movies = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies_list = []
    recommended_movies_posters = []
    for i in recommended_movies:
        recommended_movies_list.append(movies_list[i[0]])
        poster = fetch_poster(movies_df.iloc[i[0]].movie_id)
        recommended_movies_posters.append(poster)
    return recommended_movies_list, recommended_movies_posters

movies_df = pd.read_pickle("movie_list.pkl")
movies_list = movies_df['original_title'].values
st.title("Movie Recommender System")
movie_title = st.selectbox("Which Movie do wanna select?", movies_list)
similarity = pickle.load(open("similarity.pkl", "rb"))
if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(movie_title)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
