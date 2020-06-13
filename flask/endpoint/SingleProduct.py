from util import client
from util import ProductInformation
from flask import jsonify
from flask import abort

def getSingleProduct(productId):
    try:
        clientResponse = client.hypixelBazaarClient()["products"][productId]
        information = ProductInformation.generateProductInformation(clientResponse)
        return(jsonify(information))
    except Exception as e:
        abort(400, e)