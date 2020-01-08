# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-1-8 下午2:56
from flask import current_app, request
from flask_restful import Resource, marshal, reqparse

from app.article.serializer import ArticleListSerializer
from app.utils import pagination

from app.models import Post


class ArticleList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("page", type=int, default=1, help="页数")
        self.parser.add_argument("offset", type=int, default=10, help="每页数量")
        self.parser.add_argument("title", type=str, default="", help="标题")

    def get(self):
        args = self.parser.parse_args()
        start_idx, end_idx = pagination(args["page"], args["offset"])
        if args["title"]:
            post_list = Post.query.filter(
                Post.title.like('%' + args["title"] + '%')).all()
        else:
            post_list = Post.query.all()
        data = [marshal(item, ArticleListSerializer) for item in post_list][
               start_idx:end_idx]
        return {"data": data, "total": len(post_list)}, 200
