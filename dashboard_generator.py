"""
@author: annieyin
"""

# dashboard_generator.py
import os
import sys
import csv
import plotly

# define function to convert USD
def tousd(total_sale):
    return f"${total_sale:,.2f}"

print("-----------------------")
# prompt user input for month selection
# reference a file in the "data" directory
# ... adapted from: https://github.com/Annieyinx1/intro-to-python/data/monthly-sales
#csv_filepath = os.path.join(os.path.dirname(__file__), ".","intro-to-python", csv_filename)



print("MONTH")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")