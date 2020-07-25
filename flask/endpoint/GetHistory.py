from util import client
from util import ProductInformation
from flask import jsonify
from flask import abort

def getHistory(productId, mysql):
    try:
        return(jsonify(selectFromDb(productId, mysql)))
    except Exception as e:
        abort(500, e)

def selectFromDb(productId, mysql):
    try:
        con = mysql.connection
        cur = con.cursor()

        cur.execute("SELECT * FROM `bazaar`.`productStats` WHERE `name`=%s", (productId,))
        result = cur.fetchall()
        
        return(result)
    except Exception as e:
        print(e)