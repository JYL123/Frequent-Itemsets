import csv

with open('./data/cifco_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/cifco_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        cifco_dict = {rows[0]:rows[1] for rows in reader}

with open('./data/hexun_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/hexun_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        hexun_dict = {rows[0]:rows[1] for rows in reader}

with open('./data/qhrb_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/qhrb_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        qhrb_dict = {rows[0]:rows[1] for rows in reader}

with open('./data/shmet_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/shmet_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        shmet_dict = {rows[0]:rows[1] for rows in reader}

with open('./data/zdqh_out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('./data/zdqh_out_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        zdqh_dict = {rows[0]:rows[1] for rows in reader}

for key, value in hexun_dict.items():
    if key in list(cifco_dict.keys()):
        value_1 = int(cifco_dict.get(key))
        value_2 = int(value)
        cifco_dict[key]= value_1 + value_2
    else:
        cifco_dict[key]= int(value)

for key, value in qhrb_dict.items():
    if key in list(cifco_dict.keys()):
        value_1 = int(cifco_dict.get(key))
        value_2 = int(value)
        cifco_dict[key]= value_1 + value_2
    else:
        cifco_dict[key]= int(value)

for key, value in shmet_dict.items():
    if key in list(cifco_dict.keys()):
        value_1 = int(cifco_dict.get(key))
        value_2 = int(value)
        cifco_dict[key]= value_1 + value_2
    else:
        cifco_dict[key]= int(value)

for key, value in zdqh_dict.items():
    if key in list(cifco_dict.keys()):
        value_1 = int(cifco_dict.get(key))
        value_2 = int(value)
        cifco_dict[key]= value_1 + value_2
    else:
        cifco_dict[key]= int(value)

for key, value in cifco_dict.items():
    cifco_dict[key]= int(value)

cifco_dict = dict(sorted(cifco_dict.items(), key=lambda x: x[1], reverse=True))
w = csv.writer(open("./data/total_count.csv", "w"))
for key, val in cifco_dict.items():
    w.writerow([key, val])
