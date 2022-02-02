import math

def myBinConverter(a):
  l1,l2=[],[]
  for i in a:
    l1.append(ord(i))
  for i in l1:
    l2.append(int(bin(i)[2:]))
  return l2

def max_0(input_str): 
     return  max(map(len,input_str.split('1')))

def max_1(input_str): 
     return  max(map(len,input_str.split('0')))

with open('two_cities_ascii.txt') as f:
    mystring = f.read()


mystring=myBinConverter(mystring)
mystring = ''.join([str(elem) for elem in mystring])        

print("The biggest sequence of 0s was:",max_0(mystring))
print("And the longest sequence of 1s was:",max_1(mystring))