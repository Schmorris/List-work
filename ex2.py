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
					print('Max value: 0\nMin value: 0')
					break
				for itervar in numbers:
					max_value = max(numbers)
					min_value = min(numbers)
				print('Max value: ', max_value, '\nMin value: ', min_value)
				break

				
			for i in range(True):
				numbers.append(float(line))
			print(numbers)

		print('Done!')
		break

	except:
		print('Invalid Input')