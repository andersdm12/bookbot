def number_of_words(book_text):
	words = book_text.split()
	length = len(words)
	return length

def count_per_character(book_text):
	counts = {}
	characters = list(book_text)
	for character in characters:
		character = character.lower()
		if character in counts:
			counts[character] += 1
		else:
			counts[character] = 1
	return counts

def sort_book(counts):
	sorted_counts = []
	for char, num in counts.items():
		if char.isalpha():
			char_dic = {"char": char, "num": num}
			sorted_counts.append(char_dic)
	sorted_counts.sort(reverse=True, key=lambda d: d["num"])
	return sorted_counts
