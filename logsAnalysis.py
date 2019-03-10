#!/usr/bin/env python3
"""
Udacity Logs Analysis Project

Author: Efren Aguilar

Python Version 3.7.2 used when created
"""

import psycopg2

DBNAME = "news"


def executeQuery(query):
    """Executes the given query using PostgreSQL

        Args:
            query: The query to execute
        Returns:
            The table returned by the query
    """
    try:
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
        c.execute(query)
        data = c.fetchall()
        db.close()
        return data
    except Exception as err:
        print("Error connecting to the database: " + str(err))


def getPopularArticles(topN=10):
    """Returns a table containing the most viewed articles in the database

        Args:
            topN: The number of articles to return (default: 10)
        Returns:
            A table containing the topN most viewed articles
    """
    return executeQuery("""SELECT title, count(*) AS views FROM log, articles
    WHERE path LIKE '/article/%'
    AND slug = RIGHT(path, -LENGTH('/article/'))
    GROUP BY title
    ORDER BY views DESC
    FETCH first {} rows only""".format(topN))


def printPopularArticlesReport(topN=10):
    """Prints out a report of the most viewed articles in the database

        Args:
            topN: The number of articles to return (default: 10)
        Returns:
            None: Prints a report of the topN most viewed articles
    """
    popArticles = getPopularArticles(topN)
    if popArticles is None:
        return
    print("Top {} articles in the database".format(topN))
    print("================================")
    for article in popArticles:
        print("\"{}\" - {} views".format(article[0], article[1]))


def getPopularAuthors():
    """Returns a table containing the authors in the database
    along with how many views their articles have
    """
    return executeQuery("""SELECT name, count(*) AS num
    FROM log, articles, authors
    WHERE path LIKE '/article/%'
    AND slug = RIGHT(path, -LENGTH('/article/')) AND authors.id = author
    GROUP BY authors.name
    ORDER BY num DESC;
    """)


def printPopularAuthorsReport():
    """Prints a report of how many article views
     each author has in the database
    """
    popAuthors = getPopularAuthors()
    if popAuthors is None:
        return
    print("Article views by author")
    print("================================")
    for article in popAuthors:
        print("{} - {} views".format(article[0], article[1]))


def getOnePercentErrorDays():
    """Returns a table containing all the days the site had over
    1% of HTTP requests lead to errors
    """
    return executeQuery("""SELECT ((count(*) * 100.0)/table2.totalVisits)
    AS "Error Percentage",
    TO_CHAR(time, 'FMMonth DD, YYYY') AS date
    FROM log JOIN (SELECT count(*) AS totalVisits,
    time::timestamp::date AS date2
    FROM log GROUP BY date2 ORDER BY totalVisits DESC) AS table2
    ON log.time::timestamp::date = table2.date2
    WHERE status LIKE '5%' OR status LIKE '4%'
    GROUP BY date, table2.totalVisits
    HAVING count(*) > (table2.totalVisits/100);
    """)


def printOnePercentErrorReport():
    """Prints a report of what days had greater than
    1% of HTTP requests lead to errors
    """
    errorDays = getOnePercentErrorDays()
    if errorDays is None:
        return
    print("Days with over 1% HTTP request errors")
    print("================================")
    for article in errorDays:
        print("{} - {:.2f}% errors".format(
            article[1], article[0]))


if __name__ == "__main__":
    print("Analyzing database...")
    print("\n")
    printPopularArticlesReport(3)
    print("\n")
    printPopularAuthorsReport()
    print("\n")
    printOnePercentErrorReport()
