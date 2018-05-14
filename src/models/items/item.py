import requests
from src.common.database import Database
from bs4 import BeautifulSoup
import re
import src.models.items.constants as ItemConstants


class Item(object):
    def __init__(self, name, url, store):
        self.name = name
        self.url = url
        self.store = store
        tag_name = store.tag_name
        query_path = store.query_path
        self.price = self.load_price(tag_name, query_path)

    def __repr__(self):
        return "<Item {} at the URL: {}>".format(self.name, self.url)

    def load_price(self, tag_name, query_path):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query_path)
        string_price = element.text.replace(" ", "")

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)

        return match.group()

    def save_to_mongo(self):
        # insert JSON representation
        Database.insert(ItemConstants.COLLECTION, self.json())

    def json(self):
        return{
            "name": self.name,
            "url": self.url
        }
