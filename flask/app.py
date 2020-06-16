from flask import Flask
from flask_mysqldb import MySQL
from endpoint import SingleProduct
from endpoint import SortBazaar
from endpoint import GetHistory

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql_db_container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'bazaar'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

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
    response = SortBazaar.sortBazaar(mysql)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)

@app.route('/history/<productId>', methods=['GET'])
def getHistory(productId):
    response = GetHistory.getHistory(productId, mysql)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')