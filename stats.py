def get_num_words(text):
	num_words = len(text.split())
	return num_words

def get_letter_count(text):

	character_count = {
		"t": 0,
		"p": 0,
		"c": 0
	}

	letters = list(text.lower())	
	
	for letter in letters:
		if character_count.get(letter, 0) == 0:		
			character_count[letter] = 1
	
		else:
			character_count[letter] += 1

	return character_count


def count_list(text):

	letter_count = get_letter_count(text)
	
	letter_count_list = []

	for letter in letter_count:
		if letter.isalpha():
			tmp_dict = {}			
			num = letter_count[letter]
			tmp_dict["letter"] = letter
			tmp_dict["num"] = num
			letter_count_list.append(tmp_dict)
		else:
			pass

	def sort_on(items):
		return items["num"]

	letter_count_list.sort(reverse=True, key=sort_on)

	for i in range(0, len(letter_count_list)):
		print(f"{letter_count_list[i]['letter']}: {letter_count_list[i]['num']}")
