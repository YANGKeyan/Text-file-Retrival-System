### Information Retrieval System for Document Search

This GitHub repository contains 2 information retrieval systems developed in Python for querying and retrieving relevant documents from a corpus. The system is designed to support controlled vocabulary and free text search approaches to facilitate simple query and retrieval of documents.

#### Repository Contents:

- **dataset**: The original corpus of documents.
- **preprocessed**: The preprocessed corpus of documents.
- **1explore_content.ipynb**: Jupyter Notebook for exploring and understanding the content of the documents in the corpus(NLTK+word cloud+LDA).
- **2preprocessed.ipynb**: Jupyter Notebook for preprocessing the documents.
- **3controlled_vocabulary.py**: Python script for implementing the controlled vocabulary search approach.
- **4free_text_search.py**: Python script for implementing the free text search approach.

#### Usage Instructions:

1. **Controlled Vocabulary Search**:
   - Execute `3controlled_vocabulary.py` to query and retrieve documents based on controlled vocabulary.
   - Supported topics for controlled vocabulary search include:
     - "Covid-19"
     - "Omicron"
     - "VTL"
     - "Property"
    - You can use and and not as connectives to make logical connections between different controlled vocabulary words.
     - "Covid-19 and Property"
     - "Covid-19 and VTL"
     - "Covid-19 and Omicron"
     - "Covid-19 not Omicron"

2. **Free Text Search(TD-IDF)**:
   - Run `4free_text_search.py` to perform free text search and retrieve relevant documents based on user input queries.

