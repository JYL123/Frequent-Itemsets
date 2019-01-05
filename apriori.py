"""
This code processes a csv file that is in the format specified in the csv files in data folder. 
This code returns a list of freuqent items with frequency at least 3 times in the given csv files
"""

import csv
from collections import defaultdict, namedtuple

with open('./data/test_daily_data_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/test_daily_data_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        words_freq_dict = {rows[0]:rows[1] for rows in reader}

total_count = 0
# total count 
for key, value in words_freq_dict.items():
        total_count += int(value)
# calculate percentage
for key, value in words_freq_dict.items():
        words_freq_dict[key]= float(int(value)/total_count)
# generate frequent items table, if the frequency >= 3 (0.00516795865633075) per day, we count it as frequent item
frequent_items_table = dict()
for key, value in words_freq_dict.items():
        # remove non-frequent items and meaningless numbers 
        if value > 0.006 and not key.isdigit():
         frequent_items_table[key]= value
print(frequent_items_table)

# generate all unique pairs encounters a problem of chinese character sorting

# some change