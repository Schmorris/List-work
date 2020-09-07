numbers = []
while True:
	try:
		while True:
			total = 0
			count = 0 
			line = (input('Enter a number: '))
			
			if line == 'done':
				for itervar in numbers:
					count = count + 1
				print('Count: ', count)
				for itervar in numbers:
					total = total + itervar
				print('Total: ', total) 
				if count == 0:
					break
				for itervar in numbers:
					average = total / count 
				print('Average: ', average)
				break

				
			for i in range(True):
				numbers.append(float(line))
			print(numbers)

		print('Done!')
		break

	except:
		print('Invalid Input')