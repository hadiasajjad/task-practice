# Hadia Sajjad

#import All dependencies
import pandas as pd
import sqlite3
#Task no:1
# Load data from CSV file given in task

df = pd.read_csv('customer_data.csv')

#Task no: 2
# Display the first 10 rows of the DataFrame only
print(df.head(10))

#Task no: 3
# Use SQL to calculate the average age of the customers
conn = sqlite3.connect(':memory:')
df.to_sql('customers', conn, if_exists='replace')
avg_age = pd.read_sql_query('SELECT AVG(age) FROM customers', conn)
print('Average age of customers:', avg_age.iloc[0,0])


#Task no: 4
# Use SQL to count the number of customers from each country eg usa etc
count_by_country = pd.read_sql_query('SELECT country, COUNT(*) AS count FROM customers GROUP BY country', conn)
print('Count of customers by country:')
print(count_by_country)

#Task no: 5
# Create a new DataFrame that includes only customers from the United States in new variable
us_customers = df[df['country'] == 'United States']

#Task no: 6
# Save the new DataFrame to a CSV file
us_customers.to_csv('us_customers.csv', index=False)

