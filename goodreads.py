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

            if rows is not None:
                for row in rows:
                    title = row.find("span", itemprop="name")
                    author = row.find("span", itemprop="author")

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

            try:
                first_row = self.select_table_data(soup)[0]
            except:
                # important: return empty id String if there are not any search results
                return id

            if first_row is not None:
                heading = first_row.find("a", itemprop="url")
                id = heading.get("href")

        return id
    
    def select_table_data(self, soup):
            table = soup.find("table", attrs={"class": "tableList"})

            if table is not None:
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