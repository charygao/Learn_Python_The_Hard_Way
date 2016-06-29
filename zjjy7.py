
import webbrowser as web 
import time

class Recruiter(object):
	def _init_(self,myName,birth,gender,cellPhone,myEmail):
		self.myName = myName
		self.age = birth
		self.gender = gender
		self.cellPhone = cellPhone
		self.myEmail = myEmail
	def count_age(self):
		nowYear = time.strftime('%Y',time.localtime(time.time()))
		return nowYear - self.birth 
	def print_info(self):
		print("姓名:%-12s年龄:%-15s性别:%-14s" % (self.name,self.age,self.gender))
		print("手机:%-15s邮箱:%-15s" % (self.cellPhone,self.email))

gyb = Recruiter("高亚斌",1990,"男","18521517787","gaoyabing@126.com") 

gyb.print_info()
