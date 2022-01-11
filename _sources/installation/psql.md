# psql

psql is a command-line interface to interact with your Postgres database. We can use pgadmin for most of the interaction you wish with the Postgres, but sometimes you might want to use psql. E.g., Using the .dump provided for assignment1 and assignment 2, you need to import the schema to the Postgres database. 

You can do this from the pgadmin using a query tool like importing the .sql file. But since this file is big, sometimes your system might end up hanging; that's when psql comes to the rescue. 

Windows users please follow [these](https://www.postgresql.org/download/windows/) instructions.

Here are instructions for mac users,

```
brew doctor
brew update
brew install libpq
```

Once you are done with the `brew install libpq`, you probably will get something like what is given in the below code block.

```
libpq is keg-only, which means it was not symlinked into /opt/homebrew,
because conflicts with the Postgres formula.

If you need to have libpq first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/libpq/bin:$PATH"' >> ~/.zshrc

For compilers to find libpq you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/libpq/include"

```
So, first, run what it says for you and later run `brew link --force libpq`.

Check to make sure that the installation process went well,

```
(base) ggeorg02@MacBook-Pro dumps % psql --version         
psql (PostgreSQL) 14.1
```

Connect to your RDS instance using psql -h HOST_NAME -U USER_NAME DATABASE, eg:

```
psql -h mbandtweet.xxxx.us-west-2.rds.amazonaws.com -U Postgres Postgres
```
[Here](https://www.postgresqltutorial.com/psql-commands/) are some fundamental commands that you need. You can also keep this cheat sheet handy.