from flask import Flask, request
import requests, time

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Send GET request to Server 2
    print("Server 1: Ping")
    response = requests.get('http://localhost:8080/pong')
    return response.text

if __name__ == '__main__':
    requests.get(url = 'http://localhost:8080/setServer1', data="4567")
    app.run(port=4567)