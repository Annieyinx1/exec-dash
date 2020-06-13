"""
@author: annieyin
"""

# dashboard_generator.py
import os
import sys
import pandas as pd
import operator as op
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = "browser"


# define function to convert USD
def tousd(total_sale):
    return f"${total_sale:,.2f}"


print("-----------------------")
# prompt user input for month selection
csv_file_path = os.path.join(os.path.dirname(__file__),"data")
input_list = os.listdir(csv_file_path)

for file_name in input_list:
    print(file_name)
user_input = input("Select month (yyyymm) from list above:")

# validation
file_name = 'sales-' + user_input + '.csv'
if file_name not in input_list:
    sys.exit("Hey, didn't find a file at that location")

print("-----------------------")
print("CRUNCHING THE DATA...")
# read csv
df = pd.read_csv(csv_file_path + '/' + file_name)

# validating header
# should contain 'date', 'product', 'unit price', 'units sold', 'sales price'
header = ['date', 'product', 'unit price', 'units sold', 'sales price']
for head in list(df.columns):
    if head not in header:
        sys.exit("Oh, the selected file contains unexpected headers. Please try again.")

print("-----------------------")
# calculate total monthly sales
total_monthly_sales = df["sales price"].sum()
print("TOTAL MONTHLY SALES: " + tousd(total_monthly_sales))


print("-----------------------")
# find unique product
unique_product_name = df["product"].unique()

# loop through df to find sales for each product
top_sellers = []
for product_name in unique_product_name:
    matching_sales = df[df["product"] == product_name]["sales price"]
    product_monthly_sales = matching_sales.sum()
    # print(type(product_monthly_sales)) #> FYI: <class 'numpy.float64'> which is like a normal float. possible to convert, but maybe not necessary...
    top_sellers.append(
        {"name": product_name, "monthly_sales": product_monthly_sales})
top_sellers = sorted(top_sellers, key=op.itemgetter("monthly_sales"), reverse=True)

# print top sellers
print("TOP SELLING PRODUCTS:")
for i in range(0,len(top_sellers)):
    product = top_sellers[i]["name"]
    sales = tousd(top_sellers[i]["monthly_sales"])
    print(f" {i+1}) {product}: {sales}") 

print("-----------------------")
print("VISUALIZING THE DATA...")
x_axis = []
y_axis = []

for d in top_sellers:
    x_axis.append(tousd(d["monthly_sales"]))
    y_axis.append(d["name"])

# plot bar chart
fig = go.Figure(data=[go.Bar(
        x=x_axis,y=y_axis,
        text=x_axis,
        textposition='auto',
        orientation='h'
        )])
fig['layout']['yaxis']['autorange'] = "reversed"
fig.update_layout(
    title='Top Selling Products (' + user_input + ')',
    xaxis_title='Monthly Sales (USD)',
    yaxis_title='Product')
fig.show()
