#!/usr/bin/env python3
import psycopg2


def dbConnection(dbname, query):
    try:
        db = psycopg2.connect("dbname="+dbname)
        cur = db.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
    except BaseException as e:
        print("Unable to connect to the database")
        print(e)
    return results


def rankArts():
    """1 -- Returns the three articles with the most views"""
    try:
        results = dbConnection("news",
                               '''select title, count
                               from rankArticles limit 3;''')
        print("\nThe ranking for the most popular Articles is as follows")
        for i, (title, views) in enumerate(results, 1):
            print('The {} place is "{}" with {} views'.format(i, title, views))
    except BaseException as e:
        print(e)


def rankAuthors():
    """2 -- Returns a ranking with the most popular authors"""
    try:
        results = dbConnection("news",
                               '''select name, sum(count) as sum from rankArticles,
                               authors where rankArticles.author=authors.id
                               group by name order by sum desc;''')
        print("\nThe ranking for the most popular authors is as follows")
        for i, (title, views) in enumerate(results, 1):
            print("The {}  place is '{}' with {} views"
                  .format(i, title, views))
    except BaseException as e:
        print(e)


def badDays():
    """3 -- Returns the days with more than 1% of failed connections"""
    try:
        results = dbConnection(
                               "news",
                               '''select date(time) as day,(round(cast(count(*) filter
                               (where status similar to '%404%')
                               as decimal)*100/ count(*), 5)) as col1
                               from log
                               group by day
                               having ((round(cast(count(*)
                               filter (where status
                               similar to '%404%') as decimal)
                               *100 / count(*), 5))) > 1
                               order by col1;''')
        print("\nThis are the days in which the error rate was higher than 1%")
        for i in results:
            if __name__ == '__main__':
                print(str(i[0]) + " with " + str(i[1]) +
                      "% of erroneous transactions")
    except BaseException as e:
        print(e)


rankArts()
rankAuthors()
badDays()
