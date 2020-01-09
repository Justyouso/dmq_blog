# -*- coding: utf-8 -*-
# author: boe

from flask_restful import fields


class DateFormatter(fields.Raw):
    def format(self, value):
        return value.replace("T", " ")


class CommentsFormatter(fields.Raw):
    def format(self, value):
        return value.count()
