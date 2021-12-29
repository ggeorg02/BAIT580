# RDS creation

Here we will go through the steps to create your first database in RDS. 

- Go to your AWS management console ( refer to AWS installation instructions ).

```{attention}
Make sure your region is in AWS US West (Oregon) region.
```

```{figure} img/rds1.png
---
width: 900px
align: center
---
```
- Select the RDS from the Services list `SERVICES` --> `DATABASE` --> `RDS`

```{figure} img/rds2.png
---
width: 900px
align: center
---
```

- Click on `DATABASES`

```{figure} img/rds3.png
---
width: 900px
align: center
---
```

As you see here, you don't have any database running. Are you ready to create one? Stay with me...

- Click on `CREATE DATABASE.`

```{figure} img/rds4.png
---
width: 900px
align: center
---
```

This will take you to the console, where you can see various options for creating your database, starting with the type of database you want to create. 

Let's go through each option one by one in the following screenshots.

- Here, we are selecting the database engine that we want. As you see, there are 6 of them available, and we will be going with Postgres. You will be hearing more about it in your Lecture 2. Here we also select which version of Postgres we want.

```{figure} img/rds5.png
---
width: 900px
align: center
---
```

```{figure} img/rds6.png
---
width: 900px
align: center
---
```

```{figure} img/rds7.png
---
width: 900px
align: center
---
```

```{figure} img/rds9.png
---
width: 900px
align: center
---
```

```{figure} img/rds10.png
---
width: 900px
align: center
---
```

```{figure} img/rds11.png
---
width: 900px
align: center
---
```

```{figure} img/rds12.png
---
width: 900px
align: center
---
```
- Under additional configuration. Leave everything as default. Add the database name that you will be using to load the data.

```{figure} img/rds13.png
---
width: 900px
align: center
---
```

```{figure} img/rds14.png
---
width: 900px
align: center
---
```

```{figure} img/rds15.png
---
width: 900px
align: center
---
```

```{figure} img/rds16.png
---
width: 900px
align: center
---
```

- Click on CREATE DATABASE. Sit back and relax AWS is setting up your database in the cloud.


```{figure} img/sitback.png
---
width: 250px
align: center
---
```

```{attention}
This process might take some time. For me, it took around 10 min. Better you grab some coffee.
```

After your coffee, you will see your database available.

```{figure} img/rds17.png
---
width: 900px
align: center
---
```

Once the database is up and running, we need the server details and credentials to access this database.

Click on the DB identifier (I marked red in the previous image).
This contains details for connecting to the database that you created now.

Capture the endpoint and port; we need to connect to this database.


We also need to make some changes to the security group; here, it controls the range of IPs this database can accept connections. Read more about the security group here.

Click on the VPC security groups under the Security. (Check the previous screenshot). This will take you to the Security group settings ( the screenshot that you see below); after this, follow the instructions given below.

- Click on edit inbound rules
 
```{figure} img/rds18.png
---
width: 900px
align: center
---
```

Before we change this, let me tell you why we want to do this.
By default, this database only takes connections from your IP (the laptop you are using now). However, your laptop IP is dynamic and can change based on the Wi-Fi that you are using. Since this is not a production database and nothing sensitive is in there, so it's okay to accept connections from anywhere; do as shown in the following 2 screenshots (not advised to do something like this when you start working in the industry, most of the cases these security group related things would be managed by a different team, so you have to less worry about it as data scientists/ analysts).


```{figure} img/rds19.png
---
width: 900px
align: center
---
```

```{figure} img/rds20.png
---
width: 900px
align: center
---
```

Save rules…This completes the task that you need to achieve from the AWS side. Remember you got the hostname and port. Next, we will be setting up the Postgres client in your local computer to access this database. 

[Here](https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/) is another set of instructions available online to create and connect to the RDS instance. It's good to check out these if you want to know more about various options. We will be touching upon some of the options in our Lecture 2.

Congratulations, you spun up your database in the cloud !!

```{figure} img/cloudb2.png
---
width: 250px
align: center
---
```