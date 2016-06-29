import re

r1 = r"\d{3,4}-?\d{8}" #匹配电话号码,座机
print(re.findall(r1,"010-12345678"))

p_tel = re.compile(r1) #编译后运行速度更快
print(p_tel.findall("010-12345678"))

csvt_re = re.compile(r"csvt",re.I)
print(csvt_re.findall('CSvt'))

print(csvt_re.match('csvt hello'))
print(csvt_re.search('csvt hello'))
print(csvt_re.finditer('csvt hello'))

print(csvt_re.match('csvt hello').group())

print(help(re.sub))
s="hello csvt"

print(s.replace("csvt python","python"))


rs = r"c..t"

print(re.sub(rs,"python","hello csvt caat cvvt cccc"))
print(re.subn(rs,"python","hello csvt caat cvvt cccc"))

s = "123+456-789*147/556"

print(re.split(r"[\+\-\*\/]",s))

print(dir(re))