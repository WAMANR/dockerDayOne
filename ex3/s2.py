from flask import Flask, request
import requests, time, os

app = Flask(__name__)

PORT = int(os.getenv('PORT'))
S3 = os.getenv('S3')
ADRESS = os.getenv('ADRESS')
HOST = os.getenv('HOST')

@app.route('/pong', methods=['GET'])
def pong():
    # Send GET request to Server 1
    print("Server 2: Pong")
    response = requests.get(S3 + "/ping")
    return response.text

if __name__ == '__main__':
    print(S3 + "/setServer2")
    print(ADRESS + ":" + str(PORT) + "/")
    requests.get(url = S3 + "/setServer2", data=ADRESS + ":" + str(PORT) + "/")
    app.run(host=HOST,port=PORT)


