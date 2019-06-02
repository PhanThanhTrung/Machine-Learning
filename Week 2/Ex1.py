''' 
Write code to print out 1 to 100. 
If the number is a multiple of 3, print out "fizz" instead of the number. 
If the number is a multiple of 5, print out "buzz". 
If the number is multiple of 3 and 5, print out "fizzbuzz".
'''
for i in range(1,101):
    if i%3==0:
        print('fizz', end =" ")
    if i%5==0:
        print('buzz', end = " ")
    if i%3!=0 and i % 5!=0:
        print(i, end = " ")