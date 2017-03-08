def fizz_buzz(j):
  if j % 3==0:
    return 'Fizz' "msg('Fizz for number divisible by 3')"
  elif j % 5==0:  
    return 'Buzz' "msg('Buzz for number divisible by 5')"
  elif j % 3==0 and j % 5==0:
    return 'FizzBuz' "msg('FizzBuzz for number divisible by 3 and 5')"
  elif j % 3!=0 and j % 5!=0:
  	print (j)     "msg('print the number if indivisible by 3 neither 5')"
  else:
    return j

