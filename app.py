# -*- coding:utf-8 -*-
from flask import Flask
from book import search

app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':
    app.run()
