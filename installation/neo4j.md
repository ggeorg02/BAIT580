# Neo4j

In this document, we will set up a neo4j aura instance in the cloud.

Click on [this](https://neo4j.com/cloud/aura/?ref=get-started-dropdown-cta) and press on `Start Free`; this will take you to the registration page.

```{figure} img/register.png
---
width: 900px
align: center
---
```

Enter an email and password that you want to use for the registration.


Followed by this will take you to this page, 

```{figure} img/verifyemail.png
---
width: 900px
align: center
---
```

You need to verify your email and `Go to the Dashboard`. Then, agree to the `terms and conditions,` and after that, it will take you to this page to create your first database.

```{figure} img/databasesetup.png
---
width: 900px
align: center
---
```

We will be going with `AuraDB Free`. You need to keep an eye on the limitations of this database, copying and pasting it here for better visibility.

```{important}
- 1 forever free database
- Limits on graph size (50k nodes, 175k relationships)
- Standard procedure library (apoc-core)
- Auto-pause after 3 days of inactivity
```

- Give any name to the database (Here I gave as bait) 
- Select the US region. - 

```{note}
I hope you understand why we gave US region? This is the region closer to Canada, and your database will be spun in the region Iowa (USA). If you are going to use your database from any other Asian country, it makes sense to set up your database in the Singapore region.
```

- Check `Load or create your own data in a blank database`. 

You will get credentials for your database; make sure you save it safely. We need this for making a connection to this database.

```{figure} img/credentials.png
---
width: 900px
align: center
---
```

It might take some time, but you will see it `Running` once your database is ready. 

```{figure} img/aftersetup.png
---
width: 900px
align: center
---
```

Make a note of the connection URL; you will need this to connect to your database.

To summarize, now you created a neo4j graph database in the cloud. 


```{important}
You need the following information for connecting to the graph database (in our case, for connecting from our jupyter notebook).
- connection URL
- username = default is neo4j
- password
```

You can now `Open with` neo4j browser. 

```{figure} img/aftersetup.png
---
width: 900px
align: center
---
```

This will take you to a page where you want to enter your connection details. Most of them will be automatically populated, and you want to enter your password.

```{figure} img/thenyouconnect.png
---
width: 900px
align: center
---
```

This is your workspace for creating and exploring your graph database. Now it got nothing in there as we haven't exported any data.

```{figure} img/nowconnected.png
---
width: 900px
align: center
---
```