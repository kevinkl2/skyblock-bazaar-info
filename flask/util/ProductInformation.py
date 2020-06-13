def generateProductInformation(product_data):
    if ((len(product_data["sell_summary"]) == 0) or (len(product_data["buy_summary"]) == 0)):
        return None

    highestBuyOrder = product_data["sell_summary"][0]["pricePerUnit"]
    lowestSellOrder = product_data["buy_summary"][0]["pricePerUnit"]
    tax = .01

    profit = ((lowestSellOrder-0.1)*(1-tax))-(highestBuyOrder+0.1)

    return({"productName": product_data["product_id"],
            "highestBuyOrder": highestBuyOrder,
            "lowestSellOrder": lowestSellOrder,
            "profit": profit,
            "buyOrderVolume": product_data["quick_status"]["sellVolume"],
            "sellOrderVolume": product_data["quick_status"]["buyVolume"],
            "fulfilledBuyOrdersMovingWeek": product_data["quick_status"]["sellMovingWeek"],
            "fulfilledSellOrdersMovingWeek": product_data["quick_status"]["buyMovingWeek"],
            "topBuyOrders": product_data["sell_summary"][:3],
            "topSellOrders": product_data["buy_summary"][:3]})