import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_text = get_book_text(sys.argv[1])
	from stats import number_of_words
	length = number_of_words(book_text)
	from stats import count_per_character
	characters = count_per_character(book_text)
	from stats import sort_book
	sorted_books = sort_book(characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {length} total words")
	print("--------- Character Count -------")
	for sortedbook in sorted_books:
		print(f"{sortedbook['char']}: {sortedbook['num']}")
	print("============= END ===============")

main()


