# %% [markdown]
# # Coffee Sales Analysis

# %% [markdown]
# ![coffee_image](../assets/coffee-image.jpeg "alt-coffee_image")

# %% [markdown]
# ## About Author
# 
# Author: Joshua Farara
# 
# Project: title

# %% [markdown]
# ### Contact Info
# Click on link below to contact/follow/correct me:
# 
# Email: joshua.farara@gmail.com
# 
# [LinkedIn](https://www.linkedin.com/in/joshuafarara/)
# 
# [Facebook](https://www.facebook.com/josh.farara/)
# 
# [Twitter](https://x.com/FararaTheArtist)
# 
# [Github](https://github.com/JoshuaFarara)
# 

# %% [markdown]
# ## About Data
# 
# Title: Dataset Title
# 
# Dataset: [Link](https://www.kaggle.com/datasets/ihelon/coffee-sales/data)
# 
# Description of data:
# 
# This dataset contains detailed records of coffee sales from a vending machine. It is intended for analysis of purchasing patterns, sales trends, and customer preferences related to coffee products. The dataset spans from March 2024 to June 2024, capturing daily transaction data. And it's continue added new information.

# %% [markdown]
# ### Dataset Columns Names
# 
# Features:
# 

# %% [markdown]
# ### Metadata
# 
# Source:
# 
# Collection Methodology:
# 
# License:
# 
# 

# %% [markdown]
# ### Task
# 
# Describe task at hand for this dataset.

# %% [markdown]
# ### Objectives
# 
# Describe objective at had for this dataset.

# %% [markdown]
# ### Kernel Version Used
# 
# Python==3.11.7

# %% [markdown]
# ## Import Libraries
# 
# We will use the following libraries¶
# 1. Pandas: Data manipulation and analysis
# 2. Numpy: Numerical operations and calculations
# 3. Matplotlib: Data visualization and plotting
# 4. Seaborn: Enhanced data visualization and statistical graphics
# 5. Scipy: Scientific computing and advanced mathematical operations

# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [markdown]
# ## Data Loading and Exploration | Cleaning

# %% [markdown]
# ### Load a CSV file then creating a dataframe

# %%
# Kaggle Notebook
# df = pd.read_csv('/kaggle/input/coffee-sales/index.csv')


#Local Machine Notebook
df = pd.read_csv('../../data/coffee_sales_data.csv')


# %% [markdown]
# ### Set the option to show maximum columns

# %%
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

# %% [markdown]
# ### Get a sneak peek of data
# The purpose of a sneak peek is to get a quick overview of the data and identify any potential problems or areas of interest

# %%
df.head(5)

# %% [markdown]
# ### Let's see the column names

# %%
df.columns

# %% [markdown]
# ### Let's have a look on the shape of the dataset

# %%
print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

# %% [markdown]
# ### Let's have a look on the columns and their data types using detailed info function

# %%
df.info()

# %% [markdown]
# ### Count the missing values

# %%
df.isnull().sum()

# %% [markdown]
# ## Cleaning Set 1
# 
# * There are 896 rows, and 6 columns in the dataset.
# 
# * The data type of all columns are objects except for df['money'] which is float.
# 
# * The columns in the datasets are:
#     * 'date', 'datetime', 'cash_type', 'card', 'money', 'coffee_name'
#     
# * There are a few missing values in the dataset, which we will read in detail and deal with later on in the notebook.
# 
# * rename columns 'cash_type':'payment_type','card':'card_number', 'money':'amount_paid_uah'
# 
# * datetime can be split into two columns and drop column time, because data already has a column that satisfies date.
# 
# * money column after renaming 'amount_paid_uah' can derive an exchanged USD column for later comparison and analysis
# 
# 
# 

# %% [markdown]
# ### Task:
# 
# Clean the data by changing column names 
# 
# 
# 1. Change column names to appropriate names matching the data.
# 2. 

# %% [markdown]
# ## Changing column names 
# 
# Changed: cash_type to payment_type since cash and card payments are accepted

# %%
df.rename(columns={'cash_type':'payment_type', 'card':'card_number', 'money':'amount_paid_uah'}, inplace=True)

# %%
df.columns

# %% [markdown]
# ## Creating Time Column

# %%
df[['new_date', 'time']] =df['datetime'].str.split(' ', n=1, expand=True)
df = df.drop(['new_date', 'datetime'], axis=1)
# df = ['date', 'time', 'payment_type', 'card_number', 'amount_paid_usd', 'coffee_name']

# %%
# check the data
df.head()


# %%
# df['time']

# %% [markdown]
# ## Convert amount_paid_uah(formerly df['money']) to USD.

# %% [markdown]
# .024 USD  = 1 Ukrainian hryvnia
# 
# 1 USD = 40.3317	Ukrainian hryvnia

# %%
UAH_to_USD = .024
df['amount_paid_usd'] = df['amount_paid_uah'] * UAH_to_USD

# %%
df.head(5)

# %% [markdown]
# ## Analytical Questions

# %% [markdown]
# 
# 
# Product analysis:
# 1. Total Revenue
# 
# 2. Total Sales per Coffee 
# 
# 3. Average amount paid per cup 
#  
# 4. Average amount paid per cup for each coffee type in UAH
# 
# 5. Which coffee had the highest/lowest sales?
# 
# 
# Dates and Time analysis:
# 3. Which coffee is sold in the morning, afternoon, evening?
# 
# 4. Which coffee is sold most/least during the week/weekend?
# 
# 5. Which dates have the highest sales?
# 
# 6. What day's of the week do coffee sales occur the most?
# 
# 7. What is the most frequent time of sales at this vending machine?
# 
# 8. What are the sale amounts for the card numbers, frequency, total amount paid, coffee types?
# 
# 9. Are there any holidays that cause a spike or decline in sales?
# 
# 10. 
# 
# Consumer analysis:
# 
# 11. What are the sale amounts for the card numbers, frequency, total amount paid, coffee types?
# 
# 12. What is the ratio amongst card consumers and cash consumers?
# 
# 13. Do cash consumers spend more then card counterparts?
# 
# Currency analysis:
# 14. What is the exchange rate between UAH and USD at the time of this data? Compared to the average?
# 
# 15. 

# %% [markdown]
# ### Product Analysis

# %% [markdown]
# #### Coffee Sales Report

# %%
df['coffee_name'] = df['coffee_name'].astype('str') 

# %%
df[['coffee_name', 'amount_paid_uah']]

# %% [markdown]
# ##### Plot total revenue

# %%
# 1. Total Revenue
total_revenue_uah = df['amount_paid_uah'].sum()
total_revenue_usd = df['amount_paid_usd'].sum()
print(f"Total Revenue (UAH): {total_revenue_uah}, Total Revenue (USD): {total_revenue_usd}")

# %%
# Plot total revenue
plt.figure(figsize=(5, 5))
plt.bar(['Total Revenue (UAH)', 'Total Revenue (USD)'], [total_revenue_uah, total_revenue_usd], color=['blue', 'green'])
plt.xlabel('Currency')
plt.ylabel('Total Revenue')
plt.title('Total Revenue in UAH and USD')
plt.savefig('./visualizations/Total Revenue in UAH and USD.jpg')
plt.close()

# %%
# Group data by coffee_name
grouped_coffee = df.groupby('coffee_name')

# %%
# 3. Total Sales per Coffee Type in UAH
total_amount_paid_uah = grouped_coffee['amount_paid_uah'].sum()
print(total_amount_paid_uah)

# %%
# Plot total sales per coffee type in UAH
plt.figure(figsize=(5, 5))
plt.bar(total_amount_paid_uah.index, total_amount_paid_uah, alpha=0.7, color='skyblue')
plt.xlabel('Coffee Name')
plt.ylabel('Total Amount Paid (UAH)')
plt.title('Total Sales per Coffee Type in UAH')
plt.xticks(rotation=45)
plt.savefig('./visualizations/Total Sales per Coffee Type in UAH.jpg')
plt.close()

# %% [markdown]
# ##### Total Revenue by Coffee Name Avanced Plotting of 

# %%
# Group by coffee_name and calculate total revenue
total_revenue_uah_coffee = df.groupby('coffee_name')['amount_paid_uah'].sum()
total_revenue_usd_coffee = df.groupby('coffee_name')['amount_paid_usd'].sum()

# %%
# Create a plot with dual y-axes
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot UAH data
color = 'tab:blue'
ax1.set_xlabel('Coffee Name')
ax1.set_ylabel('Total Amount Paid (UAH)', color=color)
bars1 = ax1.bar(total_revenue_uah_coffee.index, total_revenue_uah_coffee, alpha=0.7, label='UAH', color=color,  align='center')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for USD data
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Total Amount Paid (USD)', color=color)
bars2 = ax2.bar(total_revenue_usd_coffee.index, total_revenue_usd_coffee, alpha=0.7, label='USD', color=color, width=0.4)
ax2.tick_params(axis='y', labelcolor=color)

plt.xticks(rotation=45)

# Title and legend
fig.suptitle('Total Amount Paid for Each Coffee Name (UAH and USD)')
fig.legend([bars1, bars2], ['UAH', 'USD'], loc='upper left')

plt.savefig('./visualizations/Total Amount Paid for Each Coffee Name (UAH and USD).jpg')
# Show plot
plt.close()

# %% [markdown]
# ##### Average amount paid per cup

# %%
# Average amount paid per cup
df['amount_paid_uah'].mean()

# %% [markdown]
# ##### Average Amount Paid by Coffee Name UAH and USD

# %%
# 2. Average Amount Paid per Cup in UAH and USD
average_amount_paid_uah = grouped_coffee['amount_paid_uah'].mean()
average_amount_paid_usd = grouped_coffee['amount_paid_usd'].mean()
print(average_amount_paid_uah)
print(average_amount_paid_usd)

# %%
# Plot average amount paid per cup for each coffee type in UAH and USD
plt.figure(figsize=(5, 5))
plt.bar(average_amount_paid_uah.index, average_amount_paid_uah, alpha=0.7, label='UAH', color='blue')
plt.bar(average_amount_paid_usd.index, average_amount_paid_usd, alpha=0.7, label='USD', color='green', width=0.4)
plt.xlabel('Coffee Name')
plt.ylabel('Average Amount Paid')
plt.title('Average Amount Paid per Cup for Each Coffee Type (UAH and USD)')
plt.legend()
plt.xticks(rotation=45)
plt.savefig('./visualizations/Average Amount Paid per Cup for Each Coffee Type (UAH and USD).jpg')
plt.close()

# %% [markdown]
# ##### Top Highest Revenue Earning Coffee Names

# %%
total_revenue_uah_coffee = df.groupby('coffee_name')['amount_paid_uah'].sum().reset_index()

# %%
total_revenue_sorted = total_revenue_uah_coffee.sort_values('amount_paid_uah', ascending=False)

# %%
# total_revenue_sorted = total_revenue_sorted.head()
print("Top Highest Revenue Earning Coffees (UAH) Table:")
total_revenue_sorted.head(8)

# %%
# Top Highest Revenue Earning Coffee Names
plt.figure(figsize=(5, 5))
plt.bar(total_revenue_sorted['coffee_name'], total_revenue_sorted['amount_paid_uah'])
plt.xlabel('Coffee Name')
plt.ylabel('Amount Paid (UAH)')
plt.xticks(rotation=90)
_ = plt.title('Top Highest Revenue Earning Coffee Names')
plt.savefig('./visualizations/Top Highest Revenue Earning Coffee Names.jpg')
plt.close()


# %%
# Print highest and lowest revenue earning coffee
highest_revenue_coffee = total_revenue_sorted.iloc[0]  # First row for highest
lowest_revenue_coffee = total_revenue_sorted.iloc[-1]   # Last row for lowest

print(f"Highest Revenue Earning Coffee (UAH): {highest_revenue_coffee['coffee_name']} - Amount: {highest_revenue_coffee['amount_paid_uah']}")
print(f"Lowest Revenue Earning Coffee (UAH): {lowest_revenue_coffee['coffee_name']} - Amount: {lowest_revenue_coffee['amount_paid_uah']}")


# %%


# %% [markdown]
# ##### Top 3 Coffees

# %% [markdown]
# ###### Print top 3 highest revenue earning coffees!
# 

# %%
top_3_revenue_coffees = total_revenue_sorted.head(3)
print("Top 3 Highest Revenue Earning Coffees (UAH):")
top_3_revenue_coffees

# %%
plt.figure(figsize=(5, 5))
plt.bar(top_3_revenue_coffees['coffee_name'], top_3_revenue_coffees['amount_paid_uah'], color='blue')
plt.xlabel('Coffee Name')
plt.ylabel('Total Amount Paid (UAH)')
plt.xticks(rotation=20)
plt.title('Top 3 Highest Revenue Earning Coffee Names')
plt.savefig('./visualizations/Top 3 Highest Revenue Earning Coffee Names.jpg')
plt.close()


# %%



