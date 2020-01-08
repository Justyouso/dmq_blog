# -*- coding: utf-8 -*-
# author: boe

from flask import Blueprint
from flask_restful import Api

from .views import (ArticleList)


article = Blueprint("article", __name__)
_api = Api(article)

# register urls
_api.add_resource(ArticleList, "/v1/articles")
