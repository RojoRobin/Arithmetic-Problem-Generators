import random
import math
a = random.randrange(1,5,1)
b = random.randrange(-15,15,3)
c = random.randrange(-25,25,1)

def checkReal(a,b,c):
	if b**2-4*a*c >=0 :
		x1= (-b + math.sqrt(b**2-4*a*c))/(2*a)
		x2= (-b - math.sqrt(b**2-4*a*c))/(2*a)

		h.write(f' {a}x^2 + {b}x + {c} = 0')
		h.write("\n\n\n")

		j.write(f' {a}x^2 + {b}x + {c} = 0 :     {x1} & {x2}')
		j.write("\n\n\n")
	else:
		a = random.randrange(1,5,1)
		b = random.randrange(-15,15,3)
		c = random.randrange(-25,25,1)
		checkReal(a,b,c)
with open("quadraticPractice.txt", "w") as h:
	with open("quadratic_AnswerKey.txt", "w") as j:
		for i in range(1,20):
			a = random.randrange(1,5,1)
			b = random.randrange(-15,15,3)
			c = random.randrange(-25,25,1)
			checkReal(a,b,c)
