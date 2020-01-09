#!/bin/bash
run_start_uwsgi(){
        `uwsgi --ini uwsgi.ini`
        `nohup python proxy.py >> /dev/null &`
        `nohup python bantang.py >> /dev/null &`
        `nohup python participle.py >> /dev/null &`
}
run_start_uwsgi




