def What_is_your_list_of_strings(my_list_of_strings):
    my_dictionary = {}
    for words in my_list_of_strings:
        my_dictionary[words] = len(words)
        if len(words) % 2 == 0:
            my_dictionary[words] = {len(words)}, {"parity" : "even"}
        else:
            my_dictionary[words] = {len(words)}, {"parity": "odd"}


    return my_dictionary

words = {"data", "science"}

final_result = What_is_your_list_of_strings(words)
print(final_result)