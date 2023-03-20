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

def average
