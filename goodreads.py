from bs4 import BeautifulSoup
import requests

class GoodReads():
    SEARCH_URL = "https://www.goodreads.com/search"
    ITEM_URL = "https://www.goodreads.com"

    def scan_result_list(self, book_title):
        data = requests.get(self.SEARCH_URL, params={"utf8": "✓", "q": book_title, "search_type": "books"})
        results = []

        if data.status_code == 200:
            soup = BeautifulSoup(data.content, "html5lib")

            rows = self.select_table_data(soup)

            if rows is not None:
                for row in rows:
                    title = row.find("span", itemprop="name")

                    heading = row.find("span", itemprop="author")
                    author = heading.find("span", itemprop="name")

                    if title and author:
                        title_str = title.text
                        author_str = author.text

                        results.append(ListItem(title_str, author_str))
        
        return results
    
    # TODO: find cover image url
    def scan_result_item(self, book_title):
        item_id = self.find_item_id(book_title)

        if self.is_valid_id(item_id):
            data = requests.get(self.ITEM_URL + item_id)

            if data.status_code == 200:
                soup  = BeautifulSoup(data.content, "html5lib")

                title = soup.find("h1", attrs={"class": "Text Text__title1"}).text
                author = soup.find("span", attrs={"class": "ContributorLink__name"}).text
                description = soup.find("span", attrs={"class": "Formatted"}).text
                
                image_url = self.find_cover_image(soup)

                return ItemDetails(title, author, description, image_url)
    
    def find_item_id(self, book_title):
        data = requests.get(self.SEARCH_URL, params={"utf8": "✓", "q": book_title, "search_type": "books"})

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
            
    def is_valid_id(self, item_id):
        return len(item_id) > 0
    
    
    def find_cover_image(self, soup):
        image_div = soup.find("div", attrs={"class": "BookCover__image"})

        return image_div.find("img")["src"]
    
class ListItem():
    def __init__(self, title, author):
        self.title = title
        self.author = author

class ItemDetails():
    def __init__(self, title, author, description, image_url):
        self.title = title
        self.author = author
        self.description = description
        self.image_url = image_url