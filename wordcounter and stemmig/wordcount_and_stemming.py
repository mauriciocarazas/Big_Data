import re
from nltk.stem import SnowballStemmer
import time

def stem_word(word, stemmer):
    return stemmer.stem(word)

def process_batch(batch_text, stemmer, word_counts):
    words = re.findall(r'\w+', batch_text.lower())
    stemmed_words = [stem_word(word, stemmer) for word in words]
    
    for word in stemmed_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

def main():
    start_time = time.time()
    stemmer = SnowballStemmer("english")
    word_counts = {}
    batch_size = 10000000  # 10 MB

    with open('large_text.txt', 'r', encoding='utf-8') as file:
        while True:
            batch_text = file.read(batch_size)
            if not batch_text:
                break
            process_batch(batch_text, stemmer, word_counts)

    # Save word counts to a file
    with open('word_counts.txt', 'w', encoding='utf-8') as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word}: {count}\n")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
