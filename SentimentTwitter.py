import pandas as pd
pd.set_option('display.max_columns', None)
print('Reading csv data')
data = pd.read_csv('Tweets.csv')
# print(data.head())

data_selected = data[data["airline_sentiment_confidence"] > 0.5]
# drop_rws=data["airline_sentiment_confidence"] < 0.5
# data_drop = data.drop(data[drop_rws].index)
# print(data_selected)
# print(data_drop)
input= data_selected['text']
output = data_selected['airline_sentiment']
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer
stop_words=stopwords.words('english')
stemmer=PorterStemmer()

import re
cleaned_data=[]
print('\ncleaning data:')
for i in range(len(input)):
   tweet=re.sub('[^a-zA-Z]',' ',input.iloc[i])
   tweet=tweet.lower().split()

   tweet=[stemmer.stem(word) for word in tweet if (word not in stop_words)]
   tweet=' '.join(tweet)
   cleaned_data.append(tweet)

# print(cleaned_data)

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = cleaned_data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())

sentiment_ordering = ['negative', 'neutral', 'positive']
print('\ndigitizing labels: ')
output = output.apply(lambda x: sentiment_ordering.index(x))
y = output
print(y)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
estim= RandomForestClassifier()
print('\ntraining:')
cv_results = cross_validate(model, X, y, cv=4)
print(cv_results)