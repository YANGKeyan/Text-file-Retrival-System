import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words] 
    return ' '.join(filtered_tokens)

dataset_path = "preprocessed"
file_names = os.listdir(dataset_path)
documents = [read_file(os.path.join(dataset_path, file_name)) for file_name in file_names]


preprocessed_documents = [preprocess_text(doc) for doc in documents]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_documents)

query = input("Input query：")

preprocessed_query = preprocess_text(query)

query_tfidf = tfidf_vectorizer.transform([preprocessed_query])

cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

top_indices = cosine_similarities.argsort()[-10:][::-1]
top_documents = [(file_names[i], cosine_similarities[i]) for i in top_indices]

print("The ten most relevant document names and their scores：")
for document, score in top_documents:
    print(f"{document}: {score}")
