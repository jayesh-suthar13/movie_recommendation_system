import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

#google drive file ID
file_id="1HpQ0vyg9x6Mm9sQmA2_UY36rM8j7gL1B"
output_path="similarity.pkl"

if not os.path.exists(output_path):
  gdown.download(f"https://drive.google.com/uc?id=1HpQ0vyg9x6Mm9sQmA2_UY36rM8j7gL1B",output_path,quiet=False)

def fetch_poster(movie_id):
   response = requests.get('http://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
   data=response.json()
   return "http://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_listss=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies=[] 
  recommended_movies_posters=[]
  for i in movies_listss:
    movie_id=(movies.iloc[i[0]].movie_id)
    recommended_movies.append(movies.iloc[i[0]].title)
    #fetch poster form API
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies,recommended_movies_posters

movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open(output_path,'rb'))
movies=pd.DataFrame(movies_list)

st.title('Movie recommender system')

selected_movie_name =st.selectbox('how would u like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    names,poster=recommend(selected_movie_name)

    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
      st.header(names[0])
      st.image(poster[0])
    with col2:
      st.header(names[1])
      st.image(poster[1])
    with col3:
      st.header(names[2])
      st.image(poster[2])
    with col4:
      st.header(names[3])
      st.image(poster[3])
    with col5:
      st.header(names[4])
      st.image(poster[4])