import re
from collections import Counter

def count_sentences(text):
    """Count the number of sentences in the given text"""
    return

def count_non_declarative_sentences(text):
    """Count the number of non-declarative sentences in the given text"""
    non_declarative_count = 0
    sentences = re.findall(r'([^.!?]*[.!?])', text)
    for sentence in sentences:
        if sentence.endswitch("?") or sentence.endswitch("!"):
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

