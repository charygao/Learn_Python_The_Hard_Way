#!/usr/bin/python  #加入该句后,在Linux下赋予chomd x权限后,可以直接执行该文件
import py_compile
py_compile.compile ("hello.py") #生成字节代码
print("编译完成")

# python -O -m py_compile hello.py #生成优化后的字节代码
