from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


tr_set = fetch_20newsgroups(subset='train')
te_set = fetch_20newsgroups(subset='test')

vec_er = TfidfVectorizer()
vec_tr = vec_er.fit_transform(tr_set.data)
vec_te = vec_er.transform(te_set.data)

multi_nb = MultinomialNB(alpha=0.02)
multi_nb.fit(vec_tr, tr_set.target)

pred = multi_nb.predict(vec_te)
accuracy = accuracy_score(te_set.target, pred)
print(f'Accuracy of Multinomial Naive Bayes: {accuracy}')
