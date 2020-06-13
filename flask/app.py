from flask import Flask
from flask import jsonify
import client

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/single/<productId>', methods=['GET'])
def getSingleProduct(productId):
    return(jsonify(client.hypixelBazaarClient()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')