#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'King'

from bs4 import BeautifulSoup
import re, urllib.parse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # 构建网页解析器
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        # new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']

            # 拼接完整的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)

            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        message_data = []

        title_node = soup.find_all('div', class_='showthread showthread--anchored flexBox noflex')

        for node in title_node:
            res_data = {'url': page_url}
            res_data['postlink'] = 'https://www.forexfactory.com/' + \
                node.find('a', class_='threadpost-header__linkicon threadpost-header__linkicon--postnum postnum')['href']
            res_data['name'] = node.find('span', class_ = 'usernamedisplay__username username').get_text()
            res_data['message'] = node.find('div', class_='threadpost-content__message').get_text()
            message_data.append(res_data)

        return message_data
