#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = ".?:"
    sentences = []
    sentence_buffer = ""
    for char in text:
        sentence_buffer += char
        if char in delimiters:
            sentences.append(sentence_buffer.strip())
            sentence_buffer = ""
    if sentence_buffer:
        sentences.append(sentence_buffer.strip())
    for sentence in sentences:
        print(sentence)
        print()
