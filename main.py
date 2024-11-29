from stock import Stock
from portfolio import Portfolio
import csv

def main():
    with open('stock_prices.csv', mode='r') as file:
        reader = csv.DictReader(file)
        
        stocksData = {}
        for row in reader:
            name = row['name']
            date = row['date']
            price = row['price']
            
            if name not in stocksData:
                stocksData[name] = {date: float(price)}
            else:
                stocksData[name][date] = float(price)
    
    stocks = []
    for name, priceHistory in stocksData.items():
        stocks.append(Stock(name, priceHistory))
    
    portfolio = Portfolio(stocks)
    
    startDate = input('Enter start date (YYYY-MM-DD): ') #'2024-01-01'
    
    endDate =  input('Enter end date (YYYY-MM-DD): ') #'2024-02-28'
    
    portfolio.profit(startDate, endDate)
    
    portfolio.annualizedReturn(startDate, endDate)
            
if __name__ == "__main__":
    main()