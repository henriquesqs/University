# Virtual calculator program (this calculator cant do math operations with negative numbers)
# Made by Henrique de Souza Q. dos Santos, Paulo H. da Silva and Witor M. A. de Oliveira
# N. USP of everyone in sequence: 10819029, 10734515 and 10692190
# 2019, USP Sao Carlos

.macro done
# This macro will stop the current program execution
# after displaying an exit message
		
	la $a0, exit_msg
	li $v0, 4
	syscall
		
	li $v0,10
	syscall	
		
.end_macro	
	
.macro enterFirstNum
# This macro will be responsible to ask for 
# a integer input and them store this input in #t1

	la $a0, integer1_input						# display message from 'integer1_input'
	li $v0, 4							# charging the register with the operation 4
	syscall								# performming a syscall
		
	li $v0, 5							# waiting for user to input a number
	syscall	
	move $t1, $v0							# moving the read number to $t0
.end_macro
	
.macro enterSecondNum
# This macro will be responsible to ask for 
# a integer input and them store this input in #t2

	la $a0, integer2_input						# display message from 'integer2_input'
	li $v0, 4							# charging the register with the operation 4
	syscall								# performming a syscall
		
	li $v0, 5							# waiting for user to input a number
	syscall	
	move $t2, $v0							# moving the read number to $t2
.end_macro
	
.macro restart
# This macro will ask user if he/she wants to perform another math operation
# If the user want to, he/she must type 1 (yes)
# Otherwise, he/she must type 0 (no)
		
	la $a0, repeat_msg
	li $v0, 4
	syscall
		
	li $v0, 5
	syscall
		
	beq $v0, 1, calc
	beqz $v0, exit
	
.end_macro
	
.macro dividingByZero
# This macro will display an error message warning the user
# that he/she can't divide by zero
		
	la $a0, cantDivideZero
	li $v0, 4
	syscall
		
.end_macro
		
.macro menu
# This macro will show a menu of options and wait
# the user to choose between one of them
		
	la $a0, chooseOperation_msg					# load addres of chooseOperation_msg to register $a0
	li $v0, 4							# load immediately the syscall value (4 - print string)
	syscall								# perform the specified syscall (4) with the given argument ($a0)
		
	la $a0, show_menu						# load addres of show_menu to register $a0
	li $v0, 4							# load immediately the syscall value (4 - print string)
	syscall								# perform the specified syscall (4) with the given argument ($a0)
		
	li $v0, 5 							# waiting for user to input a integer to be stored in $v0
	syscall								# perform the specified syscall (5) with the given argument
		
.end_macro
	
.data

	# Below, each of these statements
	# creates a string with the quoted text
		
	welcome_msg: 		.asciiz "Welcome to your virtual calculator!\n"
	exit_msg:		.asciiz "\nGoodbye and thank you for using our calculator!\n"
		
	# These messages will be displayed on screen so the user can choose an operation

	show_menu: 		.asciiz "1. Sum\n2. Sub\n3. Mul\n4. Div\n5. Pow\n6. Sqrt\n7. Mul table\n8. IMC\n9. Fibonacci\n10. Fatorial\n\n0. Exit\n\nYour option: "
	chooseOperation_msg: 	.asciiz "\nChoose your operation below:\n\n"
	repeat_msg: 		.asciiz "\n\nWould you like to perform an other operation?\nType 1 for 'yes' and '0' for 'no': "
		
	# Messages of input actions
		
	integer1_input: 	.asciiz "Please, enter a number: "
	integer2_input:		.asciiz "Please, enter another number: "
	height_input:		.asciiz "Please, enter your height: "
	weight_input:		.asciiz "Please, enter your weight: "
	msg_fib1: 		.asciiz "Enter an interval to calculate fibonnaci sequence\n(the 1st number must be >= 1 and the second >= the 1st)\n"
	msg_fib2: 		.asciiz "\n'a' from [a,b]: "
	msg_fib3: 		.asciiz "'b' from [a,b]: "
	wrong_input: 		.asciiz "Wrong input! Please, enter it correctly!\n"
	cantDivideZero:		.asciiz "Error! Can't divide by zero!\n"
		
	# Operations messages
		
	result_msg: 		.asciiz "Result: "
	quotient_msg:		.asciiz "\nQuotient: "
	remainder_msg:		.asciiz "\nRemainder: "
	str_x: 			.asciiz "x"
	str_equals: 		.asciiz " = "
	str_const:	 	.asciiz "\n"
	msg_sequence:		.asciiz "\nThe sequence is: "
	
.text
.globl main

main:
	
	la $a0, welcome_msg						# load addres of welcome_msg to register $a0
	li $v0, 4							# load immediately the syscall value (4 - print string)
	syscall								# perform the specified syscall (4) with the given argument ($a0)
		
calc:
		
	menu								# calling macro 'menu' to show the options
	seq $t8, $v0, 1 
	la $t7, sumOp							# this is a block of comparisons.
	beq $t8, 1, call_function 

	seq $t8, $v0, 2
	la $t7, subOp
	beq $t8, 1, call_function					# depending on user input, we will 'jump'
	
	seq $t8, $v0, 3
	la $t7, mulOp
	beq $t8, 1, call_function					# to the correct math operation
	
	seq $t8, $v0, 4
	la $t7, divOp
	beq $t8, 1, call_function
	
	seq $t8, $v0, 5
	la $t7, powOp
	beq $t8, 1, call_function
	
	seq $t8, $v0, 6
	la $t7, sqrtOp
	beq $t8, 1, call_function
	
	seq $t8, $v0, 7
	la $t7, mulTableOp
	beq $t8, 1, call_function					# for example
									# if the user types 1 (sum operation)
	seq $t8, $v0, 8
	la $t7, imcOp
	beq $t8, 1, call_function
	
	seq $t8, $v0, 9
	la $t7, fibonacci
	beq $t8, 1, call_function
	
	seq $t8, $v0, 10
	la $t7, fatorial
	beq $t8, 1, call_function
									# the program will jump to label 'sumOp'
	j exit								# where we will provide him the requested operation
	
call_function:
	jalr $t7 									
	j calc								# if the user types 0, or other num, the program will be stopped
	
sumOp:
	
	enterFirstNum
	enterSecondNum
		
	la $a0, result_msg						# displaying 'result_msg' on screen
	li $v0, 4								
	syscall
	
	add $a0, $t1, $t2						# sum operation between the 2 gave numbers
	li $v0, 1							# charging and displaying the result in $v0
	syscall
	
	restart								# verifying if user wants to exit or repeat the process
	
subOp:
	
	enterFirstNum	
	enterSecondNum
		
	la $a0, result_msg						# displaying 'result_msg' on screen
	li $v0, 4								
	syscall
		
	sub $a0, $t1, $t2						# sub operation between the 2 gave numbers
	li $v0, 1							# charging and displaying the result in $v0
	syscall
		
	restart								# verifying if user wants to exit or repeat the process
		
mulOp:
	
	enterFirstNum
	enterSecondNum
		
	la $a0, result_msg						# displaying 'result_msg' on screen
	li $v0, 4								
	syscall
		
	mul $a0, $t1, $t2						# mul operation between the 2 gave numbers
	li $v0, 1							# charging and displaying the result in $v0
	syscall
		
	restart								# verifying if user wants to exit or repeat the process
		
divOp:
	
	enterFirstNum
		
	checking_input:							# this label is a checkpoint in case of we get an error
		
		enterSecondNum
		
		# Here we will check if user is trying to divide by zero
		# if so, show macro dividingByZero and ask him to input the number again
		# otherwise, we can go on and divide the numbers
		
		bnez $t2, correct_input					# if the divisor is =/= of 0, we can go on the operation
		dividingByZero						# otherwise, we'll show him that we can't proceed
		j checking_input					# and we'll ask him to input the number again
		
		correct_input:
		
		div $t1, $t2						# div operation between the 2 gave numbers
		
		mflo $t1						# moving the quotient to $t1
		mfhi $t2						# moving the remainder to $t2
		
		la $a0, quotient_msg
		li $v0, 4							
		syscall
		
		move $a0, $t1
		li $v0, 1						# displaying quotient of the division
		syscall
		
		la $a0, remainder_msg
		li $v0, 4
		syscall
		
		move $a0, $t2		
		li $v0, 1						# displaying remainder of the division
		syscall
		
		restart							# verifying if user wants to exit or repeat the process
		
powOp:
	
	enterFirstNum
	enterSecondNum
		
	# $t3 will store the result
	li $t3, 1							# charging t3 with initial value 1
		
	pow_loop:
		
		beq $t2, $zero, endOperation				# while t2 != 0
		mul $t3, $t3, $t1					# $t3 will store his actul value multiplied by $t2
		sub $t2, $t2, 1						# t3 = t3 * t2
		j pow_loop
		
		endOperation:
		
		la $a0, result_msg					# displaying 'result_msg' on screen
		li $v0, 4								
		syscall
		
		move $a0, $t3					
		li $v0, 1
		syscall
		
		restart
		
sqrtOp:
# For this to works, we're going to use this math
# formula to calculate the square root:
# x = (x + n / x) / 2;
# where 'x' is the result and 'n' the num to get its square root
	
	enterFirstNum	
		
	move $t0, $t1							# $t0 (x) = $t1 (n)
	li $t2, 0							# $t2 (i) = 0
		
	div $t4, $t1, 2							# $t4 = (n) / 2
		
	sqrtOp_loop:
		
		bge $t2, $t4, endSqrt
		div $t3, $t1, $t0 					# $t3 = n / x
		add $t5, $t0, $t3					# $t5 = x + (n/x)
		div $t0, $t5, 2						# x = $t5 / 2 = x+(n/x) / 2
		add $t2, $t2, 1						# i = i+1
		j sqrtOp_loop
		
		endSqrt:
			
		la $a0, result_msg					# displaying 'result_msg' on screen
		li $v0, 4								
		syscall
		
		move $a0, $t0			
		li $v0, 1
		syscall
		
		restart
		
mulTableOp:
	
	enterFirstNum
	addi $t0, $0, 1
		
		mulTableOp_loop:
		
		beq $t0, 11, exit_1					# if the counter is equalto 11, stop the loop
	
		li $v0, 4
		la $a0, str_x						# printing "x"
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, str_equals					# printing "="
		syscall
			
		mul $t2, $t1, $t0					# doing the multiplication between the 2 numbers entered by the user
		li $v0, 1
		move $a0, $t2						# moving the multiplication result to $a0
		syscall
		
		li $v0, 4
		la $a0, str_const					# printing '\n'
		syscall
		
		addi $t0, $t0, 1					# adding 1 to the counter
		
		j mulTableOp_loop
	
		exit_1:
		
		restart
	
imcOp:
	li $v0, 4
	la $a0, height_input						# showing message asking for user height input
	syscall
		
	li $v0, 5							# waiting for the user to input his height
	syscall
	move $t1, $v0
		
	checking_input2:
	# Here we will check if user is trying to divide by zero
	# if so, show macro dividingByZero and ask him to input the number again
	# otherwise, we can go on and divide the numbers
			
		li $v0, 4
		la $a0, weight_input					# showing message on screen asking for user weight
		syscall
			
		li $v0, 5						# waiting the user input
		syscall
		move $t2, $v0
		
		bnez $t2, correct_input2				# verifying if the user didnt entered 0 for his height
		dividingByZero						# if so, we'll show him an error message
		j checking_input2					# and we'll ask him to enter the number again
	
		correct_input2: 					# if the height was correctly entered (i.e, if it's =/= of 0)
		
			mul $t3, $t2, $t2				# doing the calculation of height x height
			div $t3, $t1, $t3				# dividing the user weight to the result from the last operation

			li $v0, 4
			la $a0, result_msg				# showing the result message on screen
			syscall
			
			li $v0, 1
			move $a0, $t3					# showing the result of Body mass index (BMI)
			syscall
	
		restart
	
fibonacci:
	
	li $v0, 4
	la $a0, msg_fib1						# printing initial message 
	syscall
		
		checking_fibInput1:					# checkpoint in case we found an error
		
		li $v0, 4
		la $a0, msg_fib2					# asking for 'a' of the interval [a,b] to calculate fibonacci sequence
		syscall
		
		li $v0, 5						# waiting for the user to input the 'a' number
		syscall
		
		bge $v0, 1, correct_fibInput1				# 'a' must be >= 1. If so, we can go on the operation
		
		la $a0, wrong_input					# otherwise, we show him an error message
		li $v0, 4						# jump to the checkpoint and ask him
		syscall							# to input the number again
		j checking_fibInput1
		
		correct_fibInput1:
  		
  		move $a2, $v0 
  		
  		checking_fibInput2:
  		
  		li $v0, 4
  		la $a0, msg_fib3					# waiting for the user to input the 'b' number
		syscall
		
		li $v0, 5
  		syscall
  		
  		bge $v0, $a2, correct_fibInput2				# 'b' must be >= a. If so, we can go on the operation
  		
  		la $a0, wrong_input					# otherwise, we show him an error message
		li $v0, 4						# jump to the checkpoint and ask him
		syscall							# to input the number again
		j checking_fibInput2
		
  		correct_fibInput2:
  		
  		move $a1, $v0 
  		li $t0, 0
		li $t1, 1
  
		li $t5, 1 						# $t5 is our counter
		move $t6, $a2
		
		fib_loop:
		
		move $t2, $t1 						# storing $t1 into $t2, to update $t0 of the next iteraction
  		add $t1, $t1, $t0 					# add $t1 to $t0
  		move $t0, $t2 						# update $t0

  		bge $t5, $t6, print_num 				# if the counter is >= 'a', print the sequence number in the interval
  		addi $t5, $t5, 1 					# incremente the counter
	 	j fib_loop						# and jump back to the loop 
		
		print_num:    
			
  		bne $t5, 1, aux						# if our counter is 1, we ended the operation
  
  		li $v0, 4 
  		la $a0, msg_sequence
		syscall 
		
		aux: 
 		
  		li $v0, 1
  		move $a0, $t0						# print sequence numbers
  		syscall
  
  		bne $t5, $a1, repeat_fib 				# if counter == b, we ended this operation
  			
  		restart							# and we'll ask him if he wants to do another operation
  		
  		repeat_fib:						
  			
  		j print_virg						# we'll print the numbers followed by a comma :P

		print_virg:  
  		
  		li $v0, 11
  		li $a0, ','						# printing comma between the numbers
  		syscall  

  		li $v0, 11
  		li $a0, ' '						# print a space between comma and the number
  		syscall
  
  		addi $t5, $t5, 1					# incrementing the counter
  
  		j fib_loop						# repeat the operation
		
fatorial:

	enterFirstNum
	move $t0, $t1
	
	fatorial_loop:
		sub $v0, $v0, 1 					# v0--	
		mul $t0, $v0, $t0 					# n * n-1
		bne $v0, 1, fatorial_loop
		
		li $v0, 4
		la $a0, result_msg
		syscall	
	
		li $v0, 1
		move $a0, $t0
		syscall
	
		restart
exit:
# This label was only created to stop the program by calling a
# macro to do this

	done								# macro responsible for stopping the program
