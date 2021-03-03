films = {
	"Finding Dory":[3,5],
	"Bourne":[18,5],
	"Tarzan":[15,5],
	"Ghost Busters":[12,5]
	}
while True:
	choice = input("Waht film do you like to watch?: ").strip().title()

	if chose in films:
		age = input("How old are you?: ").strip()

		#check user age

		if age >= films[choice][0]:
			#check if there is enough seats

			num_seats = films[choise][1]

			if num_seats >= 0:
				print("Enjoy the film!")
				films[choise][1] - 1
			else:
				print("Sorry, we are sold out!")

		else:
			print("You are to young to watch the film!")

