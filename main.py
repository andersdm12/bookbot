def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def number_of_words(book_text):
	words = book_text.split()
	length = len(words)
	return length

def main():
	book_text = get_book_text("books/frankenstein.txt")
	length = number_of_words(book_text)
	print(f"{length} words found in the document")

main()



