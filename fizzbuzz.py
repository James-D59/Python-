#Clear the Screen
import os
os.system("clear")




count = 1
while (count <= 100):
	if(count % 3 ==0) and (count % 5 == 0):
		print(f"{count}. FIZZBUZZ!!!")
	elif (count % 3 ==0):
		print(f"{count}. FIZZ!!!")
	elif (count % 5 == 0):
		print(f"{count}. BUZZ!!!")
	else:
		print(f'{count}.')
	count +=1