import numpy as np

def simulation(buyDate, holdLength, money, dates, prices, windowSize):
    dateTest = []
    profit = []
    for buyDate in range(500, prices.size - holdLength - 1):
        dateTest.append(dates.iloc[buyDate])
        weekPrices = prices.iloc[buyDate - windowSize:buyDate]
        weekMean = np.average(weekPrices)
        totalMean = np.average(prices.iloc[0:buyDate-1])
        if(weekMean < totalMean):
            numContracts = np.floor(money / prices.iloc[buyDate])
            profit.append((prices.iloc[buyDate + holdLength] - prices.iloc[buyDate]) * numContracts)
        else:
            profit.append(0)
    totalProfit = np.sum(profit)/len(profit)
    return dateTest, profit, totalProfit

def annualizedReturns(startYear, endYear, profit, startIndex):
    annualProfit = sum(profit[startYear - startIndex:endYear - startIndex])
    return annualProfit




    
    
    