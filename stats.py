def get_book_text(filepath):
    file_string = ""
    with open(filepath) as f:
        file_string = f.read()
    return file_string

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
    file_text=get_book_text(file)
    count_list = count_characters(file_text)
    ret_list = []
    for key in count_list:
        ret_list.append({"char":key,"count":count_list[key]})

    ret_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_text)} total words")
    print("--------- Character Count -------")
    for item in ret_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print ("============= END ===============")



