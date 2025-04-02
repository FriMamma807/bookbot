from stats import report

def get_book_text(filepath):
    file_string = ""
    with open(filepath) as f:
        file_string = f.read()
    return file_string

def main():
    file = get_book_text("books/frankenstein.txt")
    report(file)

main()