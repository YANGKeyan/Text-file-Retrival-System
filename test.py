import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess(text):
    # 将文本转换为小写
    text = text.lower()
    # 移除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # 标记化文本
    tokens = word_tokenize(text)
    # 去除停用词
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # 词干化
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    # 返回处理后的文本
    return tokens
def search_documents_by_topic(topic):
    relevant_documents = []
    for idx, doc_tokens in enumerate(corpus):
        # 将文档中的单词或短语连接成字符串，然后再进行检查
        doc_text = ' '.join(doc_tokens)
        if topic.lower() in doc_text.lower():
            relevant_documents.append(idx)
    return relevant_documents



# 步骤 1：加载数据集和预处理
corpus_folder = "dataset"
corpus = []

for file_name in os.listdir(corpus_folder):
    with open(os.path.join(corpus_folder, file_name), "r", encoding="ISO-8859-1") as file:
        text = file.read()
        # 进行文本预处理和分词操作
        processed_text = preprocess(text)
        corpus.append(processed_text)

# 步骤 2：构建受控词汇表
controlled_vocabulary = {
    "Covid-19": ["covid", "coronavirus", "pandemic"],
    "Covid-19 和 Property": ["property", "real estate", "rent"],
    # 添加其他主题的相关词汇
}

# 步骤 3：创建自由文本搜索引擎
def controlled_vocabulary_search(query):
    relevant_documents = []
    for topic, keywords in controlled_vocabulary.items():
        if any(keyword in query.lower() for keyword in keywords):
            relevant_documents.extend(search_documents_by_topic(topic))
    return relevant_documents

def free_text_search(query):
    relevant_documents = []
    # 实现自由文本搜索
    # 可以使用倒排索引等技术来加速搜索过程
    return relevant_documents

# 步骤 4：系统集成和测试
def search(query):
    controlled_results = controlled_vocabulary_search(query)
    free_text_results = free_text_search(query)
    # 将两种结果合并或根据情况选择其中之一
    return controlled_results + free_text_results

# 测试
query = "Covid-19"
results = search(query)
print("Search results:", results)
