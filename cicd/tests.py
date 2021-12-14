#!/usr/local/bin/python
import unittest
import requests
import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL_KEY = 'SITE_BASE_URL'
SERVER_HDR_KEY = 'SERVER_HEADER'
HDR_VALUE_KEY = 'EXPECTED_HEADER_VALUE'
CONTENT_TYPE = 'Content-Type'

base_url = os.environ.get(BASE_URL_KEY)
server_header = os.environ.get(SERVER_HDR_KEY)
header_value = os.environ.get(HDR_VALUE_KEY)

class TestSiteLinks(unittest.TestCase):

    def setUp(self):
        self.page_response = requests.get(base_url)

    def test_ok_response(self):
        self.assertEqual(self.page_response.status_code, 200)
    
    def test_server_header(self):
        self.assertIn(header_value, self.page_response.headers[server_header])

    def test_page_links(self):
        soup = BeautifulSoup(self.page_response.text, 'html.parser')
        links = [link['href'] for link in soup.find_all('a')]
        for link in links:
            if 'http' not in link:
                req_url = f'{base_url}{link}'
            if req_url == base_url+'/': # no need to test the base url twice
                continue
            with self.subTest(link=req_url):
                response = requests.get(req_url)
                self.assertEqual(response.status_code, 200)
    
    def test_content_type_header(self):
        self.assertIn('html', self.page_response.headers[CONTENT_TYPE])

if __name__ == '__main__':
   test_result = unittest.main()