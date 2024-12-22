import numpy as np
import pandas as pd
import pickle
import streamlit as st
movie_title = "Avatar"
def recommend(movie):
    movie_index = np.where(movies_list == movie)
    distances = similarity[movie_index[0][0]]
    recommended_movies = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies_list = []
    for i in recommended_movies:
        recommended_movies_list.append(movies_list[i[0]])
    return recommended_movies_list
movies_list = pd.read_pickle("movie_list.pkl")
print(movies_list.head())
movies_list = movies_list['original_title'].values
similarity = pickle.load(open("similarity.pkl", "rb"))
recommendations = recommend(movie_title)
print(recommendations)
