import csv
import pymysql

# with open('movie.csv', 'w', newline='', encoding='utf-8') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(('name', 'actor', 'information', 'date', 'star', 'evaluate', 'introduction'))
#
# conn = pymysql.connect(host='localhost',
#                        user='Arcueid',
#                        password='123456',
#                        database='doubanMovies'
#                        )
# cursor = conn.cursor()
#
# cursor.execute('DROP TABLE IF EXISTS tblMovies')
# sql_create_table = """
# CREATE TABLE IF NOT EXISTS tblMovies(
# movie_rank INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# name VARCHAR(255) NOT NULL DEFAULT '',
# actor VARCHAR(255) NOT NULL DEFAULT '',
# information VARCHAR(255) NOT NULL DEFAULT '',
# date VARCHAR(255) NOT NULL DEFAULT '',
# star VARCHAR(15) NOT NULL DEFAULT '0',
# evaluate VARCHAR(15) NOT NULL DEFAULT '0.0',
# introduction VARCHAR(255) NOT NULL DEFAULT ''
# );
# """
# cursor.execute(sql_create_table)
# conn.commit()
# cursor.close()
# conn.close()

# for dangdang.com
conn = pymysql.connect(host='localhost',
                       user='Arcueid',
                       password='123456',
                       database='dangBooks'
                       )
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS tblBooks')
sql_create_table = """
CREATE TABLE IF NOT EXISTS tblBooks(
book_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL DEFAULT '',
author VARCHAR(255) NOT NULL DEFAULT '',
date DATETIME,
press VARCHAR(255) NOT NULL DEFAULT '',
price VARCHAR(15) NOT NULL DEFAULT '0',
evaluate VARCHAR(31) NOT NULL DEFAULT '0.0',
introduction VARCHAR(1023) NOT NULL DEFAULT '',
url VARCHAR(255) NOT NULL DEFAULT ''
);
"""

cursor.execute(sql_create_table)
conn.commit()

cursor.close()
conn.close()
