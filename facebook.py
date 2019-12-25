
class user(object):
	
	def __init__(self,name,email,password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []
	
	def add_friend(self,email1,friends_list):
		self.email1 = email1
		self.friends_list.append(self.email1)
		print (self.name +" had added "+self.email1 +" as a friend")
	
	def remove_friend(self,email1,friends_list):
		self.email1 = email1
		self.friends_list.remove(self.email1)
		print (self.name+" had removed "+ self.email1 +" from your friends_list ")
	
	def Post (self,text):
		post1 = post ("blhhh", [],[])
		self.posts.append(text)	
		print (self.name+"has posted: "+text)
	
	def get_userInfo (self):
		print ("Name: " + self.name)
		print ("Email: " + self.email)
		print ("Password: " + self.password)
		print ("Friends: " , self.friends_list)
		print ("Posts: " , self.posts)

class post (user):
	def __init__(self, share , likes, email):
		self.email = email
		self.comments  = []
		self.likes = likes

	def add_Like (self, likes):
		self.likes = self.likes + 1
		print ("likes: " + str(self.likes))
		


user1 = user("Loai","Loai17@meet.mit.edu", "myhiddenpassword123")
user2 = user("dod","dod@meet.mit.edu", "myhiddenpassword")
user3 = user ("zi" , "zizi@zizi.zizi.com" , "bibi")
user1.add_friend ("dod", user1.friends_list)
user1.Post ("blahhhhhhh")
user2.get_userInfo()
user1.add_friend("zi" , user1.friends_list)
user1.remove_friend("zi", user1.friends_list)


