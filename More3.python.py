'''
Sets: for sets using the keyword in is very fast on sets, a set is more appropriate than a list when we want to see what unique values are in it
'''

new_set = set()

new_set.add("first value")

new_set.add(2)

new_set.add(2)									#sets only add unique values, so this does included in the new_set

new_set.add(4.5)

print(new_set)


'''
lets try taking away all commas and periods from a document and load this stripped document into a list
'''


txt = open("document.txt").read()

spt = txt.split()								#this splits the txt and formats it as list elements

word_list = []

for i in spt:									#i iterates through each spt, if we used txt instead of spt here we would iterate through each letter of the document
	if i.endswith(','):							#method is self explanatory, endswilt() is a built in method
		w=i.rstrip(',')							#must create a new element to load the striped "word" into it
		word_list.append(w)						#and append the new element to the new list
	elif i.endswith('.'):
		w=i.rstrip('.')
		word_list.append(w)
	else:
		word_list.append(i)
	
print(word_list)


#another way, that doesn't currently work.... he he

# with open('document.txt', 'r') as f:
    # word_list = [line.rstrip(',') for line in f]

print(len(word_list))	

'''
Using previous code blocks we have done I can take this "cleaned" file to sort and count the words

Lets do some other basics instead
'''

print('giraffe' in word_list)					#Lets see if giraffe is a word in the document. Whoops this only checks the first word of the document

bool_list = []									#playing with this python code is highly recommended for example below chang 'A' to anything else to see it work differently

for j in range(0,len(word_list)): 				#using range(0,len(word_list)) makes j an integer, this is needed since lists can not iterate with strings
	bool_list.append('A' in word_list[j])		#this creates a boolean list where any time a capital A apears in a word the list holds a true, every other time it's a false.

print("\n")	
print(sum(bool_list))							#Since the boolean TRUE value is equivalent to integer 1 and FALSE is 0 we can simple sum the boolean list to count the number of times TRUE appeares

for j in enumerate(word_list):					#how enumerate works
	print(j)

print("total word count: ",len(word_list))							#if we just want the word count

