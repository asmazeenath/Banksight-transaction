import streamlit as st
import pandas as pd
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="zeenathasma@733",
    database="banksight",
    port=3306
)

print("✅ MySQL connected successfully")
cursor=conn.cursor()

st.sidebar.title("💡 BANKSIGHT HUB")

customers =pd.read_csv("bank transtract - Copy/customers.csv")
branches = pd.read_csv("bank transtract - Copy/branches.csv")
credit_cards = pd.read_json("bank transtract - Copy/credit_cards.json")
loans = pd.read_csv("bank transtract - Copy/loans.csv")
support_tickets = pd.read_csv("bank transtract - Copy/support_tickets.csv")
accounts = pd.read_csv("bank transtract - Copy/accounts.csv")
transactions=pd.read_csv("bank transtract - Copy/transactions.csv")


menu = st.sidebar.radio("Navigation",
["INTRODUCTION",
     "VIEW TABLES" , "FILTER DATA" , "CRUD OPERATIONS" , "CREDIT/DEBIT SIMULATION" , "ANALYTICAL INSIGHTS" , "ABOUT CREATOR"] )
if menu == "INTRODUCTION":
     
     st.title(":bank:","🏦Banksight - Transaction Intelligence       Dashboard")
     st.header("smart Insights For Modern Banking Operations")
     st.subheader("**DESCRIPTION**")
     st.write("""BankSight – Transaction  Intelligence  Dashboard is an interactive 
banking analytics application designed to monitor, analyze, and manage customer
transactions in real time.   It integrates multiple  banking datasets   to provide
insights into customer behavior,account activity, loan performance, and operational
efficiency through dynamic dashboards and SQL-driven analysis,account activity, loan
performance, and operational efficiency through dynamic dashboards and SQL-driven analysis""")

     st.markdown("""## 🏆**OBJECTIVES** ##

-To provide a centralized view of banking data

-To enable data filtering and CRUD operations

-To simulate basic banking transactions (credit/debit)

-To generate analytical insights using SQL queries""") 

     st.markdown("""## ⚙️**KEY FEATURES** ##""")
     st.write("""   Interactive    table views of all datasets
Multi-level  data    filtering Complete CRUD
 functionality Credit and 
debit  transaction    simulation 
 with  balance validation Analytical 
 insights             decision support .""")


     st.markdown("## 🛠️**TECHNOLOGIES USED** ##")

     st.write("""
1.Python 

2.Pandas 

3.SQL 

4.Streamlit """)

    
if menu == "VIEW TABLES":
    table = st.selectbox("SELECT TABLE" , ["options ","customers" , "accounts" ,"transactions" , "loans" , "branches" , "support_tickets" , "credit_cards" ])
    
    if table =="customers":
     st.header("🧮 Customers table ")
     st.write(customers)
    elif table == "accounts":
     st.header("🧮 Accounts table")
     st.write(accounts)
    elif table == ("transactions"):
     st.header("🧮 transactions")
     st.write(transactions)
    elif table == ("loans"):
     st.header("loans")
     st.write(loans)
    elif table == ("branches"):
     st.header("🧮 branches")
     st.write(branches)
    elif table == ("support_tickets"):
     st.header("🧮 support_tickets")
     st.write(support_tickets)
    elif table == ("credit_cards"):
     st.header("🧮 credit_cards")
     st.write(credit_cards)

elif menu == "FILTER DATA":
    table2 = st.selectbox(
        "SELECT TABLE",
        ["customers", "accounts", "transactions","loans","branches","support_tickets","credit_cards"]
    )
    
    
    txn_id = []
    customer_id = []
    txn_type = []
    amount = []
    txn_time = []
    status = []

    if table2 == "customers":
        st.write("Select Table To Filter")
    

        customer_id = st.multiselect(
            "customer_id",
            customers["customer_id"].unique()
        )
        name = st.multiselect(
            "name",
            customers["name"].unique()
        )
        gender = st.multiselect(
            "gender",
            customers["gender"].unique()
        )
        age = st.multiselect(
            "age",
            customers["age"].unique()
        )
        city = st.multiselect(
            "city",
            customers["city"].unique()
        )
        account_type = st.multiselect(
            "account_type",
            customers["account_type"].unique()
        )
        join_date = st.multiselect(
            "join_date",
            customers["join_date"].unique()
        )

        filtered_df = customers.copy()
        
    if table2 == "transactions":
        st.write("Select Table To Filter")
        

        txn_id = st.multiselect(
            "txn_id",
            transactions["txn_id"].unique()
        )
        customer_id = st.multiselect(
            "customer_id",
            transactions["customer_id"].unique()
        )
        txn_type = st.multiselect(
            "txn_type",
            transactions["txn_type"].unique()
        )
        amount = st.multiselect(
            "amount",
            transactions["amount"].unique()
        )
        txn_time = st.multiselect(
            "txn_time",
            transactions["txn_time"].unique()
        )
        status = st.multiselect(
            "status",
            transactions["status"].unique()
        )

        filtered_df = transactions.copy()

        if txn_id:
            filtered_df = filtered_df[
                filtered_df["txn_id"].isin(txn_id)
            ]

        if customer_id:
            filtered_df = filtered_df[
                filtered_df["customer_id"].isin(customer_id)
            ]

        if txn_type:
            filtered_df = filtered_df[
                filtered_df["txn_type"].isin(txn_type)
            ]

        if amount:
            filtered_df = filtered_df[
                filtered_df["amount"].isin(amount)
            ]

        if txn_time:
            filtered_df = filtered_df[
                filtered_df["txn_time"].isin(txn_time)
            ]

        if status:
            filtered_df = filtered_df[
                filtered_df["status"].isin(status)
            ]
    if table2 == "accounts":
        st.write("Select Table To Filter")
        st.text_input("Select Columns And Values To Filter")

        customer_id = st.multiselect(
            "customer_id",
            accounts["customer_id"].unique()
        )
        account_balance = st.multiselect(
            "account_balance",
            accounts["account_balance"].unique()
        ) 
        last_updated = st.multiselect(
            "last_updated",
            accounts["last_updated"].unique()
        )
        
        filtered_df = accounts.copy()

        if customer_id:
            filtered_df = filtered_df[
                filtered_df["customer_id"].isin(customer_id)
            ]

        if account_balance:
            filtered_df = filtered_df[
                filtered_df["account_balance"].isin(account_balance)
            ]

        if last_updated:
            filtered_df = filtered_df[
                filtered_df["last_updated"].isin(last_updated)
        
            ]

    if table2 == "loans":
        st.write("Select Table To Filter")
        

        Loan_ID = st.multiselect(
            "Loan_ID",
            loans["Loan_ID"].unique()
        )
        Customer_ID = st.multiselect(
            "Customer_ID",
            loans["Customer_ID"].unique()
        )
        Account_ID = st.multiselect(
            "Account_ID",
            loans["Account_ID"].unique()
        )
        Branch = st.multiselect(
            "Branch",
            loans["Branch"].unique()
        )
        Loan_Type = st.multiselect(
            "Loan_Type",
            loans["Loan_Type"].unique()
        )
        Loan_Amount = st.multiselect(
            "Loan_Amount",
            loans["Loan_Amount"].unique()
        )

        Interest_Rate = st.multiselect(
            "Interest_Rate",
            loans["Interest_Rate"].unique()
        )
        Loan_Term_Months = st.multiselect(
            "Loan_Term_Months",
            loans["Loan_Term_Months"].unique()
        )
        Start_Date = st.multiselect(
            "Start_Date",
            loans["Start_Date"].unique()
        )
        End_Date = st.multiselect(
            "End_Date",
            loans["End_Date"].unique()
        )
        Loan_Status = st.multiselect(
            "Loan_Status",
            loans["Loan_Status"].unique()
        )

        filtered_df = loans.copy()

        if Loan_ID:
            filtered_df = filtered_df[
                filtered_df["Loan_ID"].isin( Loan_ID)
            ]

        if Customer_ID:
            filtered_df = filtered_df[
                filtered_df["Customer_ID"].isin(Customer_ID)
            ]

        if Account_ID:
            filtered_df = filtered_df[
                filtered_df["Account_ID"].isin(Account_ID)
            ]

        if Branch:
            filtered_df = filtered_df[
                filtered_df["Branch"].isin(Branch)
            ]

        if Loan_Type:
            filtered_df = filtered_df[
                filtered_df["Loan_Type"].isin(Loan_Type)
            ]

        if Loan_Amount:
            filtered_df = filtered_df[
                filtered_df["Loan_Amount"].isin(Loan_Amount)
            ]
        if Interest_Rate:
            filtered_df = filtered_df[
                filtered_df[" Interest_Rate"].isin( Interest_Rate)
            ]

        if Loan_Term_Months:
            filtered_df = filtered_df[
                filtered_df["Loan_Term_Months"].isin(Loan_Term_Months)
            ]

        if Start_Date :
            filtered_df = filtered_df[
                filtered_df["Start_Date"].isin(Start_Date)
            ]
        if End_Date:
            filtered_df = filtered_df[
                filtered_df["End_Date"].isin(End_Date)
            ]

        if Loan_Status:
            filtered_df = filtered_df[
                filtered_df["Loan_Status"].isin(Loan_Status)
            ]
    if table2 == "branches":
            st.write("Select Table To Filter")
            

            Branch_ID = st.multiselect(
            "Branch_ID",
            branches["Branch_ID"].unique()
        )
            Branch_Name = st.multiselect(
            "Branch_Name",
            branches["Branch_Name"].unique()
        )
            City = st.multiselect(
            "City",
            branches["City"].unique()
        )
            Manager_Name = st.multiselect(
            "Manager_Name",
            branches["Manager_Name"].unique()
        )
            Total_Employees = st.multiselect(
            "Total_Employees",
            branches["Total_Employees"].unique()
        )
            Branch_Revenue = st.multiselect(
            "Branch_Revenue",
            branches["Branch_Revenue"].unique()
        )

            Opening_Date = st.multiselect(
            "Opening_Date",
            branches["Opening_Date"].unique()
        )
            Performance_Rating = st.multiselect(
            "Performance_Rating",
            branches["Performance_Rating"].unique()
        )

            filtered_df = branches.copy()

            if Branch_ID:
                filtered_df = filtered_df[
                filtered_df["Branch_ID"].isin( Branch_ID)
            ]

            if Branch_Name:
                filtered_df = filtered_df[
                filtered_df["Branch_Name"].isin(Branch_Name)
            ]

            if City:
                filtered_df = filtered_df[
                filtered_df["City"].isin(City)
            ]

            if Manager_Name:
                filtered_df = filtered_df[
                filtered_df["Manager_Name"].isin(Manager_Name)
            ]

            if Total_Employees:
                filtered_df = filtered_df[
                filtered_df["Total_Employees"].isin(Total_Employees)
            ]

            if Branch_Revenue:
                filtered_df = filtered_df[
                filtered_df["Branch_Revenue"].isin(Branch_Revenue)
            ]
            if Opening_Date:
                filtered_df = filtered_df[
                filtered_df["Opening_Date"].isin( Opening_Date)
            ]

            if Performance_Rating:
                filtered_df = filtered_df[
                filtered_df["Performance_Rating"].isin(Performance_Rating)
            ]
    if table2 == "support_tickets":
            st.write("Select Table To Filter")
            

            Ticket_ID = st.multiselect(
            "Ticket_ID",
            support_tickets["Ticket_ID"].unique()
        )
            Customer_ID = st.multiselect(
            "Customer_ID",
            support_tickets["Customer_ID"].unique()
        )
            Account_ID = st.multiselect(
            "Account_ID",
            support_tickets["Account_ID"].unique()
        )
            Loan_ID = st.multiselect(
            "Loan_ID",
            support_tickets["Loan_ID"].unique()
        )
            Branch_Name = st.multiselect(
            "Branch_Name",
            support_tickets["Branch_Name"].unique()
        )
            Issue_Category = st.multiselect(
            "Issue_Category",
            support_tickets["Issue_Category"].unique()
        )

            Description = st.multiselect(
            "Description",
            support_tickets["Description"].unique()
        )
            Date_Opened = st.multiselect(
            "Date_Opened",
            support_tickets["Date_Opened"].unique()
        )

            Date_Closed = st.multiselect(
            "Date_Closed",
            support_tickets["Date_Closed"].unique()
        )
            Priority= st.multiselect(
            "Priority",
            support_tickets["Priority"].unique()
        )
            Status= st.multiselect(
            "Status",
            support_tickets["Status"].unique()
        )
            Resolution_Remarks = st.multiselect(
            "Resolution_Remarks",
            support_tickets["Resolution_Remarks"].unique()
        )
            Support_Agent = st.multiselect(
            "Support_Agent",
            support_tickets["Support_Agent"].unique()
        )
            Channel= st.multiselect(
            "Channel",
            support_tickets["Channel"].unique()
        )
            Customer_Rating= st.multiselect(
            "Customer_Rating",
            support_tickets["Customer_Rating"].unique()
        )
            filtered_df = support_tickets.copy()

            if Ticket_ID:
                filtered_df = filtered_df[
                filtered_df[" Ticket_ID"].isin( Ticket_ID)
            ]

            if Customer_ID:
                filtered_df = filtered_df[
                filtered_df["Customer_ID"].isin(Customer_ID)
            ]

            if Account_ID:
                filtered_df = filtered_df[
                filtered_df["Account_ID"].isin(Account_ID)
            ]

            if Loan_ID:
                filtered_df = filtered_df[
                filtered_df["Loan_ID"].isin(Loan_ID)
            ]

            if Branch_Name:
                filtered_df = filtered_df[
                filtered_df["Branch_Name"].isin(Branch_Name)
            ]

            if Issue_Category:
                filtered_df = filtered_df[
                filtered_df[" Issue_Category"].isin( Issue_Category)
            ]
            if Description:
                filtered_df = filtered_df[
                filtered_df["Description"].isin( Description)
            ]

            if Date_Opened:
                filtered_df = filtered_df[
                filtered_df["Date_Opened"].isin(Date_Opened)
            ]

            if Date_Closed:
                filtered_df = filtered_df[
                filtered_df["Date_Closed"].isin(Date_Closed)
            ]

            if Priority:
                filtered_df = filtered_df[
                filtered_df["Priority"].isin(Priority)
            ]
            if Status:
                filtered_df = filtered_df[
                filtered_df["Status"].isin( Status)
            ]

            if Resolution_Remarks:
                filtered_df = filtered_df[
                filtered_df["Resolution_Remarks"].isin(Resolution_Remarks)
            ]
            if Support_Agent:
                filtered_df = filtered_df[
                filtered_df["Support_Agent"].isin(Support_Agent)
            ]
            if Channel:
                filtered_df = filtered_df[
                filtered_df["Channel"].isin(Channel)
            ]

            if Customer_Rating:
                filtered_df = filtered_df[
                filtered_df["Customer_Rating"].isin(Customer_Rating)
            ]
    if table2 == "credit_cards":
            st.write("Select Table To Filter")
        

            Card_ID = st.multiselect(
            "Card_ID",
            credit_cards["Card_ID"].unique()
        )
            Customer_ID = st.multiselect(
            "Customer_ID",
            credit_cards["Customer_ID"].unique()
        )
            Account_ID = st.multiselect(
            "Account_ID",
            credit_cards["Account_ID"].unique()
        )
            Branch = st.multiselect(
            "Branch",
            credit_cards["Branch"].unique()
        )
            Card_Number = st.multiselect(
            "Card_Number",
            credit_cards["Card_Number"].unique()
        )
            Card_Type= st.multiselect(
            "Card_Type",
            credit_cards["Card_Type"].unique()
        )

            Card_Network = st.multiselect(
            "Description",
            credit_cards["Description"].unique()
        )
            Credit_Limit = st.multiselect(
            "Credit_Limit",
            credit_cards["Credit_Limit"].unique()
        )

            Current_Balance= st.multiselect(
            "Current_Balance",
            credit_cards["Current_Balance"].unique()
        )
            Issued_Date = st.multiselect(
            " Issued_Date",
            credit_cards[" Issued_Date"].unique()
        )
            Expiry_Date= st.multiselect(
            " Expiry_Date",
            credit_cards["Expiry_Date"].unique()
        )
            Status = st.multiselect(
            "Status",
            credit_cards["Status"].unique()
        )
        
            filtered_df = credit_cards.copy()

            if Card_ID:
                filtered_df = filtered_df[
                filtered_df[" Card_ID"].isin( Card_ID)
            ]

            if Customer_ID:
                filtered_df = filtered_df[
                filtered_df["Customer_ID"].isin(Customer_ID)
            ]

            if Account_ID:
                filtered_df = filtered_df[
                filtered_df["Account_ID"].isin(Account_ID)
            ]

            if Branch:
                filtered_df = filtered_df[
                filtered_df["Branch"].isin(Branch)
            ]

            if Card_Number:
                filtered_df = filtered_df[
                filtered_df["Card_Number"].isin(Card_Number)
            ]

            if Card_Type:
                filtered_df = filtered_df[
                filtered_df[" Card_Type"].isin( Card_Type)
            ]
            if Card_Network:
                filtered_df = filtered_df[
                filtered_df["Card_Network"].isin( Card_Network)
            ]

            if Credit_Limit:
                filtered_df = filtered_df[
                filtered_df["Credit_Limit"].isin(Credit_Limit)
            ]

            if Current_Balance:
                filtered_df = filtered_df[
                filtered_df["Current_Balance"].isin(Current_Balance)
            ]

            if Issued_Date:
                filtered_df = filtered_df[
                filtered_df["Issued_Date"].isin(Issued_Date)
            ]
            if Expiry_Date:
                filtered_df = filtered_df[
                filtered_df["Expiry_Date"].isin( Expiry_Date)
            ]

            if Status:
                filtered_df = filtered_df[
                filtered_df["Status"].isin(Status)
            
            ]
            
        
            
    if st.button("show"):
       st.dataframe(filtered_df)  
elif menu ==  "ABOUT CREATOR":

    st.title("👩‍💻 About the Creator")

    st.subheader("Zeenath Asma")

    st.write("""
    I am a passionate learner in **Python, SQL, and Data Analytics**.
    This project **BankSight Hub** is created to demonstrate
    banking data analysis using **Streamlit and MySQL**.
    """)

    st.markdown("""
    ### 🔧 Skills Used
    - Python
    - SQL (MySQL)
    - Pandas
    - Streamlit
    """)

    st.markdown("""
    ### 🎯 Project Purpose
    - Understand banking operations
    - Perform CRUD operations
    - Analyze customer & transaction data
    - Build interactive dashboards
    """)

    st.success("Thank you for visiting BankSight Hub 💡")

elif menu == "CRUD OPERATIONS":


    table_crud =st.radio("SELECT FROM",("VIEW","ADD","UPDATE","DELETE"))
    if table_crud == "VIEW":

        table = st.selectbox("SELECT TABLE" , ["options ","customers" , "accounts" ,"transactions" , "loans" , "branches" , "support_tickets" , "credit_cards" ])

        if table =="customers":
                st.header("🧮 Customers table ")
                st.write(customers)
        elif table == "accounts":
                st.header("🧮 Accounts table")
                st.write(accounts)
        elif table == ("transactions"):
                st.header("🧮 transactions")
                st.write(transactions)
        elif table == ("loans"):
                st.header("loans")
                st.write(loans)
        elif table == ("branches"):
                st.header("🧮 branches")
                st.write(branches)
        elif table == ("support_tickets"):
                st.header("🧮 support_tickets")
                st.write(support_tickets)
        elif table == ("credit_cards"):
                st.header("🧮 credit_cards")
                st.write(credit_cards)
    

    table = st.selectbox(
        "SELECT TABLE",
        ["customers", "accounts", "transactions", "loans", "branches", "support_tickets", "credit_cards"]
    )
    if table_crud == "ADD":

    
     if table == "customers":
        st.subheader("➕ Add Customer")

        with st.form("add_customer"):
            customer_id = st.text_input("Customer ID")
            name = st.text_input("Name")
            gender = st.radio("Gender", ("Male", "Female", "Other"))
            age = st.number_input("Age", min_value=1)
            city = st.text_input("City")
            account_type = st.text_input("Account Type")
            join_date = st.date_input("Join Date")

            submit_btn = st.form_submit_button("Add Customer")

        if submit_btn:
            cursor.execute(
                "INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (customer_id, name, gender, age, city, account_type, join_date)
            )
            conn.commit()
            st.success("Customer Added Successfully")

    
     elif table == "transactions":
        st.subheader("➕ Add Transaction")

        with st.form("add_transaction"):
            txn_id = st.text_input("Transaction ID")
            customer_id = st.text_input("Customer ID")
            txn_type = st.text_input("Transaction Type")
            amount = st.number_input("Amount")
            txn_time = st.text_input("Transaction Time")
            status = st.text_input("Status")

            submit_btn = st.form_submit_button("Add Transaction")

        if submit_btn:
            cursor.execute(
                "INSERT INTO transactions VALUES (%s,%s,%s,%s,%s,%s)",
                (txn_id, customer_id, txn_type, amount, txn_time, status)
            )
            conn.commit()
            st.success("Transaction Added Successfully")

   
     elif table == "accounts":
        st.subheader("➕ Add Account")

        with st.form("add_account"):
            customer_id = st.text_input("Customer ID")
            account_balance = st.number_input("Account Balance")
            last_updated = st.date_input("Last Updated")

            submit_btn = st.form_submit_button("Add Account")

        if submit_btn:
            cursor.execute(
                "INSERT INTO accounts VALUES (%s,%s,%s)",
                (customer_id, account_balance, last_updated)
            )
            conn.commit()
            st.success("Account Added Successfully")

    
     elif table == "loans":
        st.subheader("➕ Add Loan")

        with st.form("add_loan"):
            Loan_ID = st.text_input("Loan ID")
            Customer_ID = st.text_input("Customer ID")
            Account_ID = st.text_input("Account ID")
            Branch = st.text_input("Branch")
            Loan_Type = st.text_input("Loan Type")
            Loan_Amount = st.number_input("Loan Amount")
            Interest_Rate = st.number_input("Interest Rate")
            Loan_Term_Months = st.number_input("Loan Term (Months)")
            Start_Date = st.date_input("Start Date")
            End_Date = st.date_input("End Date")
            Loan_Status = st.text_input("Loan Status")

            submit_btn = st.form_submit_button("Add Loan")

        if submit_btn:
            cursor.execute(
                "INSERT INTO loans VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    Loan_ID, Customer_ID, Account_ID, Branch, Loan_Type,
                    Loan_Amount, Interest_Rate, Loan_Term_Months,
                    Start_Date, End_Date, Loan_Status
                )
            )
            conn.commit()
            st.success("Loan Added Successfully")

    
     elif table == "branches":
        st.subheader("➕ Add Branch")

        with st.form("add_branch"):
            Branch_ID = st.text_input("Branch ID")
            Branch_Name = st.text_input("Branch Name")
            City = st.text_input("City")
            Manager_Name = st.text_input("Manager Name")
            Total_Employees = st.number_input("Total Employees", min_value=0)
            Branch_Revenue = st.number_input("Branch Revenue")
            Opening_Date = st.date_input("Opening Date")
            Performance_Rating = st.text_input("Performance Rating")

            submit_btn = st.form_submit_button("Add Branch")

        if submit_btn:
            cursor.execute(
                "INSERT INTO branches VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    Branch_ID, Branch_Name, City, Manager_Name,
                    Total_Employees, Branch_Revenue,
                    Opening_Date, Performance_Rating
                )
            )
            conn.commit()
            st.success("Branch Added Successfully")

     elif table == "credit_cards":
        st.subheader("➕ Add Credit Card")

        with st.form("add_credit_card"):
            Card_ID = st.text_input("Card ID")
            Customer_ID = st.text_input("Customer ID")
            Account_ID = st.text_input("Account ID")
            Branch = st.text_input("Branch")
            Card_Number = st.text_input("Card Number")
            Card_Type = st.text_input("Card Type")
            Card_Network = st.text_input("Card Network")
            Credit_Limit = st.number_input("Credit Limit")
            Current_Balance = st.number_input("Current Balance")
            Issued_Date = st.date_input("Issued Date")
            Expiry_Date = st.date_input("Expiry Date")
            Status = st.text_input("Status")

            submit_btn = st.form_submit_button("Add Credit Card")

        if submit_btn:
            cursor.execute(
                "INSERT INTO credit_cards VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    Card_ID, Customer_ID, Account_ID, Branch,
                    Card_Number, Card_Type, Card_Network,
                    Credit_Limit, Current_Balance,
                    Issued_Date, Expiry_Date, Status
                )
            )
            conn.commit()
            st.success("Credit Card Added Successfully")

     elif table == "support_tickets":
        st.subheader("➕ Add Support Ticket")

        with st.form("add_support_ticket"):
            Ticket_ID = st.text_input("Ticket ID")
            Customer_ID = st.text_input("Customer ID")
            Account_ID = st.text_input("Account ID")
            Loan_ID = st.text_input("Loan ID")
            Branch_Name = st.text_input("Branch Name")
            Issue_Category = st.text_input("Issue Category")
            Description = st.text_input("Description")
            Date_Opened = st.date_input("Date Opened")
            Date_Closed = st.date_input("Date Closed")
            Priority = st.text_input("Priority")
            Status = st.text_input("Status")
            Resolution_Remarks = st.text_input("Resolution Remarks")
            Support_Agent = st.text_input("Support Agent")
            Channel = st.text_input("Channel")
            Customer_Rating = st.number_input("Customer Rating")

            submit_btn = st.form_submit_button("Add Support Ticket")

        if submit_btn:
            cursor.execute(
                "INSERT INTO support_tickets VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    Ticket_ID, Customer_ID, Account_ID, Loan_ID,
                    Branch_Name, Issue_Category, Description,
                    Date_Opened, Date_Closed, Priority, Status,
                    Resolution_Remarks, Support_Agent,
                    Channel, Customer_Rating
                )
            )
            conn.commit()
            st.success("Support Ticket Added Successfully")


    if table_crud == "UPDATE":
    
  
     if table == "customers":
        st.subheader("✏️ Update Customer (All Fields)")

        customer_id = st.text_input("Customer ID (Required)")
        name = st.text_input("Name")
        gender = st.radio("Gender", ("Male", "Female", "Other"))
        age = st.number_input("Age", min_value=1)
        city = st.text_input("City")
        account_type = st.text_input("Account Type")
        join_date = st.date_input("Join Date")

        if st.button("Update Customer"):
            cursor.execute(
                """
                UPDATE customers
                SET name=%s, gender=%s, age=%s, city=%s,
                    account_type=%s, join_date=%s
                WHERE customer_id=%s
                """,
                (name, gender, age, city, account_type, join_date, customer_id)
            )
            conn.commit()
            st.success("Customer Updated Successfully")

    
     elif table == "accounts":
        st.subheader("✏️ Update Account (All Fields)")

        customer_id = st.text_input("Customer ID (Required)")
        account_balance = st.number_input("Account Balance")
        last_updated = st.date_input("Last Updated")

        if st.button("Update Account"):
            cursor.execute(
                """
                UPDATE accounts
                SET account_balance=%s, last_updated=%s
                WHERE customer_id=%s
                """,
                (account_balance, last_updated, customer_id)
            )
            conn.commit()
            st.success("Account Updated Successfully")

   
     elif table == "transactions":
        st.subheader("✏️ Update Transaction (All Fields)")

        txn_id = st.text_input("Transaction ID (Required)")
        customer_id = st.text_input("Customer ID")
        txn_type = st.text_input("Transaction Type")
        amount = st.number_input("Amount")
        txn_time = st.text_input("Transaction Time")
        status = st.text_input("Status")

        if st.button("Update Transaction"):
            cursor.execute(
                """
                UPDATE transactions
                SET customer_id=%s, txn_type=%s, amount=%s,
                    txn_time=%s, status=%s
                WHERE txn_id=%s
                """,
                (customer_id, txn_type, amount, txn_time, status, txn_id)
            )
            conn.commit()
            st.success("Transaction Updated Successfully")

  
     elif table == "loans":
        st.subheader("✏️ Update Loan (All Fields)")

        Loan_ID = st.text_input("Loan ID (Required)")
        Customer_ID = st.text_input("Customer ID")
        Account_ID = st.text_input("Account ID")
        Branch = st.text_input("Branch")
        Loan_Type = st.text_input("Loan Type")
        Loan_Amount = st.number_input("Loan Amount")
        Interest_Rate = st.number_input("Interest Rate")
        Loan_Term_Months = st.number_input("Loan Term (Months)")
        Start_Date = st.date_input("Start Date")
        End_Date = st.date_input("End Date")
        Loan_Status = st.text_input("Loan Status")

        if st.button("Update Loan"):
            cursor.execute(
                """
                UPDATE loans
                SET customer_id=%s, account_id=%s, branch=%s,
                    loan_type=%s, loan_amount=%s, interest_rate=%s,
                    loan_term_months=%s, start_date=%s,
                    end_date=%s, loan_status=%s
                WHERE loan_id=%s
                """,
                (
                    Customer_ID, Account_ID, Branch, Loan_Type,
                    Loan_Amount, Interest_Rate, Loan_Term_Months,
                    Start_Date, End_Date, Loan_Status, Loan_ID
                )
            )
            conn.commit()
            st.success("Loan Updated Successfully")

   
     elif table == "branches":
        st.subheader("✏️ Update Branch (All Fields)")

        Branch_ID = st.text_input("Branch ID (Required)")
        Branch_Name = st.text_input("Branch Name")
        City = st.text_input("City")
        Manager_Name = st.text_input("Manager Name")
        Total_Employees = st.number_input("Total Employees", min_value=0)
        Branch_Revenue = st.number_input("Branch Revenue")
        Opening_Date = st.date_input("Opening Date")
        Performance_Rating = st.text_input("Performance Rating")

        if st.button("Update Branch"):
            cursor.execute(
                """
                UPDATE branches
                SET branch_name=%s, city=%s, manager_name=%s,
                    total_employees=%s, branch_revenue=%s,
                    opening_date=%s, performance_rating=%s
                WHERE branch_id=%s
                """,
                (
                    Branch_Name, City, Manager_Name,
                    Total_Employees, Branch_Revenue,
                    Opening_Date, Performance_Rating, Branch_ID
                )
            )
            conn.commit()
            st.success("Branch Updated Successfully")


     elif table == "credit_cards":
        st.subheader("✏️ Update Credit Card (All Fields)")

        Card_ID = st.text_input("Card ID (Required)")
        Customer_ID = st.text_input("Customer ID")
        Account_ID = st.text_input("Account ID")
        Branch = st.text_input("Branch")
        Card_Number = st.text_input("Card Number")
        Card_Type = st.text_input("Card Type")
        Card_Network = st.text_input("Card Network")
        Credit_Limit = st.number_input("Credit Limit")
        Current_Balance = st.number_input("Current Balance")
        Issued_Date = st.date_input("Issued Date")
        Expiry_Date = st.date_input("Expiry Date")
        Status = st.text_input("Status")

        if st.button("Update Credit Card"):
            cursor.execute(
                """
                UPDATE credit_cards
                SET customer_id=%s, account_id=%s, branch=%s,
                    card_number=%s, card_type=%s, card_network=%s,
                    credit_limit=%s, current_balance=%s,
                    issued_date=%s, expiry_date=%s, status=%s
                WHERE card_id=%s
                """,
                (
                    Customer_ID, Account_ID, Branch,
                    Card_Number, Card_Type, Card_Network,
                    Credit_Limit, Current_Balance,
                    Issued_Date, Expiry_Date, Status, Card_ID
                )
            )
            conn.commit()
            st.success("Credit Card Updated Successfully")


     elif table == "support_tickets":
        st.subheader("✏️ Update Support Ticket (All Fields)")

        Ticket_ID = st.text_input("Ticket ID (Required)")
        Customer_ID = st.text_input("Customer ID")
        Account_ID = st.text_input("Account ID")
        Loan_ID = st.text_input("Loan ID")
        Branch_Name = st.text_input("Branch Name")
        Issue_Category = st.text_input("Issue Category")
        Description = st.text_input("Description")
        Date_Opened = st.date_input("Date Opened")
        Date_Closed = st.date_input("Date Closed")
        Priority = st.text_input("Priority")
        Status = st.text_input("Status")
        Resolution_Remarks = st.text_input("Resolution Remarks")
        Support_Agent = st.text_input("Support Agent")
        Channel = st.text_input("Channel")
        Customer_Rating = st.number_input("Customer Rating")

        if st.button("Update Support Ticket"):
            cursor.execute(
                """
                UPDATE support_tickets
                SET customer_id=%s, account_id=%s, loan_id=%s,
                    branch_name=%s, issue_category=%s,
                    description=%s, date_opened=%s,
                    date_closed=%s, priority=%s, status=%s,
                    resolution_remarks=%s, support_agent=%s,
                    channel=%s, customer_rating=%s
                WHERE ticket_id=%s
                """,
                (
                    Customer_ID, Account_ID, Loan_ID,
                    Branch_Name, Issue_Category, Description,
                    Date_Opened, Date_Closed, Priority, Status,
                    Resolution_Remarks, Support_Agent,
                    Channel, Customer_Rating, Ticket_ID
                )
            )
            conn.commit()
            st.success("Support Ticket Updated Successfully")
    
    
    if table_crud == "DELETE":



    
     if table == "customers":
        st.subheader("🗑️ Delete Customer")

        customer_id = st.text_input("Customer ID (Required)")

        if st.button("Delete Customer"):
            cursor.execute(
                "DELETE FROM customers WHERE customer_id = %s",
                (customer_id,)
            )
            conn.commit()
            st.success("Customer Deleted Successfully")

    
     elif table == "accounts":
        st.subheader("🗑️ Delete Account")

        customer_id = st.text_input("Customer ID (Required)")

        if st.button("Delete Account"):
            cursor.execute(
                "DELETE FROM accounts WHERE customer_id = %s",
                (customer_id,)
            )
            conn.commit()
            st.success("Account Deleted Successfully")

    
     elif table == "transactions":
        st.subheader("🗑️ Delete Transaction")

        txn_id = st.text_input("Transaction ID (Required)")

        if st.button("Delete Transaction"):
            cursor.execute(
                "DELETE FROM transactions WHERE txn_id = %s",
                (txn_id,)
            )
            conn.commit()
            st.success("Transaction Deleted Successfully")


     elif table == "loans":
        st.subheader("🗑️ Delete Loan")

        Loan_ID = st.text_input("Loan ID (Required)")

        if st.button("Delete Loan"):
            cursor.execute(
                "DELETE FROM loans WHERE loan_id = %s",
                (Loan_ID,)
            )
            conn.commit()
            st.success("Loan Deleted Successfully")


     elif table == "branches":
        st.subheader("🗑️ Delete Branch")

        Branch_ID = st.text_input("Branch ID (Required)")

        if st.button("Delete Branch"):
            cursor.execute(
                "DELETE FROM branches WHERE branch_id = %s",
                (Branch_ID,)
            )
            conn.commit()
            st.success("Branch Deleted Successfully")

    
     elif table == "credit_cards":
        st.subheader("🗑️ Delete Credit Card")

        Card_ID = st.text_input("Card ID (Required)")

        if st.button("Delete Credit Card"):
            cursor.execute(
                "DELETE FROM credit_cards WHERE card_id = %s",
                (Card_ID,)
            )
            conn.commit()
            st.success("Credit Card Deleted Successfully")

    
     elif table == "support_tickets":
        st.subheader("🗑️ Delete Support Ticket")

        Ticket_ID = st.text_input("Ticket ID (Required)")

        if st.button("Delete Support Ticket"):
            cursor.execute(
                "DELETE FROM support_tickets WHERE ticket_id = %s",
                (Ticket_ID,)
            )
            conn.commit()
            st.success("Support Ticket Deleted Successfully")
elif menu == "CREDIT/DEBIT SIMULATION":

    st.header("💳 Credit / Debit Simulation")

    from decimal import Decimal
    import uuid

    customer_id = st.text_input("Enter Customer ID")
    amount = st.number_input("Enter Amount (₹)", min_value=0.0, step=100.0)
    amount = Decimal(str(amount))

    action = st.radio(
        "Select Action",
        ["Check Balance", "Deposit", "Withdraw"]
    )

    if st.button("Submit"):

        
        cursor.execute(
            "SELECT account_balance FROM account_balances WHERE customer_id = %s",
            (customer_id,)
        )
        result = cursor.fetchone()

        if result is None:
            st.error("❌ Account not found")

        else:
            balance = Decimal(result[0])

            
            if action == "Check Balance":
                st.success(f"💰 Current Balance: ₹{balance}")

            
            elif action == "Deposit":
                new_balance = balance + amount
                txn_id = str(uuid.uuid4())[:8]

                cursor.execute(
                    "UPDATE account_balances SET account_balance = %s WHERE customer_id = %s",
                    (new_balance, customer_id)
                )

                cursor.execute(
                    """
                    INSERT INTO transactions
                    (customer_id, txn_id, txn_type, amount, txn_time, status)
                    VALUES (%s, %s, %s, %s, NOW(), %s)
                    """,
                    (customer_id, txn_id, "CREDIT", amount, "SUCCESS")
                )

                conn.commit()

                st.success("✅ Amount Deposited Successfully")
                st.info(f"💰 Updated Balance: ₹{new_balance}")

        
            elif action == "Withdraw":
                txn_id = str(uuid.uuid4())[:8]

                if amount > balance:
                    st.error("❌ Insufficient Balance")

                    cursor.execute(
                        """
                        INSERT INTO transactions
                        (customer_id, txn_id, txn_type, amount, txn_time, status)
                        VALUES (%s, %s, %s, %s, NOW(), %s)
                        """,
                        (customer_id, txn_id, "DEBIT", amount, "FAILED")
                    )
                    conn.commit()

                else:
                    new_balance = balance - amount

                    cursor.execute(
                        "UPDATE account_balances SET account_balance = %s WHERE customer_id = %s",
                        (new_balance, customer_id)
                    )

                    cursor.execute(
                        """
                        INSERT INTO transactions
                        (customer_id, txn_id, txn_type, amount, txn_time, status)
                        VALUES (%s, %s, %s, %s, NOW(), %s)
                        """,
                        (customer_id, txn_id, "DEBIT", amount, "SUCCESS")
                    )

                    conn.commit()

                    st.success("✅ Withdrawal Successful")
                    st.info(f"💰 Remaining Balance: ₹{new_balance}")
elif menu == "ANALYTICAL INSIGHTS":

    st.header("📊 BankSight – Analytical Insights")

    insight = st.selectbox(
        "Select an Analysis",
        [
            "Q1:Customers per City & Avg Balance",
            "Q2: Account Type with Highest Balance",
            "Q3:Top 10 Customers by Balance",
            "Q4:High Balance Accounts Opened in 2023",
            "Q5:Transaction Volume by Type",
            "Q6:Failed Transactions by Type",
            "Q7:Transaction Count by Type",
            "Q8:High-Value Transaction Accounts",
            "Q9:Average Loan & Interest by Loan Type",
            "Q10:Customers with Multiple Active Loans",
            "Q11:Top 5 Customers by Outstanding Loans",
            "Q12:Average Loan Amount per Branch",
            "Q13:Customer Age Group Distribution",
            "Q14:Ticket Resolution Time by Category",
            "Q15:Top Support Agent (Critical Tickets)"
        ]
    )

    if st.button("Run Analysis"):

        Query = None   

        if insight == "Q1:Customers per City & Avg Balance":
            Query = """
            SELECT city, COUNT(customer_id) AS TOTAL_CUSTOMERS,
                   AVG(account_balance) AS AVG_BALANCE
            FROM customers
            LEFT JOIN account_balances USING (customer_id)
            GROUP BY city;
            """

        elif insight == "Q2: Account Type with Highest Balance":
            Query = """
            SELECT account_type, SUM(account_balance) AS TOTAL_BALANCE
            FROM customers
            JOIN account_balances USING (customer_id)
            GROUP BY account_type
            ORDER BY TOTAL_BALANCE DESC
            LIMIT 1;
            """

        elif insight == "Q3:Top 10 Customers by Balance":
            Query = """
            SELECT c.customer_id, c.name,
                   SUM(a.account_balance) AS TOTAL_BALANCE
            FROM customers c
            JOIN account_balances a USING (customer_id)
            GROUP BY c.customer_id, c.name
            ORDER BY TOTAL_BALANCE DESC
            LIMIT 10;
            """

        elif insight == "Q4:High Balance Accounts Opened in 2023":
            Query = """
            SELECT c.customer_id, c.name,
                   a.account_balance, c.join_date
            FROM customers c
            JOIN account_balances a USING (customer_id)
            WHERE YEAR(c.join_date) = 2023
              AND a.account_balance > 100000;
            """

        elif insight == "Q5:Transaction Volume by Type":
            Query = """
            SELECT txn_type, SUM(amount) AS TOTAL_VOLUME
            FROM transactions
            GROUP BY txn_type;
            """

        elif insight == "Q6:Failed Transactions by Type":
            Query = """
            SELECT txn_type, COUNT(*) AS FAILED_COUNT
            FROM transactions
            WHERE status = 'FAILED'
            GROUP BY txn_type;
            """

        elif insight == "Q7:Transaction Count by Type":
            Query = """
            SELECT txn_type, COUNT(*) AS TOTAL_TRANSACTIONS
            FROM transactions
            GROUP BY txn_type;
            """

        elif insight == "Q8:High-Value Transaction Accounts":
            Query = """
            SELECT account_id, COUNT(*) AS HIGH_VALUE_TXNS
            FROM transactions
            WHERE amount > 20000
            GROUP BY account_id
            HAVING COUNT(*) >= 5;
            """

        elif insight == "Q9:Average Loan & Interest by Loan Type":
            Query = """
            SELECT loan_type,
                   AVG(loan_amount) AS AVG_LOAN,
                   AVG(interest_rate) AS AVG_INTEREST
            FROM loans
            GROUP BY loan_type;
            """

        elif insight == "Q10:Customers with Multiple Active Loans":
            Query = """
 
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
    

        


        elif insight == "Q11:Top 5 Customers by Outstanding Loans":
            Query = """

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



        elif insight == "Q12:Average Loan Amount per Branch":
           Query = """

                 SELECT 
                 b.branch_name,
                 AVG(l.loan_amount) AS avg_loan_amount
                 FROM loans l
                 JOIN branches b
                 ON l.branch = l.branch
                GROUP BY b.branch_name;"""

        

        elif insight == "Q13:Customer Age Group Distribution":
            Query = """
            SELECT
                CASE
                    WHEN age BETWEEN 18 AND 25 THEN '18-25'
                    WHEN age BETWEEN 26 AND 35 THEN '26-35'
                    WHEN age BETWEEN 36 AND 45 THEN '36-45'
                    WHEN age BETWEEN 46 AND 60 THEN '46-60'
                    ELSE '60+'
                END AS AGE_GROUP,
                COUNT(*) AS CUSTOMER_COUNT
            FROM customers
            GROUP BY AGE_GROUP
            ORDER BY AGE_GROUP;
            """

        elif insight == "Q14:Ticket Resolution Time by Category":
            Query = """
            SELECT issue_category,
                   AVG(DATEDIFF(date_closed, date_opened)) AS AVG_DAYS
            FROM support_tickets
            WHERE date_closed IS NOT NULL
            GROUP BY issue_category
            ORDER BY AVG_DAYS DESC;
            """

        elif insight == "Q15:Top Support Agent (Critical Tickets)":
            Query = """
            SELECT support_agent,
                   COUNT(*) AS RESOLVED_TICKETS
            FROM support_tickets
            WHERE priority = 'Critical'
              AND customer_rating >= 4
              AND status = 'Resolved'
            GROUP BY support_agent
            ORDER BY RESOLVED_TICKETS DESC
            LIMIT 1;
            """

        if Query:
            cursor.execute(Query)
            result = cursor.fetchall()
            st.dataframe(result)
        else:

            st.warning("⚠️ Please select a valid analysis")

