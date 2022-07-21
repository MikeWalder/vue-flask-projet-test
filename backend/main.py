from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# CORS = Cross Origin Request : for API calls basically

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

# CORS(app, resources={r"/*":{'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})

# hello world route (for example)
@app.route('/', methods=['GET'])
def greetings():
    return("Hello here !")

@app.route('/shark', methods=['GET'])
def shark():
    return("This is a message from the backend ! And it works !! ")

@app.route('/tensor', methods=['GET'])
def receive_datas():
    return("This is our first TensorFlow application !!")


GAMES = [
    {
        'title': 'GTA San Andreas',
        'genre': 'action',
        'played': True,
    },
    {
        'title': 'GTA Vie City',
        'genre': 'action',
        'played': False,
    }

]

# GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'} # default response when an HTTP request is successfull 
    
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] = 'Game Added !'
    else: 
        response_object['games'] = GAMES
    
    return jsonify(response_object)
    
    """
    return jsonify({
        'games': GAMES,
        'status': 'success'
    })
    """

# The PUT and DELETE route handler
@app.route('/games/<game_id>', methods = ['PUT'])
def single_game(game_id):
    response_object = {'status' : 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Updated !'
    return jsonify(response_object)

# Remove the game to update
def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False


if __name__ == "__main__":
    app.run(debug=True)