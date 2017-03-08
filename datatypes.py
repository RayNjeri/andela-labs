def data_type(y):
	if isinstance(y,str):
		return len(y)

	elif y is None:
		return 'no value'

	elif isinstance(y,bool):
		return y

	elif isinstance(y,int):
		if y < 100:
			return 'less than 100'

		elif y == 100:
			return 'equals to 100'

		elif y > 100:
			return 'more than 100'


	elif isinstance(y,list):
		if len(y) > 2:
			return y[2]
		else:
			return None 

	else:
		return None


	
