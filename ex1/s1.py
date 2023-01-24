from flask import Flask, request
import requests, time

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Send GET request to Server 2
    time.sleep(1)
    print("Server 1: Ping")
    response = requests.get('http://localhost:5372/pong')
    return response.text

if __name__ == '__main__':
    app.run(port=4567)