# pgAdmin

pgadmin is a client that Postgres provides to administer, manage, and query the database ( in our case, the database we created in RDS). There are other softwares that you can use, like the [toad](https://www.quest.com/landing/toad-for-sql-administration/?gclid=Cj0KCQiAy4eNBhCaARIsAFDVtI2MaI13ZasUviGbi0Yiei2wnI-5hDhnFYC1idlqsfKk4UIMGt9vMcgaAgicEALw_wcB&gclsrc=aw.ds).


Install pgAdmin from [here](https://www.pgadmin.org/download/). You can download and use pgAdmin without having a local instance of PostgreSQL on your client computer (that's your laptop).

```{figure} img/pg1.png
---
width: 900px
align: center
---
```

```{figure} img/pg2.png
---
width: 900px
align: center
---
```

Enter `endpoint` and `port`

```{hint}
Here, the endpoint and port from AWS RDS is mentioned in the RDS creation instruction.
```

```{figure} img/pg3.png
---
width: 900px
align: center
---
```

Here enter the `hostname` and `password` of your RDS instance. 


```{figure} img/pg4.png
---
width: 900px
align: center
---
```


```{figure} img/pg5.png
---
width: 900px
align: center
---
```

```{attention}
You will see one active connection to your database from your AWS console if you want to confirm.
```

```{figure} img/pg6.png
---
width: 900px
align: center
---
```

- How to use it?

Here is the query tool that you can use to query your database.

```{figure} img/pg7.png
---
width: 900px
align: center
---
```

Now you successfully connected the database in the cloud to your pgadmin client. So whatever query you run here will be running in the cloud.

```{figure} img/connectionb3.png
---
width: 250px
align: center
---
```