# -*- coding: utf-8 -*-
import urllib2

__author__ = 'zx'
__date__ = '6/1/17 12:14'


class HtmlDownloader(object):
    def download(self, url):
        if url is not None:
            try:
                response = urllib2.urlopen(url, timeout=10)
                if response.getcode() == 200:
                    return response.read()
                else:
                    return None
            except Exception as e:
                print(str(e))
        else:
            return None
