from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectors(chunks):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunks)
    return vectorizer, vectors