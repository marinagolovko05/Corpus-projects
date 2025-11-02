
import re
from collections import Counter
import math

input_file = "D:/corpus/sample_text.txt"

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def compute_entropy(text):
    counter = Counter(text)
    total = sum(counter.values())
    entropy = -sum((freq/total) * math.log2(freq/total) for freq in counter.values() if freq > 0)
    return entropy

with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

text = clean_text(text)
words = text.split()

num_chars = len(text)
num_words = len(words)
num_unique_words = len(set(words))
entropy = compute_entropy(text)

print(f"Размер текста (символы): {num_chars}")
print(f"Количество слов: {num_words}")
print(f"Количество уникальных слов: {num_unique_words}")
print(f"Энтропия текста: {entropy:.4f} бит на символ")
