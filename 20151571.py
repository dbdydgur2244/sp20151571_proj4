from bs4 import BeautifulSoup
import requests
import urllib.error
from lib_LocalFileAdapter import LocalFileAdapter
import os
class COLLECT_HREF:
    def __init__(self):
        self.pages = set()
        self.URLS = list()
        self.file_url = "file://" + os.getcwd()
        self.url = "/public_html/"
        self.full_url = self.file_url + self.url
        self.idx = 1
        self.requests_session = requests.session()
        self.requests_session.mount('file://',LocalFileAdapter())

    def crawling(self, url):
        if url in self.pages:
            pass
        try:
            r = self.requests_session.get(self.full_url + url)
            bsObj = BeautifulSoup(r.content, 'html.parser')
            self.URLS.append(url)
            with open("Output_" + "%04d"%(self.idx) + ".txt", "w") as fr:
                print(bsObj.getText(), file = fr, end = "")
                self.idx += 1
            for Obj in bsObj.findAll("a"):
                page = Obj["href"]
                if page.find("html") == -1 or page in self.pages :
                    continue
                self.pages.add(page)
                self.crawling(page)

        except:
            pass
            #print(Error)
    
    def Write_visited(self):
        idx = 1
        with open("URL.txt", "w") as f:
            for url in self.URLS:
                print("[%d]%s"%(idx, "." + self.url + url) , file = f)
                idx += 1

HREFS = COLLECT_HREF()
HREFS.pages.add("index.html")
HREFS.crawling("index.html")
HREFS.Write_visited()


