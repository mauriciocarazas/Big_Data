import re
from nltk.stem import SnowballStemmer
import os
from multiprocessing import Pool, cpu_count
import time

def stem_word(word, stemmer):
    return stemmer.stem(word)

def process_batch(args):
    batch_text, stemmer, batch_num = args
    words = re.findall(r'\w+', batch_text.lower())
    stemmed_words = [stem_word(word, stemmer) for word in words]
    print(f"Processed batch {batch_num} on CPU {os.getpid()}")
    return stemmed_words

def main():
    start_time = time.time()
    stemmer = SnowballStemmer("english")
    batch_size = 10 * 1024 * 1024  # 10 MB
    word_counts = {}

    num_cpus = cpu_count()  # Obtener el número de núcleos de CPU
    print(f"Number of CPU cores available: {num_cpus}")

    with open('large_text.txt', 'r', encoding='utf-8') as file:
        batch_texts = []
        while True:
            batch_text = file.read(batch_size)
            if not batch_text:
                break
            batch_texts.append(batch_text)

    pool = Pool(num_cpus)
    results = pool.map(process_batch, [(text, stemmer, i+1) for i, text in enumerate(batch_texts)])
    pool.close()
    pool.join()

    for result in results:
        for word in result:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    # Print word counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
