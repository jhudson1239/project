import csv

p = []
n = []
amount = []

with open ("150000_training_data_final_backup.csv", 'r', encoding="utf-8") as CSVfile:
    reader = csv.reader(CSVfile, delimiter=",")
    for line in reader:
        if line[2] == "positive":
            p.append(line)
        else:
            n.append(line)

idx = 0

while idx < 150:
    amount.append(p[idx])
    amount.append(n[idx])
    idx = idx + 1

with open("300_tweets.csv", 'w', encoding="utf-8", newline="") as writeCSV:
    writer = csv.writer(writeCSV, delimiter=",")
    for row in amount:
        writer.writerow(row)