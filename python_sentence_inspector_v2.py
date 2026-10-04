"""
Original sentence:
Character count:
First character:
Last character:
Words:
Reversed sentence:
First word:
Last word:
"""

def big_handler_method(sentence):
    print(sentence)
    print(len(sentence))

    list_words = sentence.split(" ")
    print(len(list_words))

    sentence_reversed = sentence[::-1]
    print(sentence_reversed)

    print(list_words[0] + " " + list_words[-1])


    print(f"First character: {sentence[0]}")
    print(f"Last character: {sentence[-1]}")

    print(f"Words: {list_words}")


if __name__ == "__main__":
    list_of_sentence_tests = ["Python is fun", "Manchester is lovely", "I love programming",]

    for item in list_of_sentence_tests:
        big_handler_method(item)
    
	
	