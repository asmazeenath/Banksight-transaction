
import pymysql
import mysql.connector 
import pandas as pd
import json
import streamlit as st


customers = pd.read_csv("bank transtract - Copy/customers.csv")
accounts = pd.read_csv("bank transtract - Copy/accounts.csv")
transactions = pd.read_csv("bank transtract - Copy/transactions.csv")
branches = pd.read_csv("bank transtract - Copy/branches.csv")
loans = pd.read_csv("bank transtract/loans.csv")
support_tickets = pd.read_csv("bank transtract - Copy/support_tickets.csv")
credit_cards = pd.read_json("bank transtract - Copy/credit_cards.json")

# %%


# %%
customers.head()

# %%
customers.isnull().sum()

# %%
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="zeenathasma@733",
    database="banksight"
)
cursor=conn.cursor()

# %%
print(type(conn))

# %%
cursor.execute("CREATE DATABASE IF NOT EXISTS customer_data")
print("✅ Database created or already exists.")

# %%
#CUSTOMERS
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    gender CHAR(1),
    age INT,
    city VARCHAR(50),
    account_type VARCHAR(20),
    join_date DATE
)
               """)
 #ACCOUNTS_BALANCES
cursor.execute("""
CREATE TABLE IF NOT EXISTS account_balances (
  customer_id VARCHAR(50) PRIMARY KEY,
  account_balance DECIMAL(15,2),
  last_updated DATE,
  CONSTRAINT fk_acc_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
                 )
                 """)
#TRANSACTIONS
cursor.execute("""
               CREATE TABLE IF NOT EXISTS transactions (
  txn_id VARCHAR(50) PRIMARY KEY,
  customer_id VARCHAR(50),
  txn_type VARCHAR(50),
  amount DECIMAL(15,2),
  txn_time DATETIME,
  status VARCHAR(30),
  CONSTRAINT fk_txn_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
               )
               """)
#LOANS
cursor.execute("""
               CREATE TABLE IF NOT EXISTS loans (
  loan_id INT PRIMARY KEY,
  customer_id VARCHAR(50),
  account_id VARCHAR(50),
  branch VARCHAR(100),
  loan_type VARCHAR(50),
  loan_amount INT,
  interest_rate DECIMAL(5,2),
  loan_term_months INT,
  start_date DATE,
  end_date DATE,
  loan_status VARCHAR(30),
  CONSTRAINT fk_loan_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id))
               """)
#CREDIT_CARDS
cursor.execute("""
               CREATE TABLE IF NOT EXISTS credit_cards (
  card_id INT PRIMARY KEY,
  customer_id VARCHAR(50),
  account_id VARCHAR(50),
  branch VARCHAR(100),
  card_number VARCHAR(30),
  card_type VARCHAR(50),
  card_network VARCHAR(30),
  credit_limit INT,
  current_balance DECIMAL(15,2),
  issued_date DATE,
  expiry_date DATE,
  status VARCHAR(30),
  CONSTRAINT fk_card_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id))
               """)
#BRANCHES
cursor.execute("""
              CREATE TABLE IF NOT EXISTS branches (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(150),
  city VARCHAR(100),
  manager_name VARCHAR(100),
  total_employees INT,
  branch_revenue DECIMAL(15,2),
  opening_date DATE,
  performance_rating INT)
              """)
#SUPPORT_TICKETS
cursor.execute("""CREATE TABLE IF NOT EXISTS support_tickets (
  ticket_id VARCHAR(50) PRIMARY KEY,
  customer_id VARCHAR(50),
  account_id VARCHAR(50),
  loan_id VARCHAR(50),
  branch_name VARCHAR(150),
  issue_category VARCHAR(100),
  description TEXT,
  date_opened DATE,
  date_closed DATE,
  priority VARCHAR(20),
  status VARCHAR(30),
  resolution_remarks TEXT,
  support_agent VARCHAR(100),
  channel VARCHAR(30),
  customer_rating INT,
  CONSTRAINT fk_ticket_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
)""")
               



# %%
for _, row in customers.iterrows():
    cursor.execute
    ("""
        INSERT INTO customers ('customer_id', 'name, gender', 'age', 'city', 'account_type', 'join_date')
        VALUES ( %s , %s , %s , %s , %s , %s , %s )
    """, (row['customer_id'], row['name'], row['gender'], row['age'], row['city'], row['account_type'], row['join_date']))

conn.commit()

# %%
for _, row in accounts.iterrows():
    cursor.execute
    ("""
         INSERT INTO accounts ('customer_id','account_balance','last_updated')
     VALUES ( %s , %s , %s )
     """, (row['customer_id'], row['account_balance'], row['last_updated']))
     
    
conn.commit()

# %%
for _, row in transactions.iterrows():
    cursor.execute
    ("""
                   INSERT INTO transactions('txn_id','customer_id','txn_type','amount','txn_time','status')
      VALUES(%s , %s , %s , %s , %s , %s)
     """,(row['txn_id'],row['customer_id'],row['txn_id'],['amount'],row['txn_time'],row['status'])  
    )
    conn.commit()           

# %%
for _, row in loans.iterrows():
    cursor.execute
    ("""
                   INSERT INTO loans ('Loan_ID','Customer_ID','Account_ID','Branch','Loan_Type','Loan_Amount','Interest_Rate','Loan_Term_Months','Start_Date', 'End_Date', 'Loan_Status')
     VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s )
     """,(row ['Loan_ID'], row ['Customer_ID'], row ['Account_ID'], row ['Branch'], row ['Loan_Type'], row ['Loan_Amount'], row ['Interest_Rate'], row ['Loan_Term_Months'], row ['Start_Date'], row ['End_Date'], row ['Loan_Status']))
    
    conn.commit()

# %%
for _, row in branches.iterrows():
    cursor.execute
    ("""
     INSERT INTO branches ('Branch_ID','Branch_Name','City','Manager_Name','Total_Employees','Branch_Revenue','Opening_Date','Performance_Rating')
     VALUES ( %s , %s , %s , %s , %s ,%s , %s , %s )
     """, ( row['Branch_ID'], row['Branch_Name'], row['City'], row['Manager_Name'], row['Total_Employees'], row['Branch_Revenue'], row['Opening_Date'], row['Performance_Rating'])
     )
    conn.commit()

# %%
for _, row in support_tickets.iterrows():
    cursor.execute
    ("""
        INSERT INTO support_tickets ('Ticket_ID',	'Customer_ID',	'Account_ID',	'Loan_ID',	'Branch_Name',	'Issue_Category',	'Description',	'Date_Opened',	'Date_Closed',	'Priority',	'Status',	'Resolution_Remarks',	'Support_Agent',	'Channel',	'Customer_Rating')
        VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s ,%s)
        """, ( row['Ticket_ID'], row	['Customer_ID'],	row['Account_ID'],	row['Loan_ID'],	row['Branch_Name'],	['Issue_Category'],	row['Description'],	row['Date_Opened'],	row['Date_Closed'],	row['Priority'],	row['Status'],	row['Resolution_Remarks'],	row['Support_Agent'],   row	['Channel'], row['Customer_Rating'])
        )
    conn.commit()

# %%
for _, row in credit_cards.iterrows():
    cursor.execute
    ("""
          INSERT INTO credit_cards ('Card_ID' , 'Customer_ID' , 'Account_ID' , 'Branch' , 'Card_Number'  , 'Card_Type' , 'Card_Network' , 'Credit_Limit' , 'Current_Balance' , 'Issued_Date' , 'Expiry_Date' , 'Status')
     VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s)
     """, ( row['Card_ID'], row['Customer_ID'], row['Account_ID'], row['Branch'], row['Card_Number'], row['Card_Type'] , row['Card_Network'], row['Credit_Limit'], row['Current_Balance'], row['Issued_Date'], row['Expiry_Date'], row['Status'])
    )
    conn.commit()

# %%
from tabulate import tabulate


Query_1 ="""
    SELECT customers.CITY,
COUNT(customers.customer_id)AS
TOTAL_CUSTOMERS,
AVG(account_balances.account_balance)AS
AVERAGE_BALANCES
FROM customers
LEFT JOIN account_balances
ON customers.customer_id=account_balances.customer_id
group by customers.city;"""
cursor.execute(Query_1)
result_1 = cursor.fetchall()
headers = ["CITY","CUSTOMERS","AVERAGE ACCOUNT BALANCE"]
print("How Many Customers Exist Per City,And What is their Average Account Balance?")
print(tabulate(result_1,headers=headers))


Query_2 = """
    SELECT customers.account_type,
SUM(account_balances.account_balance)AS total_balance
FROM customers
JOIN account_balances
ON customers.customer_id=customers.customer_id
GROUP BY customers.account_type
ORDER by total_balance DESC
LIMIT 1;"""
cursor.execute(Query_2)
result_2 = cursor.fetchall()
headers = ["ACCOUNT TYPE","HIGHEST TOTAL BALANCE"]
print("Which Account Type Holds the Highest Total Balance?")
print(tabulate(result_2,headers=headers))


Query_3 = """

    select customers.customer_id,
customers.name,
SUM(account_balances.account_balance)
AS total_balance
FROM customers
JOIN account_balances
ON customers.customer_id=account_balances.customer_id
group by customers.customer_id,customers.name
ORDER BY total_balance DESC
LIMIT 10;"""
cursor.execute(Query_3)
result_3 = cursor.fetchall()
headers = ["CUSTOMER ID","CUSTOMERS NAME","TOTAL ACCOUNT BALANCE"]
print("Who are the Top 10 Customers By Total Account Balance Across All Account Types?")
print(tabulate(result_3,headers=headers))


Query_4 = """

    SELECT 
    customers.customer_id,
    customers.name,
    account_balances.account_balance,
    customers.join_date
FROM customers
JOIN account_balances
ON customers.customer_id = account_balances.customer_id
WHERE YEAR(customers.join_date) = 2023
  AND account_balances.account_balance > 100000;"""
cursor.execute(Query_4)
result_4 = cursor.fetchall()
headers = ["CUSTOMER_ID","CUSTOMERS_NAME","ACCOUNT BALANCE","OPENED_DATE"]
print("Which Customers Opened Accounts in 2023 with a Balance Above ₹1,00,000?")
print(tabulate(result_4,headers = headers))


Query_5 = """

 SELECT
    transactions.txn_type,
    SUM(amount) AS total_transaction_volume
FROM transactions
GROUP BY txn_type;"""
cursor.execute(Query_5)
result_5= cursor.fetchall()
headers = ["TRANSACTION TYPE","TOTAL TRANSACTION VOLUME"]
print("What is the Total Transaction Volume by Transaction Type?",result_5)
print(tabulate(result_5,headers = headers))


Query_6 = """

  SELECT transactions.txn_type,
count(*) as FAILED_TRANSACTIONS
FROM transactions
WHERE status='failed'
group by txn_type;"""
cursor.execute(Query_6)
result_6 = cursor.fetchall()
headers = ["TRANSACTION TYPE","FAILED TRANSACTION COUNTS"]
print("How Many Failed Transaction Occured For Each Transaction Type?",result_6)
print(tabulate(result_6,headers = headers))



Query_7 = """

 SELECT transactions.txn_type,
count(amount)as TOTAL_NUMBER_OF_TRANSACTION
FROM transactions
group by txn_type;"""
cursor.execute(Query_7)
result_7 = cursor.fetchall()
headers = ["TRANSACTION TYPE","NUMBER OF TRANSACTIONS"]
print("What is the Total Number of Transactions Per Transaction Type?",result_7)
print(tabulate(result_7,headers = headers))


Query_8 = """

 SELECT 
    cc.account_id,
    COUNT(*) AS high_value_txn_count
FROM transactions t
JOIN credit_cards cc
    ON t.amount = cc.account_id
WHERE CAST(REPLACE(t.amount, ',', '') AS DECIMAL(10,2)) > 20000
GROUP BY cc.account_id
HAVING COUNT(*) >= 5;"""
cursor.execute(Query_8)
result_8 = cursor.fetchall()
headers = ["ACCOUNT NAME","High_value_txn_count"]
print("Which Accounts Have 5 or More High-Value Transactions Above ₹20,000?",result_8)
print(tabulate(result_8,headers = headers))


Query_9 = """

 SELECT 
    loan_type,
    AVG(CAST(REPLACE(loan_amount, ',', '') AS DECIMAL(12,2))) AS avg_loan_amount,
    AVG(CAST(REPLACE(interest_rate, '%', '') AS DECIMAL(5,2))) AS avg_interest_rate
FROM loans
GROUP BY loan_type;"""
cursor.execute(Query_9)
headers = ["LOAN TYPE","AVERAGE AMOUNT" , "INTEREST RATE"]
result_9 = cursor.fetchall()

print("What is the average loan amount and interest rate by loan type ?")
print(tabulate(result_9,headers = headers))




Query_10 = """
 
          SELECT 
    loans.customer_id,
    customers.name,
    
    COUNT(*) AS active_approved_loan_count
FROM loans
join customers
on loans.customer_id=loans.customer_id
WHERE loan_status IN ('Active', 'Approved')
GROUP BY customer_id,name
HAVING COUNT(*) > 1;"""
cursor.execute(Query_10)
result_10 = cursor.fetchall()
headers = ["CUSTOMER ID","CUSTOMERS NAME" , "ACCOUNT HOLDING COUNT"]
print("Which customers currently hold more than one active or approved loan?")
print(tabulate(result_10,headers = headers))



Query_11 = """

 SELECT 
    c.customer_id,
    c.name,
    SUM(l.loan_amount) AS total_loan
FROM loans l
JOIN customers c
    ON l.customer_id = l.customer_id
WHERE l.loan_status != 'ACTIVE''APPROVED''DEFAULTED'
GROUP BY c.customer_id, c.name
ORDER BY total_loan DESC
LIMIT 5;"""
cursor.execute(Query_11)
result_11 = cursor.fetchall()
headers = ["CUSTOMER NAMES","HIGH LOAN AMOUNT"]
print("Who are the top 5 customers with the highest outstanding (non-closed) loan amount?")
print(tabulate(result_11, headers = headers))




Query_12 = """

 SELECT 
    b.branch_name,
    AVG(l.loan_amount) AS avg_loan_amount
FROM loans l
JOIN branches b
    ON l.branch = l.branch
GROUP BY b.branch_name;"""
cursor.execute(Query_12)
result_12 = cursor.fetchall()
headers = ["BRANCH","AVERAGE  LOAN AMOUNT"]
print("What is the average loan amount per branch?")
print(tabulate(result_12, headers = headers))





Query_13 = """

 SELECT 
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18–25'
        WHEN age BETWEEN 26 AND 35 THEN '26–35'
        WHEN age BETWEEN 36 AND 45 THEN '36–45'
        WHEN age BETWEEN 46 AND 60 THEN '46–60'
        ELSE '60+'
    END AS age_group,
    COUNT(*) AS customer_count
FROM customers
GROUP BY age_group
ORDER BY age_group;"""
cursor.execute(Query_13)
result_13 = cursor.fetchall()
headers = ["AGE","CUSTOMERS COUNT"]
print("How many customers exist in each age group?")
print(tabulate(result_13, headers = headers))







Query_14 = """

SELECT
    issue_category,
    AVG(DATEDIFF(date_closed,date_opened)) AS avg_resolution_days
FROM
    support_tickets
WHERE
    date_closed IS NOT NULL
GROUP BY
    issue_category
ORDER BY
    avg_resolution_days DESC;"""
cursor.execute(Query_14)
result_14 = cursor.fetchall()
headers = ["CATEGORIES","AVERAGE RESOLUTION TIME" ]
print("Which issue categories have the longest average resolution time?")
print(tabulate(result_14, headers = headers))



Query_15 = """

SELECT
    support_agent,
    COUNT(*) AS critical_high_rated_tickets
FROM
    support_tickets
WHERE
    priority = 'Critical'
    AND customer_rating >= 4
    AND status = 'Resolved'
GROUP BY
    support_agent
ORDER BY
    critical_high_rated_tickets DESC
LIMIT 1;"""
cursor.execute(Query_15)
result_15 = cursor.fetchall()
headers = ["SUPPORT AGENT","HIGH CUSTOMER RATING"]
print("Which support agents have resolved the most critical tickets with high customer ratings (≥4)?")
print(tabulate(result_15, headers = headers))





