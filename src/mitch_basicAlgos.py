# Basic Algo Trading Demo

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Importing the dataset
path = os.getcwd().replace('src', 'data/')
dataset = pd.read_excel(path + 'WTIPriceData.xls')

# Simple Graph of data
date = dataset.iloc[:, 0]
price = dataset.iloc[:, 1]

plt.plot(date, price)
plt.title("WTI Crude Data")
plt.xlabel("Date")
plt.ylabel("Price")
#plt.show()

