# with sum function:-
def Is_harshad_number(num):
    x = [int(i) for i in str(num)]
    y = sum(x)	
    if num % y == 0:
        print(True)
    else:
        print(False)
number = int(input("enter the number"))    
Is_harshad_number(number)





# without sum function:-
def harshad_nummber(num):
	x = [int(i) for i in str(num)]
	sum1=0
	for i in x:
		sum1 = i +sum1
	if num % sum1 == 0:
		print(True)
	else:
		print(False)
number = int(input("enter the number"))	
harshad_nummber(number)
