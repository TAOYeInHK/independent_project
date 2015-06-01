'''
@author: ty
'''

import codecs
from os import listdir
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class node(object):
    def __init__(self, order=0, sum_value=0):
        self.order = order
        self.sum_value = sum_value


def compare(node_1, node_2):
    if node_1.sum_value < node_2.sum_value:
        return True
    else:
        return False


def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    m = len(sequence) / 2
    return merge(merge_sort(sequence[:m]), merge_sort(sequence[m:]))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

vectorizer = CountVectorizer()
transformer = TfidfTransformer()
file_str_collection = []
file_collection = listdir("/Users/ty/Desktop/allpaper2txt")
index = 0
for single_file in file_collection:
    if index == 0:
        index += 1
        pass
    else:
        with codecs.open("/Users/ty/Desktop/allpaper2txt/"+single_file, encoding="utf-8") as fp:
            file_str_collection.append(fp.read())
print "txt analysis start"

X = vectorizer.fit_transform(file_str_collection)

tfidf = transformer.fit_transform(X)

word = vectorizer.get_feature_names()

print "building matrix start"
weight = tfidf.toarray()

# get top 20 key words for each article
keywords_of_each = []
temp_list = []
for i in range(weight.shape[0]):
    temp_list = []
    for j in range(weight.shape[1]):
        temp_node = node(j, weight[i][j])
        temp_list.append(temp_node)
    temp = merge_sort(temp_list)[::-1][:5]
    for item in temp:
        keywords_of_each.append(item.order)

keywords_of_each_set = set(keywords_of_each)

print len(keywords_of_each_set)
print keywords_of_each_set

word_count = {}
for item in keywords_of_each_set:
    value = keywords_of_each.count(item)
    word_count[item] = value

top_words = sorted(word_count.iteritems(), key=lambda d: d[1], reverse=True)
top_words_list_1000 = []
top_words_list_5000 = []
top_words_list_10000 = []
for item in top_words:
    if i < 1000:
        top_words_list_1000.append(word[item[0]])
    if i < 5000:
        top_words_list_5000.append(word[item[0]])
    if i < 10000:
        top_words_list_10000.append(word[item[0]])

with open("/Users/ty/Desktop/result_1000.csv", "wb") as word_list_1000:
    word_list_writer = csv.writer(word_list_1000)
    word_list_writer.writerow(top_words_list_1000)

with open("/Users/ty/Desktop/result_5000.csv", "wb") as word_list_5000:
    word_list_writer = csv.writer(word_list_5000)
    word_list_writer.writerow(top_words_list_5000)

with open("/Users/ty/Desktop/result_10000.csv", "wb") as word_list_10000:
    word_list_writer = csv.writer(word_list_10000)
    word_list_writer.writerow(top_words_list_10000)











'''
sum_list = []
sum_list.sort()
for word_index in range(weight.shape[1]):
    sum_tfidf = 0.0
    for article_index in range(weight.shape[0]):
        sum_tfidf += weight[article_index, word_index]
    temp = node(word_index, sum_tfidf)
    sum_list.append(temp)

print "sort start"

sum_list = merge_sort(sum_list)[::-1]
word_to_be_chosen_1000 = []
word_to_be_chosen_5000 = []
word_to_be_chosen_10000 = []

for i in range(10000):
    if i < 10000:
        print word[sum_list[i].index]
        #word_to_be_chosen_10000.append(word[sum_list[i].index])

        #if i<5000:
        #    word_to_be_chosen_5000.append(word[sum_list[i].index])
        #    if i<1000:
        #        word_to_be_chosen_1000.append(word[sum_list[i].index])


with codecs.open("/Users/ty/Desktop/result_1000.csv","wb",encoding='utf-8') as csvfile_1000:
    writer_1000=csv.writer(csvfile_1000)
    writer_1000.writerow(word_to_be_chosen_1000)
with codecs.open("/Users/ty/Desktop/result_5000.csv","wb",encoding='utf-8') as csvfile_5000:
    writer_5000=csv.writer(csvfile_5000)
    writer_5000.writerow(word_to_be_chosen_5000)
with codecs.open("/Users/ty/Desktop/result_10000.csv","wb",encoding='utf-8') as csvfile_10000:
    writer_10000=csv.writer(csvfile_10000)
    writer_10000.writerow(word_to_be_chosen_10000)



for i in range(len(sum_list)):
    for j in range(i,len(sum_list)):
        if(compare(sum_list[i],sum_list[j])):
            pass
        else:
            temp_node=sum_list[i]
            sum_list[i]=sum_list[j]
            sum_list[j] = temp_node





#print weight_new.shape


count=0
with codecs.open("/Users/ty/Desktop/result1.csv","wb",encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    #writer.writerow(word)
    for line in weight_new:
        writer.writerow(line)
        count+=1
        if count==200:
            break

'''



