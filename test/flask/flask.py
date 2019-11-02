# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 23:48 
# @Author : DollarKillerx
# @Description :

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello,World!'


if __name__ == '__main__':
    app.run(":8081")
