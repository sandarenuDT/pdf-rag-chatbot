from sklearn.metrics.pairwise import cosine_similarity

def retrieve(question, chunks, vectorizer, vectors, top_k=3):
    q_vec = vectorizer.transform([question])
    scores = cosine_similarity(q_vec, vectors)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]