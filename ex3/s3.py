from flask import Flask, request
import requests, time, os

app = Flask(__name__)

global server1
global server2
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

@app.route('/setServer1', methods=['GET'])
def setServer1():
    global server1
    server1 = request.data.decode("utf-8")
    print("Get server 1 url => " + server1)
    return "ok"

@app.route('/setServer2', methods=['GET'])
def setServer2():
    global server2
    server2 = request.data.decode("utf-8")
    print("Get server 2 url => " + server2)
    return "ok"

@app.route('/ping', methods=['GET'])
def pong():
    if(not server2):
        return "server2 not set"
    # Send GET request to Server 1
    time.sleep(1)
    print("Redirection to " + server1)
    response = requests.get(server1 + "ping")
    return response.text

@app.route('/pong', methods=['GET'])
def ping():
    if(not server1):
        return "server1 not set"
    # Send GET request to Server 2
    time.sleep(1)
    print("Redirection to " + server2)
    response = requests.get(server2 + "pong")
    return response.text

if __name__ == '__main__':
    app.run(host=HOST,port=PORT)

