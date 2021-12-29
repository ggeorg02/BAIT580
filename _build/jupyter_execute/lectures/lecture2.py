#!/usr/bin/env python
# coding: utf-8

# # Lecture 1: Data Management in a Big Data Environment
# Gittu George, January 4 2022

# ## Learning objectives
# - You will understand how database management systems can be optimized for big data applications
# - You will understand how the axes of big data (the 4Vs) apply to databases
# - You will understand how the questions you ask affect the tools needed for data analysis
# 
# ## Let's hear a story on 'it Depends.'
# You probably might have come across many questions like this in Reddit or StackOverflow. 
# 
# <img src = 'img/l21.png'>
# 
# ```{margin}
# ***“Focus on the business challenge first and then figure out the technology required to support this challenge.”***
# 
# Lopes et al., 2017. Software Architecture for Big Data and the Cloud.
# DOI:[10.1016/B978-0-12-805467-3.00010-7](https://www.sciencedirect.com/science/article/pii/B9780128054673000107?via%3Dihub)
# ```
# You probably want to check out these questions and answers,[1](https://www.reddit.com/r/datascience/comments/hd3tqs/the_best_sql_vs_nosql_mindset_ive_ever_heard/
# ),[2](https://www.reddit.com/r/datascience/comments/i0y3po/how_big_is_big_data/
# ),[3](https://www.reddit.com/r/datascience/comments/9vwhl8/when_to_use_r_vs_when_to_use_python/
# ),[4](https://www.reddit.com/r/learnprogramming/comments/lo5kpt/can_someone_explain_with_example_when_to_choose/
# ),[5](https://www.reddit.com/r/webdev/comments/9g0z6f/sql_vs_nosql/
# ),[6](https://www.reddit.com/r/webdev/comments/c3226n/when_should_one_use_sql_and_when_should_one_use/
# ),[7](https://www.reddit.com/r/datascience/comments/b09mfj/for_data_visualization_what_is_the_benefit_of/
# ) to see what they are talking about. Reading these questions and answers is interesting, but before thinking about all these technologies, you have to first think about the problem in your hand. If you have a clear understanding of the business problem in hand and list down all the features of your problem, you can list out the pros and cons of using one technology over another. 
# 
# So which technology should I use? 
# It all boils down to `it depends` on your business problem. Let me take you through some of the `Depends`.
# 
# ```{margin}
# <img src = 'img/depends.png'>
# ```
# 
# - `Depends` on the output you need
#   - Interactive or static graphs?
#   - Integrated reports, tables, websites?
#   - For yourself, for your company, for the public?
# 
# - `Depends` on the data you use
#   - One large file, many small files?
#   - Use the whole file at once or in small chunks?
#   - Is data static (cold) or dynamic (hot)
# 
# - `Depends` on the question(s) you are trying to ask
#   - Is it high value?
#   - Are they complex (OLAP) or simple (OLTP)
#   - Do you need results quickly?
#   - For yourself, for your company, for the public?
# 
# ```{margin}
# The analysis also showed that the underlying infrastructures have special usage and operational characteristics. ***Clusters should be operated at high utilisation rate to keep costs low;*** in the cloud, careful management of virtual machine instances and data transfer between frequent and infrequent-access storage services are necessary for minimising cost........
# 
# Juhasz, Z. 2020. Cluster Computing. [DOI: 10.1007/s10586-020-03141-y](https://link.springer.com/article/10.1007%2Fs10586-020-03141-y)
# ```
# 
# `It Depends` matters a lot, especially in “Big Data,” as
# - The costs and benefits are much higher
# - The impact on a business's bottom line can be significant
# 
# Some of you might be thinking now, how big the data should be for it to be big data ? that too `It Depends.`
# It depends on many `V's.` Let's discuss 4 `V's` in our next section.

# ## 4 Vs of Big Data
# 
# Whenever you come across any big-data article, you will hear about V's. 3V ’s definition was introduced in 2001 by Gartner Inc. analyst Doug Laney. After this, it evolved a lot with many other V's. Here I will be going through 4 V more common V's discussed in today's industry. The Four V's are, broadly speaking, Velocity, Veracity, Volume, and Variety. These were introduced to help understand the challenges of Big Data in computing and analytics.  The concepts are broadly applicable across all disciplines—for example, check what my colleague wrote about [big data in Ecology](https://doi.org/10.1093/biosci/biy068).  Various datasets or problems are affected differently by each of the different axes, so understanding the different dimensions of big data is critical to finding the analytic solutions we intend to apply.
# 
# <img src='img/vvvv.png'>
# 
# Source: Farley, Dawson, Goring & Williams, Ecography, 2018 [Open Access](https://academic.oup.com/bioscience/article/68/8/563/5049569)
# 
# Other people have spoken about five Vs ([Value](https://bizibl.com/marketing/download/fifth-v-big-data)), [seven Vs](https://impact.com/marketing-intelligence/7-vs-big-data/) (adding Variability, Visualization and Value), and even more.  If you want to know more V's ( 42 of them ) and add your vocabulary, you can check out [this](https://www.elderresearch.com/blog/the-42-vs-of-big-data-and-data-science/) article. These additional V's can be informative, but, by and large, the Four V's provide the most insight into data challenges.
# 
# Let's checkout 4 V's in detail.
# 
# ### Volume
# ```{margin}
# <img src = 'img/volume.png'>
# ```
# When we think about "Big Data, " this is often the most familiar dimension.  We think of Big Data in terms of gigabytes, terabytes, or petabytes.  The volume presents a significant challenge for data storage, although modern technology has reduced this challenge to some degree.  It also produces a challenge for recall (simply finding information) and for data processing (transforming and analyzing data). Here are the pointers to look out for:
# 
# - How big is the data?
# - Total File Size
# - Number of Data Points
# 
# #### Volume Solutions
# 
# - Cloud storage solutions
# 
# But in most cases, it's not just about storing your data; it's more about how you will process the data. Then there will be limitations by read-write access or/and memory capacity.
# ```{margin}
# <img src = 'img/volumesolu.png'>
# ```
# - Partitioning/Sharding
# 
# We must look at this from different angles, partitioning/sharding from a database perspective, which we will touch upon later in this course. Another option is to go for distributed file system where it stores data in small blocks so that it's easy to process when needed. 
# 
# - Parallel processing 
# 
# Small chunks of files can be processed simultaneously by using different servers/cores and aggregate results at the end. This is mainly made possible in the industry by high-performance/cluster computing or other map-reduce-based frameworks like Hadoop/spark.
# 
# 
# ### Velocity
# 
# ```{margin}
# <img src = 'img/velocitysolu.png'>
# ```
# ```{margin}
# “The speed of transmission is what allows HFTs to always have a head start because they closeout and softsell [more] rapidly than anyone.”
# [High Frequency Trading - Medium post](https://medium.com/@moonxfamily/high-frequency-trading-races-to-nanoseconds-689f86109fb4)
# ```
# 
# Velocity is a second factor.  We may be interested in only the most recent data, minutes or seconds, requiring low volumes of data, but at a high velocity.  For example, quant traders might be using high-frequency stock data to maximize trading profits.  This involves analysis with extremely fast turnover. Here are the pointers to look out for:
# 
# - How fast is the data arriving?
#   - Annual data from Stats Can?
#   - Real-time data from stock tickers or Twitter?
# - How fast do we need our answers?
#   - Monthly or annual strategy planning?
#   - Real-time commodities purchasing?
# - How fast is the data changing?
#   - Changing interpretations?
# 
# #### Velocity Solutions
# ```{margin}
# <img src = 'img/coldhot.png'>
# ```
# - Agile development.
# - BASE databases (Basically available).
# - Modular analytics & fault tolerance.
# - Identify “Key Performance Indicators”.
# - Develop real-time reporting.
# - Split the data into hot (Redis , RAM) and cold data (RDBMS, Disk Storage).
# 
# ### Variety
# ```{margin}
# <img src = 'img/variety.png'>
# ```
# When we bring in multiple data sources or build data lakes, how well do data fields align?  Are temporal scales aligned?  Are addresses, zip codes, census tracts, or electoral districts aligned with other spatial data?  Are financial values in standard units? If not, how do we transform the values to account for fluctuating exchange rates? Here are the pointers to look out for 
# 
# - How different is the data source?
# - Are data coming from multiple sources?
#   - Do fields in sources align well?
#   - Do files have similar formatting?
# - How different are the data structures?
#   - Can the data work in a relational model?
#   - Do we need multiple data models?
# 
# 
# #### Variety Solutions
# - Normalize using multiple data sources.
# - Clear interface layers (structured based on velocity and volume).
# - Different management systems (RDBMS & Graph DB).
# 
# ### Veracity
# ```{margin}
# <img src = 'img/veracitybi.png'>
# ```
# Is data scraped from the web, contributed by individuals, or obtained from other external sources reliable?  How do spam accounts, scraping tools, or missing data affect our interpretations of patterns in the data? Here are the pointers to look out for 
# 
# - How much do (should) we trust the data?
# - What assumptions or biases are inherent?
# - Does the value change over time?
# - How do we manage missing data?
# - How do we validate or check data validity?
#   - Incoming data
#   - Outgoing analysis
# 
# #### Veracity Solutions
# ```{margin}
# <img src = 'img/veracity.png'>
# ```
# ```{margin}
# 
# ...abstracts of papers comparing citizen science data to professional data indicated that the citizen science data quality was good in 73% of the abstracts, the results of our quantitative assessment cast more doubt on the accuracy of the data.
# [Aceves-Bueno et al., 2017. Bulletin of the Ecological Society of America](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/bes2.1336)
# ```
# - Know your data
# - Data volatility (how long is it accurate)?
# - Domain knowledge is critical
# - Clear definition of assumptions
# - Clear checks on key processes
# - TDD - Test Driven Development (assertions & tests)
# 
#  . . . abstracts of papers comparing citizen science data to professional data indicated that the citizen science data quality was good in 73% of the abstracts, the results of our quantitative assessment cast more doubt on the accuracy of the data.
# Aceves-Bueno et al., 2017. Bulletin of the Ecological Society of America
# [Open Access]
# 
# ## The Four V's and Analytic Workflows
# 
# These challenges come to the forefront when we're working with data.  The goto standard is to open up an Excel or read in a comma-separated file to look at the data, get a sense of what is happening, or summarise the key elements.  
# 
# *  When that file is <10MB in size, that's often not a big problem, but as files get bigger and bigger, even calculating a simple mean is an issue (**Volume**).
# *  When the data contains text, images, values in different currencies, summary becomes problematic (**Variety**)
# *  When the data contain transcription errors, conflicting values, and biases in data collection or coverage, how do we trust our summaries? (**Veracity**)
# *  When the 10MB you just summarized are out-of-date, as soon as you're done outlining them, how do you present these results to your colleagues? (**Velocity**)
# 
# ### Problem Based Approaches
# 
# Many of these challenges have straightforward(ish) solutions, but how we apply those solutions and our choices are often specific to the problem we are trying to answer.  For example, a common solution people present to **Volume** is to use a NoSQL database to store and index information.  This is an appropriate solution in many cases; however, most data is well suited to relational databases, and these often provide advantages over non-relational databases.
# 
# One of the most important steps in choosing how to set up your analytic workflow is the proper framing of your question.  This will help you understand:
# 
#   1. What data sources do you need ?
#   2. How you will transform that data ?
#   3. How you will represent your data ?
# 
# ## 4 V quadrant
# Now, look at these 4 V's in this quadrant and see how different industries score.
# <img src='img/variousbig.png'>
# 
# To summarize, when is big data appropriate? `Depends on:`
#  - Velocity, Veracity, Volume, and Variety
#  - When traditional tools begin to fail
#  - If analysis crashes your computer

# ## General Framework for Big Data Analysis
# 
# How to Approach Big Data
# 
# ### Understand your data
# 
# <img src ='img/understanddata.png' width="60%"/>
# 
# ```{sidebar} Various sections in workflow
# - Submission Information Package
# It shows how the data enters the process
# - Archive Information Package
# Shows what are the processes involved in archiving. 
# - Dissemination Information Package
# It shows how the users consume the data
# 
# In short, this shows the processes that data goes through right from its raw state to when it reaches the hands of the person/software who will be consuming the data for further insight generation. 
# ```
# 
# ```{margin}
# “a data dictionary is possibly one of the most valuable artifacts that a data team can deliver to the business.” - Carl Anderson [Medium](https://medium.com/@leapingllamas/data-dictionary-a-how-to-and-best-practices-a09a685dcd61)
# ```
# 
# `Descriptive information` - As you see, this appears 2 times in this workflow; this is a vital piece. We can also call it a data dictionary. it helps
# 
# - Manage data variety
# - Align source data with project or organization goals
# - Manage veracity (we know what the data means)
# - Dictionaries Power Models
#   - Understanding your data allows you to build better models
#   - It drives BI applications for your “clients.”
#   - It helps motivate and simplify modeling
#   - It is an iterative & ongoing process
# 
# Here is an example of how a dictionary looks like.
# 
# 
# | Division   | Term         | Type | Description                                              | Example                      |
# |------------|--------------|------|----------------------------------------------------------|------------------------------|
# | hr         | firstname    | text | An individual’s first name                               | “Arjun”, “Amaira”, “Socorro” |
# | hr         | lastname     | text | An individual’s last name                                | “Tarana”, “Bolio”, “”        |
# | realestate | projectname  | text | Name for an individual Real Estate Project               | “Capital Square Acquisition” |
# | realestate | projectstart | date | Start date for a project within the Real Estate division | “2021-12-02”                 |
# 
# 
# ### Interrogate errors & issues
# - Start with the Data Dictionary
# 
# As we discussed earlier, you can get a lot of information from a data dictionary, so it's best to check it out and understand the data to identify if errors exist with the data. 
# 
# For example; Most of us got last-name/surname, and we often think everyone got one. With this assumption, if we came across a row for an individual without a surname, we might consider it an error. But some countries don't indeed have the culture of adding surnames to their names. Check out [this](https://theculturetrip.com/europe/iceland/articles/how-did-iceland-become-a-nation-with-no-surnames/) why Icelandic people have no surnames. If you want to know more on how they name, check out [this](https://wsimag.com/culture/2248-the-peculiarities-of-icelandic-naming) article :)
# 
# - What biases exist?
#   - Uneven/unaligned sampling (census tracts vs. electoral boundaries)
#   - Artifacts of data collection (survey questions, temporal sampling)
#   - Incomplete or misaligned data models
# - How might these biases affect our analysis?
#   - Spurious correlations
# 
# ### Turn assumptions into assertions & tests
# Use the right tools!
# 
# - Relational DBMSs are optimized 
#   - for data access & transformation
#   - Strategies of normalization improve data validity & reduce data size
#   - Indexing speeds up data access
#   - Constraints improve data validity
#     - Domain Constraint (field values cannot be null, entity must possess attribute)
#     - Entity Integrity Constraint (values must be of a value type)
#     - Referential Integrity Constraint (foreign key must relate to value in another table)
#     - Key Constraint (primary key must be unique and not null)
# - Python & R are optimized
#   - For data transformation & analysis
#   - For reproducibility
#   - For visualization (to some degree)
# 
# You can add assertions when writing your program.
# These assertions will break execution at critical points if some of your workflows don’t meet your prior expectations.  
# Good use cases:  filtering, map functions, complex functions, places where input data may change frequently but must meet some prior expectation.
# 
# In Python: [pytest](https://docs.pytest.org/en/stable/assert.html).
# 
# In R: [assertthat](https://github.com/hadley/assertthat).

# ```
# import pytest
# data = [1,2,3]
# data_out = sum(data)
# assert data_out == 6, "Sum isn’t working."
# ```

# Finally, let's talk about the dangers of too much data!!!! Checkout [this](https://www.forbes.com/sites/kimberlywhitler/2018/03/17/why-too-much-data-is-a-problem-and-how-to-prevent-it/?sh=2854371a755f) article.
