from sklearn.feature_extraction.text import CountVectorizer


with open('../chap13/mini_newsgroups/alt.atheism/51121', 'r') as doc:
    text = doc.read()
    vec_er = CountVectorizer()
    vec = vec_er.fit_transform([text])
    print(vec_er.get_feature_names_out())
    print(vec.toarray())
