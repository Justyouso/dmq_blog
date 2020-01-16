# -*- coding: utf-8 -*-
# author: boe

from flask import Blueprint
from flask_restful import Api

from .views import (RecommendAuthor)


user = Blueprint("user", __name__)
_api = Api(user)

# register urls
_api.add_resource(RecommendAuthor, "/v1/recomd/author")
