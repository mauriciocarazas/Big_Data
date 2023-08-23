import re
from collections import Counter
from nltk.stem import SnowballStemmer

def stem_word(word, stemmer):
    return stemmer.stem(word)

def process_batch(batch_text, stemmer, word_counter):
    words = re.findall(r'\w+', batch_text.lower())  # Tokenize and convert to lowercase
    stemmed_words = [stem_word(word, stemmer) for word in words]
    word_counter.update(stemmed_words)

def main():
    stemmer = SnowballStemmer("english")
    word_counter = Counter()
    batch_size = 100000  # Number of characters per batch

    with open('large_text.txt', 'r', encoding='utf-8') as file:
        while True:
            batch_text = file.read(batch_size)
            if not batch_text:
                break
            process_batch(batch_text, stemmer, word_counter)

    # Print the top N most common words
    top_n = 10
    for word, count in word_counter.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
