from flask import Flask
import socket
app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    body = app.request.json
    hostname = body['hostname']
    ip = body['ip']
    as_ip = body['as_ip']
    as_port = body['as_port']


    messageToSend = "TYPE=A \n NAME=fibonacci.com \n VALUE=%s \n TTL=10 \n"%ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str.encode(messageToSend), ('0.0.0.0', 53533))

    response = sock.recvfrom(1024)
    if(response == "success"): return (response, 201)
    return ("Fail", 400)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    args = app.request.args
    number = args.get('number')
    if(not isinstance(number, int)):
        return ("Fail", 400)
    
    return (getFibonacci(number), 200)

def getFibonacci(X):
    if X <= 1: return X
    return getFibonacci(X-1)+getFibonacci(X-2)

app.run(host='0.0.0.0', port=9090, debug=True)