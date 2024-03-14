import os
import re

# 定义受控词汇列表
controlled_vocabulary = {
    #"sg":["singapor"],
    "Covid-19": ["covid"],
    "Covid-19 and Omicron": ["covid" ,"omicron"],
    "Covid-19 not Omicron": ["covid"],
    "Covid-19 and Property": ["covid","properti"],
    "Covid-19 and VTL": ["covid" ,"vtl","vaccin","travel","lane"]
}
 
# 定义搜索函数
def search_documents(folder_path, controlled_vocabulary):
    relevant_documents = {}

    # 遍历文件夹下的所有txt文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            
            # 读取文档内容
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().lower()  # 将文本内容转换为小写以进行匹配

            # 检查文档中是否同时包含每个主题的受控词汇
            for topic, keywords in controlled_vocabulary.items():
                found_keywords = [word for word in keywords if re.search(r'\b' + re.escape(word.lower()) + r'\b', content)]

                # 特殊情况：Covid-19 not Omicron
                if topic == "Covid-19 not Omicron":
                    # 检查文档中是否包含 "covid" 但不包含 "omicron"
                    if 'covid' in found_keywords and 'omicron' not in content:
                        if topic not in relevant_documents:
                            relevant_documents[topic] = {'documents': [], 'count': 0}
                        relevant_documents[topic]['documents'].append(file_name)
                        relevant_documents[topic]['count'] += 1
                # 普通情况
                elif len(found_keywords) == len(keywords):
                    if topic not in relevant_documents:
                        relevant_documents[topic] = {'documents': [], 'count': 0}
                    relevant_documents[topic]['documents'].append(file_name)
                    relevant_documents[topic]['count'] += 1
    return relevant_documents

# 搜索相关文档
relevant_documents = search_documents("preprocessed", controlled_vocabulary)

# 打印相关文档
for topic, documents_info in relevant_documents.items():
    print("Topic:", topic)
    print("Number of Related Documents:", documents_info['count'])
    #print("Related Documents:")
    #for document in documents_info['documents']:
        #print("-", document)
    #print()
    