from flask import Flask, request
import requests, time

app = Flask(__name__)

server1 = "http://localhost:4567/ping"
server2 = "http://localhost:5372/pong"

@app.route('/pong', methods=['GET'])
def pong():
    # Send GET request to Server 1
    time.sleep(1)
    print("Redirection to " + server2)
    response = requests.get(server2)
    return response.text

@app.route('/ping', methods=['GET'])
def ping():
    # Send GET request to Server 2
    time.sleep(1)
    print("Redirection to " + server1)
    response = requests.get(server1)
    return response.text

if __name__ == '__main__':
    app.run(port=8080)

