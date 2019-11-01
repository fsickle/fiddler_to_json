# -*- coding:utf-8 -*-
import os
import re
import subprocess


def get_package_name():
    file_path = 'F:\\Review\\APP\\30-new'
    file_list = os.listdir(file_path)

    name_list = list()

    # 读取文件，获得包名
    for file in file_list:
        aapt_com = 'aapt d badging ' + file_path + "\\" + file
        p = subprocess.Popen(aapt_com, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        status = p.wait()
        # print(out.decode())
        pac = re.match(r'package: name=\'(.+?)\' ver', out.decode())
        # pac_name = pac.match(line).group(0)
        name_list.append(pac.group(1))
    # print(name_list)
    return name_list

if __name__ == '__main__':
    get_package_name()