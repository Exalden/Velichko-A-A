# -- coding: utf-8 --
k = int(input())
n = int(input())
a = 0
b = 1
z = k+n
for i in range (1, z+1):
  f_s = a + b
  a = b
  b = f_s
print(f_s)