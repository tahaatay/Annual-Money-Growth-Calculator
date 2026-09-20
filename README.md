Annual Money Growth Calculator

A simple Python program that calculates how much money you could have after one year based on your current savings, monthly income, and monthly return rate.

The program calculates the balance month by month and displays the yearly money growth as a graph using Matplotlib.

Features
Enter your current savings
Enter your monthly income
Enter your monthly return rate
Calculate the balance for 12 months
Apply monthly compound growth
Store monthly balances for visualization
Display the yearly money change with a line graph
Colored terminal output using Colorama
Delayed output for a more interactive terminal experience
Technologies Used
Python
Colorama
Matplotlib
Time
Installation

Install the required libraries with:

pip install colorama matplotlib
How to Run

Run the Python file:

python Main.py

Then enter:

Your current savings
Your monthly income
Your monthly return rate

The program will calculate your balance for each month and display the results in a graph.

How It Works

The program starts with the user's current savings.

Each month:

The monthly income is added.
The monthly return is calculated based on the current balance.
The updated balance is saved.
The process continues until 12 months are completed.

The monthly values are then used to create a line graph showing the change in money over the year.

Example
Current savings: 10000
Monthly income: 5000
Monthly return: 10%

The program calculates the balance month by month and visualizes the growth at the end.

Project Purpose

This project was created as a Python learning project to practice:

Variables
User input
Loops
Lists
Mathematical calculations
Compound growth calculations
Data visualization
Matplotlib
Colorama
Basic project structure
Disclaimer

This program is a programming project and its calculations are for educational and illustrative purposes only. It does not provide financial advice or guarantee future returns.
