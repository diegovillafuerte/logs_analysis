#!/usr/local/bin/python3
import psycopg2


def rankArts():
    """1 -- Returns the three articles with the most views"""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute("select title, count from rankArticles limit 3;")
    res = cur.fetchall()
    cur.close()
    j = 1
    print("\nThe ranking for the most popular Articles is as follows")
    for i in res:
        print("The " + str(j) + " place is " +
              i[0] + " with " + str(i[1]) + " views")
        j = j + 1


def rankAuthors():
    """2 -- Returns a ranking with the most popular authors"""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute("select name, sum(count) as sum from rankArticles,\
        authors where rankArticles.author=authors.id\
        group by name order by sum desc;")
    res = cur.fetchall()
    cur.close()
    print("\nThe ranking for the most popular authors is as follows")
    j = 1
    for i in res:
        print("The "+str(j) + " place is " +
              i[0] + " with " + str(i[1]) + " views")
        j = j+1


def badDays():
    """3 -- Returns the days with more than 1% of failed connections"""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute("select date(time) as day,\
        (trunc(cast(count(*) filter (where status similar to '%404%')\
        as decimal)/ count(*), 5))*100 as col1\
        from log\
        group by day\
        having ((trunc(cast(count(*) filter (where status similar to '%404%')\
        as decimal) / count(*), 5))*100) > 1\
        order by col1;")
    res = cur.fetchall()
    print("\nThis are the days in which the error rate was higher than 1%")
    cur.close()
    for i in res:
        print(str(i[0]) + " with " + str(i[1]) + " erroneous transactions")
rankArts()
rankAuthors()
badDays()
