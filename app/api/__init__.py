# @Time    : 2019-06-01 08:00
# @Author  : __apple
import os
from config.config import CONFIG_DIR

# 如果没有 image 目录就创建
image_dir = os.path.join(CONFIG_DIR, 'image')
if not os.path.exists(image_dir):
    os.mkdir(image_dir)
