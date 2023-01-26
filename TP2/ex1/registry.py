from flask import Flask, request
import requests, time, os

app = Flask(__name__)

global server1
global server2
global broker
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

@app.route('/setBroker', methods=['GET'])
def setBroker():
    global broker
    broker = request.data.decode("utf-8")
    print("Get broker url => " + broker)
    return "ok"

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

@app.route('/getBroker', methods=['GET'])
def getBroker():
    global server1
    if(not server1):
        print("Unable to get broker => Broker isn't set in the registry.")
        return ""
    else:
        print("Return the broker adress to the server")
        return broker

@app.route('/getServer1', methods=['GET'])
def getServer1():
    global server1
    if(not server1):
        print("Unable to get server 2 => Server 2 isn't set in the registry.")
        return ""
    else:
        print("Return the server 1 adress to server 2 : " + server1)
        return server1

@app.route('/getServer2', methods=['GET'])
def getServer2():
    global server2
    if(not server2):
        print("Unable to get server 1 => Server 1 isn't set in the registry.")
        return ""
    else:
        print("Return the server 2 adress to server 1 : " + server2)
        return server2

if __name__ == '__main__':
    app.run(host=HOST,port=PORT)

