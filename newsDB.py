#!/usr/bin/env python3
import psycopg2


def rankArts():
    """1 -- Returns the three articles with the most views"""
    try:
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()
        cur.execute("select title, count from rankArticles limit 3;")
        results = cur.fetchall()
        cur.close()
        print("\nThe ranking for the most popular Articles is as follows")
        for i, result in enumerate(results, 1):
            print('The {} place is "{}" with {} views'.format(i, result[0], result[1]))
    except BaseException as e:
        print("Unable to connect to the database")
        print(e)


def rankAuthors():
    """2 -- Returns a ranking with the most popular authors"""
    try:
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()
        cur.execute('''select name, sum(count) as sum from rankArticles,
            authors where rankArticles.author=authors.id
            group by name order by sum desc;''')
        results = cur.fetchall()
        cur.close()
        print("\nThe ranking for the most popular authors is as follows")
        for i, result in enumerate(results, 1):
            print("The {}  place is '{}' with {} views".format(i, result[0], result[1]))
    except BaseException:
        print("Unable to connect to the database")


def badDays():
    """3 -- Returns the days with more than 1% of failed connections"""
    try:
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()
        cur.execute('''select date(time) as day,(round(cast(count(*) filter
        (where status similar to '%404%')
        as decimal)*100/ count(*), 5)) as col1
        from log
        group by day 
        having ((round(cast(count(*) filter (where status
        similar to '%404%') as decimal)*100 / count(*), 5))) > 1 
        order by col1;''')
        res = cur.fetchall()
        print("\nThis are the days in which the error rate was higher than 1%")
        cur.close()
        for i in res:
            if __name__ == '__main__':
                print(str(i[0]) + " with " + str(i[1]) +
                      "% of erroneous transactions")
    except BaseException:
        print("Unable to connect to the database")  

rankArts()
rankAuthors()
badDays()