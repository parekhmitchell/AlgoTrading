## Basic Algo Trading Demo

# Import libraries
from mitch_tradingAccount import tradingAccount
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Importing the dataset
path = os.getcwd().replace('src', 'data/');
df = pd.DataFrame(pd.read_excel(path + 'WTIPriceData.xls'));
df = df.dropna();

# Initializing Variables
date = df.iloc[:, 0];
price = df.iloc[:, 1];

startBalance = 100000;
smallMA = 30;
largeMA = 90;

# Simple Graph of data
plt.plot(date, price);
plt.title("WTI Crude Data");
plt.xlabel("Date");
plt.ylabel("Price");
#plt.show();

# Create trading account and run mean reversion algo
account = tradingAccount(startBalance);

sdMA = pd.DataFrame(np.zeros(price.size));
ldMA = pd.DataFrame(np.zeros(price.size));

count = 0;
for i in price:
	if(count >= smallMA - 1):
		sdMA.iloc[count] = price.iloc[count-smallMA-1:count+1].mean();
	if(count >= largeMA - 1):
		ldMA.iloc[count] = price.iloc[count-largeMA-1:count+1].mean();

		if(sdMA.iloc[count, 0] >= ldMA.iloc[count, 0]):
			account.liquidate(i);
		else:
			account.buyAll(i);

	count += 1;
	print(account.getBalance());

account.liquidate(i);
print(account.getBalance());

plt.plot(date, sdMA, 'r')
plt.plot(date, ldMA, 'b')
#plt.show()
