from flask import Flask
app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def get_params():
    args = request.args
    hostname = args.get('hostname')
    fs_port = args.get('fs_port')
    number = args.get('number')
    as_ip = args.get('as_ip')
    as_port = args.get('as_port')

    if not args or not hostname or not fs_port or not number or not as_ip or not as_port 
        abort(400)
    
    return 
