import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('itc.csv', index_col= 'Date', parse_dates=True)
#take input from user for days
x = int(input("Enter Number of Days for SMA Calculation\n"))
#calculate mean and plot it with closing data
plt.plot(df['Close'])
plt.plot(df['Close'].rolling(window = x).mean())
plt.show()
#add Moving Average to the our file
df['SMA'] = df['Close'].rolling(window = x).mean()
print(df.head(100))