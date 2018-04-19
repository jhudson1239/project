import csv

tweets = []

with open("negative_tweet_no_repeat.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        row.append("negative")
        tweets.append(row)

with open("positive_tweet_no_repeat.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        row.append("positive")
        tweets.append(row)

with open("training_data_no_pre.csv", 'w', encoding="utf-8", newline="")as writerFile:
    writer = csv.writer(writerFile, delimiter =",")
    for tweet in tweets:
        writer.writerow(tweet)