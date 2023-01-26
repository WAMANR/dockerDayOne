from flask import Flask, request
import requests, time, os

app = Flask(__name__)

PORT = int(os.getenv('PORT'))
REGISTRY = os.getenv('REGISTRY')
ADRESS = os.getenv('ADRESS')
HOST = os.getenv('HOST')
global server2, broker
broker = ""
server2 = ""

@app.route('/ping', methods=['GET'])
def ping():
    global server2, broker
    print("Server 1 : Ping")
    if(server2 == ""):
        server2Request = requests.get(REGISTRY + "/getServer2")
        if(server2Request.text == ""):
            print("Server 2 isn't in the registry.")
            return "Server 2 isn't in the registry."
        else:
            server2 = server2Request.text
            print("Server 2 available : " + server2)
    if(server2 == ""):
        return
    else:
        if(broker == ""):
            brokerRequest = requests.get(REGISTRY + "/getBroker")
            if(brokerRequest.text == ""):
                print("Broker isn't in the registry.")
                return "Broker isn't in the registry."
            else:
                broker = brokerRequest.text

        if(broker == ""):
            return
        else:
            time.sleep(1)
            print("requête : " + broker + "shareMessage | data = " + server2 + "pong")
            response = requests.get(url=broker + "shareMessage", data = server2 + "pong")
            return response.text

if __name__ == '__main__':
    requests.get(url = REGISTRY + "/setServer1", data=ADRESS + ":" + str(PORT) + "/")
    app.run(host=HOST,port=PORT)