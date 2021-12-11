#This simply imports a yahoo finance library which utilizes an API to pull stock data
import yfinance as yf
import pandas as pd

#Ask the user to input the stock ticker they would like to view
Ticker = input("Enter the ticker of the stock you would like to research: ")

Stock = yf.Ticker(Ticker)
Stock.history(period="max")

#Set up variable for chosen companies balance sheet
bs = Stock.balance_sheet

#Set up a simple dataframe outputting example financial metrics
df = pd.DataFrame([
    round(bs.loc["Total Current Assets"][0] / bs.loc["Total Current Liabilities"][0], 2),
    round((bs.loc["Total Current Assets"][0] - bs.loc["Inventory"][0]) / bs.loc["Total Current Liabilities"][0], 2)],
    
    index=['Current Ratio', 'Quick Ratio'],
    columns=['Value'])
df.index.name = "Metric"
print(df)

#Print out 10 most recent analyst recommendations for this stock
print(Stock.recommendations.tail(10))