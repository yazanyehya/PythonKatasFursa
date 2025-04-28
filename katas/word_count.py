def count_words(sentence):
    is_word = False
    count = 0

    for char in sentence:
        if char.isalpha():
            if not is_word:
                count+=1
                is_word=True
        else:
                is_word=False
    return count


if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed