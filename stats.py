def get_word_count(string):
    list = string.split()
    return len(list)

def get_character_count(string):
    lower_case = string.lower()
    letter_dict = {}
    for k in lower_case:
        letter_dict[k] = letter_dict.get(k, 0) + 1   
    return letter_dict

def dict_to_list(dict):
    character_list = []
    for k in dict:
        character_list.append({"char":k, "num":dict[k]})
    def sort_on(character_list):
        return character_list["num"]
    character_list.sort(reverse=True, key=sort_on)
    return character_list




     
