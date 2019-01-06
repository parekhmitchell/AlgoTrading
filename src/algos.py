import pandas as pd
import matplotlib.pyplot as plt
import algosFunctions as fnc

## Project Path
myPath = "C:/Users/ianha/OneDrive/Documents/Misc/QuantFinance/AlgoTrading/"

## Load, clean, and plot data
df = pd.read_excel(myPath + 'data/WTIPriceData.xls')
df = df.dropna()
dates = df["observation_date"]
prices = df["DCOILWTICO"]
fig0 = plt.figure(0)
plt.plot(dates, prices)
plt.title("All Original WTI Crude Data")
plt.xlabel("Date")
plt.ylabel("Price/Contract ($)")

## Split data into years
start2014 = 10
end2014 = 261
start2015 = 262
end2015 = 513
start2016 = 514
end2016 = 765
start2017 = 766
end2017 = 1015

## Define time spans
oneWeek = 5
twoWeek = 10
threeWeek = 15
fourWeek = 20

## Set simulation parameters
startIndex = 261
holdLength = 20
money = 10000

## Run simulation and plot total profits for one week check
dateTestOne, profitOne, totalProfitOne = fnc.simulation(startIndex, holdLength, money, dates, prices, oneWeek)
print("Profit using one week mean: %s" % totalProfitOne)
fig1 = plt.figure(1)
plt.plot(dateTestOne, profitOne)
plt.title("Profit Using One Week")
plt.xlabel("Date")
plt.ylabel("Profit ($)")
returns2014 = fnc.annualizedReturns(start2015, end2015, profitOne, startIndex)


## Run simulation and plot total profits for two week check
dateTestTwo, profitTwo, totalProfitTwo = fnc.simulation(startIndex, holdLength, money, dates, prices, twoWeek)
print("Profit using two week mean: %s" % totalProfitTwo)
fig1 = plt.figure(2)
plt.plot(dateTestTwo, profitTwo)
plt.title("Profit Using Two Weeks")
plt.xlabel("Date")
plt.ylabel("Profit ($)")


## Run simulation and plot total profits for three week check
dateTestThree, profitThree, totalProfitThree = fnc.simulation(startIndex, holdLength, money, dates, prices, threeWeek)
print("Profit using three week mean: %s" % totalProfitThree)
fig1 = plt.figure(3)
plt.plot(dateTestThree, profitThree)
plt.title("Profit Using Three Weeks")
plt.xlabel("Date")
plt.ylabel("Profit ($)")

## Run simulation and plot total profits for four week check
dateTestFour, profitFour, totalProfitFour = fnc.simulation(startIndex, holdLength, money, dates, prices, fourWeek)
print("Profit using four week mean: %s" % totalProfitFour)
fig1 = plt.figure(4)
plt.plot(dateTestFour, profitFour)
plt.title("Profit Using Four Weeks")
plt.xlabel("Date")
plt.ylabel("Profit ($)")

plt.show()
