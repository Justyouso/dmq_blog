# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-1-15 下午3:46

from flask_restful import Resource, marshal, reqparse
from sqlalchemy import text

from app.article.serializer import ArticleListSerializer
from app.utils import pagination

from app.models import Article
from app import db


class RecommendAuthor(Resource):
    def get(self):
        sql = text(
            'select b.author_id,b.username,b.a_count,COUNT(f.follower_id)'
            ' as f_count from (select a.author_id,u.username,'
            'count(a.author_id) as a_count from articles as a ,users as u'
            ' WHERE a.author_id=u.id group by a.author_id) as b LEFT JOIN'
            ' follow as f on b.author_id=f.followed_id GROUP BY b.author_id')

        # 查询结果
        article_result = db.engine.execute(sql)
        result = []
        for item in article_result:
            if len(result) >= 5:
                break
            tmp = {"author_id": item[0], "author": item[1],
                   "article_count": item[2],
                   "followed_count": item[3]}
            result.append(tmp)

        return {"data": result}, 200
