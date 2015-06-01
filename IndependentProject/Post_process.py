__author__ = 'ty'
import re
import csv

pattern = r'A[\d]+'

i = 1
dic = {}
with open('/Users/ty/Desktop/feature_words.csv', 'r') as f0:
    feature_words = csv.reader(f0)
    ls = feature_words.next()
    for item in ls:
        key = "A"+str(i)
        dic[key] = item
        i += 1

flag = True
with open('/Users/ty/Downloads/HLTA/TopicsTable.txt', 'r') as f1:
    while flag:
        line = f1.readline()
        if line != "":
            code_collection = re.findall(pattern, line)
            for item in code_collection:
                line = re.sub(item, dic[item], line)
            with open('/Users/ty/Desktop/TopicsTable_trans.txt', 'a') as f2:
                f2.writelines(line)
        else:
            flag = False