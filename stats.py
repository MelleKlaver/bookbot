def get_num_words(text):
    split_text = text.split()
    wordcount = len(split_text)
    return wordcount

def lettercounter(text):
    dic = {}
    lower_text = text.lower()
    split_text = lower_text.split()
    for word in split_text:
        for letter in word:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] =1
    return dic

def sort_characters(text):
    character_counts = lettercounter(text)
    sorted_list = []  
    for char, count in character_counts.items():
        sorted_list.append({"character": char, "count": count})   
    sorted_list.sort(key=lambda item: item["count"], reverse=True)
    return sorted_list

