Log report is an internal reporting tool that generate following reports from newspaper database. 
- Three most popular articles of all time.
- The most popular article authors of all time.
- Day(s) where connection request errors exceed 1% of all connections.
Information is displayed directly to the terminal.


Installation

Download the zip file and extract to a directory of your choosing.
Files names :
-	log_report.py

The program was designed to run under Linux with PSQL database installed 

Running
Program requires database news, and Python 2.7 installed.

For correct operation five views are required to be created within news database
1.
CREATE VIEW articles_popularity AS 
SELECT articles.title, report.views 
FROM articles LEFT JOIN 
(SELECT path, COUNT(*) AS views FROM log GROUP BY path) AS report 
ON report.path LIKE CONCAT('%',articles.slug) 
ORDER BY report.views DESC;	
2.
CREATE VIEW articles_author AS 
SELECT articles.title,authors.name 
FROM articles JOIN authors ON articles.author = authors.id;
3.
CREATE VIEW all_connection AS 
(SELECT CAST(time AS date) AS day, COUNT(*) AS num 
FROM log GROUP BY day);
4.
CREATE VIEW error_connection AS 
(SELECT CAST(time AS date) AS day , COUNT(*) AS num 
FROM log WHERE status NOT LIKE '200 OK' GROUP BY day);
5.
CREATE VIEW errors_per_day As 
SELECT all_connection.day,
CAST(CAST(error_connection.num AS FLOAT)/CAST(all_connection.num AS FLOAT)*100 AS NUMERIC(18,2)) AS p 
FROM all_connection LEFT JOIN error_connection 
ON all_connection.day = error_connection.day;


