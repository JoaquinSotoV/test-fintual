from typing import List, Dict

class Stock:
    # The structure of a stock is the name of the stock and a dictionary with the price history
    # that has the date as the key and the price as the value
    # Example:
    # this.name = 'A'
    # this.priceHistory = {
    #       '2024-01-01': 100.0,
    #       '2024-01-02': 101.0
    #   },
    # }
    def __init__(self, name: str, priceHistory: Dict[str, float]):
        self.name = name
        self.priceHistory = priceHistory
    
    # Checks if the stock has a price for a given date and returns it
    def price (self, date: str) -> float:
        if date in self.priceHistory:
            return self.priceHistory[date]
        else:
            print(f'No price found for {self.name} on {date}')
            return None