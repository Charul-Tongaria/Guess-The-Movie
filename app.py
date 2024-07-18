from flask import Flask, render_template, request, redirect, url_for, session
import random
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load movie data
with open('movies.json') as f:
    movies = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    session['username'] = request.form['username']
    session['score'] = 0
    session['current_movie_index'] = 0
    session['movies'] = random.sample(movies, 10)  # Select 10 random movies
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('index'))
    current_movie = session['movies'][session['current_movie_index']]
    feedback = session.pop('feedback', None)
    return render_template('game.html', movie=current_movie, feedback=feedback)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    guess = request.form['guess']
    current_movie = session['movies'][session['current_movie_index']]
    correct_answer = current_movie['title'].lower()
    feedback = ''

    if guess.lower() == correct_answer:
        session['score'] += 1
        feedback = 'congratulations'
    elif correct_answer in guess.lower() or guess.lower() in correct_answer:
        feedback = 'almost_near'
    else:
        feedback = 'wrong_answer'

    session['feedback'] = feedback
    session['current_movie_index'] += 1

    if session['current_movie_index'] >= 10:
        return redirect(url_for('end_game'))
    return redirect(url_for('game'))

@app.route('/end_game')
def end_game():
    score = session['score']
    if score <= 5:
        message = "Try better next time!"
    elif 6 <= score <= 8:
        message = "You were good, but could be better next time!"
    else:
        message = "You were fabulous! 🎉"

    return render_template('end_game.html', score=score, message=message)

@app.route('/play_again', methods=['POST'])
def play_again():
    return redirect(url_for('index'))


