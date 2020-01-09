# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-12 下午2:15

from flask_restful import fields
from app.article.formatters import CommentsFormatter

ArticleListSerializer = {
    "id": fields.Integer(),
    "title": fields.String(default=""),
    "summary": fields.String(default=""),
    "author": fields.String(default=""),
    "author_id": fields.Integer(),
    "comments": CommentsFormatter,
    "reader_count": fields.Integer(),
    "timestamp": fields.String()
}
