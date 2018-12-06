import pandas as pd
import csv
import collections
import pprint


file_names = ["./data/cifco.csv", "./data/hexun.csv", "./data/qhrb.csv", "./data/shmet.csv", "./data/zdqh.csv"]
# combine all csv files
combined_csv = pd.concat( [ pd.read_csv(f) for f in file_names ] )
# export the combines csv files
combined_csv.to_csv( "./data/combined_csv.csv", index=False )


with open('./data/combined_csv.csv', "rt") as fp:
    root = csv.reader(fp, delimiter=',')
    result = collections.defaultdict(list)
    for row in root:
        year = row[1].split("-")[0]
        result[year].append(row)

# print("Result:-")       
pprint.pprint(result)

for i,j in result.items():
    file_path = "%s%s_test.csv"%('./data/', i)
    with open(file_path, 'wt') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerows(j)