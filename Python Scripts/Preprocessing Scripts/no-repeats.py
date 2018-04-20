#This file takes a csv file and checks it for repeating posts, it then creats another CSV that contians no repeats.


import csv
def compute (file, outFile):
    tweet = []
    tweets = []

    with open(file, 'r', encoding="utf-8") as CSVfile:
        reader = csv.reader(CSVfile, delimiter = ",")
        for row in reader:
            if row[1] not in tweet:
                    tweet.append(row[1])
                    tweets.append(row)

    with open(outFile, 'w', newline="", encoding="utf-8") as writerFile:
        writer = csv.writer(writerFile, delimiter = ",")
        for row in tweets:
            writer.writerow(row)


compute('positive.csv', 'positive_no_repeat.csv')
