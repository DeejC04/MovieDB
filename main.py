from flask import Flask, request, render_template, jsonify
from movieDB import get_movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=['POST'])
def movies():
    numofmovies = int(request.form['numofmovies'])
    recommended_movies = get_movies(numofmovies)
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)