import random
print("***Rock, Paper, Scissors***")

counter_human = 0
counter_comp = 0


def returnf():
	choice = input("Enter your element: ")
		#print(choise, "\n")
	if choice == 'q' or choice == 'Q':
		print("\n", "Computer: ", counter_comp, "You: ", counter_human)
		raise SystemExit()
	if choice == 'paper' or choice == 'rock' or choice == 'scissors':
	
		ch_arrey = ('rock', 'paper', 'scissors')
		def comp_step():
			global counter_human
			global counter_comp
			decision = random.choice(ch_arrey)
			print("Comp: ", decision)
			
			if choice == 'rock' and decision == 'paper':
				print("You loose!")
				counter_comp += 1
			elif choice == 'rock' and decision == 'scissors':
				print("You WIN!")
				counter_human += 1
			elif choice == 'paper' and decision == 'rock':
				print("You WIN!")
				counter_human += 1
			elif choice == 'paper' and decision == 'scissors':
			 	print("You loose!")
			 	counter_comp += 1
			elif choice == 'scissors' and decision == 'rock':
				print("You loose!")
				counter_comp += 1
			elif choice == "scissors" and decision == "paper":
				print("You WIN!")
				counter_human += 1

			if decision == choice:
				print("ooops, is's draw! ", '\n')
			return returnf()
	else:
		print("Please input the correct figure! ")
		return returnf()


	comp_step()
returnf()



#x = input()

# if not x != 'rock' or not x != 'paper':
# 	print("true")
# else:
# 	print("false")








	# b = []
	# c = []
	# def counter(n):
	# 	if n == 0:
	# 		return 1
	# 	else: 
	# 		b.append(int(num_array[n-1]) % 10)
	# 		c.append(int(num_array[n-1]) // 10)
	# 	counter(n-1)
	# counter(n=len(num_array))

	# def SB(a, d):
	# 	with open('result.txt', 'a', encoding='UTF-8') as out:
	# 		if a < d:
	# 			print(a, 'is smaller than', d, file=out)
	# 		elif a > d:
	# 			print(a, "si bigger than", d, file=out)
	# 		else:
	# 			print(a, "is equaly", d, file=out)
	# def sUmmer():
	# 	a = 0
	# 	d = 0
	# 	for i in b:
	# 		a += i
	# 	for j in c:
	# 	 	d += j
	# 	SB(a, d)
	# sUmmer()
	

		








	# summa = 0
	# summa_2 = 0
	# for i in num_array: #конвертация массива в int  #
	# 	s = int(i)                                    #
	# 	#s = s*2                                      #
	# 	if s <= 0:
	# 		print(s, "Invalid operation!")
	# 		break
	# 	elif s > 0 and s < 10:
	# 		print("s > 0 and < 10!")
	# 	elif s >= 10:
	# 		test_num = s%10
	# 		#summa = 0
	# 		summa += test_num
	# 		test_num_2 = s//10
	# 		#summa_2 = 0
	# 		summa_2 += test_num_2
	# 	print(summa, "-----", summa_2)
	# 		#a = input()
	# if summa < summa_2:
	# 	print(summa, "is smaller than", summa_2)
	# elif summa > summa_2:
	# 	print(summa, "is bigger than", summa_2)
	# else:
	# 	print("Arguments is equaly!")


	# 	print(type(s), s)
	


	# test = int(input("Input: "))
	# if test >= 10:
	# 	test_num = test % 10
	# 	summa = 0 
	# 	summa += test
	# 	test_num_2 = test//10
	# 	if test_num == test_num_2:
	# 		print("arguments are valid!")
	# 	elif test_num < test_num_2:
	# 		print("First argument is bigger")
	# 	else:
	# 		print("Second argument is bigger")


	#print(list(num_array))
	# while num_array != 0:
	# 	for i in num_array:
	# 		first_el = num_array[i]
	# 		if num_array 
	#print(type(num_array)
					#ls = [int(s) for s in num_array.split()]
					#print(ls)