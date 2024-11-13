def rebuild_sentence(words, lenghts) :
    i = 0
    j = 0
    for word in words : # iteration over each word in the words list
        if lenghts[i] > 0 :
            temp = lenghts[i] #assigns the value at lengths[i] to a temporary variable temp
            print(word[:temp], end=" ")
            i += 1 # move to the next word and its corresponding length in the next iteration

words = ["the", "sky", "okay"]
ints = [3, 2, 4]
rebuild_sentence(words, ints)