export function change_stock_price(stock_price){
    document.getElementById("stockprice").innerHTML = stock_price;

}
export function change_percentage(percentage){
    document.getElementById("percentage").innerHTML = percentage;
}

export function change_chart(stock_data){
    const xValues = stock_data.time_data;
    
    
    new Chart("stockchart", {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
            data: stock_data.stock_prices,
            borderColor: "red",
            fill: false,
            tension: 0 
        },
        
        {
            data: stock_data.short_ema,
            borderColor: "green",
            fill: false
        },

        {
            data: stock_data.long_ema,
            borderColor: "blue",
            fill: false
        },

        {
            data: stock_data.average_ema,
            borderColor: "yellow",
            fill: false
        },
    
    ]
         
      },
      options: {
        legend: {display: false}
      }
    });
}

