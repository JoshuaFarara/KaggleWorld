import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Display title and header
st.title("Coffee Sales EDA and Insights")
st.image("./assets/coffee-image.jpeg", caption="Coffee Image")
st.header("About Author")
st.markdown("""
**Author:** Joshua Farara

**Project:** Coffee Sales EDA

### Contact Info
- Email: [joshua.farara@gmail.com](mailto:joshua.farara@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/joshuafarara/)
- [Facebook](https://www.facebook.com/josh.farara/)
- [Twitter](https://x.com/FararaTheArtist)
- [Github](https://github.com/JoshuaFarara)
""")

# About Data
st.header("About Data")
st.markdown("""
**Title:** Dataset Title

**Dataset:** [Link](https://www.kaggle.com/datasets/ihelon/coffee-sales/data)

**Description:** This dataset contains detailed records of coffee sales from a vending machine. It is intended for analysis of purchasing patterns, sales trends, and customer preferences related to coffee products.

### Dataset Columns Names
Features: 'date', 'datetime', 'cash_type', 'card', 'money', 'coffee_name'

**Source:** Yaroslav Isaienkov @ihelon

**Collection Methodology:** The dataset spans from March 2024 to June 2024, capturing daily transaction data. And it's continue added new information.

**License:** CC0: Public Domain
""")

# Load Data
df = pd.read_csv('./data/coffee_sales_data.csv')
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

# Display Data Overview
st.header("Data Overview")
st.write(df.head())

# Rename columns
df.rename(columns={'cash_type':'payment_type', 'card':'card_number', 'money':'amount_paid_uah'}, inplace=True)

# Create Time Column
df[['new_date', 'time']] = df['datetime'].str.split(' ', n=1, expand=True)
df = df.drop(['new_date'], axis=1)

# Convert datetime Column from object to datetime64 dtype
df['datetime']= pd.to_datetime(df['datetime'])

# Creating hour, day, month columns
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# Convert amount_paid_uah to USD
UAH_to_USD = 0.024
df['amount_paid_usd'] = df['amount_paid_uah'] * UAH_to_USD

# Restructure dataframe order
df = df[['date', 'datetime','time', 'hour', 'day', 'month', 'payment_type', 'card_number', 'amount_paid_uah', 'amount_paid_usd', 'coffee_name']]

# Analytical Questions
st.header("Analytical Questions")
st.markdown("""
1. Total Revenue
2. Total Sales per Coffee 
3. Average amount paid per cup 
4. Average amount paid per cup for each coffee type in UAH
5. Which coffee had the highest/lowest sales?
6. Number of coffee sales for each coffee name?
7. Sales by Transaction Date
8. Dates With the Highest Number of sales?
9. Coffee Sales by Hour of the Day
10. Coffee sales by hour of the day per coffee type
11. How many coffees sold in the morning, afternoon, evening?
12. Which coffee is sold most/least during the week/weekend?
13. Card Numbers With the Most Purchases
14. Total amount spent by each card numbers
15. Coffees Bought by each buyer
16. What is the ratio amongst card consumers and cash consumers?
""")

# Sales Analysis
st.header("Sales Analysis")
total_revenue_uah = df['amount_paid_uah'].sum()
total_revenue_usd = df['amount_paid_usd'].sum()
st.write(f"Total Revenue (UAH): {total_revenue_uah}, Total Revenue (USD): {total_revenue_usd}")

# Plot total revenue
fig, ax = plt.subplots()
ax.bar(['Total Revenue (UAH)', 'Total Revenue (USD)'], [total_revenue_uah, total_revenue_usd], color=['blue', 'green'])
ax.set_xlabel('Currency')
ax.set_ylabel('Total Revenue')
ax.set_title('Total Revenue in UAH and USD')
st.pyplot(fig)

# Total Sales per Coffee Type in UAH
grouped_coffee = df.groupby('coffee_name')
total_revenue_per_coffee_type_uah = grouped_coffee['amount_paid_uah'].sum().sort_values(ascending=False)
st.write(total_revenue_per_coffee_type_uah)

# Plot total sales per coffee type in UAH
fig, ax = plt.subplots()
ax.bar(total_revenue_per_coffee_type_uah.index, total_revenue_per_coffee_type_uah, alpha=0.7, color='brown')
ax.set_xlabel('Coffee Name')
ax.set_ylabel('Total Amount Paid (UAH)')
ax.set_title('Total Revenue per Coffee Type in UAH')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Average Amount Paid per Cup
average_amount_paid_uah = grouped_coffee['amount_paid_uah'].mean()
average_amount_paid_usd = grouped_coffee['amount_paid_usd'].mean()
st.write(average_amount_paid_uah)
st.write(average_amount_paid_usd)

# Plot average amount paid per cup for each coffee type in UAH and USD
fig, ax = plt.subplots()
ax.bar(average_amount_paid_uah.index, average_amount_paid_uah, alpha=0.7, label='UAH', color='blue')
ax.bar(average_amount_paid_usd.index, average_amount_paid_usd, alpha=0.7, label='USD', color='red', width=0.4)
ax.set_xlabel('Coffee Name')
ax.set_ylabel('Average Amount Paid')
ax.set_title('Average Amount Paid per Cup for Each Coffee Type (UAH and USD)')
ax.legend()
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Number of Coffees Sold for each Coffee Name
number_of_sales_by_coffee_name = df['coffee_name'].value_counts()
st.write("Number of Coffees Sold for each Coffee Name:", number_of_sales_by_coffee_name)

# Plot Number of Coffees Sold for each Coffee Name
fig, ax = plt.subplots()
number_of_sales_by_coffee_name.plot(kind='bar', color='brown', ax=ax)
ax.set_title('Number of Coffees Sold for each Coffee Name')
ax.set_xlabel('Number of Sales')
ax.set_ylabel('Coffee Types')
ax.legend(title='Coffee Name')
ax.tick_params(axis='x', rotation=0)
ax.grid(axis='y')
st.pyplot(fig)

# Sales by Transaction Date
number_of_sales_by_date = df['date'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.plot(number_of_sales_by_date.index, number_of_sales_by_date.values, 'b.-') 
ax.set_xticklabels(number_of_sales_by_date.index[::31], rotation=90)
ax.set_xlabel('Date')
ax.set_ylabel('Number of Sales')
ax.set_title('Number of Coffee Sales by Date')
fig.tight_layout()
st.pyplot(fig)

# Dates With the Highest Number of Sales
highest_sale_dates = df['date'].value_counts().head(7)
fig, ax = plt.subplots()
ax.bar(highest_sale_dates.index, highest_sale_dates)
ax.set_xlabel('Sale Count')
ax.set_ylabel('Dates')
ax.set_title('Highest Sale Dates')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Coffee Sales by Hour of the Day
coffee_sales_by_hour = df.groupby('hour')['coffee_name'].count()
fig, ax = plt.subplots()
ax.hist(df['hour'], bins=24, range=(0, 24), edgecolor='black', alpha=0.7)
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Number of Coffee Sales')
ax.set_title('Coffee Sales by Hour of the Day')
ax.grid(True)
st.pyplot(fig)

# Coffee sales by hour of the day per coffee type
coffee_sales_by_hour_per_coffee = pd.crosstab(df['hour'], df['coffee_name'])
fig, ax = plt.subplots(figsize=(12, 8))
coffee_sales_by_hour_per_coffee.plot(kind='bar', stacked=True, ax=ax, colormap='tab20')
ax.set_title('Coffee Sales by Hour of Day for Each Coffee')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Number of Coffees Sold')
ax.legend(title='Coffee Name')
ax.tick_params(axis='x', rotation=0)
st.pyplot(fig)

# Day Cycle categorization
df['day_cycle'] = df['hour'].apply(lambda hour: 'morning' if 6 <= hour <= 11 else 
                                                'afternoon' if 12 <= hour <= 17 else 
                                                'evening' if 18 <= hour <= 22 else 
                                                'night')

coffee_sales_day_cycle = df['day_cycle'].value_counts()
fig, ax = plt.subplots()
ax.bar(coffee_sales_day_cycle.index, coffee_sales_day_cycle)
ax.set_title('Coffee Sales by Day Cycle')
ax.set_xlabel('Day Cycle')
ax.set_ylabel('Number of Coffees Sold')
ax.legend(title='Day Cycle')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Most Sold Coffee During the Week/Weekend
df['weekend'] = df['datetime'].dt.dayofweek >= 5
weekend_sales = df[df['weekend']].groupby('coffee_name').size()
weekday_sales = df[~df['weekend']].groupby('coffee_name').size()

fig, ax = plt.subplots()
ax.bar(weekend_sales.index, weekend_sales, alpha=0.7, label='Weekend', color='blue')
ax.bar(weekday_sales.index, weekday_sales, alpha=0.7, label='Weekday', color='red', width=0.4)
ax.set_title('Coffee Sales by Weekday/Weekend')
ax.set_xlabel('Coffee Type')
ax.set_ylabel('Number of Coffees Sold')
ax.legend()
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Cards with Most Purchases
card_numbers_with_most_purchases = df['card_number'].value_counts().head(7)
fig, ax = plt.subplots()
card_numbers_with_most_purchases.plot(kind='bar', color='brown', ax=ax)
ax.set_title('Card Numbers with Most Purchases')
ax.set_xlabel('Number of Purchases')
ax.set_ylabel('Card Numbers')
ax.tick_params(axis='x', rotation=0)
ax.grid(axis='y')
st.pyplot(fig)

# Total Amount Spent by Each Card Number
amount_spent_by_each_card = df.groupby('card_number')['amount_paid_uah'].sum().sort_values(ascending=False)
st.write(amount_spent_by_each_card)

# Plot Amount Spent by Each Card Number
fig, ax = plt.subplots()
amount_spent_by_each_card.head(7).plot(kind='bar', color='brown', ax=ax)
ax.set_title('Total Amount Spent by Each Card Number')
ax.set_xlabel('Card Number')
ax.set_ylabel('Total Amount Spent (UAH)')
ax.tick_params(axis='x', rotation=0)
ax.grid(axis='y')
st.pyplot(fig)

# Coffees Bought by Each Buyer
coffees_bought_by_each_buyer = df.groupby('card_number')['coffee_name'].apply(lambda x: x.value_counts().head(7))
st.write(coffees_bought_by_each_buyer)

# Consumer Ratio (Card vs Cash)
payment_type_ratio = df['payment_type'].value_counts()
fig, ax = plt.subplots()
ax.pie(payment_type_ratio, labels=payment_type_ratio.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Payment Type Ratio')
ax.axis('equal')
st.pyplot(fig)
