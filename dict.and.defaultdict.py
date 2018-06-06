from collections import Counter, defaultdict

'''
Counter: We want to count how many times something occurred, or how many times one element in a list showed itself, we will use Counter later on
'''

keep_track = Counter([5,3,8,7,4,6,9,8,5,1,3,6,4,5])

print((keep_track),'\n')

print(sorted(keep_track.items()),'\n')				#different ways to format your output


'''
More on Dictionaries: In dictionaries we can use lists as values but the keys are immutable and cannot use lists as keys. We can use tuples as a key but it is better to use a string as a key instead
'''

health_data ={ "Mike": 100, "Sue":130,"George":145}

try:												#without creating this try catch the program would crash and say KeyError: 'Tony' since there is no key Tony in the health_data dictionary
	Tonys_blood_pressure = health_data["Tony"]
except KeyError:
	print("no blood pressure for Tony")

health_data["Tony"] = 95							#adds another key and value to the dictionary

print(health_data)

B = "Sue" in health_data							#the in keyword can be used in dictionaries as well

print(B,'\n')



'''
Lets group some items in a dictionary: When we have a list of tuples with multiple values associated with the same key we can create a list of values with the same key in a dictionary
'''
data = [ ("Mike", 100), ("Sue",130),("George",145),('Tony',95),("Mike", 120), ("Sue",120),('Tony',90), ("Sue",85),("George",100)] #So this list has paired tuples within it as you can see

new = {}											#the new dictionary that is initially empy
for key,value in data:								
	if key in new:									#since the for loop iterates through all values and keys for the first iteration there is no key but later this will change 
		new[key].append(value)						#creates the key in the new dictionary and appends the value to the list
	else:
		new[key] = [value]							#if the new key is not in the data creates the new key in the dictionary and the new value associated with it

		
print(new,'\n')

'''
setdefault(key[, "default"]): if key is in the dictionary, return its value. if not, insert key with a value of "default" and return "default". "default" defaults to None

setdefault() is a built in type so there is no need to import anything, lets use it. NOTE: we can index dictionaries with strings but we can not index lists with strings
'''

new_d = {}

for i, j in data:									#here i "represents" key and j "represents" value. This is more common notation than previous
	new_d.setdefault(i,[]).append(j)				#I'm using set default's functionality to replace the if else statement in the previous example. If the key is in the data is just appends the value; if it's not it creates a list and appends the value
	
print(new_d,'\n')	

'''
I will do this again with a module function but first I want to introduce it using it another way
defaultdict: if we want to count the number of letters in a word the defaultdict from the collections module is very useful. 
'''

word = 'illinois'
letters_count = defaultdict(int)					#the object letters_count creates a dictionary (defaultdict(int)) that keeps an int count of different letters. We call the int argument the default_factory
for l in word:										#for letters l in word illinois
    letters_count[l] += 1							#we increment up one integer of the dictionary created above for each letter counted and defaultdict automatically keeps track of the number of letters that are the same

print(sorted(letters_count.items()),'\n')			#sorting the items in the dictionary


#now we will use defaultdict(list) with list as the default_factory. Now it can hold lists instead of just integers within it.

new_dd = defaultdict(list)

for (x,y) in data:
	new_dd[x].append(y)

print(new_dd,'\n')

'''
Using defaultdict(list) we count the number of times the same "word" occured in a file. In the same folder you downloaded this python file download a large text file with saved as document.txt
'''	


txt = open("document.txt").read()					#first lets get a document to read. We need the body in the variable created to use it later. Using .read() is needed to "store" the text into the variable
cnt = Counter(txt.split())									#this object is used to automatically split the file into separate words. The default for split() is a white space. If I wanted to split by a comma I would use split(",")

print(cnt,'\n')										#this has already done the majoity of the work, it has counted the frequency of a word, this is given as a dictionary. Without Counter() it would be a list of words
													
freqword = defaultdict(list)						#this object represents the defaultdict

#print(txt)											#uncomment and run to see the whole document				

for word, freq in cnt.items():						#the cnt.items() is going through the entire document (txt) of it's each split item
	freqword[freq].append(word)						#here the string word can iterate through the defaultdict and apppend into the list of defaultdict while freq is counting the frequency of words due to cnt
	
for freq in sorted(freqword):						#to format the dictionary we must iterate through each item
	print('count {}: {}' .format(freq, sorted(freqword[freq])),'\n')

print(sorted(freqword.items()),'\n')				#Another way to format the output and reformat the dictionary

print(Counter(txt.split()),'\n')					#if we wanted to count the occurrence of each word without utilizing the defaultdict(list); not if we didn't use split it would count each letter and other notations

print(cnt.most_common(5),'\n')						#Counter instance has a most_common(int) method, shown here
