from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':

    vectorizer = CountVectorizer(min_df=1)
    example_content = ["How to create a word bag", "How build a word bag"]

    words_vector = vectorizer.fit_transform(example_content)

    print(vectorizer.get_feature_names())

    print(words_vector.toarray().transpose())