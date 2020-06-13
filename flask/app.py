from flask import Flask
from endpoint import SingleProduct
from endpoint import SortBazaar

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/single/<productId>', methods=['GET'])
def getSingleProduct(productId):
    response = SingleProduct.getSingleProduct(productId)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)

@app.route('/sortBazaar', methods=['GET'])
def sortBazaar():
    response = SortBazaar.sortBazaar()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')