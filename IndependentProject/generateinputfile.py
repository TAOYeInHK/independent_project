__author__ = 'ty'

import csv
import codecs
import sys
from os import listdir
reload(sys)
sys.setdefaultencoding('utf-8')

keyword = []
with open("/Users/ty/Desktop/result_10000_new.csv", "rb") as keyList:
    reader = csv.reader(keyList)
    keyword = reader.next()
    print keyword[:20]

file_collection = listdir("/Users/ty/Desktop/allpaper2txt")
index = 0
print len(file_collection)
for single_file in file_collection:
    if index == 0:
        index += 1
        pass
    else:
        with codecs.open("/Users/ty/Desktop/allpaper2txt/"+single_file, encoding="utf-8") as fp:
            show_or_not = []
            txt_str = fp.read()
            for item in keyword:
                if str(txt_str).find(item) == -1:
                    show_or_not.append(0)
                else:
                    show_or_not.append(1)

            with open("/Users/ty/Desktop/result_10000_new.csv", "a") as output:
                writer = csv.writer(output)
                writer.writerow(show_or_not)
