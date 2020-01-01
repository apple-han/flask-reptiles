# @Time    : 2019-06-10 20:06
# @Author  : __apple

from base.proxypool.scheduler import Scheduler
import sys
import io
from multiprocessing import freeze_support



if __name__ == "__main__":
    freeze_support() # 兼容 windows 
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    s = Scheduler()
    s.run()