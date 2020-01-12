#!/bin/bash
ps -ef | grep python | cut -c 9-15| xargs kill -s 9
run_start_uwsgi(){
    `uwsgi --ini uwsgi.ini >> /dev/null &
     python proxy.py >> /dev/null &
     python bantang.py >> /dev/null &
     python participle.py >> /dev/null`
}
run_start_uwsgi




