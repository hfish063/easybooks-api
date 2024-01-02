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

class Quote():
    def __init__(self, quote):
        self.quote = quote