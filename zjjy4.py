import re
r1 = r"csvt.tt"

print(re.findall(r1,"csvt\ntt",re.S))

s = """
hello csvt 
csvt hello
hello csvt hello
csvt hehe
"""
r = r"^csvt"
print(s)
print(re.findall(r,s,re.M))

tel = r'''
\d{3,4}
-?
\d{8}
'''
print(tel)
print(re.findall(tel,"010-12345678",re.X))

email = r"\w{3}@\w+(\.com|.cn)"

print(re.match(email,"zzz@csvt.com"))

print(re.findall(email,"zzz@csvt.com"))

#利用分组的特性--优先显示特性

s='''
hhsdj dskj hello src=csvt yes jdjsds
djhsjk sr=123 yes jdsa
src=234 yes
hello src=python yes ksa
'''

r1 = "hello src=.+yes"


print(re.findall(r1,s))

r2 = "hello src=(.+)yes"

print(re.findall(r2,s))