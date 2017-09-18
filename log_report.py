import psycopg2


DBNAME = "news"


print "\nReports:"


# display three most popular articles
def articles():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("select * from articles_popularity limit 3")
    rows = cursor.fetchall()
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
    cursor = db.cursor()
    cursor.execute("select name,sum(views)" +
                   " from articles_popularity,articles_author " +
                   "where articles_popularity.title = articles_author.title" +
                   " group by name order by sum(views) desc;")
    rows = cursor.fetchall()
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
    cursor = db.cursor()
    cursor.execute("select * from errors_per_day where p>1;")
    rows = cursor.fetchall()
    print "Days with more than 1% connection errors :"
    for row in rows:
        print "\t* ", row[0], "\t\t-", row[1], ' %'
    db.close()
    print '\n'

# functions execution
articles()
authors()
connection_errors()
