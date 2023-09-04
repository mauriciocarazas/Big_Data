import random

def generate_large_file(dictionary_file, output_file, target_size_gb):
    with open(dictionary_file, 'r', encoding='utf-8') as dict_file:
        dictionary = [line.strip() for line in dict_file]

    target_size_bytes = target_size_gb * 1024 * 1024 * 1024

    with open(output_file, 'w', encoding='utf-8') as output:
        bytes_written = 0
        while bytes_written < target_size_bytes:
            random_word = random.choice(dictionary)
            output.write(random_word + '\n')
            bytes_written += len(random_word) + 1  # Include newline character

    print(f"Archivo '{output_file}' generado con éxito.")

if __name__ == "__main__":
    dictionary_file = "C:\\Users\\mauri\\Escritorio\\words.txt"
    output_file = "C:\\Users\\mauri\\Escritorio\\large_text.txt"
    target_size_gb = 0.1

    generate_large_file(dictionary_file, output_file, target_size_gb)
