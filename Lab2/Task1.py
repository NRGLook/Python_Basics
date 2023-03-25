import re
from collections import Counter

def count_sentences(text):
    """Count the number of sentences in the given text"""
    return len(re.findall(r'[.]{1,3}\s', text))

def count_non_declarative_sentences(text):
    """Count the number of non-declarative sentences in the given text"""
    non_declarative_count = 0
    sentences = re.findall(r'([^.!?]*[.!?])', text)
    for sentence in sentences:
        if sentence.endswith("?") or sentence.endswith("!"):
            non_declarative_count += 1
        return non_declarative_count

def average_sentence_length(text):
    """Calculate the average sentence length in characters"""
    sentences = re.findall(r'([^.!?]*[.!?])', text)
    sentence_length = [len(sentence.split()) for sentence in sentences]
    return sum(sentence_length) / len(sentence_length)

def average_world_length(text):
    """Calculate the average word length in characters"""
    words = re.findall(r'\b\w+\b', text)
    word_length = [len(word) for word in words]
    return sum(word_length) / len(word_length)

def top_ngrams(text, n = 4, k = 10):
    """Return the top k n-grams in the given text"""
    words = re.findall(r'\b\w+\b', text)
    ngrams = Counter(zip(*[words[i:] for i in range(n)]))
    return ngrams.most_common(k)

text = "This 123 123abc 34567 is a simple text. It has multiple sentences.  "
print(f"Number of sentences: {count_sentences(text)}")
print(f"Number of non declarative sentences: {count_non_declarative_sentences(text)}")
print(f"Average sentence length: {average_sentence_length(text)}")
print(f"Average world length: {average_world_length(text)}")
print(f"Average world length: {top_ngrams(text, n = 4, k = 10)}")





