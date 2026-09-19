storing_sentence = """
Sentence in a variable.
Stored."""

def print_char_count(sentence):
    print(len(sentence))

def first_last_char(sentence):
    print(f"First char: {sentence[0]}, and last char: {sentence[-1]}")

def split_words_from_sentence(sentence):
    split_words = sentence.split("")

    for index, word in enumerate(split_words):
        print(f"{index} position for word: {word}")

def reverse_sentence(sentence):
    print(sentence[::-1])
    