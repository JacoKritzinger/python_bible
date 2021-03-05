students={
	"Male":["Tom","Charlie","Harry","Frank"],
	"Female":["Sarah","Huda","Samantha","Emily","Elizabith"]
	}

for key in students.keys():
	for name in students[key]:
		if "a" in name:
			print(name)

