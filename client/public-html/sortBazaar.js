window.chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
  };

var app = document.getElementById('root')

var container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(container)

var request = new XMLHttpRequest()

request.open('GET', 'https://api.dev.bazaar.sphor.us/sortBazaar', true)

request.onload = function() {
    var data = JSON.parse(this.response)

    if (request.status >= 200 && request.status < 400) {
        data.forEach(product => {
            var card = document.createElement('div')
            card.setAttribute('class', 'card')

            var productName = document.createElement('h3')
            productName.setAttribute('style', 'margin-left: 5px')
            productName.textContent = product.productName

            var informationTable = document.createElement('table')
            informationTable.setAttribute('class', 'table table-bordered table-sm')

            var tableBody = document.createElement('tbody')

            var orderPrices = document.createElement('tr')
            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Lowest Sell Order'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.lowestSellOrder.toLocaleString()}`

            orderPrices.appendChild(header)
            orderPrices.appendChild(quantity)

            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Highest Buy Order'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.highestBuyOrder.toLocaleString()}`

            orderPrices.appendChild(header)
            orderPrices.appendChild(quantity)
            tableBody.appendChild(orderPrices)

            var profit = document.createElement('tr')
            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Profit'
            var quantity = document.createElement('td')
            quantity.setAttribute('style', 'font-weight: bold;')
            quantity.textContent = `${product.profit.toLocaleString()}`

            profit.appendChild(header)
            profit.appendChild(quantity)
            tableBody.appendChild(profit)

            var orderVolume = document.createElement('tr')
            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Sell Order Volume'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.sellOrderVolume.toLocaleString()}`

            orderVolume.appendChild(header)
            orderVolume.appendChild(quantity)

            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Buy Order Volume'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.buyOrderVolume.toLocaleString()}`

            orderVolume.appendChild(header)
            orderVolume.appendChild(quantity)
            tableBody.appendChild(orderVolume)

            var fulfilledVolume = document.createElement('tr')
            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Fulfilled Sell Order Volume (week)'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.fulfilledBuyOrdersMovingWeek.toLocaleString()}`

            fulfilledVolume.appendChild(header)
            fulfilledVolume.appendChild(quantity)

            var header = document.createElement('th')
            header.setAttribute('scope', 'row')
            header.textContent = 'Fulfilled Buy Order Volume (week)'
            var quantity = document.createElement('td')
            quantity.textContent = `${product.fulfilledSellOrdersMovingWeek.toLocaleString()}`

            fulfilledVolume.appendChild(header)
            fulfilledVolume.appendChild(quantity)
            tableBody.appendChild(fulfilledVolume)

            informationTable.appendChild(tableBody)

            // Sell Orders
            var sellOrderTitle = document.createElement('h5')
            sellOrderTitle.setAttribute('style', 'margin-left: 5px')
            sellOrderTitle.textContent = "Sell Orders"

            var sellOrderTable = document.createElement('table')
            sellOrderTable.setAttribute('class', 'table table-bordered table-sm')
            
            var tableHeader = document.createElement('thead')
            var headerRecord = document.createElement('tr')

            var price = document.createElement('th')
            price.setAttribute('scope', 'col')
            price.textContent = "Price Per Unit"

            var amount = document.createElement('th')
            amount.setAttribute('scope', 'col')
            amount.textContent = "Amount"

            var orders = document.createElement('th')
            orders.setAttribute('scope', 'col')
            orders.textContent = "Orders"

            headerRecord.appendChild(price)
            headerRecord.appendChild(amount)
            headerRecord.appendChild(orders)
            tableHeader.appendChild(headerRecord)
            sellOrderTable.appendChild(tableHeader)

            var tableBody = document.createElement('tbody')

            product.topSellOrders.forEach(sellOrder => {
                var bodyRecord = document.createElement('tr')

                var price = document.createElement('td')
                price.textContent = `${sellOrder.pricePerUnit.toLocaleString()}`

                var amount = document.createElement('td')
                amount.textContent = `${sellOrder.amount.toLocaleString()}`

                var orders = document.createElement('td')
                orders.textContent = `${sellOrder.orders.toLocaleString()}`

                bodyRecord.appendChild(price)
                bodyRecord.appendChild(amount)
                bodyRecord.appendChild(orders)

                tableBody.appendChild(bodyRecord)
            })

            sellOrderTable.appendChild(tableBody)

            // Buy Orders
            var buyOrderTitle = document.createElement('h5')
            buyOrderTitle.setAttribute('style', 'margin-left: 5px')
            buyOrderTitle.textContent = "Buy Orders"

            var buyOrderTable = document.createElement('table')
            buyOrderTable.setAttribute('class', 'table table-bordered table-sm')
            
            var tableHeader = document.createElement('thead')
            var headerRecord = document.createElement('tr')

            var price = document.createElement('th')
            price.setAttribute('scope', 'col')
            price.textContent = "Price Per Unit"

            var amount = document.createElement('th')
            amount.setAttribute('scope', 'col')
            amount.textContent = "Amount"

            var orders = document.createElement('th')
            orders.setAttribute('scope', 'col')
            orders.textContent = "Orders"

            headerRecord.appendChild(price)
            headerRecord.appendChild(amount)
            headerRecord.appendChild(orders)
            tableHeader.appendChild(headerRecord)
            buyOrderTable.appendChild(tableHeader)

            var tableBody = document.createElement('tbody')

            product.topBuyOrders.forEach(buyOrder => {
                var bodyRecord = document.createElement('tr')

                var price = document.createElement('td')
                price.textContent = `${buyOrder.pricePerUnit.toLocaleString()}`

                var amount = document.createElement('td')
                amount.textContent = `${buyOrder.amount.toLocaleString()}`

                var orders = document.createElement('td')
                orders.textContent = `${buyOrder.orders.toLocaleString()}`

                bodyRecord.appendChild(price)
                bodyRecord.appendChild(amount)
                bodyRecord.appendChild(orders)

                tableBody.appendChild(bodyRecord)
            })

            buyOrderTable.appendChild(tableBody)

            var chart = document.createElement('canvas')
            var request2 = new XMLHttpRequest()

            request2.open('GET', 'https://api.life.bazaar.sphor.us/history/' + product.productName, true)
            
            request2.onload = function() {
                var data = JSON.parse(this.response)

                if (request.status >= 200 && request.status < 400) {
                    var TIMESTAMPS = []
                    var PROFIT = []
                    data.forEach(entry => {
                        TIMESTAMPS.push(entry.ts)
                        PROFIT.push(entry.profit)
                    })
                    var config = {
                        type: 'line',
                        data: {
                            labels: TIMESTAMPS,
                            datasets: [{
                                label: "Profit",
                                backgroundColor: window.chartColors.red,
                                borderColor: window.chartColors.red,
                                data: PROFIT,
                                fill: false
                            }]
                        },
                        options: {
                            responsive: true,
                            title: {
                                display: true,
                                text: 'Chart.js Line Chart'
                            },
                            tooltips: {
                                mode: 'index',
                                intersect: false,
                            },
                            hover: {
                                mode: 'nearest',
                                intersect: true
                            },
                            scales: {
                                xAxes: [{
                                    display: true,
                                    scaleLabel: {
                                        display: true,
                                        labelString: 'Timestamp'
                                    }
                                }],
                                yAxes: [{
                                    display: true,
                                    scaleLabel: {
                                        display: true,
                                        labelString: 'Profit'
                                    }
                                }]
                            }
                        }
                    }
                    window.myLine = new Chart(chart, config);
                }
            }

            request2.send()

            container.appendChild(card)
            card.appendChild(productName)
            card.appendChild(informationTable)
            card.appendChild(sellOrderTitle)
            card.appendChild(sellOrderTable)
            card.appendChild(buyOrderTitle)
            card.appendChild(buyOrderTable)
            card.appendChild(chart)
        })
    } else {
        var errorMessage = document.createElement('marquee')
        errorMessage.textContent = "Error"
        app.appendChild(errorMessage)
    }
}

request.send()