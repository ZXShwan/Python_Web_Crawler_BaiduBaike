# -*- coding: utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup

__author__ = 'zx'
__date__ = '6/1/17 12:15'


class HtmlParser(object):
    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item'))
        # links = soup.find_all('a', href=re.compile(r'/item/(.*)'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1> </dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        if title_node.get_text() is not None:
            res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node.get_text() is not None:
            res_data['summary'] = summary_node.get_text()

        return res_data
