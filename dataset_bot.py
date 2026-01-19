import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def dataset_answer(user_question, questions, answers, vectorizer, question_vectors, threshold=0.3):
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, question_vectors)[0]

    best_index = np.argmax(similarities)

    if similarities[best_index] >= threshold:
        return answers[best_index]

    return "Sorry, I don't know the answer to that yet."





# import numpy as np
# from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def dataset_answer(user_question, questions, answers, embeddings, threshold=0.6):
#     query_embedding = model.encode([user_question])
#     similarities = util.cos_sim(query_embedding, embeddings)[0]

#     best_match = similarities.argmax()
#     if similarities[best_match] >= threshold:
#         return answers[best_match]

#     return "Sorry, I don't know the answer to that yet."
