# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-12 下午2:15

from flask_restful import fields

ArticleListSerializer = {
    "id": fields.Integer(),
    "title": fields.String(default=""),
    "summary": fields.String(default="")
}
