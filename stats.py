def get_num_words(text):
        word_count = text.split()
        return len(word_count)

def get_num_letters(text):
    letter_count = text.lower()
    char_count = {}
    for char in letter_count:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
