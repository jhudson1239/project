import tweepy
import re
import csv
import time

consumer_key= 'PXhXlHgbNzbcqOdtRN2z20YSK'
consumer_secret= 'OOUzo1KarUKvsbxlu0cFIkHyQgDEiqgZhpSCu1cUqafvmgtnZu'

access_token='921145622417346561-kQKaQHegZzboeaChbWOAGo321JR7TZb'
access_token_secret='aufYGhC1nTkLMFrMFdDM2fqgxgItjwOOJv659ErEoA9jN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def company ():
    company = "microsoft"
    emojis = ('\U0001f642', '\U0001f60d', '\U0001f602', '\U0001f615', '\u2728')

    public_tweets = api.search(company ,lang="en", count = 100)
    print(len(public_tweets)," company tweets collected")
    for tweet in public_tweets:
        text = tweet.text
        if company in text:
            text = re.sub(r'^RT', "", text) #Removes RT
            text = re.sub(r'@\w{1,16}.', "", text) #Removes usernames
            text = re.sub(r"http\S+", "", text) #Removes URL
            text = re.sub(r"\n","", text) #Removes newlines
            text = re.sub(r"^\s","", text) #Removes white space at the beginning (Needs work)
            text = re.sub(r"\S+\.\.\.","", text) #Removes truncated endings
            text = re.sub(r"&amp", "", text) #Removes & signs
            text = re.sub(r"\#\S+", "", text) #Removes #
            text = re.sub(r"\:\(","", text) #Removes Smiley Face
            text = re.sub(r"\'", "",text)
            text = re.sub(r"\"", "",text)
            text = re.sub(r"^\s","",text) #Removes blank space at the beginning
            for emoji in emojis:
                text = text.replace(emoji, '')

            with open('microsoft_tweets.csv', 'a', newline='', encoding="utf-8") as testFile:
                testFileWriter = csv.writer(testFile, delimiter=',')
                testFileWriter.writerow([tweet.user.screen_name , text])
            testFile.close()
    
idx=0
while idx < 100 :
    company()
    time.sleep(15)