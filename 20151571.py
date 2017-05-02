from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error
import os
class COLLECT_HREF:

    def __init__(self):
        self.pages = set()
        self.URLS = list()
        self.file_url = "file://" + os.getcwd()
        self.url = "/public_html/"
        self.full_url = self.file_url + self.url
        self.idx = 1

    def crawling(self, url):
        if url in self.pages:
            pass
        try:
            html = urlopen(self.full_url + url)
            bsObj = BeautifulSoup(html, 'html.parser')
            self.URLS.append(url)
            with open("Output_" + "%04d"%(self.idx) + ".txt", "w") as fr:
                print(bsObj.getText(), file = fr)
                self.idx += 1
            for Obj in bsObj.findAll("a"):
                page = Obj["href"]
                if page.find("html") == -1 or page in self.pages :
                    continue
                self.pages.add(page)
                self.crawling(page)

        except urllib.error.URLError as Error:
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


