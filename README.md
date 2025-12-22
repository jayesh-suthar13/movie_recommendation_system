# Movie Recommendation System
**Live Web Application (Render)**
https://movie-recommendation-system-coot.onrender.com/

##  Project Overview

This project is a **Content-Based Movie Recommendation System** that suggests movies similar to a selected title based on metadata such as cast, crew, genre, and keywords. The system uses natural language processing techniques to compute similarity between movies and generate top recommendations.

##  Dataset

The dataset contains movie metadata including titles, genres, overviews, cast, crew, and more. This information is used to create a consolidated feature space for content comparison.

##  Key Steps in the Pipeline

### 1. Data Cleaning

* Removed unnecessary columns and dropped missing/null values to ensure the integrity of the dataset.

### 2. Feature Engineering

* Parsed complex string-formatted JSON columns using `ast.literal_eval`.
* Extracted relevant features:

  * **Genres**, **cast**, **keywords** from lists of dictionaries.
  * **Director** from crew information using a custom `fetch_director()` function.

### 3. Text Preprocessing

* Combined selected features into a single "tags" column.
* Converted all text to lowercase, removed spaces, and tokenized.
* Used **NLTK** for:

  * Removing stop words
  * Applying **PorterStemmer** to normalize text

### 4. Vectorization and Similarity Computation

* Converted text data into vectors using **CountVectorizer**.
* Calculated **cosine similarity** between vectors to measure how similar one movie is to another.

### 5. Recommendation Function

This function retrieves the top 5 most similar movies to the given title using cosine similarity scores.

### 6. Model Saving and Web Deployment

* The model and vector data were saved using **pickle** for reuse.
* A simple user interface was built using **Streamlit** where users can input a movie name and receive recommendations instantly.

### 7. File structure 
📦 movie-recommendation-system
│
├── README.md                     # Project overview + usage instructions
├── requirements.txt              # All Python dependencies
├── app.py                        # Flask/Streamlit app for deployment
├── movie_recomm_system.ipynb     # Jupyter notebook (EDA, model training)
├── movies.pkl                    # Saved similarity/model file
├── tmdb_5000_movies.csv          # Dataset used for training
│
├── screenshots/                  # output/ui images
   ├── Screenshot 2025-07-29 181251.png
   └── Screenshot 2025-07-29 181251.png

##  Conclusion

This recommendation system effectively demonstrates how content-based filtering can be implemented using Python and NLP techniques. It serves as a strong foundation for building more advanced hybrid or collaborative filtering systems in the future.
