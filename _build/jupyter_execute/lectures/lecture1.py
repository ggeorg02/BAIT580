#!/usr/bin/env python
# coding: utf-8

# # Lecture 0: Course Introduction
# Gittu George, January 4 2022

# ## Learning objectives
# 
# - To think critically about databases as part of an analytics workflow
# - Learn how to design, use and understand the inner working of the SQL based databases
# - Taking you from level zero to intermediate with the NoSQL databases (document and graph-based databases)
# - To work with the data to find the tools best suited to answering the questions you pose
# - To be able to present analytic workflows and decisions clearly to stakeholders

# ## Teaching squad
# ### Instructor
# ![](img/l1.png)
# - I am Gittu George, Ph.D
# - I am a Postdoctoral Teaching & Learning Fellow.
# - Email Me: ggeorg02@cs.ubc.ca
# - Office Hours: Tue 2 -3 pm
# - Research interests are at the intersection of computer science and genomics.
# - I primarily teach cloud computing courses with MDS, and it is my first time teaching BAIT 580A.
# - Simon Goring developed this course, and I made my changes/additions to the course.
# ### Teaching Assistants
# |               |                               |
# | :--------------------------------------- | :-----------------   | 
# | <img src="img/colby.jpg" alt="Colby" class="bg-primary" width="600px"/>| **Colby DeLisle:** Hey There! I'm a PhD candidate in physics at UBC, and I study quantum information and quantum field theory. Originally from Missouri, USA, I got my BSc in computer science from the University of Missouri before coming to Vancouver..| 
# |<img src="img/daniel.png" alt="Brie" class="bg-primary" width="600px"/> | **Daniel Ramandi:** Hey There! I'm a PhD student, working in a Neuroscience lab in the department of Psychiatry, looking at Neural correlates of behavior. I use machine learning to model brain activity and behavior. I'm originally from Iran,  and love swimming, cooking and Vancouver! :))|
# | <img src="img/hu_elisa.jpg" alt="Rubia" class="bg-primary" width="600px"/> | **Elisa Hu:** Hi there, my name is Elisa, I am in my last year of undergrad majoring computer science and statistics. I had 2 years TA experience before this course. Besides that, I love eating good food and explore new places. Hope to see you all in the class!

# ## Todays Agenda
# - Course Overview
# - Data management in a big data environment
#     - What is big data?
#     - Which tool to use?
#     - How big is big data?
# - How to approach big data? – Some guidelines

# ## Course Overview
# 
# ### My Goals for the Course
# - To think critically about databases as part of an analytics workflow
# - Learn how to design, use and understand the inner working of the SQL based databases
# - Taking you from level zero to intermediate with the NoSQL databases (document and graph-based databases)
# - To work with the data to find the tools best suited to answering the questions you pose
# - To be able to present analytic workflows and decisions clearly to stakeholders
# 
# ### What this course is not about
# - SQL or python programming 
# - Cloud computing 
# - Visualization
# 
# ### Course plan
# 
# | Date        | Topic                                         | Assessments due                                              |
# |-------------|-----------------------------------------------|--------------------------------------------------------------|
# | January 4   | Introduction to Big Data Analytics            |                                                              |
# | January 6   | Introduction to Cloud Computing               |                                                              |
# | January 11  | Data Modeling for Business Applications       | Group Assignment: Question Presentation                      |
# | January 13  | SQL for Visualization, constraints & cleaning | Assign1: Setting up AWS & Linking Jupyter to RDS (Postgres)- Jan 14th |
# | January 18  | Faster SQL for Visualization                  | |
# | January 20  | (de)Normalization & Data Warehousing          |  Group Assignment: Data Dictionary and Jupyter Notebook Draft- Jan 21st                                                            |
# | January 25  | Introduction to NoSQL and Graph Databases     |                                                              |
# | January 27  | Querying Graph Databases                      | Assign2: Data pipelines with Postgres (DDL)- Jan 28th                 |
# | February 1  | Modeling Data with Graphs                     |                                                              |
# | February 3  | Class Conclusions/ Special Topics             |                                                              |
# | February 7  |                                               | Assign3: Setting up & asking questions to Graph Database     |
# | February 10 |                                               | Group Assignment: Final Report and Presentation              |
# 
# ### Course Model
# 
# <img src='img/l2.png'  width = "65%"/>
# 
# ```{sidebar} Toolsets we will be using
# - Data - JSON, CSV
# - Cloud Vendor - AWS
# - RDBMS - PostgreSQL , Neo4j, MongoDB
# - Analysis - Python & Jupyter
# 
# ```
# 
# ### Individual Assignments (60 %)
# 
# #### Assignment 1 (20 %)
# 
# ```{sidebar} Let's checkout some tweets!!
# ```{figure} img/l3.png
# ---
# alt: ec2-1
# width: 400px
# align: center
# ---
# ```
# 
# Introduce you to AWS, working with Postgres in a Jupyter notebook
# - Think about data in the context of a research problem
# - Setup your AWS account
# - Launch your database in AWS
# - Use Python & Jupyter
# - Get code to download data directly from an FTP
# 
# #### Assignment 2 (20 %)
# 
# Data Pipelines in Jupyter/Postgres
# - Connect to a database
# - Generate a query to select data
# - Produce reasonable plots to explain a feature
# 
# <img src='img/l4.png' >
# 
# #### Assignment 3 (20 %)
# 
# Six Degrees of Sampling
# - An introduction to graph databases using the initial Twitter data
# - Using the graph to answer questions about networks of interaction
# - Producing interactive plots to represent knowledge
# 
# ### Group Assignments (40 %)
# 
# There will 5 students in a randomly assigned group. Checkout [this](https://canvas.ubc.ca/courses/89141/discussion_topics/1258994) to find your group.
# - Ask the question (10 %)
# - Find the data (Jupyter & data dictionary) (10 %)
# - Presentation and reproducible Jupyter workbook (10 %)
# 
# ```{figure} img/ready.png
# ---
# width: 250px
# align: center
# ---
# ```
