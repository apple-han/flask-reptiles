FROM daocloud.io/python:3.6
ENV TZ=Asia/Shanghai
RUN mkdir -p /home/apple/app
WORKDIR /home/apple/app

ADD ./requirements.txt /home/apple/app/requirements.txt

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /home/apple/app
RUN chmod a+x ./execute.sh
CMD ["./execute.sh"]