import scrapy
import csv
import pymysql
from lxml import etree

current_rank = 1


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250?start={}&filter=".format(i) for i in range(0, 250, 25)]


    def parse(self, response):
        with open('movie.csv', 'a', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            conn = pymysql.connect(host='localhost',
                                   user='Arcueid',
                                   password='123456',
                                   database='doubanMovies'
                                   )
            cursor = conn.cursor()

            # writer.writerow(('name', ))
            movies = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
            # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
            # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()[1]
            # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()[2]
            # //*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/div/span[2]
            # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]
            # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span
            for movie in movies:
                movie_name = movie.xpath('./div/div[2]/div[1]/a/span[1]/text()').get()
                try:
                    movie_actor = movie.xpath('./div/div[2]/div[2]/p[1]/text()[1]').get()\
                        .replace(' ', '').split('主演:')[1]
                except:
                    movie_actor = '无信息'
                movie_info = movie.xpath('./div/div[2]/div[2]/p[1]/text()[2]').get().replace(' ', '').replace('\n', '')
                movie_info_list = movie_info.split('/')
                try:
                    movie_information = ' '.join(movie_info_list[1:])
                except:
                    movie_information = '无信息'
                try:
                    movie_date = movie_info_list[0]
                except:
                    movie_date = '无信息'
                movie_star = movie.xpath('./div/div[2]/div[2]/div/span[2]/text()').get()
                movie_evaluate = movie.xpath('./div/div[2]/div[2]/div/span[4]/text()').get()
                movie_introduction = movie.xpath('./div/div[2]/div[2]/p[2]/span/text()').get()
                if movie_introduction is None:
                    movie_introduction = '无介绍'

                movie_rank = int(cursor.execute('select * from tblMovies')) + 1
                insert_sql = """
                INSERT INTO tblMovies (name, actor, information, date, star, evaluate, introduction) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                cursor.execute(insert_sql, (movie_name, movie_actor, movie_information, movie_date,
                                            movie_star, movie_evaluate, movie_introduction))
                conn.commit()
                writer.writerow((movie_name, movie_actor, movie_information, movie_date,
                                 movie_star, movie_evaluate, movie_introduction))

            cursor.close()
            conn.close()


        pass
