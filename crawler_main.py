# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_parser, html_outputer

__author__ = 'zx'
__date__ = '6/1/17 12:14'


class CrawlerMain(object):
    def __init__(self):
        # max count to crawl
        self.max_count = 1000
        # url manager
        self.urls = url_manager.UrlManager()
        # html downloader
        self.downloader = html_downloader.HtmlDownloader()
        # html parser
        self.parser = html_parser.HtmlParser()
        # html outputer
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        print 'Start'
        # record url
        count = 1
        # add new url to url set
        self.urls.add_new_url(root_url)
        # when url set has new url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawling %d: %s' % (count, new_url)
                # open downloader to download html page
                html_content = self.downloader.download(new_url)
                # analyse data from html page
                new_urls, new_data = self.parser.parse(new_url, html_content)
                # process data
                self.urls.add_new_urls(new_urls)
                # collect data
                self.outputer.collect_data(new_data)

                if count == self.max_count:
                    break
                count = count + 1
            except Exception as e:
                print 'craw failed'

        # output the result as a html page
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_crawler = CrawlerMain()
    obj_crawler.craw(root_url)
    print 'Finish'
