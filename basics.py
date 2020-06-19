import sys
import os
import random

print("Hi")
#Comment
'''
a
long
comment
'''

#vars are sorta like in JS
name = "Chris"
print(name)

#Normal math stuff + - * / % **(Power) //(Round down)
# ' and " are the same

# , to concatenate
print(name, 18)

multi_line_string = '''just
sing'''

print("%s" % (multi_line_string))

array_list = ["list", "are", "the", "arrays", "of", "python"]
print(array_list[0])

array_list[0] = "liiist"
print(array_list[0])

print(array_list[0:2])

print(array_list[0:])

array_list.append("!")
array_list.remove("the")
array_list.insert(2, "I made IT!")
del array_list[3]
print(array_list[0:])
print("array_list %s" % (len(array_list)))

#you can nest lists

#tuples are list you cant change line arrays in Java


#Dictionary are like maps in Java
dict = {"key" : "value", "key2" : "value2"}

print(dict["key"])
print(dict.get("key2"))
print(dict.keys())
print(dict.values())

#if else elif use noraml operators

number = 5
if number > 6:
    print("More then 6")
else :
    print("Less then 6")

if((number < 6) and (number > 2)) :
    print(number)

for x in range(0, 10) :
    print(x, " ", end="")

for x in [2 ,4 ,8] :
    print(x, " ", end="")

#while loops are normal
#break used to exit loops
#no braces {} just newlines

#functions
def addNum(num1, num2) :
    return num1 + num2

print(addNum(5, 2))


print("Name: ")
in_name = sys.stdin.readline()
print("Hi ", in_name)

#String are like arrays
#in line conatanation is like in c++ %(Var inital) eg %s(string) %d(double)

test_file = open("./test.txt", "wb")
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Written from Python", "UTF-8"))

test_file.close();

test_file = open("./test.txt", "r+")

print(test_file.read())
test_file.close()

#os.remove("test.txt")
#print("test.txt is deleated")

#Classes exist
#self is this. in Java

class C:
    __a = "AAAAAAAAaa" #__ Means its private

    def get_a(self) :
        return self.__a

class_var = C()
print("Class C: ", class_var.get_a())

#Inheratance (extends)
class CC(C):
    def get_string(self):
        return "StRiNg"

class_class = CC()
print("Class CC: ", class_class.get_a())
print("Class CC: ", class_class.get_string())




