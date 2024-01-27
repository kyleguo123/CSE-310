from binance.client import Client
from key import api_key, api_secret
import time
import matplotlib.pyplot as plt
import numpy as np

client = Client(api_key, api_secret)
# using my personal account to get info from client
stock_symbol= "ETHUSDT"


def get_historical_klines():
    # create a function with pramerter
    global stock_symbol 
    # set my variable that it can find it outside of the fucntion
    historical_klines = client.get_historical_klines(stock_symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    klinesArray = []
    # create a empty array
    for i in range(len(historical_klines)-1):
        klinesArray.append(float(historical_klines[len(historical_klines)-i-1][4]))
    return klinesArray
    # get 1 day ago to current time history from Client. 
    # create a for loop that to Length. using append funciton that adding the newest price and other prices(depend on the length) into klinesArray.

def get_current_price():
    global stock_symbol
    current_price_info = client.get_symbol_ticker(symbol=stock_symbol)
    current_price = float(current_price_info['price'])
    print(current_price)
    return current_price
    

def getEMAtime_preiod(Length,historical_klines):

    klinesArray = []
    # create a empty array
    for i in range(Length):
        klinesArray.append(historical_klines[i])
    return klinesArray

def EmaLines(Length,Numbers):
    # EMA fuction
    Weight=Length 
    average=0
    divider=0
    # create three variables

    # This will count the leanth of the array
    for i in range(Length):
        Price=Numbers[i]
        
        WPrice=Price*Weight
        divider+=Weight
        average+=WPrice
        Weight-=1
        
    return(average/divider)

def drawchart(timeArray,priceArray,shortArray,longArray,averageArray):
    plt.clf()  # Clear the current plot
    timepoints = np.array(timeArray)
    pricepoints = np.array(priceArray)
    shortpoints = np.array(shortArray)
    longpoints = np.array(longArray)
    averagepoints = np.array(averageArray)
    plt.plot(timepoints,pricepoints, color='red',label = "price")
    plt.plot(timepoints,shortpoints, color='blue',label = "short")
    plt.plot(timepoints,longpoints, color='orange',label = "long")
    plt.plot(timepoints,averagepoints, color='green',label = "average")
    plt.legend(loc="upper left")
    plt.show()
    plt.pause(0.1)  # Add a short pause to allow the plot to update
    


def main():

    ShortLine = 8
    LongLine = 13
    AverageLine = 50
    nextaction= "buy"
    maxdatapoint = 100
    # simulation
    boughtprice= 0
    profit = 0
    # chart variable
    priceArray = []
    shortArray = []
    longArray = []
    averageArray = []
    timeArray = []
    currenttime = 0
    historical_klines = get_historical_klines()
    
    plt.ion()  # Enable interactive mode
    # ... (rest of your code)
    while True:
        
        ShortLineArray=getEMAtime_preiod(ShortLine,historical_klines)
        ShortLineEMA=EmaLines(ShortLine,ShortLineArray)
        currentprice= get_current_price()

        LongLineArray=getEMAtime_preiod(LongLine,historical_klines)
        LongLineEMA=EmaLines(LongLine,LongLineArray)

        AverageLineArray=getEMAtime_preiod(AverageLine,historical_klines)
        AverageLineEMA=EmaLines(AverageLine,AverageLineArray)
        

        if ShortLineEMA > LongLineEMA and LongLineEMA > AverageLineEMA and nextaction == "sell":
            nextaction = "buy"
            profit += currentprice - boughtprice
            print("Sell","Current price", currentprice,"Profit",profit)

        elif ShortLineEMA < LongLineEMA and ShortLineEMA < AverageLineEMA and nextaction == "buy":
            nextaction = "sell"
            boughtprice = currentprice
            print("Buy", "Current price", currentprice)

        else:
            print("No trading going yet")
            
     
        priceArray.append(currentprice)
        shortArray.append(ShortLineEMA)
        longArray.append(LongLineEMA)
        averageArray.append(AverageLineEMA)
        timeArray.append(currenttime)

        if len(timeArray)-1 > maxdatapoint:
            priceArray.pop(len(priceArray)-1)
            shortArray.pop(len(shortArray)-1)
            longArray.pop(len(longArray)-1)
            averageArray.pop(len(averageArray)-1)
            timeArray.pop(len(timeArray)-1)

        currenttime +=1
        drawchart(timeArray,priceArray,shortArray,longArray,averageArray)
        historical_klines.append(currentprice)
        historical_klines.pop(len(historical_klines)-1)

        time.sleep(5)
main()