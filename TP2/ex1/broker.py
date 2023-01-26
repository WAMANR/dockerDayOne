from flask import Flask, request
import requests, time, os

app = Flask(__name__)

PORT = int(os.getenv('PORT'))
REGISTRY = os.getenv('REGISTRY')
ADRESS = os.getenv('ADRESS')
HOST = os.getenv('HOST')

@app.route('/shareMessage', methods=['GET'])
def shareMessage():
    message = request.data.decode("utf-8")
    print("Share message : " + message)
    response = requests.get(message)
    return response.text

if __name__ == '__main__':
    requests.get(url = REGISTRY + "/setBroker", data=ADRESS + ":" + str(PORT) + "/")
    app.run(host=HOST,port=PORT)