def find_max_min(y):
	"""check for max_min value"""


	if len(set(y)) == 1:
		return list(set(y))
	else:
		l = len(y)
		y_sorted = sorted(y)

		minVal = y_sorted[0]
		maxVal = y_sorted[len(y)-1]

		return [minVal, maxVal]
