											#this hasthag # symbol starts a comment, comments do not affect the code at all, they exist so coders can comment to anyone who would be looking at the code
import random 								#import modules which provides specialty functions, this provides random numbers
import sys									#system specific module; access to some variables and functions
import os									#operating system; provides a portable way of using operating system dependent functionality

print ("Hello World")						#printing, pretty easy

'''
Anther way to create comment other than # by using these three ' before and after a comment 
'''

name = "Tony"										#How to create a string variable

print(name)											#How to print another way

name2 = "Grant"										#variable must start with a letter but then a number and/or _ can follow

print(name + " " + name2)

'''
the five main types of variables in Python
Numbers, Strings, Lists, Tuples, Dictionaries

+ - * / % ** //   these are the 7 main types of arithmetic operators
+ - * / these are self explanatory
% modulus returns the remainder of dividing two numbers
** exponential
// performs a division and discards the remainder 7.5 rounds to 7
'''

print("3+11 =", 3+11)								#Order of operation matters, use braces when needed
print("3-11 =", 3-11)								#inside the quotes is just what is printed, python is doing the actual calculations to the right of the comma
print("5*3 =", 5*3)
print("7/4 =", 7/4)
print("7%4 =", 7%4)
print("3**4 =", 3**4)
print("7//4 =", 7//4)
print("(5+5)/2//2 =", (5+5)/2//2)
print("(5+5)/(2//2) =", (5+5)/(2//2))

quote = '\"To create a quote in a string\"'  		#we use \",  also notice a string can be created using double or single quothes

print(quote+" 1")									#I am including the 1, and numbers for future print outs, so you can keep track of which out put is which

multi_line_quote = ''' just 
like everyone else'''								#use multi line string, when you want to have the output on different lines


new_string = quote + multi_line_quote

print(new_string+" 2")
print()												#adds a blank line

print("%s %s %s" %('I like the quote', quote, multi_line_quote)+" 3")	# the %s is a format specifier for a string, which is a string of characters; "%s %s %s" identifies the three expressions in the parenthesis are strings
print('\n' *2)															#also a way to add line is '\n' and the *2 adds two new lines

print("I don't like ", end="")						# the end= formats code to connect two prints statements as seen here with the output.
print("newlines" " 4")
print('\n'*3)

'''
Lists:  lists are mutable
'''
print('Lists','\n')

my_list = ['item1', 'string2', 'anyvariable','yep']	#lists use square brackets and can have any type of variable in a list

keep_order_list = [" 7"," 8"," 9"," 10"," 11"," 12", " 13", " 14", " 15", " 16"," 17"," 18"," 19"," 20"," 21"]   #to help you see what output is with which input


print('first entry', my_list[0]+" 5")				#notice the index for lists starts at 0
print('fourth entry', my_list[3]+" 6",'\n')			#so fourth entry is at index 3

my_list[1]= "differentString"						#to change a value in a list

print("my_list ", end="")
print(my_list, keep_order_list[0],'\n')				#can only concatenate lists not strings so I can't add my usual +" 7" String with this here
															#0 is 7, you will see why this is important with the output.
print(my_list[1:3], keep_order_list[1],'\n')		#chooses items 2 through 4
															#1 is 8
second_list = [5.4,'learning python is fun','byork']

combining_list = [my_list,second_list]				#here we have 2 lists inside of a list

print("combining_list ", end="")
print(combining_list, keep_order_list[2],'\n')				#2 is 9

print((combining_list[1][2]), keep_order_list[3]) 	#the 1 chooses the second list, a zero would choose the first 									
													#the 2 chooses the third item in the second list
second_list.append('was allright')					#appends an entry onto the end of second list
print(second_list,keep_order_list[4])				#can see append puts string at end of list and updates combining_list
															#4 is 11
my_list.insert(2,"inserted")						#insert at index 2 or string 3
print(my_list, keep_order_list[5])							

second_list.remove("learning python is fun")
print(combining_list, keep_order_list[6])					#6 is 13

my_list.sort()
print(my_list, keep_order_list[7])					#sorts by alphabetical order or smallest number to larges, can only do to a list of just strings or just numbers 

second_list.reverse()								#sorts in reverse alphabetical order, can do with numbers and strings
print(second_list, keep_order_list[8])						#8 is 15

del my_list[0]
print(combining_list,keep_order_list[9])		

my_third_list = ['one','two','three','four']
second_combining_list = my_list+my_third_list		#another way to combine lists
print(second_combining_list, keep_order_list[10])			#10 is 17
print(len(second_combining_list))					#len counts number of entries in list or its lenght
print(max(second_combining_list))					#last value in alphabet in list
print(min(second_combining_list),'\n'*2)			#first value in alphabet in list

'''
tuples, when you don't want to change a value we use tuples
'''
print('Tuples','\n')

first_tuple = (1,2,3,4,5,6,7)

a_list = list(first_tuple)							#tuple is now a list

a_tuple = tuple(a_list)								#now it's back to a tuple

print(len(first_tuple))								#self describing
print(min(first_tuple), '\n'*2)

'''
dictionaries and maps: A dictionary maps it's key to the keys value.  for dictionaries I can't join them together like I can with lists by using the + sign 
'''
print('Dictionaries','\n')

first_dictionary = {'alpha' : 'A', 'beta' : 'B', 'gama' : 'G', 'delta' : 'D'}	#notice dictionary has a first value called keys and another value associated with the key

print(first_dictionary['alpha']+" "+first_dictionary['delta'])	#to print two values, key beta associated with B and key Delta associated with D

del first_dictionary['gama']				
first_dictionary['alpha']= 'Hi There'				#replace alpha with Hi There, can only replace by using a key, if we introduce a new value, dictornary[new_value] = 'replace', this appends the dictionary
print(len(first_dictionary))						#finds length of dictionary
print(first_dictionary.get("alpha"))				#using get will get that value
print(first_dictionary.keys())						
print(first_dictionary.values(), '\n'*2)			#note if we used print(first_dictionary.values) where values lacked the () it would output the memory location of values

'''
conditionals; if, else, elif (means else if) for == (same elements) != (not same) > (greater than) < (less than) >= (greater than or equal) <= (less than or equal) 
'''
print("Conditions",'\n')

age = 21											#play with these numbers to see how the conditions work

if age >= 21 :
	print('You can drink booze')
else:
	print('You can not drink')

age2 = 23

if age2>= 21:
	print('You can drink')
elif age2 >= 16:
	print('You can drive but not drink')
else : print("you are not old enough to drive")	

#combine conditions using logical operators (and, or, not)

age3 = 50

if((age3>=1) and (age3 <= 18)):
	print("you are not able to vote")
elif( (age3>18)or (age3 >= 65)):
	print("you should be working")
elif not(age3==100):
	print("you are not exactly a century old")
else:
	print("you are able to retire",'\n'*2)
'''
looping, perform an actions for a set number of times;  for loop;  while loop
'''
print("Loops",'\n'*2)

for n in range(0,10):								#for loop to output range 0 to 9, loop iterates through values
	print(n, ' ', end="")							#take end out and see what the code does

print('\n'*2)
	
for y in my_list:									#using for loop to print a list
	print(y)

print('\n')	
	
for x in [2,4,5,8,10]:
	print(x, ' ',end="")

print('\n')	

num_list = [[1,2,3],[10,20,30],[100,200,300]]		#this is a 2 dimensional list, comparative to a 2-D array or a list with lists inside of it 												
													#double up for loop to cycle through a 2-D list, 2-D list iterations look like num_list[x][y]=[[x=0 y=0,x=0 y=1,x=0 y=2],[x=1 y=0,x=1 y=1,x=1 y=2],[x=2 y=0,x=2 y=1,x=2 y=2]]
for x in range(0,3):								#this flows through each different list
	for y in range(0,3):							#this flows through each different element in the list
		print(num_list[x][y])						#you can see here num_list[x][y] is 2-D where a_list[i] is 1-D

#use a while loop when we have no idea how many times we need to iterate a loop

random_num = random.randrange(0,100)				#a random number between 0 to 99

while(random_num !=15):								#while a random number is not 15 the loop iterates
	print(random_num, ' ',end="")					#we print the random number each time
	random_num = random.randrange(0,100)			#we change the random number each time, so this loop ends when it hits 15

i = 0;												#create an iterator for a while loop

while(i <=20):										#while i is less than or equall to 20
	if(i%2 == 0):									#if the iterator is an even number,   recall how modulus works
		print(i)									#print the iterator
	elif(i == 9):									#if we want to change it to printing up to 9, this just a way to show how to use elif in our while loop 
		break										#this command ends the loop and in this case when the iterator gets to 9
	else:											#for all other possibilities in these conditions, is what else means 
		i +=1										#this iterates up, shorthand for i = i+1
		continue									#when there is an odd iterator the continue command brings it back up to the beginning of the loop 
	i +=1											#need this to iterate up for the odd iteration...............try deleting some of this loop to see how it effects it, or test this yourself

print("\n")											

'''
functions
'''
print("Functions",'\n')

def addNumber(fNum, lNum):							#define a function  addNumber(firstNumber, lastNumber)
	sumNum = fNum + lNum							#just adds two numbers for this function
	return sumNum

print(addNumber(2,10))								#can not use sumNum in the print statement because it doesn't exist outside of the function out of scope, this is a very handy tool actually

print('What numbers do you want to enter in')

#name_string = sys.stdin.readline()					#to get input from the user; we are using our import sys; stdin.readline() is standard in read line, reads input until enter is hit; but we don't use this here

#x = int(input('enter first number \n'))				#another way to input is to use input("output message"), this alone creates a string variable but encasing it in the int() converts the input value to and integer

#y = int(input('enter last number \n'))


print(addNumber(x,y))

'''
more on String
'''
print("More on Strings",'\n')

var_string = "Here is a very very long String"
		
print(var_string[0:11])							#Prints first 11 characters, starts at index  0 end one before 11

print(var_string[-7:])							#Starting at end prints string characters to left until just before 7

print(var_string[7:])							#cuts off 7 characters starting from beginning

print(var_string[:-7])							#cuts off 7 characters from the end

print(var_string[:7])							#prints first seven characters from beginning

print(var_string[:10]+"new concatenated string")

print("%c is my %s letter and my number %d number is %.5f"%		#%c for character, %s for string, %d for integer, %.5f for a decimal with 5 places past the decimal point. And
('X',"favorite",1,.14))											#from output you can see how each data entry was placed in with these variable types. This shows a formating standard that in the future we will put variables in the place of those data entries

var_string2 = "are you having fun?"

print(var_string2.capitalize())					#capitalizes first letter of string

print(var_string2.find("Having"))				#returns the index of the start of the string, case sensitive, has to be exactly the same

print(var_string2.isalpha())					#returns true if the string is all letters

print(var_string2.isalnum())					#returns true if the string is all numbers
	
print(len(var_string2))							#returns the length of the string

print(var_string2.replace("fun","hate"))		#replaces fun with hate

print(var_string2.strip())						#strips all white space from a string, if there was spaces before or after the string it would be removed

string_to_list=[var_string]						#recall how to create a list, if we want the entire var_string to be one element of a list we can do this

print(string_to_list)

string_to_list_spliting_string = var_string.split(" ")	#splitting the string to a list based on the space delimiter; so in this case each seperate word is an element in this list string_to_list_spliting_string

print(string_to_list_spliting_string,"\n"*2)			#recall how mutable a list is, this is a useful tool

'''
File input and outputs I/O
'''
print("File I/O\n")
												#file modes: wb write to, r only read, w only writing, a opens the file for appending, r+ opens the file for both reading and writing, in windows b appended opens the file in binary mode,
file_name = open("file.txt","wb")				#creates or opens a file called file_name; to write to this file use wb as command. This is the file mode. We could use ab+ to read and append to file
												#now check the folder (or directory) where you saved this python file you are reading FirstPythonLesson.py and hopefully you will see the text file file.txt. At this point it is blank

print(file_name.mode)							#returns the file mode used

print(file_name.name)							#returns the file name

file_name.write(bytes("this is written into the file called file_name\n", 'UTF-8'))	#writes into the file

file_name.close()								#need to close file to reopen it in a different mode

file_name = open("file.txt","r+")				#open in read and write

body_of_file = file_name.read()					#pulls text from file into variable body_of_file

print(body_of_file)								

#os.remove("file_name")							#If I wanted to delete file I would do this. Utilizing the os module 


file_name.close()								
'''
Classes and Objects:	Object Oriented Programs (OOP) use objects/Classes that can hold large amounts of different types of data, that can perform multiple types of object functions to be used as a nice powerful 'package' called an object
														The class is like the blueprint of an object. When we use a class to create an object we call that instantiating a class which also means creating an object. 
														Below you will see me create a class, then see me instantiate an object of that class. 
'''														
print("Classes and Objects")

class ClassName:								#class keyword designates we are creating a.... class and ClassName (notice it's capital) can be any class name and should briefly summarize what the class is for.
												#the __ designates a private variable. private variables are associated with the class only. We need to create functions in the class to access private variable outside of the class. All variables we have created so far are public variables which can be accessed and changed anywhere
	__var1 = None								#Notice this is indented, this is important to tell the compiler that it is part of the class. Everything written after class ClassName: is part of this class. None is equivalent to Null, meaning there is no value with the variable yet and this is needed.
	__var2 = None								
	__size = None								
	__temp = None
												#We call this the constructor: def means define, init means initialization or initialize. The self keyword always refers to the newly created object. So when this class is instantiated these variables will refer to the value assigned to them at the instantiation . In other languages self is equivalent to this
	def __init__(self, var1,var2,size,temp):		#the constructor sets up or initializes the variables of the class. In this case the initialization will be given during instantiation of the class (or when the classes object is created)
		self.__var1 = var1						#all variable Must be passed into the constructor
		self.__var2 = var2
		self.__size = size
		self.__temp = temp

	def set_var1(self, var1):				#this is called a setter function which allows us to set the value of the variable outside of the class. A more correct way to say this is the setter function changes the object of the class. Self it allows the object to refer to itself
		self.__var1=var1
	
	def get_var1(self):						#getter function, lets us get the value of the variable from the object. since the variable is private to this we need to use this function outside of the class to get it outside of the class....I know that was redundant.... but it's all true
		return self.__var1					#using private variables which forces us to create these getter and setter functions is called encapsulation. Since we are forcing the data of a class to not be seen outside of it (through private) it encapsulates the class's information; which is good for security purposes.
		
	def set_var2(self, var2):				#setters allows us, again outside of the class, to ensure the variable is valid, since var2 is indicated to be a string (from initialization None) then when the setter is used if var2 is not a String python will say, hold on a minute that's not right. And the same goes with numbers		
		self.__var2=var2
		
	def get_var2(self):						
		return self.__var2
		
	def set_size(self, size):				
		self.__size=size
		
	def get_size(self):		
		return self.__size
			
	def set_temp(self, temp):				
		self.__temp=temp
	
	def get_temp(self):		
		return self.__temp
		
	def get_type(self):						#this can be used later to see what the class is
		print("ClassName")
		
	def toString(self):						#This specific function toString is used to format data. It automatically formats the data when using an object, for this example we are formatting all the data but it does not have to do this 					
		return "{} is variable 1 {} is variable 2 {} cm {} Fahrenheit".format(self.__var1,self.__var2,self.__size,self.__temp) 						#for python {} represents where we want information to go. Since we are inside of the class don't need to use getters and setters. But outside we will
		
		

object1 = ClassName('value of var1','string value of var2',5,98)		#This is creating the object called object1 from class ClassName. Inside the parenthesis I am initializing the variables. So this is a unique object of the class I created.

print(object1.get_type())

print(object1.toString())						#notice how I formatted the use of the function (sometimes called a method) toString that was defined in my class. This is how an object is utilized.

object1.set_size(20)

print(object1.toString())




		
			#return "{} is variable 1 {} is variable 2 {} cm {} Fahrenheit".format(self.get_var1(),self.get_var2(),self.get_size(),self.get_temp(),self.__owner)