import scrapy

class CoursesSpider(scrapy.Spider):

    name = 'courses'

    start_urls = ['https://www.shiyanlou.com/bootcamp/']

    def parse(self, response):
        for course in response.css('div.col-3'):
            yield {
                'name': course.css('p.course-name::text').extract_first().strip(),
                'description': course.css('p.course-desc::text').extract_first(
                        ).strip(),
                'image_url': course.css('img.course-cover::attr(src)').extract_first()
            }
