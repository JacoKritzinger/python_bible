# number = 1

# while number <= 1500:
# 	if number % 2 == 0:
# 		print(number)
# 	number = number + 1

L = []
while len(L) < 5:
	new_name = input("please add a new name: ").strip().capitalize()
	L.append(new_name)

print("sorry list is full!")
print(L)