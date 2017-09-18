import psycopg2


DBNAME = "news"


print "\nReports:"


# display three most popular articles
def articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH articles_popularity AS " +
              "(SELECT articles.title, report.views FROM " +
              "articles LEFT JOIN " +
              "(SELECT path,COUNT(*) AS views FROM log GROUP BY path) " +
              "AS report ON report.path LIKE CONCAT('%',articles.slug) " +
              "ORDER BY report.views DESC) " +
              "SELECT * FROM articles_popularity LIMIT 3")
    rows = c.fetchall()
    # print results to the terminal with visual formating
    print 'Three most populart articles :'
    for row in rows:
        offset = 35 - len(row[0])
        str = row[0]
        str += " " * offset
        print "\t* ", str, "  -", row[1], ' views'
    db.close()
    print '\n'


# display most popular authors
def authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH articles_popularity AS " +
              "(SELECT articles.title, report.views FROM " +
              "articles LEFT JOIN " +
              "(SELECT path,COUNT(*) AS views FROM log GROUP BY path) " +
              "AS report ON report.path LIKE CONCAT('%',articles.slug) " +
              "ORDER BY report.views DESC), " +
              "articles_author AS " +
              "(SELECT articles.title,authors.name FROM " +
              "articles JOIN authors ON articles.author = authors.id) " +
              "SELECT name,SUM(views) FROM " +
              "articles_popularity,articles_author WHERE " +
              "articles_popularity.title = articles_author.title " +
              "GROUP BY name ORDER BY SUM(views) DESC")
    rows = c.fetchall()
    # print results to the terminal with visual formating
    print 'Most popular article authors :'
    for row in rows:
        offset = 35 - len(row[0])
        str = row[0]
        str += " " * offset
        print "\t* ", str, "  -", row[1], ' views'
    db.close()
    print '\n'


# display days with more than 1% error connection
def connection_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH all_connection AS " +
              "(SELECT CAST(time AS date) AS day, COUNT(*) AS num " +
              "FROM log GROUP BY day), " +
              "error_connection AS " +
              "(SELECT CAST(time AS date) AS day , COUNT(*) AS num " +
              "FROM log WHERE status NOT LIKE '200 OK' GROUP BY day), " +
              "errors_per_day AS"
              "(SELECT all_connection.day, " +
              "CAST(CAST(error_connection.num AS FLOAT)/" +
              "CAST(all_connection.num AS FLOAT)*100 AS NUMERIC(18,2)) " +
              "AS percentage FROM " +
              "all_connection LEFT JOIN error_connection " +
              "ON all_connection.day = error_connection.day) " +
              "SELECT * FROM errors_per_day WHERE percentage > 1")
    rows = c.fetchall()
    # print results to the terminal
    print "Days with more than 1% connection errors :"
    for row in rows:
        print "\t* ", row[0], "\t\t-", row[1], ' %'
    db.close()
    print '\n'


# functions execution
articles()
authors()
connection_errors()
