from stats import report
import sys


def main():
    file_path= ""
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path=sys.argv[1]

    report(file_path)

main()