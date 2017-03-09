# coding: utf8
# Bot class
# @author: Nicolas Drufin <nicolas.drufin@ensc.fr>

import re
import random
from requests import session


class Bot(object):

    PATTERN = re.compile("<a.*?href=[\"'](?P<href>.+?)['\"].*?>(?P<name>.+?)</a>")

    def __init__(self, search_url="https://www.google.fr/search?q=%s"):
        """
        Constructor
        """
        self._session = session()
        self._search_url = search_url
        self.last_url = None

    def pick_link_from(self, text, is_url):
        """
        Pick a link in a page or string element
        :param element:
        :return:
        """
        url = text
        if not is_url:
            url = self._search_url % text

        try:
            result = self._session.get(url)
            list_links = self.parse_links(result.content)
            if not list_links:
                raise Exception("No links available on page %s" % result.url)
        except Exception as e:
            print "Oops you hit a wall!"
            print repr(e)
            return

        # search a site
        self.last_url = result.url
        return random.choice(list_links)

    def parse_links(self, page):
        """
        Parse links from page
        :param page:
        :return:
        """
        linklist = []
        for m in self.PATTERN.finditer(page):
            url = m.group(1)
            linklist.append(url)
        # delete doublons in list
        return list(set(linklist))

    @staticmethod
    def is_url(url):
        return url.startswith('http://') or url.startswith('https://')
