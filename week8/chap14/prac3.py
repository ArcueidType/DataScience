from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer


text_set = fetch_20newsgroups()
vec_er = TfidfVectorizer()
text_vecs = vec_er.fit_transform(text_set.data)
print(text_vecs[0])
