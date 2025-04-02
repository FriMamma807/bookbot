def count_words(file):
    words=file.split()
    num_words = len(words)
    return num_words

def count_characters(file):
    file_lower = file.lower()
    char_count = {i: file_lower.count(i) for i in set(file_lower)}
    return char_count

def sort_on(dict_file):
    return dict_file["count"]

def report(file):
    count_list = count_characters(file)
    ret_list = []
    for key in count_list:
        ret_list.append({"char":key,"count":count_list[key]})

    ret_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file)} total words")
    print("--------- Character Count -------")
    for item in ret_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print ("============= END ===============")



