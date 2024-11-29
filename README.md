# test-fintual
This repository contains my technical test response for Fintual to solve the following problem:

```
Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.

Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.
```
Given the freedom provided by the statement, I chose Python as the language to develop the task.

## Instructions
This code was tested using Python 3.12.

You can run the project using the following command:

```
python3 main.py
```

The program will request input in the terminal for a start and end date to calculate the profits and the annualized return. The format of the dates is as follows

```
YYYY-MM-DD
ex: "2024-01-01"
```
A CSV file named stock_prices.csv is included, where each row contains the stock name, the date, and its price for that date.
```
name,date,price
A,2024-01-01,100.0
```

After execution, the terminal will look as follows:
```
Enter start date (YYYY-MM-DD): 2024-01-01
Enter end date (YYYY-MM-DD): 2024-02-28
Profit for A: -4.9
Profit for B: -4.9
Profit for C: -4.9
Total profit: -14.7
Annualized Return: -27.1067%
```
Where it displays the profit for each stock, the total profit, and the annualized return.