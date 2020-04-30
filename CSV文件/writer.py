# -*- coding: utf-8 -*-
__author__ = "LY"

import csv
# headers = ['姓名', '学号', '班级']
# values = [
#     ("小王", 1001, 9),
#     ('小张', 1002, 9),
#     ('小李', 1101, 10)
#     ]
# with open('csv_writer.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(headers)
#     writer.writerows(values)

with open('csv_writer.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for x in reader:
        value = {"姓名": x["姓名"], "学号": x["学号"], "班级": x["班级"]}
        print(value)