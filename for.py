# for number in range(1,11,2):
# 	print(number) 


vowels = 0
consonants = 0

for letter in "Hello":
	if letter.lower() in "aeiou":
		vowels = vowels + 1
	elif letter == "":
		pass
	else:
		consonantd = consonants + 1 

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))