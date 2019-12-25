

import math
x = input ("please insert a number between 1 - 10")
while 11 > x > 0: 
	y = input ("please insert another number between 1 - 10")

	if 11 > y > 0:
		z = math.pow(x,y)
		print (z)

		b = math.sqrt(z)
		print (b)
		
		while b < 100000:
		
			b = b + 1


		
else:
	print ('please try again')

	