# -*- coding: utf-8 -*-
__author__ = "LY"

# file = open("新建文本文档.txt", 'r+', encoding='utf-8')
# str = file.read(2)
# print(str)
# file.close()
#
# with open("新建文本文档.txt", 'r+', encoding='utf-8') as f:
#     print(f.read(10))


# 文件定位
with open("新建文本文档.txt", 'r+', encoding='utf-8') as f:
    print(f.read(10))
    # 查找当前位置
    position = f.tell()
    print("当前文件位置：", position)
    # 把指针重新定位到文件开头
    position = f.seek(0, 0)
    str = f.read(0)
    position = f.tell()
    print(position)
