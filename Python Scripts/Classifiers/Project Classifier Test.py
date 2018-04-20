import csv

#As you can see this file was used to test all the classifiers. Each classifier is imported and then changed on line 
#40, this allowed different combinations to be tested out.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.svm import LinearSVC

def load_dataset_from_csv (input_csv_file):
    review_labels = []
    review_texts = []

    with open(input_csv_file, 'r', encoding="utf-8")as csvFile:
        reader = csv.reader(csvFile, delimiter = ",")
        for row in reader:
            review_labels.append(row[2])
            review_texts.append(row[1])
    return review_texts, review_labels

training_texts, training_labels = load_dataset_from_csv('150000_training_data.csv')#Change the training data here

testing_texts, testing_labels = load_dataset_from_csv('testing_data.csv')#change the testing data here

training_count_vectorizer = CountVectorizer(max_features=10000, stop_words='english', ngram_range=(1,2))#change amount of features here

training_bow_instances = training_count_vectorizer.fit_transform(training_texts)

training_words = training_count_vectorizer.get_feature_names()

test_count_vectorizer = CountVectorizer(stop_words='english', vocabulary=training_words)

test_bow_instances = test_count_vectorizer.fit_transform(testing_texts)

classifier =RandomForestClassifier(n_estimators = 20, n_jobs=5) #Change the classifer here

classifier.fit(training_bow_instances, training_labels)

predicted_labels = classifier.predict(test_bow_instances)
print(classification_report(testing_labels, predicted_labels))