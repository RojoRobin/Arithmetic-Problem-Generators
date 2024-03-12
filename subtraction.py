import random
myProblems=[1,2,3,4,5,6,7,8,9,10,11,12]
with open("subtraction_Practice.txt", "w") as h:
	with open("subtraction_AnswerKey.txt", "w") as j:
		for i in range(1,20):
			x = random.randrange(1,100,1)
			y = random.randrange(1,100,1)
			answerDiff = x - y
			#print(f' {x} - {y} = {answerDiff}')
			h.write(f' {x} - {y} = ___')
			h.write("\n")
			h.write("\n")
			h.write("\n")
			j.write(f' {x} - {y} = {answerDiff}')
			j.write("\n")
			j.write("\n")
			j.write("\n")

