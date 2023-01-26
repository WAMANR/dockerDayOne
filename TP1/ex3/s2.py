from flask import Flask, request
import requests, time, os

app = Flask(__name__)

PORT = int(os.getenv('PORT'))
REGISTRY = os.getenv('REGISTRY')
ADRESS = os.getenv('ADRESS')
HOST = os.getenv('HOST')
global server1
global broker
broker = ""
server1 = ""

@app.route('/pong', methods=['GET'])
def pong():
    global server1, broker
    print("Server 2: Pong")
    if(server1 == ""):
        server1Request = requests.get(REGISTRY + "/getServer1")
        if(server1Request.text == ""):
            print("Server 1 isn't in the registry.")
            return "Server 1 isn't in the registry."
        else:
            server1 = server1Request.text
    if(server1 == ""):
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
            print("requête : " + broker + "shareMessage | data = " + server1 + "ping")
            response = requests.get(url=broker + "shareMessage", data = server1 + "ping")
            return response.text

if __name__ == '__main__':
    requests.get(url = REGISTRY + "/setServer2", data=ADRESS + ":" + str(PORT) + "/")
    app.run(host=HOST,port=PORT)


