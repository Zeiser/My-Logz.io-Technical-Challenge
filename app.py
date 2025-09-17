import logging
from flask import Flask, request, jsonify

# Configure logging to output to stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    if name:
        message = f'Hello "{name}"'
        logging.info(f"method=GET path=/?name={name} status=200 name_provided=true")
        return message
    else:
        message = "Hello World"
        logging.info("method=GET path=/ status=200 name_provided=false")
        return message

@app.route('/healthz')
def healthz():
    # A simple health check endpoint
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify



# Configure logging to output to stdout

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



app = Flask(__name__)



@app.route('/')

def hello():
    name = request.args.get('name')
    if name:
     message = f'Hello "{name}"'
     logging.info(f"method=GET path=/?name={name} status=200 name_provided=true")
     return message
    else:
     message = "Hello World"
     logging.info("method=GET path=/ status=200 name_provided=false")
     return message



@app.route('/healthz')

def healthz():
    # A simple health check endpoint
    return jsonify(status="ok"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
