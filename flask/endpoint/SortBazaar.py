from util import client
from util import ProductInformation
from flask import jsonify
from flask import abort

def sortBazaar(mysql):
    try:
        clientResponse = client.hypixelBazaarClient()

        productStore = {}

        for product in clientResponse["products"]:
            productInformation = ProductInformation.generateProductInformation(clientResponse["products"][product])
            if (productInformation != None):
                # if (productInformation["fulfilledBuyOrdersMovingWeek"] >= 1000000):
                productStore[product] = productInformation

        insertToDb(productStore, mysql)

        sortedProducts = sorted(productStore.values(), key=lambda x:x["profit"], reverse=True)

        return(jsonify(sortedProducts))
    except Exception as e:
        abort(500, e)

def insertToDb(productStore, mysql):
    try:
        con = mysql.connection
        cur = con.cursor()
        # cur.execute('SET autocommit = 0')
        # con.commit()

        for product in productStore:
            product = productStore[product]
            cur.execute("INSERT INTO `bazaar`.`productStats`(`name`,`lowestSellOrderPrice`,`highestBuyOrderPrice`,`profit`,`sellOrderVolume`,`buyOrderVolume`,`fulfilledSellOrderVolumeWeek`,`fulfilledBuyOrderVolumeWeek`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (product["productName"], product["lowestSellOrder"], product["highestBuyOrder"], product["profit"], product["sellOrderVolume"], product["buyOrderVolume"], product["fulfilledSellOrdersMovingWeek"], product["fulfilledBuyOrdersMovingWeek"]))

        # cur.execute('SET autocommit = 1')
        con.commit()
    except Exception as e:
        print(e)