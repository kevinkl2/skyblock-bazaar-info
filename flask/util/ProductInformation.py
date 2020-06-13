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