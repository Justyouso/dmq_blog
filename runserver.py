# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-1-8 下午3:18

from app import create_app
from config import config

app = create_app(config["development"])

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
