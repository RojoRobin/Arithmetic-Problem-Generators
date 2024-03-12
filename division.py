import random
myProblems=[1,2,3,4,5,6,7,8,9,10,11,12]
with open("divisionPractice.txt", "w") as h:
	with open("division_AnswerKey.txt", "w") as j:
		for i in range(1,20):
			x = random.randrange(20,100,1)
			y = random.randrange(1,20,1)
			answerQuotient = x / y
			#print(f' {x} / {y} = {answerQuotient}')
			h.write(f' {x} / {y} = ___')
			h.write("\n")
			h.write("\n")
			h.write("\n")
			j.write(f' {x} / {y} = {answerQuotient}')
			j.write("\n")
			j.write("\n")
			j.write("\n")
