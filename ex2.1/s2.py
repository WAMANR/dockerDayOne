from flask import Flask, request
import requests, time

app = Flask(__name__)

@app.route('/pong', methods=['GET'])
def pong():
    # Send GET request to Server 1
    print("Server 2: Pong")
    response = requests.get('http://localhost:8080/ping')
    return response.text

if __name__ == '__main__':
    app.run(port=5372)


