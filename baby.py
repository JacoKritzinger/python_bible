from random import choice


questions = ["Why is the sky blue?","Why is there a face on the moon?","Where are all the dinosaurs?"]

questions = choice(questions)
answer = imput(questions).lower()

while answer != "just because":
	answer = input("why?").strip().lower()

print("Oh...Okay")
