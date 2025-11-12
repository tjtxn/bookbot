def get_book_text():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	return file_contents

from stats import get_num_words

from stats import get_letter_count

from stats import count_list

file_contents = get_book_text()

def main():
	num_words = get_num_words(file_contents)
	print(f"Found {num_words} total words")

def char_count():
	character_count = get_letter_count(file_contents)
	print(character_count)

print("============ BOOKBOT ============\nby: tjtxn\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	
main()

print("--------- Character Count -------")

count_list(file_contents)

print("============= END ===============")
