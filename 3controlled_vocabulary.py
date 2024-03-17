import os

thesaurusDict = {
    'covid-19': ['covid', 'coronavirus'],
    'property': ['real estate', 'land', 'assets', 'property'],
    "omicron": ["omicron"],
    "vtl": ["vtl", "vaccinate", "travel"]
}

def search_documents(keywords):
    results = []
    all_files = os.listdir('preprocessed')
    for filename in all_files:
        with open(os.path.join('preprocessed', filename), 'r', encoding='utf-8') as file:
            content = file.read().lower()
            keyword_matches = []
            not_flag = False
            for keyword in keywords:
                if keyword == 'and':
                    continue
                if keyword == 'not':
                    not_flag = True
                    continue
                if not_flag and keyword in thesaurusDict and any(term in content for term in thesaurusDict[keyword]):
                    break
                if not not_flag and not any(term in content for term in thesaurusDict[keyword]):
                    break
                keyword_matches.append(True)
            else:
                if all(keyword_matches):
                    results.append(filename)
    return results

def search(query):
    keywords = query.split()
    print(f"Results for '{query}':")
    documents = search_documents(keywords)
    if documents:
        for doc in documents:
            print(doc)
        print(f"Total documents found containing '{query}': {len(documents)}")
    else:
        print("No documents found containing the query.")

def main():
    while True:
        print("\nEnter keywords to search ('q' to quit):")
        query = input("Enter your query: ").lower()
        
        if query == 'q':
            print("Exiting...")
            break
        
        search(query)

if __name__ == "__main__":
    main()
