from flask import Flask, request
import requests, time, os

app = Flask(__name__)

PORT = int(os.getenv('PORT'))
S3 = os.getenv('S3')
ADRESS = os.getenv('ADRESS')
HOST = os.getenv('HOST')

@app.route('/ping', methods=['GET'])
def ping():
    # Send GET request to Server 2
    print("Server 1: Ping")
    response = requests.get(S3 + "/pong")
    return response.text

if __name__ == '__main__':
    print(S3 + "/setServer1")
    print(ADRESS + ":" + str(PORT) + "/")
    requests.get(url = S3 + "/setServer1", data=ADRESS + ":" + str(PORT) + "/")
    app.run(host=HOST,port=PORT)