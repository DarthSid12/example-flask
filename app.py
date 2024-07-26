from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/proxy', methods=['GET'])
@cross_origin(supports_credentials=True)
def getSummary():
    print(1)
    req = request.headers
    print(2)
    response = requests.get(req['url'],headers=req)
    print(3)
    return response.text


@app.route('/')
def home():
    return "Hello!!"

if __name__ == "__main__":
    app.run()
