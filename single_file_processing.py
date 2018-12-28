"""
This code processes a csv file that is in the format specified in the csv files in data folder. 
This code displays a graph of top 20 items in the csv file 
"""

# Python 3 is UTF-8 by default
import jieba
import string
import pandas as pd 
from matplotlib import font_manager
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import _rebuild
import operator
from itertools import islice
import csv

# reload for displaying chinese characters
_rebuild() 

# n is an integer. this function returns first n items in a dictionary(iterable)
def take(n, iterable):
    return dict(islice(iterable, n))

# value is a string. This moethod removes the punctuation in a string
def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

# file name has to be in the format of: xxx.xlsx
def read_file(file_name):
    # convert xlsx to csv
    data_xls = pd.read_excel(file_name, index_col=None)
    name = (file_name.split("/")[2]).split(".")[0]
    new_file_name = "./data/"+ name + ".csv"
    data_xls.to_csv(new_file_name, encoding='utf-8', index=False)
    # read csv file
    file_data = pd.read_csv(new_file_name) 
    # get title, title is in a dataframe
    titles = file_data[['title']]
    # test: print first 5 lines
    # print(titles.head())

    return titles

def plot_graph_with_chinese_characters(bag_of_words, x_label, y_label, title):
    fontP = font_manager.FontProperties()
    # SimHei to display chinese characters
    fontP.set_family("SimHei")
    fontP.set_size(14)

    index = np.arange(len(list(bag_of_words.keys())))
    plt.bar(index, list(bag_of_words.values()))
    plt.xlabel(x_label, fontproperties=fontP)
    plt.ylabel(y_label, fontproperties=fontP)
    plt.xticks(index, list(bag_of_words.keys()), rotation=90, fontproperties=fontP, size="x-small")
    plt.legend(loc=0, prop=fontP)
    plt.title(title, fontproperties=fontP)
    plt.grid(True)
    plt.axis("tight")
    plt.show()

def write_dict_to_csv(bag_of_words, file_name):
    w = csv.writer(open(file_name, "w"))
    for key, val in bag_of_words.items():
        w.writerow([key, val])


# get all the titles in the specified excel file
titles = read_file("./data/test_daily_data.xlsx")

# creating a hashmap
bag_of_words = dict()
for index, row in titles.iterrows():
       title = row['title']
       data = remove_punctuation(title).replace(" ", "")
       seg_list = jieba.cut(data, cut_all=True)
       for seg in seg_list:
           if not seg.isspace() and seg:
            if seg in bag_of_words:
                bag_of_words[seg] += 1
            else:
                bag_of_words[seg] = 1

# reverse = true: descending order
bag_of_words = dict(sorted(bag_of_words.items(), key=lambda x: x[1], reverse=True))
write_dict_to_csv(bag_of_words, "./data/test_daily_data_out.csv")
# print the top 20 items
bag_of_words = take(20, bag_of_words.items())
# plot the graph
plot_graph_with_chinese_characters(bag_of_words, "phrases", "frequencies", "Frequency Graph")