# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    def start_requests(self):
        url_list = ['https://www.shiyanlou.com/courses/',
                    'https://www.shiyanlou.com/courses/?page=2',
                    'https://www.shiyanlou.com/courses/?page=3'
                ]        

        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)




    def parse(self, response):
        for course in response.css('div.col-sm-12.col-md-3'):
            yield {
                    'name':course.css('h6.course-name::text').extract_first().strip(),
                    'description':course.css('div.course-description::text').extract_first().strip(),
                    'type':course.css('span.course-type::text').extract_first().strip(),
                    'students':course.css('span.students-count span::text').extract_first()
                    }


