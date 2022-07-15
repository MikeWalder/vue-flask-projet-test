from flask import Flask, jsonify
from flask_cors import CORS

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

if __name__ == "__main__":
    app.run(debug=True)