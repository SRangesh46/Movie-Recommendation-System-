from flask import Flask, render_template, request, jsonify
import difflib
import joblib
import pandas as pd

app = Flask(__name__)

movies_data, similarity = joblib.load('recommendation system.pkl')
list_of_all_titles = movies_data['title'].tolist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('movie_name', '').strip()

    if not movie_name:
        return jsonify({"movie_name": None, "recommendations": [], "message": "Please enter a movie name."})

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return jsonify({"movie_name": movie_name, "recommendations": [], "message": "No close matches found."})

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = [
        movies_data[movies_data.index == movie[0]]['title'].values[0]
        for movie in sorted_similar_movies[1:31]
    ]

    return jsonify({"movie_name": close_match, "recommendations": recommended_movies, "message": None})

if __name__ == '__main__':
    app.run(debug=True)
