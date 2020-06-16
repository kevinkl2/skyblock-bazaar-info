var request = new XMLHttpRequest()

request.open('GET', 'https://api.life.bazaar.sphor.us/history/YOUNG_FRAGMENT', true)

function toTimeZone(time) {
    // console.log(time)
    // console.log(moment(time).tz("America/Los_Angeles"))
    // console.log(moment(time))
    // return(moment(time).format('LLLL'))
}

window.chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
  };

request.onload = function() {
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
                    fill: true
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
        var ctx = document.getElementById('canvas').getContext('2d');
        window.myLine = new Chart(ctx, config);
    }
}

request.send()