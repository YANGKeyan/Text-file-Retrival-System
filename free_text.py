import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 遍历dataset文件夹下的所有txt文档
document_texts = []
document_paths = []

dataset_folder = "preprocessed"  # 数据集文件夹路径

for filename in os.listdir(dataset_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(dataset_folder, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            document_texts.append(text)
            document_paths.append(filepath)

# 构建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 对文档进行TF-IDF向量化
tfidf_matrix = tfidf_vectorizer.fit_transform(document_texts)

# 定义查询
query = "Covid-19 and Property"

# 将查询转换为TF-IDF向量
query_vector = tfidf_vectorizer.transform([query])

# 计算查询与每个文档之间的余弦相似度
cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

# 获取排名前N个相关文档的索引
top_n = 5
top_indices = cosine_similarities.argsort()[-top_n:][::-1]

# 打印排名前N个相关文档的路径
print(f"Top {top_n} relevant documents:")
for index in top_indices:
    print(document_paths[index])
