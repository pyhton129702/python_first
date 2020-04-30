# -*- coding: utf-8 -*-
__author__ = "LY"

import csv

# with open('test.csv', newline='') as f:
#     spamreader = csv.reader(f, delimiter=" ", quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# with open('test.csv', 'w', newline='') as f:
#     spamwriter = csv.writer(f, delimiter=' ', quotechar='|',
#                             quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['spam']*5 + ['Baked Beans'])
#     spamwriter.writerow(['spam', 'Lovely spam', 'Wonderful Spam'])



def writer_csv_demo1():
    headers = ["name","age","height"]
    values = [
        ("小王",18,178),
        ("小张",20,180),
        ("小李",17,166)
    ]
    with open("classroom.csv","w",encoding="utf-8",newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

writer_csv_demo1()
