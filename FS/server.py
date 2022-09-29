from flask import Flask, request
import socket
import json
app = Flask(__name__)

@app.route('/register', methods=['PUT'], strict_slashes=False)
def register():
    raw_data = request.get_data().decode('utf8')
    body = json.loads(raw_data)
    print(body)
    print("HERE22222")
    hostname = body['hostname']
    ip = body['ip']
    as_ip = body['as_ip']
    as_port = int(body['as_port'])


    messageToSend = "TYPE=A \n NAME=%s \n VALUE=%s \n TTL=10 \n"%(hostname, ip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('%s'%(as_ip), as_port)
    sock.sendto(str.encode(messageToSend), ('%s'%(as_ip), as_port))
    print("RESPONSEEE")
    response = sock.recvfrom(1024)[0].decode('utf8')
    print(response)
    if(response == "success"): return (response, 201)
    return ("Fail", 400)


@app.route('/fibonacci', methods=['GET'], strict_slashes=False)
def fibonacci():
    print("HERRRRREEEE")
    args = request.args
    number = int(args.get('number'))
    print(number)
    if(not isinstance(number, int)):
        return ("Fail", 400)
    
    response = getFibonacci(number)
    print(response)
    return (str(response), 200)

def getFibonacci(X):
    if X <= 1: return X
    print(X, "########")
    return getFibonacci(X-1)+getFibonacci(X-2)

app.run(host='127.0.0.1', port=9090, debug=True)