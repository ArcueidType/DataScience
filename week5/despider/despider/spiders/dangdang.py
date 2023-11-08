import pymysql
import scrapy


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["search.dangdang.com", "product.dangdang.com"]
    start_urls = ["https://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input"]

    def parse(self, response):
        with pymysql.connect(host='localhost', user='Arcueid', password='123456', database='dangBooks') as conn:
            # /html/body/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/ul
            # /html/body/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]
            cursor = conn.cursor()
            books = response.xpath('//*[@id="component_59"]/li')
            # /html/body/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/p[1]/a
            # //*[@id="p29522644"]/p[5]/span[1]/a
            # //*[@id="p29522644"]/p[5]/span[2]
            # //*[@id="p29522644"]/p[5]/span[3]/a
            # //*[@id="p29328835"]/p[3]/span[1]
            # //*[@id="p29328835"]/p[4]/a
            # //*[@id="p29328835"]/p[2]/text()
            insert_sql = """
            INSERT INTO tblBooks (name, author, date, press, price, evaluate, introduction, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            for book in books:
                book_name = book.xpath('./p[1]/a/@title').get()
                book_author = book.xpath('./p[5]/span[1]/a/@title').get()
                if book_author is None:
                    book_author = '未知'
                try:
                    book_date = book.xpath('./p[5]/span[2]/text()').get().replace('/', '')
                except:
                    book_date = None
                book_press = book.xpath('./p[5]/span[3]/a/text()').get()
                if book_press is None:
                    book_press = '未知'
                book_price = book.xpath('./p[3]/span[1]/text()').get()
                if book_price is None:
                    book_price = '暂无报价'
                book_evaluate = book.xpath('./p[4]/a/text()').get()
                if book_evaluate is None:
                    book_evaluate = '无'
                book_introduction = book.xpath('./p[2]/text()').get()
                if book_introduction is None:
                    book_introduction = '无'
                book_url = book.xpath('./p[1]/a/@href').get()
                cursor.execute(insert_sql, (book_name, book_author, book_date, book_press, book_price,
                                            book_evaluate, book_introduction, book_url))
            # //*[@id="12810"]/div[5]/div[2]/div/ul/li[10]/a
            conn.commit()
            cursor.close()
            try:
                next_page = 'https://search.dangdang.com' + response.xpath(
                    '//*[@id="12810"]/div[5]/div[2]/div/ul/li[10]'
                    '/a/@href').get()
                yield scrapy.Request(next_page, callback=self.parse)
            except:
                pass
        pass
