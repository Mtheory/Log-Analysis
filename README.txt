Log report is an internal reporting tool that generate following reports from newspaper database. 

- Three most popular articles of all time.
- The most popular article authors of all time.
- Day(s) where connection request errors exceed 1% of all connections.

Information is displayed directly to the terminal.

To start you need :

PostgreSQL 			https://www.postgresql.org/download/
Python 2			https://www.python.org/download/releases/2.7/
The psycopg 2 library  		from command line run:   pip install psycopg2 
newsdata.sql file: 		https://d17h27t6h515a5.cloudfront.net/
topher/2016/August/57b5f748_newsdata/newsdata.zip
Linux machine or VM 
For VM use :
VirtualBox			https://www.virtualbox.org/wiki/Downloads
Vagrant				https://www.vagrantup.com/downloads.html
VM configuration files with vagrant directory:
https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip

Installation
If using (VM), go to vagrant directory inside VM configuration directory FSND-virtual-machine. 
Run the command 'vagrant up’ to install linux then run command 'vagrant ssh' to log in. 
The file newsdata.sql should be inside vagrant directory, command 'psql -d news -f newsdata.sql'  would  load the data into database.

Running
Run the program using one of the commands : 
python log_report.py 
./log_report.py



