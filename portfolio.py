from typing import List
from stock import Stock
from datetime import datetime


class Portfolio:
    def __init__(self, stocks: List[Stock]):
        self.stocks = stocks
    
    # Calculates the profit of the portfolio between two dates for each stock and adds them up
    def profit(self, startDate: str, endDate: str) -> float:
        if self.checkDates(startDate, endDate) == False:
            return None

        profit: float = 0.0
        for stock in self.stocks:
            startPrice = stock.price(endDate)
            endPrice = stock.price(startDate)
            
            if startPrice is not None and endPrice is not None:
                stockProfit = startPrice - endPrice
                print(f'Profit for {stock.name}: {round(stockProfit, 2)}')
                profit += stockProfit
                
            elif startPrice is None:
                print(f'No price found for {stock.name} on {endDate}')
            
            elif endPrice is None:
                print(f'No price found for {stock.name} on {startDate}')
            
        print(f'Total profit: {round(profit, 2)}')
        
        return profit
    
    # Calculates the annualized return of the portfolio between two dates
    # The formula used is: ((endPrice / startPrice) ^ (365 / amount of days between the dates)) - 1
    def annualizedReturn(self, startDate: str, endDate: str) -> float:
        if self.checkDates(startDate, endDate) == False:
            return None
        
        startTotalPrice = 0.0
        endTotalPrice = 0.0
        for stock in self.stocks:
            startTotalPrice += stock.price(startDate)
            endTotalPrice += stock.price(endDate)
        
        startDateTime = datetime.strptime(startDate, '%Y-%m-%d')
        endDateTime = datetime.strptime(endDate, '%Y-%m-%d')
        
        days = (endDateTime - startDateTime).days
        
        finalReturn = ((endTotalPrice / startTotalPrice) ** (365 / days)) - 1
        
        print(f'Annualized Return: {round(finalReturn * 100, 4)}%')
        
        return finalReturn
    
    def checkDates(self, startDate: str, endDate: str) -> bool:
        for stock in self.stocks:
            if startDate not in stock.priceHistory:
                print(f'No price found for {stock.name} on {startDate}')
                return False
            if endDate not in stock.priceHistory:
                print(f'No price found for {stock.name} on {endDate}')
                return False
        return True