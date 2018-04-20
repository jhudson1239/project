#This script was used to test the precision, recall and f-measure of TextBlob

import csv 
from textblob import TextBlob
from sklearn.metrics import classification_report

predicted_labels = []
testing_labels = []
tweets = []

with open("testing_data.csv", 'r', encoding="utf-8") as csvFile:
    reader = csv.reader(csvFile, delimiter=",")
    for row in reader:
        tweets.append(row)
        testing_labels.append(row[2])
        text = row[1] 
        analysis = TextBlob(text)
        if analysis.sentiment[0] < 0:
            predicted_label = "negative"
            predicted_labels.append(predicted_label)
        else:
            predicted_label = "positive"
            predicted_labels.append(predicted_label)

print(classification_report(testing_labels, predicted_labels))