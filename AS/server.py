from encodings import utf_8
from pandas import pd
import socket
import csv

app = Flask(__name__)
columns  = ('TYPE', 'NAME', 'VALUE', 'TTL')



UDP_PORT = 53533

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', UDP_PORT))

while True:
    message, address = server_socket.recvfrom(1024)
    msgData = message.split("\n")
    data = {}
    for d in msgData:
        field = d.split["="]
        data[field[0]] = field[1]
    
    if len(data) == 5:
        df = pd.DataFrame(data=data, index=columns)
        df.to_csv('db.csv', mode='a')
        server_socket.sendto(str.encode("success"), address)
    
    if len(data) == 2:
        df = pd.read_csv('db.csv')
        a_dict = (df.loc[df['NAME'] == data['NAME']]).to_dict(orient='reccords')
        response = ""
        for key in a_dict:
            response = response + key + "=" + a_dict[key]+"\n"

        server_socket.sendto(str.encode(response), address)

    


# @app.route('/fibonacci', methods=['GET'])