from bs4 import BeautifulSoup
import requests

class GoodReads():
    URL = "https://www.goodreads.com/search"

    def scan_result_list(self, book_title):
        data = requests.get(self.URL, params={"utf8": "✓", "q": book_title, "search_type": "books"})
        results = []

        if data.status_code == 200:
            soup = BeautifulSoup(data.content, "html5lib")

            rows = self.select_table_data(soup)

            for row in rows:
                cols = row.find_all("td")
                
                for col in cols:
                    title = col.find("span", itemprop="name")
                    author = col.find("span", itemprop="author")

                    if title and author:
                        title_str = title.text
                        author_str = author.text

                        results.append(ListItem(title_str, author_str))
        
        return results
    
    def scan_result_item(self):
        return
    
    # TODO: method implmentation
    def find_item_id(self, book_title):
        data = requests.get(self.URL, params={"utf8": "✓", "q": book_title, "search_type": "books"})

        id = ""

        if data.status_code == 200:
            soup = BeautifulSoup(data.content, "html5lib")

            first_row = self.select_table_data(soup)[0]          

        return id
    
    def select_table_data(self, soup):
            table = soup.find("table", attrs={"class": "tableList"})

            return table.find_all("tr")
    
class ListItem():
    def __init__(self, title, author):
        self.title = title
        self.author = author

class ItemDetails():
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description