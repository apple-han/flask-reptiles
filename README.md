# flask-reptiles
相信这个项目，对于学习用flask开发web你来说，帮助是巨大的。
抓紧试试这个分词+web的组合吧！
### 必须要做的
- git clone https://github.com/apple-han/flask-reptiles.git
- cd flask-reptiles
- 在 config/config.py 中手动更改 `mysql` 的密码(`SQLALCHEMY_DATABASE_URI`), 并创建数据库 `CREATE DATABASE products CHARSET=UTF8` 
- uwsgi.ini 改成你自己的文件路径，注意module也要改！
### Docker的方式部署
- docker build . -t reptiles-srv:latest
- docker-compose up -d
- http://127.0.0.1:5000/v1/goods/search?q=衣服还不错 (需要先获取token)
### 本地安装（python version > 3.6）运行时注意你使用的版本
- pip install -r requirements.txt 
- python apple.py
- python proxy.py
- python bantang.py
- python participle.py
- http://127.0.0.1:5000/v1/goods/search?q=衣服还不错 (需要先获取token)
  
### 小贴士
1. 文件分开有利于你的学习，每一个都可以单独成一个项目
2. 创建一个~/.pip/pip.conf 然后文件保存一下的内容
    [global]
    
    index-url = https://pypi.douban.com/simple
