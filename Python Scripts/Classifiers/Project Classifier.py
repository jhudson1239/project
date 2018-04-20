#This script was the final classifier that was used to classify the data.
#the naive bayes algorithm was used.

import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB

def load_dataset_from_csv (input_csv_file):
    review_labels = []
    review_texts = []

    with open(input_csv_file, 'r', encoding="utf-8")as csvFile:
        reader = csv.reader(csvFile, delimiter = ",")
        for row in reader:
            review_labels.append(row[2])
            review_texts.append(row[1])
    return review_texts, review_labels

def load_company_csv (input_csv_file):
    review_texts = []
    review_username = []

    with open(input_csv_file, 'r', encoding="utf-8")as csvFile:
        reader = csv.reader(csvFile, delimiter = ",")
        for row in reader:
            review_username.append(row[0])
            review_texts.append(row[1])
    return review_username, review_texts

def compute_data (testfile, finalFile):

    training_texts, training_labels = load_dataset_from_csv('150000_training_data_final_backup.csv')

    username,testing_texts = load_company_csv(testfile)

    training_count_vectorizer = CountVectorizer(max_features=10000, stop_words='english')

    training_bow_instances = training_count_vectorizer.fit_transform(training_texts)

    training_words = training_count_vectorizer.get_feature_names()

    test_count_vectorizer = CountVectorizer(stop_words='english', vocabulary=training_words)

    test_bow_instances = test_count_vectorizer.fit_transform(testing_texts)

    classifier = GaussianNB()
    classifier.fit(training_bow_instances, training_labels)

    predicted_labels = classifier.predict(test_bow_instances)

    idx = 0
    tweets = []

    while idx<len(predicted_labels):
        id = idx+1
        tweets.insert(idx,[id, username[idx], testing_texts[idx] ,predicted_labels[idx]])
        idx = idx +1
    
    with open(finalFile, 'a', newline='', encoding="utf-8") as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        for row in tweets:
            writer.writerow(row)

compute_data('google_tweets_processed.csv', 'google_sentiment.csv')#Change these outputs depending on what data was being classified.