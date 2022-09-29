from flask import Flask, request
from encodings import utf_8
from pandas import pandas as pd
import socket

app = Flask(__name__)
columns  = ['TYPE', 'NAME', 'VALUE', 'TTL']

UDP_PORT = 53533

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', UDP_PORT))

while True:
    print("In ASSSSSS")
    message, address = server_socket.recvfrom(1024)
    msgData = message.decode('utf8').split("\n")
    print(message)
    data = []
    for d in msgData:
        field = d.split("=")
        if(len(field) == 2 and field[0].strip() != ""):
            data.append(field[1].strip())
    
    if len(data) == 4:
        print(data)
        df = pd.DataFrame([data])
        print(df)
        df.to_csv('.\AS\db.csv', mode='a', header=columns, index=False)
        server_socket.sendto(str.encode("success"), address)
    
    if len(data) == 2:
        df = pd.read_csv('.\AS\db.csv')
        a_dict = (df.loc[df['NAME'] == data['NAME']]).to_dict(orient='reccords')
        response = ""
        for key in a_dict:
            response = response + key + "=" + a_dict[key]+"\n"

        server_socket.sendto(str.encode(response), address)

    server_socket.sendto(str.encode("Fails"), address)