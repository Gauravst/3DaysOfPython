class Task:

	def __init__(self, description, priority):
		self.description = description
		self.priority = priority

	def __str__(self):
		return f"{self.description},{self.priority}"

def menu():
	while True:

		print("\n Main Menu :- \n")
		print("1) Show Task")
		print("2) New Task")
		x = int(input())

		match x:
			case 1:
				loadTask()
			case 2:
				task = newTask()
				saveTask(task)
		print("\n")

def loadTask():

	with open("db.txt", "r") as file:
		for index, line in enumerate(file, start = 1):
			d, p = line.split(",")
			print(f"{index}) {d} - {p}")
		
def saveTask(task):

	with open("db.txt", "a") as file:
		file.write(str(task) + "\n")
	print("saved")

def newTask():

	a = input("Write Your Task... \n")
	print("Chose your priority :- ")
	print("1) High")
	print("2) Medium")
	print("3) Low")

	b = int(input())

	match b:
		case 1:
			b = "High"
		
		case 2:
			b = "Medium"
		
		case 3:
			b = "Low"
		case _:
			b = "Normal"

	return Task(a,b)

def main():
	menu()

if __name__ == "__main__":
	main()