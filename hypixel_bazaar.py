import requests
from dotenv import load_dotenv
import os

previousProduct = "ROTTEN_FLESH"

def start():
    while True:
        global previousProduct
        
        productInput = input("Product: ")

        try:
            if (productInput == "r"):
                productInput = previousProduct
                printProductInformation(singleSearch(productInput, hypixelBazaarClient()))
            elif (productInput == "s"):
                sortBazaar(hypixelBazaarClient())
            elif (productInput == ""):
                continue
            else:
                previousProduct = productInput
                printProductInformation(singleSearch(productInput, hypixelBazaarClient()))
        except Exception as e:
            print(e)
            continue

def singleSearch(productName, response):
    return(generateProductInformation(response["products"][productName]))

def sortBazaar(response):
    productStore = {}

    print(len(response["products"]))

    for product in response["products"]:
        productInformation = generateProductInformation(response["products"][product])
        if (productInformation != None):
            if (productInformation["fulfilledBuyOrdersMovingWeek"] >= 1000000):
                productStore[product] = productInformation

    sortedProducts = sorted(productStore.values(), key=lambda x:x["profit"], reverse=True)

    for product in sortedProducts[:10]:
        printProductInformation(product)

def generateProductInformation(product_data):
    if ((len(product_data["sell_summary"]) == 0) or (len(product_data["buy_summary"]) == 0)):
        return None

    lowestBuyOrder = product_data["sell_summary"][0]["pricePerUnit"]
    highestSellOrder = product_data["buy_summary"][0]["pricePerUnit"]
    tax = .01

    profit = ((highestSellOrder-0.1)*(1-tax))-(lowestBuyOrder+0.1)

    return({"productName": product_data["product_id"],
            "lowestBuyOrder": lowestBuyOrder,
            "highestSellOrder": highestSellOrder,
            "profit": profit,
            "buyOrderVolume": product_data["quick_status"]["sellVolume"],
            "sellOrderVolume": product_data["quick_status"]["buyVolume"],
            "fulfilledBuyOrdersMovingWeek": product_data["quick_status"]["sellMovingWeek"],
            "fulfilledSellOrdersMovingWeek": product_data["quick_status"]["buyMovingWeek"],
            "topBuyOrders": product_data["sell_summary"][:3],
            "topSellOrders": product_data["buy_summary"][:3]})

def printProductInformation(product):
        print("Product: {}".format(product["productName"]))
        print("Lowest Buy Order: {:,}".format(product["lowestBuyOrder"]))
        print("Highest Sell Order: {:,}".format(product["highestSellOrder"]))
        print("\033[1m Profit: {:,} \033[0m".format(product["profit"]))
        print("Sell Order Volume: {:,}".format(product["sellOrderVolume"]))
        print("Buy Order Volume: {:,}".format(product["buyOrderVolume"]))
        print("Fulfilled Buy Orders Volume Moving Week: {:,}".format(product["fulfilledBuyOrdersMovingWeek"]))
        print("Fulfilled Sell Orders Volume Moving Week: {:,}".format(product["fulfilledSellOrdersMovingWeek"]))

        print("Top Buy Orders: ")
        for order in product["topBuyOrders"]:
            for field in order:
                order[field] = "{:,}".format(order[field])
            print("     {}".format(order))

        print("Top Sell Orders: ")
        for order in product["topSellOrders"]:
            for field in order:
                order[field] = "{:,}".format(order[field])
            print("     {}".format(order))

        print()

def hypixelBazaarClient():
    load_dotenv()
    response = requests.get("https://api.hypixel.net/skyblock/bazaar?key={}".format(os.getenv("API_KEY")))

    if (response.status_code != 200):
        raise Exception("API error")

    response = response.json()

    return(response)

if __name__ == "__main__":
    start()