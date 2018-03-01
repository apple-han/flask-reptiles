"""
    系统文件夹和文件相关的工具类
"""

import os
import re


def get_this_path(file):
    pass


def create_folder(folder_path):
    """
    创建文件夹
    :param folder_path: 文件夹的路径
    """
    # 先判断文件夹是不是存在
    status = is_has_folder(folder_path)
    if not status:
        # 不存在此文件夹，创建
        os.makedirs(folder_path)


def write_file(file_path, content):
    """
    写出一个文件，如果文件不存在则先创建
    :file_path: 文件路径
    :return:
    """
    status = is_has_file(file_path)
    # 检查文件是否包含这个ID
    has_id = False
    if status:
        # 文件已存在，只能追加写
        write_type = "a"
        results = read_file_to_search(file_path)
        if str(content.split('-')[0]) in results:
            has_id = True
    else:
        write_type = "w"
    if not has_id:
        if content:
            with open(file_path, write_type) as f:
                f.write(content)
            return True
        else:
            return False
    return True


def is_has_folder(folder_path):
    """
    判断一个路径是不是存在一个文件夹
    :param folder_path: 文件夹的路径
    :return: True 代表有这个文件夹 False代表没有
    """
    if isinstance(folder_path, str):
        # 判断文件是否存在
        if os.path.exists(folder_path):
            if os.path.isfile(folder_path):
                # 如果是文件说明不是文件夹
                return False
            else:
                # 不是文件说明是文件夹
                return True
        else:
            return False
    else:
        return False


def read_file_to_search(file_path):
    """
    接收一个路径，返回search.big文件的list，每个id只有一次
    :param file_path:
    :return:
    """
    if is_has_file(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                results = line.split('-')
                results = set(results)
                results.remove('')
                return list(results)
    else:
        return False





def is_has_file(file_path):
    """
        判断一个路径是不是存在一个文件
        :param file_path: 文件的路径
        :return: True 代表有这个文件 False代表没有
        """
    if isinstance(file_path, str):
        # 判断文件是否存在
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                # 存在此文件
                return True
            else:
                # 不存在此文件
                return False
        else:
            return False
    else:
        return False


def get_file_size(file_path):
    pass
