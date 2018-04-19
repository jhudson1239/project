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


compute('150000_training_data.csv', '150000_training_data.csv')

#This scripts takes a file and make sures there is no reapeats of text in the data