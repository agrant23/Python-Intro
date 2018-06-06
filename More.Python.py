
'''
Exceptions  : there are types of error that can crash your program. These possible errors are handled by Exceptions
'''

try:													#Whatever code could cause an error goes in the try block							
	print (0/0)
except ZeroDivisionError:								#There are specific Exception error codes for python ZeroDivisionError is one for python: for a list of Exception errors check out https://docs.python.org/3/library/exceptions.html
	print ("this gives us infinity and that is bad")	#You can write any message here that will show when the specific error occurs


'''
more on functions
'''

def quadruple(x):
	return x*4

def assign_func(f):			#python functions are first-class, meaning we can assign them to variables and pass them into functions just like any other argument
	return f(3)				#this line calls function f with 1 as it's argument

my_quad = quadruple			#setting the function quadruple to a new variable my_quadruple; exhibiting first-class
y = assign_func(my_quad)	#here I put the quadruple function into the assign_func; exhibiting first-class

print(y)					#assign_func assigned the value 3 to the quadruple function hence we get twelve

#lambdas

z = assign_func(lambda a: a + 6)	#lambda expressions or anonymous functions are not bound to an identifier, they are short and easy to create
									#here I used a lambda function as the argument for the assign_function which assigns a to be 3 so we get out a 9
print(z,"\n")

#default arguments for functions

def arithmetic(x=0,y=0):				#by defining the variables to zero python doesn't require an x and y value to be placed into the argument since it's default is now 0
	return x+5*y						#the default output will be 0 as seen below
	
print(arithmetic())

print(arithmetic(6,3))

print(arithmetic(6))

print(arithmetic(x=6),"\n")					#sometimes it is useful to name the argument notice this is the same as the output one line above

'''
More on Lists
'''
list_range = range(25)							#range creates a list from 0 to 24 as shown in the print loop for list

for i in list_range:
	print(list_range[i], " ", end="")				#notice I can shorten this code by using just i instead of list[i]

heterogeneous_list = ["String", False, 5, 3.2 ]	#As shown in the last lesson a list can have multiple data types including a Boolean value which is true or false

print('\n',True in heterogeneous_list)		#the in operator outputs a boolean value since there is no True in the heterogeneous_list then it outputs a fals

print(False in heterogeneous_list)

print(26 in list_range)							#the in operator can be used on all data types; also this kind of conditional statement does not have to be within the print function

list2 = [30,40,45]

list2.extend([50,51,53,1001])				#extend is used when you want to extend to a previous list, this is similar to append but append will only add one value at a time while extend can do multiple

print(list2)

print(len(list2))							#len(list) gives the length of the list

a,b,c=[20,30,45]							#unpacking lists can be useful; this list with three elements are assigned to three different variables. You will get a ValueError if you don't have the same number of elements on both sides

print(a)

print(b)

print(c)

_,b,_=[20,30,45]							#using an underscore will "throw away" a value; the default for the _ is the last element of a list though we don't care about it

print(_)

print(b)

print(_)

'''
More on Tuples
'''

dif_var_Tuple = ('string',True,2.5)

try:										#Here is an exception to handle the case where we cannot modify a tuple
	dif_var_Tuple[1]=False
except TypeError:
	print("cannot change a tuple")
	
#Using tuples in a function

def divide_subtract(x,y):					#here we utilize a tuple (x,y) in this function; technically I should write an exception to handle the case if x=0 and y=0
	return(x/y),(x-y)						#it returns a tuple as well
	
ds = divide_subtract(30,5)					#this is a single variable assigned to represent the tuple returned from the function

print(ds)

d,s = divide_subtract(30,5)					#this creates two separate variables to represent each element of the tuple

print(d)

print(s)

#Tuples and lists can be used for Multiple assignment

e,f = 'one','two'
e,f = f,e									#this switches the values for e and f

print(e,f)



new_dict1 = {}

for key, value in health_data:
	new_dict1.setdefault("Tim","no Tim here")

print(new_dict1)

new_dict2 = {}

for k in health_data:
	new_dict2.setdefault("Tony","no Tim here")

print(new_dict2)






