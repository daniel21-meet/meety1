
#common numbers list

def common_numbers (x,y):
	common_numbers_list = []
	for item in x:
	
		y.append(item)
		c = len(y)
		c = c-1

		print(x.count(item))


		if y.index(item) != c and common_numbers_list.count(item) < y.count(item) - 1 and common_numbers_list.count(item) <= x.count(item): 
			common_numbers_list.append(item)
			y.remove(item)
		else:
			y.remove(item)
	

	print(common_numbers_list)

list=[2,4,6,8,2,6,5,2,2,2,2,2]
list2=[3,5,7,8,2,2]

common_numbers(list,list2)
"""

#dictionaries

encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p', 'n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
def encoder_caeser_word_maker (word):
	
	x = len(word) - 1
	list = []
	while x > -1:
		list.append(x)
		x = x-1
	print(list)
	
	meet = []
	for i in list:
		x = str(word)
		print (encoder_caesar[x[i]])
		
		y = (encoder_caesar[x[i]])
		meet.append(y)


	output = ''
	for letter in meet:
		output = letter + output

	print (output)


encoder_caeser_word_maker('jbbq')
"""