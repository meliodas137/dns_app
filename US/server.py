from flask import Flask, request
import socket
app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def get_params():
    args = request.args
    hostname = args.get('hostname')
    fs_port = args.get('fs_port')
    number = args.get('number')
    as_ip = args.get('as_ip')
    as_port = int(args.get('as_port'))

    if not args or not hostname or not fs_port or not number or not as_ip or not as_port :
        return ("Fail", 400)

    ip = getIpFromDNS(as_ip, as_port)

    return app.redirect(ip+':'+'%s/fibonacci?number=%s'%(fs_port, number))

def getIpFromDNS(as_ip, as_port):
    messageToSend = "TYPE=A \n NAME=fibonacci.com\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.sendto(str.encode(messageToSend), ('%s'%(as_ip), as_port))

    msg, server = sock.recvfrom(1024)
    msgData = msg.split("\n")
    data = {}
    for d in msgData:
        field = d.split["="]
        data[field[0]] = field[1]
    
    return data['VALUE']

app.run(host='0.0.0.0', port=8080, debug=True)