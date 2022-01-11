#!/usr/bin/env python
# coding: utf-8

# # Lecture 2: Introduction to cloud computing and connection to cloud
# Gittu George, January 6 2022

# ## Todays Agenda
# 
# - Intro to cloud computing – WHAT ?, WHY ?, HOW?
# - General overview on services available in AWS (Amazon web services)
# - Various database services available in AWS
# - Details on RDS - Relational Database Service
# - Connecting to RDS (Postgres)
# 
# ## Learning objectives
# - Have a general understanding of cloud computing and help you get started.
# - You will know how to connect to a remote database from a Jupyter notebook.
# - Different ways in interacting with the database from jupyter notebook.
# - Showing different ways of loading the data.
# - You will use queries to bring data into a Jupyter notebook and provide a simple data analysis.
# 
# 
# 
# ## Intro to cloud computing
# 
# Let me tell you a short cloud-computing tale. This story starts from a computer that you all are familiar with. By the end of this tale, you will answer WHAT, WHY & HOW cloud computing.
# 
# Here is the computer that I am talking about:
# <br>
# <img src='img/l31.png'>
# <br>
# OKAY! So now we all agreed to call monitor as the client and that box as server. Now let's take this knowledge to a bigger picture or think about how this idea will be when you start working in the industry. 
# <br>
# <img src="img/l32.png">
# <br>
# 
# 
# Collectively we call these servers data centers ( you can also hear people calling some other names like on-premise infrastructure). Mostly all companies (may be used to as there is this trend of moving to cloud) have data centers, which is considered a company powerhouse for powering data needs (like storage, processing, etc.)
# 
# If you want to check out more on those gigantic data centers. Checkout [here](https://www.youtube.com/watch?v=g7JaN3rTK2A)
# 
# Let me pause and take a minute to answer this question:
# 
# ```{sidebar} Question is here..
# So assume that UBC has some server, and we are using this “client-server model” to do our analysis, then what do we not care about in the laptop requirements that MBAN mandates?
# ```
# <img src='img/l33.png' width='55%'>
# 
# <br>
# <br>
# 
# Now that you understand this client-server model, let's look inside these data centers to see which parties are involved.
# 
# 
# ```{margin}
# <img src="img/funny.png">
# ```
# <img src=img/l35.png>
# 
# 
# List down in your notes about the labor costs:
# 
# List down costs other than labor cost:
# 
# With cloud computing, we are bringing down most of the costs you listed now. Look how neat and clean the diagram below is as cloud providers are taking care of most of the responsibilities that we discussed and using their infrastructure servers as services.
# 
# ```{margin}
# <img src="img/whocares.png">
# ```
# <img src=img/l34.png>
# 
# 
# I hope by now you can formulate an answer for questions WHAT, WHY, and HOW cloud computing. 
# 
# - ***WHAT?***
# Cloud Computing is when we get a server in the cloud for our compute, storage, databases, and network services provided to users via the internet.
# 
# - ***WHY?***
# Save lots of money that otherwise need to spend for on-premise infrastructure, and I don't want to worry about infrastructure and can focus on your analysis right from day1.
# 
# - ***HOW?***
# Some cloud vendors provide infrastructure as a service by taking care of all the responsibilities that otherwise need to be done on-premise.
# 
# ## Benefits of cloud computing:
# - Trade capital expense for variable expense
# - Massive economies of scale
# - Stop guessing capacity
# - Increase speed and agility
# - Stop spending money on running and maintaining data centers
# - Go global in minutes
# 
# Source: aws
# 
# ## Cloud providers
# - Amazon Web Services (AWS)
# - Microsoft Azure
# - Google Cloud
# 
# ## Category of services available in AWS
# - Compute
#   - EC2 – Elastic Cloud Compute
# - Storage
#   - EBS - Elastic Block Storage
#   - S3 - Simple Storage Service
# - Database
# 
# <img src="img/l36.png">
# 
# Source: [dbtest](https://www.dbbest.com/technologies/nosql-databases/)
# 
# ### Database (Amazon RDS)
# - Relational database service (RDS) provides a simple way to provision, create, and scale a relational database within AWS.
# - Managed service – AWS takes responsibility for the administrative tasks
# - Following database engines are supported
#   - Amazon Aurora
#   - PostgreSQL
#   - MySQL
#   - MariaDB
#   - Oracle Database
#   - SQL Server
# 
# For a list of entire services and details, check out [here](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)
# 
# ## Ways to interact with AWS
# 
# - [Web interface](https://www.awsacademy.com/LMS_Login)
# 
#     A web-based GUI provides the capability to interact with the services within AWS.
# 
# - [AWS CLI](https://aws.amazon.com/cli/)
# 
# - [SDK](https://aws.amazon.com/sdk-for-python/)
# 
# A good blog [here](https://adamraffe.com/2019/02/20/aws-fundamentals-part-3-interacting-with-aws/) explains various ways of interaction.
# 
# ## Demo
# Lets together explore AWS
# 
# ```{figure} img/explore.png
# ---
# width: 200px
# align: center
# ---
# ```

# ## Connecting To Cloud (RDS)
# Consider your database what you built as an independent entity. Then, follow instructions to set up your database in the cloud.
# 
# OKAY.. so now you have your database ready! In our case, we set up our Postgres database in RDS. Since you are not using an already existing database, you created it, so it's empty now. So we need to load data into this database. After loading data to the database, we are all set with querying from the database.
# 
# Whether it's for loading or querying the database, we need to connect to the database. You all are aware of 2 other ways that you can use to interact with the database outside of this jupyter notebook.
# 
# - pgadmin
# - psql
# 
# What information do you want to know if you're going to connect to the above? We need to know the information of the database that you wanted to connect to 
# - Hostname
# - Port number
# - User name (need to make sure that this user have access to the database)
# - Password (Ofcourse !! you need to know the password for this user)
# 
# If you want to know more details refer to the installation notes for pgadmin & psql
# 
# Now let's think about other sources you want to connect to the database. Here are a few that I thought of
# - From a programming language (java, R, python, etc..)
# - From your jupyter notebook
# - From tableau 
# - From excel 
# - From R Studio
# - OR from any other application that you are using, e.g., your banking website
# 
# Besides knowing the hostname, port name, username, and password, we also need to install an Application programming interface (API) that helps the applications on the client-side communicate with the server-side (in our case database). Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC) are 2 of such APIs that are provided by the database vendor (Postgres, Oracle, MySQL, etc..) to access their database.
# 
# JDBC is language-specific, and its the standard interface between any java application and database. JDBC converts the java programmer's requests to the database to something that the database understands (you can think of it as a translator). Meanwhile, ODBC is not language-specific, so it can convert requests from any application/software/programming language to something the database understands. Here is a diagram that will help you understand how ODBC works.
# 
# <img src="img/connection.png" width= 65%>
# 
# ```{sidebar} How ODBC connects ?
# ```{figure} img/odbc.png
# ---
# width: 450px
# align: center
# ---
# ```
# In the rest of the section, let's focus on connecting to the database from python and the jupyter notebook. We will be using specific packages to make this possible, but as we have discussed, it uses ODBC for the connection. Many packages make this possible, but we will discuss a package named `psycopg2.`

# ## Using psycopg2 package
# Let first install the package using [conda](https://anaconda.org/anaconda/psycopg2)
# 
# ```bash
# %%sh
# conda install -c anaconda psycopg2 
# ```
# Let's make sure that we can import it.

# ```
# import psycopg2
# ```

# Now we have `psycopg2` imported into our notebook. `psycopg2` package manages the interaction between python and our database. So the first takeaway message here is that psycopg2 has nothing to do with jupyter notebook; rather, it's tied to python. So we use jupyter notebook as an interactive programming environment to query in python. Later if time permits, we will talk about `SQL magics,` which is a specific way of interacting with databases from jupyter notebook.
# 
# Okay! Let's now get to the steps to connect to a database using psycopg2.
# 
# - ***Create a connection*** 
# 
#     This connection allows communication with the database; It opens up a network connection.
# 
# - ***Create a cursor***
# 
#     The cursor is an address for the memory on the database management server to say this is what we are looking at. This python object helps you execute the query and fetch the results from the database. You can read more about cursors [here](https://medium.com/dev-bits/understanding-postgresql-cursors-with-python-ebc3da591fe7).
# 
# - ***Formulate your query***
# 
#     Formulate the SQL query that you want to execute in the database.
# 
# - ***Execute***
# 
#     Pass your query to execute() method of cursor object, run the query in the database.
# 
# - ***Fetch/commit/rollback***
# 
#     The query that we performed in execute doesn't return the query right away. To return it, we need to perform a fetch. If the query is to write something, then we need to commit it. If some transaction went wrong, then we need to roll back it.
# 
# Let's now check out these by creating a ticker table, loading data to it, and doing some querying. Let's first create schema import,
# 
# ```{note}
# Below you need to replace the `conString` values with your `host`,`dbname`,`user`, `password`, and `port` you used while creating your RDS instance.
# ```

# ```bash
# # Create a connection
# conString = {'host':'mbandtweet.xxxxx.amazonaws.com',
#              'dbname':'postgres',
#              'user':'postgres',
#              'password':'password',
#              'port':5432}
# conn = psycopg2.connect(**conString)
# # Create a cursor
# cur = conn.cursor()
# # - Formulate your query
# query = """CREATE SCHEMA IF NOT EXISTS classwork"""
# # - Execute
# cur.execute(query)
# # - commiting.
# conn.commit()
# ```

# In the above code we created schema import. You probably already know about it, but if you want to read more on when & why use schema, check this [out](https://www.postgresql.org/docs/8.1/ddl-schemas.html). Let's create table,

# ```
# ## Here we create the table tickers
# cur.execute("""CREATE TABLE IF NOT EXISTS classwork.tickers(
#                actsymbol text PRIMARY KEY,
#                securityname text,
#                exchange text,
#                cqssymbol text,
#                etf text,
#                roundlotsize text,
#                testissue text,
#                nasdaqsymbol text)""")
# conn.commit()
# ```

# ### Loading the data to database
# Now we have our table ready, let's load data into this table. Here we read line by line using python and then insert it into the table using `execute.` This took me around ~5 min.
# 
# ```bash
# from ftplib import FTP
# from io import StringIO
# import csv
# 
# session = FTP('ftp.nasdaqtrader.com')
# session.login()
# r = StringIO()
# session.retrlines('RETR /SymbolDirectory/otherlisted.txt', lambda x: r.write(x+'\n'))
# r.seek(0)
# csvfile = list(csv.DictReader(r, delimiter='|'))
# 
# ## Here we are reading each row and then inserting it to the table one at a time 
# for row in csvfile:
#     cur.execute("INSERT INTO classwork.tickers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", list(row.values()))
# 
# conn.commit()
# ```

# There are many other ways of loading the data to the table. Few to mention
# 
# - [copy_from](https://naysan.ca/2020/06/21/pandas-to-postgresql-using-psycopg2-copy_from/)
# - [COPY](https://www.postgresql.org/docs/13/sql-copy.html) command.
# 
# When using these methods, make sure your CSV file is formatted correctly, or else you will be getting errors.
# 
# If you want to read more on other ways to load data in Postgres, check out [this](https://www.highgo.ca/2020/12/08/bulk-loading-into-postgresql-options-and-comparison/) article.

# ### Reading data from database
# As discussed before, an execute doesn't return the data right away, and we need to perform a fetch. There are mainly 3 flavors of fetch 
# - fetchone
# - fetchmany
# - fetchall

# ```
# query = """SELECT * FROM classwork.tickers"""
# cur.execute(query)
# row = cur.fetchone()
# print(row)
# ````

# ```
# query = """SELECT * FROM classwork.tickers"""
# cur.execute(query)
# row = cur.fetchmany(5)
# print(row)
# ````

# ```
# query = """SELECT * FROM classwork.tickers LIMIT 5"""
# cur.execute(query)
# row = cur.fetchall()
# print(row)
# ```

# Sometimes you might not need everything that is returned from a database. For example, you might want to transform each row returned from the database. In these cases fetching each row at a time will be of help.

# ```
# query = """SELECT * FROM classwork.tickers LIMIT 5"""
# cur.execute(query)
# for rows in cur:
#     print(rows[1])
# ```

# But in general most of the cases, you can go with fetchall, provided you write an efficient SQL query to execute and get just the columns and rows that you are interested in. 

# Before we move to the next topic, let me show you how rollback works. Say, for instance, your query ends up failing for some reason.

# ```
# query = """SELECT * FROM classwrk.tickers LIMIT 5"""
# cur.execute(query)
# row = cur.fetchall()
# print(row)
# ```

# You realized it and corrected it.

# ```
# query = """SELECT * FROM classwork.tickers LIMIT 5"""
# cur.execute(query)
# row = cur.fetchall()
# print(row)
# ```

# But this query, even though it's correct it won't end up going through and will get this error saying `your current transaction is aborted`
# 
# <img src='img/error.png' width='55%'>

# You need to do a `rollback()` to back to the previous stable state and then execute your query.

# ```
# conn.rollback()
# ```

# ```
# query = """SELECT * FROM classwork.tickers LIMIT 5"""
# cur.execute(query)
# row = cur.fetchall()
# print(row)
# ```

# ```{important}
# Whenever you get an error, as we showed before, `InFailedSqlTransaction: current transaction is aborted, commands ignored until end of transaction block
# `, make sure you do a `rollback`.
# ```
# 
# ```{tip}
# It's not a bad idea to develop your SQL query in pgadmin, toad or any other GUI interface and then bring it in once you know it's ready.
# ```

# ## Dealing with passwords
# ```{margin}
# <img src="img/secret.png">
# ```
# Say if you want to share this notebook with your colleague, or if somebody came by and looked at your notebook, they can see your database connection details, including your password. It's probably okay now as it's a toy database, but when you start working in the industry, you will be dealing with a database ( or, in other words, business), and it can cause lots of problems if the password is compromised. So now on, let's practice not doing the connection call as I did.
# 
# We will make use of a python package dotenv. Install python package

# ```
# %%sh
# conda install -c anaconda python-dotenv
# ```

# ```{seealso}
# https://anaconda.org/conda-forge/python-dotenv
# ```
# 
# This package looks for a .env file in the folder where your notebook resides, and it loads your database connection details to the environment variable for your session. Here is how my env file looks like
# 
# ```bash
# (base) ggeorg02@MacBook-Pro assign1 % cat .env  
# DB_HOST=mbandtweet.xxxxx.us-west-2.rds.amazonaws.com
# DB_NAME=postgres
# DB_USER=postgres
# DB_PASS=password
# DB_PORT=5432
# ```
# You have to change this to your connection details
# To create a .env file, you might want to use your terminal. Check how to use [vi editor](https://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/)
# 
# ```bash
# cd <path to your notebook folder>
# vi .env
# ```
# 
# ```{note}
# I purposely created this file with just an extension, not a filename. And you can usually make this kind of file only from the terminal, so I am using vi editor. You might not be able to find this file from your file explorer, and that's the reason we created it starting with a period. This means that `.iamasecretfile`. So no wonder why you can't see, right? This way, no one can accidentally look at this file when using your computer. if you want to see it, then again, you want to go to terminal and type `ls -a`
# ```
# 
# After this, you can call all variables like this. 

# ```
# import os
# import psycopg2
# 
# ##Make sure you import and load your .env file
# from dotenv import load_dotenv
# load_dotenv()
# 
# conString = {'host':os.environ.get('DB_HOST'),
#              'dbname':os.environ.get('DB_NAME'),
#              'user':os.environ.get('DB_USER'),
#              'password':os.environ.get('DB_PASS'),
#              'port':os.environ.get('DB_PORT')}
# print(conString["port"])
# ```

# This way, you don't have to worry about exposing your password to anyone.
# 
# ```{caution}
# Nowhere in assignments/projects should you include the hostname or password. If anything needs to be checked, then TA's will contact you.
# ```
# 
# ```{important}
# Make sure you close the cursor and connection before quitting your jupyter notebook. This is a good practice and can protect you from memory leakage and too many open connections.
# ```

# ```
# cur.close()
# conn.close()
# ```

# ## Working with dumps
# Taking dumps comes in handy when you want to share a copy of your database with someone or if you're going to keep it as a backup. 
# 
# - How can I take a dump of the database that I already have. 
# ```bash
# pg_dump -h mbandtweet.xxxxx.ca-central-1.rds.amazonaws.com --username=postgres -n import -f import.sql`_
# ```
# Read more about how to take database dumps [here](https://www.postgresql.org/docs/12/app-pgdump.html).
# 
# - How can you load these dumps to make your schema and tables ready?
# 
# psql -h HOST_NAME -U USER_NAME DATABASE < PATH_TO_THE_.sql_DUMP_FILE
# 
# ```bash
# psql -h mbandtweet.xxxx.us-west-2.rds.amazonaws.com -U Postgres Postgres < import.sql
# ```

# ```{warning}
# If you are not using your RDS instance, make sure you shut it down from your AWS console. You can always restart it when working on your assignments/projects. However, your credits are limited, and if those get exhausted, we won't provide you with more.
# ```
# 
# ```{note}
# Closing your lab doesn't shut down the RDS instance; you need to shut it down from your AWS console explicitly.
# ```
