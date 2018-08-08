"""
Script introduction: 
    Read csv file.

@Time :       2018-08-07 21:36
@Author :     nulijiushimeili
@Site :       
@File :       read_csv.py
@Software :   PyCharm
"""

import csv

filename = "example.csv"

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print("Open file error:", filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
        # print("{}\t{}\t{}".format(item[0],item[1],item[2]))
