
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#        word_count = file_contents.split()
        char_freq = check_counts(file_contents)
        dict_list = get_list_dicts(char_freq)
        dict_list.sort(reverse = True, key=get_sorted_dict)
        print("letter frequency report")
        for i in dict_list:
            print (i)
def check_counts(file_contents):
    char_freq = {}
    word_list = file_contents

    for word in word_list:
        lower_word = word.lower()
        for char in lower_word:
            if char in char_freq:
                char_freq[char] +=1
            else: 
                char_freq[char] = 1       
    return char_freq   
        
def get_list_dicts(char_freq):
    dict_list = []

    for k in char_freq:
        if k.isalpha() != True:
            pass
        else:
            new_pair = {"char": k, "freq": char_freq[k]}
            dict_list.append(new_pair)
    return dict_list

def get_sorted_dict(dict_list):
    return dict_list["freq"]


main()
