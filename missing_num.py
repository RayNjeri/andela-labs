def find_missing(list_x, list_y):
	list_x = sorted(list_x) 
	list_y = sorted(list_y) 

	if list_x == list_y:
		return 0
	elif list_x == [] and list_y == []:
		return 0
	else:
		missing = abs(sum(list_x) - sum(list_y))
		return (missing)
