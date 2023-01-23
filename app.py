from flask import Flask, request, render_template
from movieDB import get_movies
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=['POST'])
def movies():
    numofmovies = int(request.form['numofmovies'])
    recommended_movies = get_movies(numofmovies)
    return json.dumps(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)



