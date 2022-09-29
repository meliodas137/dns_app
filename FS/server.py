from flask import Flask
import socket
app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    body = request.json
    hostname = body['hostname']
    ip = body['ip']
    as_ip = body['as_ip']
    as_port = body['as_port']


    messageToSend = "TYPE=A NAME=fibonacci.com VALUE=%s TTL=10"%ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str.encode(messageToSend), ('0.0.0.0', 53533))

    response = sock.recv(1024)
    if(response == "success") return response 201
    abort(400)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    args = request.args
    number = args.get('number')
    if(not isinstance(i, int)):
        abort(400)
    
    return getFibonacci(number) 201

def getFibonacci(X):
    if X <= 1 return X
    return getFibonacci(X-1)+getFibonacci(X-2)

app.run(host='0.0.0.0', port=9090, debug=True)