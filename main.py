from flask import Flask, request, Response
import json

app = Flask(__name__)

# KEY : VALUE
movie_db = {
    "1": {"name": "Stargate", "release_date": "1994"},
    "2": {"name": "Sunshine", "release_date": "2007"},
    "3": {"name": "The Holidays", "release_date": "2006"}
}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/movies")
def list_hello():
    return "Here is a list of all movies"

if __name__ == "__main__":
    app.run(host="127.0.0.1")


@app.route("/movie/add", method=['POST'])
def add_movie():
    # Collect the new movie from the user/url
    req_data = request.get_json()

    # Extract the movie data from the request
    new_movie = req_data['movie']
    
    # Get the last position in the database
    new_id = len(movie_db) + 1

    # Create a new entry for my movie
    new_movie_data = { str(new_id) : new_movie}

    # Update the database with the new entry
    movie_db.update(new_movie_data)
    
    return "The movie was added successfully"
    
    
    
    
    if_name_
