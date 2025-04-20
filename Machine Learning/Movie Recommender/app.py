import streamlit as st
import pickle
import pandas as pd
import requests

## Not using movies.pkl because its a dataframe

movies_dict = pickle.load(open('movies_dict.pkl','rb')) #rb - read binary mode
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values  

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
                      'How would you like to be contacted?',
                      (movies_list))
   
# def fetch_poster(movie_id):
#     response = requests.get(.format(movie_id)
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        
        ## fetch poster from API 
        # recommended_movies_poster.append(fetch_poster(movie_id))
        
    return recommended_movies
 
if st.button('Recommend'):
    recommendations =  recommend(selected_movie)
    for i in recommendations:
        st.write(i)

    # names,poster = recommend(selected_movie)
    
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     # st.image(poster[0])
    
    # with col2:
    #     st.text(names[1])
    #     # st.image(poster[1])
    
    # with col3:
    #     st.text(names[2])
    #     # st.image(poster[2])
    
    # with col4:
    #     st.text(names[3])
    #     # st.image(poster[3])
    
    # with col5:
    #     st.text(names[4])
    #     # st.image(poster[4])
