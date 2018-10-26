# Logs Analysis project

This is the logs analysis project file created for the first module of the fullstack developer nanodegree at Udacity

### Prerequisites

In order to run this file, you will need to have access to the SQL "views" database provided by Udacity

### Getting the program running

The only step needed to run the program is to create the view "rankArticles" which you can do with the following command:

```
create view rankArticles as select title, count(*) as count from articles, log where substring(log.path,10,13)=substring(articles.slug,0,14) group by title order by count desc;

```

## Running script

Once you are all set you just have to run the Python file "newsDB.py" directly from the command line

```
python newsDB.py
```

### Project structure

The project consists in three main functions

## Rank Articles

This function uses the logs to determine which articles have been read and how many times. Once it has that information, it orders it by number of times it has been read and shows only the top 3 articles

## Rank Authors

This function uses the results obtained in Rank articles and compares it to the Authors table to determine which author wrote each of the Articles. With this information, the function determines how many times an author has been read and ranks them accordingly

## Bad days

This function Checks the log to obtain the ratio of failed connections to succesfull connections per day. It the uses that information to classify the individual days, showing only the days with a failure rate above 1%.

### Built With

* [psycopg2](http://initd.org/psycopg/docs/) - PostgreSQL database adapter for Python

### Authors

* **Diego Villafuerte Soraiz** - (https://github.com/diegovillafuerte) - (diego.villafuerte.soraiz@gmail.com)
