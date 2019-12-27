# @Time    : 2019-06-10 20:06
# @Author  : __apple

from base.proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
s = Scheduler()
s.run()