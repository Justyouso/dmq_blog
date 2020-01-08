# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-1-8 下午2:59


def pagination(page=1, offset=10):
    """
    处理分页
    :param page: 页码
    :param offset: 每页数量
    :return: tupl
    """
    start_index = (page - 1) * offset
    end_index = page * offset

    return start_index, end_index
