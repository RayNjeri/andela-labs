def words(sentence):
	string_list = sentence.split()
	string_dict = {}

	for word in string_list:
	  if word.isdigit():
	    total_words = string_list.count(word)
	    string_dict[int(word)] = total_words
	  else:
	    total_words = string_list.count(word)
	    string_dict[word] = total_words
	    
	return string_dict
