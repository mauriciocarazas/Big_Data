import re

def simple_stem(word):
    # Define rules for stemming here
    if word.endswith("ing"):
        return word[:-3]
    if word.endswith("ed"):
        return word[:-2]
    # Add more rules as needed
    return word

def process_batch(batch_text, word_counts):
    words = re.findall(r'\w+', batch_text.lower())
    stemmed_words = [simple_stem(word) for word in words]
    
    for word in stemmed_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

def main():
    word_counts = {}
    batch_size = 100000

    with open('large_text_file.txt', 'r', encoding='utf-8') as file:
        while True:
            batch_text = file.read(batch_size)
            if not batch_text:
                break
            process_batch(batch_text, word_counts)

    top_n = 10
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
