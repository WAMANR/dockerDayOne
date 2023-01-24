from flask import Flask, request
import requests, time

app = Flask(__name__)

global server1
global server2

@app.route('/setServer1', methods=['GET'])
def setServer1():
    server1 = "http://localhost:" + request.data.decode("utf-8") + "/ping"
    print("Get server 1 url => " + server1)
    return "ok"

@app.route('/setServer2', methods=['GET'])
def setServer2():
    server2 = "http://localhost:" + request.data.decode("utf-8") + "/pong"
    print("Get server 2 url => " + server2)
    return "ok"

@app.route('/pong', methods=['GET'])
def pong():
    if(not server2):
        return "server2 not set"
    # Send GET request to Server 1
    time.sleep(1)
    print("Redirection to " + server2)
    response = requests.get(server2)
    return response.text

@app.route('/ping', methods=['GET'])
def ping():
    if(not server1):
        return "server1 not set"
    # Send GET request to Server 2
    time.sleep(1)
    print("Redirection to " + server1)
    response = requests.get(server1)
    return response.text

if __name__ == '__main__':
    app.run(port=8080)

