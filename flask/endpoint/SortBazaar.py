from util import client
from util import ProductInformation
from flask import jsonify
from flask import abort

def sortBazaar():
    try:
        clientResponse = client.hypixelBazaarClient()

        productStore = {}

        for product in clientResponse["products"]:
            productInformation = ProductInformation.generateProductInformation(clientResponse["products"][product])
            if (productInformation != None):
                if (productInformation["fulfilledBuyOrdersMovingWeek"] >= 1000000):
                    productStore[product] = productInformation

        sortedProducts = sorted(productStore.values(), key=lambda x:x["profit"], reverse=True)

        return(jsonify(sortedProducts))
    except Exception as e:
        abort(500, e)