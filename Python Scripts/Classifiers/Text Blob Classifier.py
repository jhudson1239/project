#This script is the classification script for Textblob that was used for its final sentiment analysis results.

import csv 
from textblob import TextBlob

predicted_labels = []
tweets = []

def sentiment(file, proFile):
    with open(file, 'r', encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        for row in reader:
            tweets.append(row)
            text = row[1] 
            analysis = TextBlob(text)
            if analysis.sentiment[0] < 0:
                predicted_label = "negative"
                predicted_labels.append(predicted_label)
            else:
                predicted_label = "positive"
                predicted_labels.append(predicted_label)

    idx = 0
    while idx < len(predicted_labels):
        tweets[idx].append(predicted_labels[idx])
        print(tweets[idx])
        idx = idx + 1

    with open(proFile, 'w', encoding="utf-8", newline="") as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        for row in tweets:
            writer.writerow(row)
    


sentiment('amazon_tweets_processed.csv', 'amazon_textblob.csv')#Change these outputs depending on what data was being classified.
print(tweets)